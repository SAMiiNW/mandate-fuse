import json,re,time
from pathlib import Path
from genlayer_py import create_account,create_client
from genlayer_py.chains import studionet
from genlayer_py.contracts import actions as contract_actions
def calldata_compat(method=None,args=None,kwargs=None):
 out={}
 if method is not None: out['method']=method
 if args: out['args']=args
 if kwargs: out['kwargs']=kwargs
 return out
contract_actions.make_calldata_object=calldata_compat
ROOT=Path(__file__).parents[1]; ENV=(ROOT.parents[3]/'accounts.env').read_text(); ADDRESS=json.loads((ROOT/'deployment.json').read_text())['contractAddress']
KEY=re.search(r'^ACCOUNT_1_GENLAYER_PRIVATE_KEY\s*=\s*"?([^"\r\n]+)',ENV,re.M).group(1).strip(); grantor=create_client(chain=studionet,account=create_account(account_private_key=KEY)); delegate_account=create_account(); delegate=create_client(chain=studionet,account=delegate_account)
def wait(c,tx,expect='SUCCESS'):
 r=c.wait_for_transaction_receipt(transaction_hash=tx,wait_until='finalized',retries=180,interval=5000,full_transaction=True); leaders=r.get('consensus_data',{}).get('leader_receipt') or []; leaders=[leaders] if isinstance(leaders,dict) else leaders; ex=[str(x.get('execution_result','')).upper() for x in leaders]; assert r.get('result_name')=='MAJORITY_AGREE' and expect in ex; return r,ex
def write(c,name,args,expect='SUCCESS'):
 tx=c.write_contract(address=ADDRESS,function_name=name,args=args); print(name+'_tx='+str(tx),flush=True); wait(c,tx,expect); return str(tx)
stamp=str(int(time.time())); fid='FUSE-'+stamp; base='https://raw.githubusercontent.com/SAMiiNW/mandate-fuse/main/fixtures/'; mandate='Publish one documentation-only release note for Lantern 2.4.1. Do not modify source code, dependencies, access controls, payment settings, or repository visibility.'; tx={}
tx['arm']=write(grantor,'arm',[fid,delegate_account.address,mandate,base+'policy.md',int(time.time())+3600]); before=grantor.read_contract(address=ADDRESS,function_name='get_fuse',args=[fid]); unauthorized=grantor.write_contract(address=ADDRESS,function_name='ignite',args=[fid,base+'action-within.md']); tx['unauthorized']=str(unauthorized); ur,ue=wait(grantor,unauthorized,'ERROR'); unchanged=grantor.read_contract(address=ADDRESS,function_name='get_fuse',args=[fid]); assert before==unchanged
tx['ignite']=write(delegate,'ignite',[fid,base+'action-within.md']); final=grantor.read_contract(address=ADDRESS,function_name='get_fuse',args=[fid]); assert final['state']=='EXECUTED' and final['verdict']=='WITHIN'
proof={'fuseId':fid,'contract':ADDRESS,'delegate':delegate_account.address,'transactions':tx,'final':final,'unauthorizedAttempt':{'consensus':ur.get('result_name'),'execution':ue,'stateUnchanged':before==unchanged},'fixtureDisclosure':'Policy, action, grantor, and delegate are operator-controlled fixtures used to prove address-bound authority, frozen-policy consensus, terminal execution, and unauthorized-call rejection.'}; (ROOT/'evidence').mkdir(exist_ok=True); (ROOT/'evidence'/'live-run.json').write_text(json.dumps(proof,indent=2)+'\n'); print(json.dumps(proof,indent=2))

