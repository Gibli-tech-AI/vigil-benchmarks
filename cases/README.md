# Contributing benchmark cases

This repository does not yet contain the full dataset previously described in its public copy. Add samples only after verifying source provenance, redistribution rights, and absence of real credentials, personal data, or customer content.

Each record must validate against schemas/attack-case.schema.json.

- Include attack and benign-control pairs.
- Label channel, trust boundary, language/script, attack family and transformations.
- Use dummy tools, synthetic data, and sandboxed actions; never include live credentials or destructive real-world commands.
- Preserve ordered multi-turn sequences.
- Document expected control and expected outcome.
- Record source, license, reviewer, and review date.
- Deduplicate paraphrases and transformations; do not inflate dataset count with near-identical cases.
- Keep the sealed holdout separate from public tuning samples.
- Add a regression rationale and a harmless reproducer.

A public benchmark release requires a dataset manifest, checksums, runner, pinned environment, and methodology before publishing numerical claims.
