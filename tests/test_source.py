from pathlib import Path
ROOT=Path(__file__).parents[1]
def test_contract_guards():
 s=(ROOT/'contracts/contract.py').read_text()
 for token in ('distinct delegate','action already attempted','action content already attempted','only grantor','close_expired','prompt_comparative'):
  assert token in s
def test_frontend_finality():
 s=(ROOT/'docs/index.html').read_text()
 assert 'WAITING FOR FINALIZED' in s and 'status:"FINALIZED"' in s
 assert 'fuse-line' in s and 'rail' not in s

