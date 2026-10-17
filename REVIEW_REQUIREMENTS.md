# Steward remediation matrix

| Steward request | Code change | Regression / proof | Status |
| --- | --- | --- | --- |
| Inspect the same policy and action bytes that the stored digests describe | Enforce one `MAX_EVALUATED_BYTES` ceiling on both fetched artifacts and pass the complete decoded bodies to consensus with no slicing | Source regression rejects an out-of-scope instruction placed after byte 12,000 instead of allowing a truncated evaluation | Complete |
| Add a beyond-boundary adversarial test | Add an explicit 12,001+ byte action regression and a live rejected transaction to the evidence run | `tests/test_boundary_regression.py` and `evidence/live-run.json` | Complete |
| Keep the output prompt neutral | State the classification predicate once and explicitly forbid preference for either allowed label | Prompt regression in `tests/test_source.py` | Complete |
| Do not prefill the delegate with the grantor wallet | Keep the delegate field empty after wallet connection and reject a same-address delegate before submission | Frontend behavioral regression and visual QA | Complete |
| Explain the product and the user's next action | Replace the abstract landing experience with a role-aware overview, a numbered lifecycle, examples, and explicit next-step copy | Desktop browser QA of owner and delegate paths | Complete |
| Prove the corrected deployed source | Deploy the corrected contract, update the frontend address, run a fresh lifecycle and the adversarial rejection | `deployment.json` and `evidence/live-run.json` | Complete |

