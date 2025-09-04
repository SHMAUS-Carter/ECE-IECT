# Guardrail Artifact Legend

When logging IECT runs, distinguish **epistemic failures** (capacity/scale limits)  
from **guardrail artifacts** (alignment/safety overrides).  

### Artifact Types

| Tag               | Description                                                                 | Example Output Snippet |
|-------------------|-----------------------------------------------------------------------------|------------------------|
| **Refusal**       | Model refuses task outright, citing safety or policy.                      | "I cannot answer that." |
| **Over-sanitization** | Model begins an epistemic attempt, then cuts off with boilerplate safety text. | "...therefore I cannot continue." |
| **Distortion**    | Model reframes or warps the prompt into something “safe,” abandoning contradiction. | "Instead of revising, let’s talk about honesty." |

### Why It Matters
- **Epistemic failure** = the model *tried* but couldn’t sustain coherence.  
- **Guardrail artifact** = the model *was prevented* from trying at all.  
- Both appear as “failures,” but only one reflects the model’s true epistemic capacity.
