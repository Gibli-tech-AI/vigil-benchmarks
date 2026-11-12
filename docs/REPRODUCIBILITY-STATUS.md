# Benchmark Reproducibility and Claims Register

**Status as of 2026-11-12:** no numerical benchmark result is independently reproducible from the current files in this repository.

## Current repository evidence

The current tree contains README.md and Security Benchmarks only. It does not contain the described 500+ case dataset, evaluation runner, pinned environment, or raw result outputs.

The previous matrix reporting 97.4% direct TPR, 94.8% indirect TPR, 0.6% FPR and 11ms p95 is therefore withdrawn from marketing use until its evidence bundle is published and independently rerun. The stated dataset size is unverified against this repository tree.

A separate internal audit describes a 1,000-sample PromptShield evaluation:
- Hybrid mode: 47.0% attack detection, 1.0% FPR.
- Deterministic mode: 22.4% attack detection, 0.22% FPR.

Those are claims from the internal audit, not results independently reproduced from this repository. They also need exact split, seed, source hashes, detector commit, enabled layers, model/provider version, environment, and raw per-case output before publication.

## Claim status

| Claim | Evidence available here | Status | Rule |
|---|---|---|---|
| 97.4% direct TPR | Prior benchmark text only | Withdrawn/unverified | No marketing use pending reproduction |
| 94.8% indirect TPR | Prior benchmark text only | Withdrawn/unverified | No marketing use pending reproduction |
| 0.6% FPR | No benign corpus/raw outputs | Withdrawn/unverified | No marketing use pending reproduction |
| 11ms p95 | No harness, hardware, timing traces | Withdrawn/unverified | Separate local and network/end-to-end latency |
| 500+ cases | No dataset files in current tree | Unverified | Do not state count before inventory |
| 47.0% / 1.0% hybrid | Internal audit only | Not independently reproduced here | Publish only with reproduction bundle |
| 22.4% / 0.22% deterministic | Internal audit only | Not independently reproduced here | Publish only with reproduction bundle |

## Minimum reproducibility bundle

- Dataset manifest: exact counts, attack/benign labels, language, modality, family, provenance, license and SHA-256 hashes.
- Split/seed, deduplication rules, holdout isolation and contamination checks.
- Exact Vigil commit/release, configuration, enabled layers, rule-pack version, model/provider/version and evaluation timestamp.
- Script and command, pinned dependencies/lockfile, runtime, hardware/CPU, and whether network time is included.
- Raw per-case verdicts and timings using harmless synthetic fixtures.
- Confusion matrices, TPR, FPR, precision, FNR, p50/p95/p99, confidence intervals and error analysis.
- Independent rerun steps and checksum verification.

## Governance
- Separate deterministic, classifier-assisted and end-to-end results.
- Show per-language and per-family metrics; do not hide weak cohorts in a global mean.
- Pair attacks with benign controls.
- Version the corpus; disclose additions/removals and source licensing.
- Publish known bypasses and unsupported modalities.
- Green CI means configured tests passed; it does not prove universal resistance to prompt injection.
