# Mandate Fuse

A password can be shared forever. A Mandate Fuse cannot. It binds one delegate, one natural-language scope, one frozen public policy, and one expiry into a single-use authority.

The delegate proposes a public action artifact. GenLayer validators fetch the frozen policy and action, verify their digests, and agree on the exact WITHIN or OUTSIDE verdict plus bounded reason codes. The first completed inspection burns the fuse into EXECUTED or DENIED. The grantor may revoke before use, and anyone may close an expired fuse.

## Lifecycle
ARMED -> EXECUTED | DENIED | REVOKED | EXPIRED.

## Safety boundaries
The delegate must differ from the grantor. The UI deliberately leaves the delegate field blank after wallet connection and explains the two roles before any transaction.

Policy and action artifacts must each contain 30 to 12,000 bytes. Validators inspect the complete accepted bodies: no prefix slicing or partial evaluation is allowed. An artifact over that ceiling is rejected before semantic classification, so a prohibition placed beyond the former 12,000-byte boundary cannot be hidden. Action URL and content replay are rejected, policy mutation is detected, and expiry closure is permissionless.

## First-run path
1. The owner defines the mandate and freezes the digest of a public policy.
2. The owner binds a different delegate wallet and an expiry.
3. The delegate loads the fuse ID and submits one public action artifact.
4. Validators classify the complete action against the complete frozen policy, and the contract records `EXECUTED` or `DENIED` permanently.

## Tests
Run `python -m pytest tests -q` and `genvm-lint contracts/contract.py`. The suite includes the steward-requested beyond-boundary adversarial regression.

