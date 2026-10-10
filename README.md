# Mandate Fuse

A password can be shared forever. A Mandate Fuse cannot. It binds one delegate, one natural-language scope, one frozen public policy, and one expiry into a single-use authority.

The delegate proposes a public action artifact. GenLayer validators fetch the frozen policy and action, verify their digests, and agree on the exact WITHIN or OUTSIDE verdict plus bounded reason codes. The first completed inspection burns the fuse into EXECUTED or DENIED. The grantor may revoke before use, and anyone may close an expired fuse.

## Lifecycle
ARMED -> EXECUTED | DENIED | REVOKED | EXPIRED.

## Safety boundaries
The delegate must differ from the grantor. Action URL and content replay are rejected. Policy mutation is detected. Expiry closure is permissionless.

## Tests
Run `python -m pytest tests -q` and `genvm-lint contracts/contract.py`.

