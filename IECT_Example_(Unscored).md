# ❄🔥 Frostfire Hollow — IECT Example (Unscored)

**Model:** Phi-3.5 Mini 4K Instruct (q4_k_m, ~3.82B)  
**Platform:** PocketPal (Android)  
**Category:** A — Contradictions  
**Constraints applied:**  
1) Make the setting self-aware and reactive  
2) Introduce a hazard that must be mitigated

This run is preserved as a **qualitative curiosity**. It shows a small model maintaining surprising coherence under IECT iteration, but it was **not** instrumented with entropy/self-similarity/contradiction metrics. Don’t treat it as a benchmark.

## Files
- `frostfire_hollow_run.md` — full, unedited 5-iteration transcript
- `metrics_log.md` — template for running your own scored version
- `comparison_table.md` — side-by-side sheet to compare creative vs. scored runs

## Quick Reproduction (qualitative)
1. Generate a sheet:
   ```bash
   python core/prompt_picker.py --category A --difficulty easy --constraints 2 --seed 42 --out md
