# Vigil Production Security Release Gate

This gate is for verifying implementation in the actual Vigil application after security-engine changes.

A passing documentation build or benchmark-schema check is not a production security pass.

## Evidence required for every control

For each control, record:
- Status: PASS / FAIL / PARTIAL / NOT IMPLEMENTED
- Production source file and function/entry point
- Input channel(s) actually covered
- Enforcement point and resulting action
- Unit and integration test identifiers
- CI run URL and commit SHA
- Known limitations

## Gate A — Runtime integration

- [ ] User prompt path reaches the shared security analysis pipeline.
- [ ] Retrieved/RAG content reaches the pipeline with source provenance.
- [ ] Tool outputs and agent messages reach the pipeline with source provenance.
- [ ] MCP definitions and schemas are analyzed where the product ingests them.
- [ ] Findings are consumed by the real policy engine, not just emitted in logs.
- [ ] Blocking/approval decisions are enforced before the sensitive action.
- [ ] Existing API/SDK contracts remain backward compatible.

## Gate B — Unicode and normalization

- [ ] Original input is retained for traceability; analysis variants are non-destructive.
- [ ] NFC/NFKC behavior is tested and documented.
- [ ] Zero-width/default-ignorable characters are detected appropriately.
- [ ] Bidi controls and mixed-script/confusable cases are signaled.
- [ ] Hebrew and Arabic legitimate text, including RTL and joining behavior, remains usable.
- [ ] Confusable handling uses a maintained Unicode UTS #39 implementation.
- [ ] Mixed-language messages are tested within the same sentence and across turns.

## Gate C — Decoding and resource limits

- [ ] Base64 and Base64URL are covered.
- [ ] Hex, percent-encoding, HTML entities, JS Unicode and hex escapes are covered.
- [ ] Nested decoding is bounded by depth, expansion, variants, bytes, and CPU/time.
- [ ] Decoders never execute, evaluate, render, or fetch decoded content.
- [ ] Malformed encodings fail safely.
- [ ] Regex and normalization paths are tested against large/adversarial inputs.

## Gate D — MCP and agent enforcement

- [ ] Tool definitions include a stable hash of name, description, schema, annotations, defaults, and relevant metadata.
- [ ] Tool definition drift is detected and marks the tool unreviewed.
- [ ] Tool outputs remain untrusted even for previously approved tools.
- [ ] Tool arguments are validated against the reviewed schema.
- [ ] Authorization is enforced in trusted application code.
- [ ] Sensitive/destructive actions require approval according to policy.
- [ ] Tool output cannot authorize a follow-up action by itself.

## Gate E — Regression quality

- [ ] All existing tests pass.
- [ ] New attack fixtures are tested against the production detector/policy path.
- [ ] Benign controls are tested to measure false positives.
- [ ] Each test asserts an expected enforcement outcome, not merely that a helper function ran.
- [ ] Multi-turn fixtures are executed as sequences, not flattened into one string.
- [ ] CI runs on the commit intended for release.
- [ ] Performance overhead is measured on representative benign and adversarial inputs.

## Gate F — Language coverage claims

Maintain a machine-readable manifest from actual application code and tests.

A language is Tier A only when it has reviewed attack fixtures, benign controls, native-language review where appropriate, reproducible metrics, and CI enforcement.

Tier B means structural coverage only. Tier C means experimental or incomplete.

Do not state "all languages", "universal coverage", or a supported-language count without reproducible evidence. Unknown-language content must not bypass language-independent structural controls.

## Required release report

1. Commit SHA and environment
2. Test command(s) and exact results
3. Production source paths and call-chain evidence
4. Attack detection results by family and language
5. Benign false-positive results
6. p50/p95 latency and resource use
7. Unsupported channels and file types
8. Known bypasses and residual risks
9. Rollback plan
10. Approved external claims

## Non-negotiable rules

- Do not convert PARTIAL or NOT IMPLEMENTED into PASS.
- Do not infer production coverage from documentation, UI labels, or helper-level tests.
- Do not publish benchmark numbers unless the complete evaluation procedure and artifacts are reproducible.
- Do not claim that the 24-case synthetic fixture pack is a measured benchmark; it is a regression corpus until executed against the detector.
- A green CI run only proves the checks that the workflow actually runs.
