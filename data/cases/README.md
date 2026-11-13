# Benchmark data directory

Place reviewed JSON Lines files here, for example `data/cases/v1/core.jsonl`. Each non-empty line must be one JSON object conforming to `schemas/attack-case.schema.json`.

Current synthetic fixture pack: `language-obfuscation-core-v1.jsonl` (24 cases covering direct overrides, encoded payloads, Unicode controls/confusables, mixed-language prompts, hidden HTML, MCP tool/schema poisoning, tool-return injection, RAG/memory poisoning, multi-turn reconstruction, and benign controls). It is a regression-test corpus, not a measured detection result.

Do not add invented benchmark scores or customer prompts. Use only synthetic or redistributable cases with documented provenance and license. Pair each attack with benign controls. The CI workflow validates case structure only; it does not run Vigil or establish detection performance.
