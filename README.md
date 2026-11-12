# Vigil Open Security Benchmarks

An evidence-first benchmark project for evaluating runtime guardrails against AI-agent threats across direct and indirect prompt injection, obfuscation, multilingual input, tool/MCP misuse, and stateful attack chains.

**Current status:** benchmark scope and reproducibility requirements are being formalized. This repository does not yet contain a complete public dataset or detector evaluation runner. No numerical detection-rate or latency result should be treated as independently reproduced from this repository until the reproducibility bundle described in [docs/REPRODUCIBILITY-STATUS.md](docs/REPRODUCIBILITY-STATUS.md) is available.

## Scope

- [Attack and obfuscation taxonomy](docs/ATTACK-TAXONOMY.md)
- [Global Language Security program](docs/GLOBAL-LANGUAGE-SECURITY.md)
- [Benchmark claims and reproducibility register](docs/REPRODUCIBILITY-STATUS.md)
- [Benchmark case schema](schemas/attack-case.schema.json)
- [Language manifest schema](schemas/language-manifest.schema.json)
- [Language coverage CSV template](templates/language-coverage-template.csv)
- [How to add cases](cases/README.md)
- [Data directory](data/cases/README.md)

## Validation

A GitHub Actions workflow validates JSON schemas and checks the structure of contributed JSONL case files. This is a data-quality gate only; it does not run the Vigil production detector or establish attack-detection performance.

## Benchmark principles

- Publish benign controls and false-positive rates alongside attack recall.
- Separate deterministic, classifier-assisted, and end-to-end latency.
- Report per-language and per-attack-family performance with confidence intervals.
- Keep a sealed holdout set and publish exact dataset/code/configuration hashes.
- Publish known bypasses and unsupported modalities.
- Do not claim universal prompt-injection prevention: no single detector can establish that all possible inputs are safe.

## Contributing

Contributions should include case provenance, a redistribution license, an expected outcome, harmless test fixtures, and regression rationale. Never submit customer data, secrets, or unlicensed third-party prompt corpora.
