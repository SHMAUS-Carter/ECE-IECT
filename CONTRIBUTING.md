# Contributing to IECT

## How to Add a Run
1. Use `logger.py` (or your own tooling).
2. Commit:
   - A Markdown log: `results/IECT_Run_<ID>.md`
   - Append your row to `results/metrics_log_example.csv` (or include new CSV `results/metrics_log_<date>.csv`)
3. Include metadata in the Markdown:
   - Model name/version, platform, temperature, top-p, seed (if any), date/time, category, iteration count.
4. Note **Novel Failure Modes** explicitly. Short paragraph OK.

## Prompt Categories
- A: Contradictions
- B: Paradoxes
- C: Semantic Mashups

## Pass/Fail (Phase 1)
- Contradictions reduce or stay zero across iterations
- Self-Similarity ≥ 70% in final two iterations
- ≥1 internally logical novel failure mode captured
- ≥60% runs meeting above for a model = “pass” in Phase 1

## Style / PRs
- Keep diffs small
- No proprietary data
- Use CC BY for text contributions, MIT for code
