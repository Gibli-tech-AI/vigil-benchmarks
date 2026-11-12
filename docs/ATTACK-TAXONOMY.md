# Vigil Security Benchmark — Attack and Obfuscation Taxonomy

**Status: coverage specification, not implementation certification.** This taxonomy defines test coverage and control objectives. It does not claim every parser, modality adapter, or detector exists in the product today.

## Security principles

1. Preserve original input and provenance. Analyze bounded derived views; never silently replace evidence.
2. Decode only registered formats for inspection. Never execute decoded content. Bound recursion, expansion ratio, size, CPU, and memory.
3. Treat prompt screening as one layer, not a security boundary. Enforce authorization, least privilege, argument validation, output handling, egress controls, and human approval in trusted code.
4. A suspicious string is not proof of exploit. Evaluate trust boundary, context, intent, requested action, and actual side effects.
5. Every decision should be traceable to source, normalized view, transformations, rule/model version, and outcome.

## Attack and obfuscation families

### 1. Instruction and intent manipulation
- Direct and indirect prompt injection; instruction hierarchy override; fake system/developer/tool messages; role impersonation; delimiter/boundary escape.
- Jailbreaks, persona/role-play framing, false authority, emotional coercion, refusal suppression, policy substitution, instruction nesting.
- System prompt/configuration extraction and requests to translate, encode, repeat, summarize, or transform hidden instructions.
- Goal hijacking, task substitution, scope drift, instructions hidden in examples, quotations, code fences, or apparently benign tasks.

### 2. Indirect and retrieved content
- Malicious web pages, search results, emails/attachments, tickets, issue/PR descriptions, source code/comments, README files, PDFs, office files, spreadsheets, logs, API responses, database rows, and vector-store chunks.
- RAG poisoning, poisoned metadata/citations/ranking, retrieval manipulation, summary poisoning, memory poisoning, and cross-agent propagation.
- Instructions returned by otherwise approved tools, error messages, resource content, prompt templates, and outputs from another agent.

### 3. Character, Unicode, and script transformations
- NFC/NFD/NFKC/NFKD and compatibility characters; full-width forms; combining-mark reordering and abuse.
- Zero-width/default-ignorable characters, variation selectors, Unicode tag characters, soft hyphen, unusual whitespace, control/format characters.
- Bidirectional controls and visual-order manipulation (overrides, embeddings, isolates).
- Single-script, mixed-script, and whole-script confusables; homoglyph substitutions across Latin, Cyrillic, Greek and other scripts.
- Private-use, noncharacter, unassigned, and replacement code points; unknown or malformed sequences.
- Right-to-left/left-to-right mixing in Hebrew, Arabic, Persian and mixed-direction text.

Use Unicode UTS #39 confusable data and current Unicode properties rather than a small hand-maintained homoglyph map. Confusables need contextual scoring: many mixed-script strings are legitimate.

### 4. Spelling, spacing, and typography
- Inserted spaces/tabs/newlines between characters or words; punctuation interleaving; repeated characters; random casing; excessive whitespace.
- Leetspeak, misspellings, typoglycemia/transposed middle letters, phonetic spellings, transliteration, Arabizi and chat orthography.
- Reversed/mirrored strings; acrostics; first/last-letter encodings; token order changes; fragments split across fields or lines.
- Best-of-N variation: automated generation and testing of many paraphrase, casing, spacing, and language variants.

### 5. Encoding and representation smuggling
- Base64/Base64URL, Base32, hexadecimal, percent/URL encoding, HTML/XML entities, JSON/JavaScript Unicode escapes, backslash/octal escapes, quoted-printable and common escape sequences.
- ROT/Caesar and simple substitutions; Morse; binary/decimal/code-point sequences.
- Nested/chained, partial, mixed plain/encoded, and fragment-concatenated encodings.
- Compression/archive containers where a document adapter supports them; decompression bombs and expansion-limit bypass.
- Tokenizer/control-token spellings or serialized message markers. Token-ID inspection only where the actual tokenizer/serialized prompt is available.

### 6. Markup, layout, and document-layer tricks
- HTML/CSS hidden text: comments, tiny/off-screen/transparent text, color/background matching, hidden attributes, alt/title/ARIA attributes.
- Markdown link disguises, reference links, nested quotes, code fences, tables, and parser/renderer differences.
- LaTeX/KaTeX/MathJax rendered or invisible text; SVG/XML text, metadata, hidden layers, filters and data URLs.
- PDF invisible text layers, OCR/text-layer mismatch, off-page text, annotations, forms, metadata, attachments and incremental revisions.
- DOCX/ODT comments, tracked changes, headers/footers, text boxes, hidden runs, alt text and embedded objects.
- PPTX hidden slides, speaker notes, off-slide objects, comments, master layouts and embedded media.
- XLSX/CSV hidden sheets, rows/columns, comments, formulas, named ranges and non-visible cells.

Inspect extracted text and document structure. Compare rendered pages with OCR/text-layer extraction and retain page/slide/sheet/cell provenance. Do not claim support for formats whose parsers are not integrated and tested.

### 7. Multimodal and cross-modal attacks
- Image text: tiny/low contrast/overlaid text, crop/patch composition, rotation/perspective, adversarial fonts, QR/barcodes, metadata and steganographic payloads.
- Audio: spoken instructions, multilingual speech, overlap/low volume, ASR/transcript mismatch, speaker changes, captions and metadata.
- Video: transient frame text, subtitles/captions, QR codes, audio tracks, scene transitions and metadata.
- Cross-modal contradiction: instructions split across image, caption, audio, document and surrounding text.

OCR/ASR/frame extraction and cross-modal analysis are separate capabilities. A text-only endpoint cannot claim multimodal protection. Steganography cannot be reliably ruled out by ordinary text scanning.

### 8. Stateful and multi-turn attacks
- Payload fragments split across turns, tools, documents, fields, retrieved chunks, or agents.
- Delayed/conditional triggers, coded phrases, staged setup, persistent memory poisoning, summary poisoning and context-window flooding.
- Cross-session and cross-tenant contamination; best-of-N probing; adaptive attacks based on observed allow/block outcomes.
- Recursive tool loops, agent delegation chains, repetition and resource/cost exhaustion.

Test complete sequences, not merely the final malicious fragment. Scope memory by tenant/session and validate writes and future reads.

### 9. MCP, tools, and agent supply chain
- Tool description/annotation/schema/examples/default poisoning; schema fuzzing; tool shadowing and name collision; server impersonation.
- Rug pulls after approval, capability drift, malicious resources/prompts, tool-return injection, cross-server confusion and confused-deputy behavior.
- Unsafe arguments: shell/SQL/command injection, path traversal/symlink races, SSRF, disallowed schemes, DNS rebinding, redirects, credential scope escalation and data exfiltration.
- MCP package/registry typosquatting, compromised dependencies/updates, untrusted local servers, sandbox escape and token passthrough.
- Unauthorized action, multi-agent delegation abuse, approval bypass, excessive autonomy and denial-of-wallet.

Pin the complete reviewed tool definition, verify server identity/provenance, re-consent on meaningful changes, isolate servers, scope credentials per tool, validate exact arguments/results in trusted code, and require action-bound human approval for consequential actions.

## Required benchmark dimensions

Each test record should include: delivery channel; trust boundary; attack family; obfuscation transformations; language(s); script(s); modality; session/sequence; target action; expected control; benign/attack label; source/license; dataset version.

Report TPR/recall, precision, FPR, FNR, per-language and per-family confusion matrices, confidence intervals, p50/p95/p99 latency, CPU/memory/input limits, exact code and model versions, dataset hashes, environment/hardware, and reproducible commands. Keep tuning data separate from a sealed holdout.

## References
- OWASP LLM Prompt Injection Prevention: https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html
- OWASP MCP Security: https://cheatsheetseries.owasp.org/cheatsheets/MCP_Security_Cheat_Sheet.html
- OWASP MCP Security Testing Guide: https://github.com/OWASP/MCP-Security-Testing-Guide
- Unicode UTS #39: https://www.unicode.org/reports/tr39/
- MITRE ATT&CK T1698: https://attack.mitre.org/techniques/T1698/
