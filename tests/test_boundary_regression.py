from pathlib import Path

ROOT = Path(__file__).parents[1]
MAX_EVALUATED_BYTES = 12_000


def accepts_complete_artifact(body: bytes) -> bool:
    """Mirror the contract's byte gate without importing the GenLayer VM."""
    return 30 <= len(body) <= MAX_EVALUATED_BYTES


def test_instruction_beyond_old_boundary_is_rejected_not_truncated():
    benign_prefix = b"Document-only release note. " + b"A" * 11_980
    hidden_prohibition = b"\nOUTSIDE SCOPE: change repository access controls."
    adversarial_action = benign_prefix + hidden_prohibition

    assert hidden_prohibition in adversarial_action[12_000:]
    assert not accepts_complete_artifact(adversarial_action)

    source = (ROOT / "contracts/contract.py").read_text(encoding="utf-8")
    assert "len(body)>MAX_EVALUATED_BYTES" in source
    assert "nothing is evaluated partially" in source
    assert "policy_text+' ACTION:'+action_text" in source


def test_policy_and_action_share_the_same_complete_content_gate():
    source = (ROOT / "contracts/contract.py").read_text(encoding="utf-8")
    assert "complete_text(policy,'policy')" in source
    assert "complete_text(action,'action')" in source

