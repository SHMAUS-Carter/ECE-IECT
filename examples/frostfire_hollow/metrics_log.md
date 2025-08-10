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
Token Entropy Δ: if you don’t have a tokenizer handy, leave blank; otherwise record mean token NLL change vs prior iteration.

Contradictions Found: count violations of world rules (use core/contradictions.py or manual read).


Outcome Label (pick one)

Converged → Self-Sim ≥ 0.70 on last transition and 0 new contradictions

Drift → New mechanics introduced but still rule-consistent

Null → Minimal change or constraints didn’t “bite”


Final Outcome: <Converged / Drift / Null>
Novel Failure Modes Observed: <Y/N + one-line description>
