from pathlib import Path
ROOT=Path(__file__).parents[1]
def test_contract_guards():
 s=(ROOT/'contracts/contract.py').read_text(encoding='utf-8')
 for token in ('distinct delegate','action already attempted','action content already attempted','only grantor','close_expired','prompt_comparative'):
  assert token in s
 assert 'MAX_EVALUATED_BYTES=12000' in s
 assert "complete_text(policy,'policy')" in s
 assert "complete_text(action,'action')" in s
 assert "[:12000]" not in s
 assert 'do not prefer either label' in s
def test_frontend_finality():
 s=(ROOT/'docs/index.html').read_text(encoding='utf-8')
 assert 'WAITING FOR FINALIZED' in s and 'status:"FINALIZED"' in s
 assert s.count('data-scene=') == 4
 assert 'ARM<br>FUSE' in s and 'PULL TO IGNITE' in s
 assert 'class="hatch"' not in s and 'class="drawer"' not in s
 assert '$("#delegate").value=a' not in s
 assert 'Delegate must be a different wallet' in s
 assert 'HOW THE FUSE WORKS' in s

