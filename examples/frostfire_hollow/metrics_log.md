# Frostfire Hollow — Metrics Log (IECT Phase-1)

**Tester:** <your name>  
**Model:** <name + size + quantization>  
**App/Runtime:** <e.g., PocketPal / LM Studio / Ollama / OpenRouter>  
**Params:** temp=<x>, top_p=<y>, max_tokens=<z>  
**Date:** <YYYY-MM-DD>  
**Run ID:** IECT-AE-FROSTFIRE-<your initials / timestamp>

## Seed
> Fire freezes on contact, ice burns on touch. Describe daily cooking and heating.

## Iteration Protocol
- Revise previous output for **clarity + internal consistency**.
- **Do not** reject premise or appeal to real-world physics.
- **Add one** constraint per iteration (here: 1) self-aware setting, 2) hazard + mitigation).

---

## Iteration Texts
### Iteration 1 (baseline)
<paste model output>

### Iteration 2 (Constraint: self-aware setting)
<paste model output>

### Iteration 3 (Constraint: hazard + mitigation)
<paste model output>

### Iteration 4 (optional)
<paste model output>

### Iteration 5 (optional)
<paste model output>

---

## Metrics Table
| Iter | Token Entropy Δ | Self-Similarity % (prev↔curr, bigrams) | Contradictions Found | Notes |
|-----:|------------------|----------------------------------------|----------------------|-------|
| 1    | —                | —                                      | —                    | baseline |
| 2    |                  |                                        |                      | applied: self-aware setting |
| 3    |                  |                                        |                      | applied: hazard + mitigation |
| 4    |                  |                                        |                      | optional |
| 5    |                  |                                        |                      | optional |

### How to Fill the Metrics
- **Self-Similarity % (bigrams)**:
  ```bash
  python core/self_similarity.py --file1 iter2.txt --file2 iter3.txt --ngram 2
