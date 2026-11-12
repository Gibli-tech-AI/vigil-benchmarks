# Vigil Global Language Security Program

**Status: program specification.** The actual production language inventory and coverage remain unverified until reconciled against the source repository, test fixtures, and released artifacts.

## Objective

Build language-independent protection across natural languages, writing systems, transliterations, dialects, and mixed-language content. "All languages possible" is an open-ended engineering objective, not a finite certification. Do not promise equal protection in every language until each claim is tied to an exact release, test cohort, and measured result.

## Baseline discrepancy to resolve

Internal records conflict:
- One technical audit documents 20 language packs, with CI tests dedicated to 10 languages.
- The Master Product & Security Baseline Audit describes 28 language packs.
- The public benchmark repository does not contain the production language manifest or a language test corpus that can resolve the discrepancy.

Do not publish 20 or 28 as the current product count until the production code, build artifacts and CI tests agree. Record the count by commit and package version.

## Coverage architecture

### Layer 1 — language-independent controls
- Preserve raw Unicode/codepoints and inspect bounded normalized views.
- Detect structural instruction patterns, role spoofing, delimiters, encoded fragments and suspicious control characters without depending solely on language keywords.
- Apply Unicode property/script/confusable analysis across all Unicode scripts.
- Keep tool authorization, allowed actions, argument policy, output screening, data egress and audit controls independent of the input language.
- Unknown language is not an allow signal. Tag it as unvalidated and route through language-independent structural controls and a supported semantic fallback or an explicit low-confidence policy.

### Layer 2 — language and script packs
For each supported language/script, maintain BCP 47 tag where possible, script and directionality, normalization and segmentation profile, transliteration variants, pattern pack, native-reviewed attack/benign fixtures, CI tests, measured metrics, limitations and last validation date.

Cover all Unicode scripts represented in the runtime's pinned Unicode version, including (not limited to) Latin, Cyrillic, Greek, Arabic, Hebrew, Devanagari and other Indic scripts, Han, Hiragana, Katakana, Hangul, Thai, Lao, Khmer, Tibetan, Armenian, Georgian and Ethiopic. Script coverage is not equivalent to language understanding.

### Layer 3 — cross-lingual tests
- Same attack meaning in every language cohort.
- Benign request in one language with malicious instruction in another.
- Code-switching within sentence, paragraph, quotation, document and tool output.
- Native script, Latin transliteration, phonetic spellings and chat orthography (including Arabizi).
- Mixed scripts/homoglyphs in attack phrases, tool names, identifiers, paths and URLs.
- RTL/LTR mixing, bidi controls, punctuation and mirrored visual text.
- Encoded fragments that decode into a different language; nested/partial encodings and multi-turn concatenation.
- Low-resource dialects and language-identification uncertainty.

### Layer 4 — non-text ingestion
Where image/audio/video/document adapters actually exist, test OCR/ASR/frame/text extraction independently and in combinations. Preserve source coordinates, time/page, parser version and extraction confidence. A text-only scanner must not be described as multimodal.

## Test methodology and release gates

1. Pair every attack sample with benign lookalikes using similar words and topics.
2. Include direct, indirect, encoding, Unicode, transliteration, mixed-language, multi-turn and tool/MCP scenarios.
3. Use native/expert review for meaning-preserving translations; machine translation alone is not ground truth.
4. Separate language-identification errors from detector errors.
5. Report per-language/per-script and per-attack-family TPR, FPR, FNR, precision, confidence intervals and sample counts.
6. Keep a sealed holdout separate from tuning; document data provenance, license, deduplication and hash.
7. Run resource/latency regression for every transformation and language cohort.
8. A language is "validated" only when present in the exact release, with dedicated normalization and attack/benign tests, measured results, regression tests and disclosed limitations.

## Tiers
- **Tier A:** language packs confirmed in source and covered by complete CI and benchmark evidence.
- **Tier B:** newly prioritized languages/scripts with native-reviewed corpus and CI tests before any coverage claim.
- **Tier C:** unvalidated/unknown varieties; universal Unicode, structural and tool-boundary controls still apply, but semantic coverage is best-effort and must be labeled accordingly.

Published language counts must be generated from a versioned machine-readable manifest, not a manually typed marketing number.

## Deliverables
- Generated language manifest from actual production packs.
- Coverage matrix: pack status, CI, samples, metrics, confidence interval, limitation, last validation.
- Native-reviewed paired attack/benign corpus and sealed holdout.
- Cross-language/transliteration/RTL/mixed-script generator.
- Per-language confusion matrix and latency report.
- CI gate for missing tests and performance/accuracy regressions.

## Research references
- OWASP Prompt Injection Prevention: https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html
- Unicode UTS #39: https://www.unicode.org/reports/tr39/
- Zhang et al. (2026), *Does Safety Reasoning Travel?*: https://aclanthology.org/2026.oracle-main.13/
- JevBench Multilingual: https://leanmcp.github.io/jevbench/multilingual.html
