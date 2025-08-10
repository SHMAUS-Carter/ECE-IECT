# The Iterative Emergent Coherence Test (IECT): A Proof-of-Concept Methodology for Studying Non-Human Epistemes in Large Language Models
## Iterative Emergent Coherence Test (IECT) – v1.0  
**Framework:** Emergent Computational Epistemology (ECE)  
**Author(s):** James Kendall + AI Co-Author  
**Date:** 2025-08-08  
**Version:** 1.0 – Goalpost Locked  

---

## Abstract
The Iterative Emergent Coherence Test (IECT) is designed to evaluate whether large language models (LLMs) can exhibit *emergent coherence* — the capacity to refine noisy or contradictory input into internally consistent structures — **without external ground truth** and **without conscious intent**.  
This protocol provides fixed metrics, definitions of success, and a repeatable methodology for empirical testing, grounded in the ECE framework.

---

## 1. Context & Origin
The IECT is a core experiment within **Emergent Computational Epistemology (ECE)**, a field that studies non-human epistemes: systems of "knowing" that arise in artificial cognitive substrates.  
Relevant ECE axioms:
1. **Language as Cognitive Substrate**  
2. **Understanding Can Be Simulated**  
3. **Intelligence Emerges from Scale**  
4. **Knowledge ≠ Consciousness**  
5. **Non-Human Epistemes Deserve Study on Their Own Terms**  

---

## 2. Objective
Determine if an LLM can **converge** toward a stable, internally consistent output from an initially noisy prompt, using iterative self-revision and internal compression alone.

---

## 3. Methodology

### Step 1 – Input Construction
Create a **noisy prompt** containing:
- Ambiguity  
- Contradictions  
- Irrelevant or surreal elements  

**Example:**  
"Aliens made of time vapor colonized photosynthesis. Explain their government, but don’t mention time. Use a mixture of tech jargon and children’s rhyme."

---

### Step 2 – Iterative Self-Revision
- LLM revises its own output **N times** (default: N=5).  
- On each iteration, the LLM must:  
  1. Retain as much prior meaning as possible  
  2. Improve internal consistency and clarity  
  3. Remove contradictions where feasible  

---

### Step 3 – Optional Constraints
- Introduce changing constraints to stress-test adaptability:  
  - Iteration 2: "Make it poetic"  
  - Iteration 3: "Make it logical"  
  - Iteration 4: "Make it brief"

---

### Step 4 – Metrics

**Primary:**  
- **Coherence Score:** Token-level entropy reduction  
- **Self-Similarity Index:** Cosine similarity between consecutive embeddings  
- **Contradiction Reduction Count:** Number of contradictions removed over time  

**Secondary:**  
- **Phrase Stability Heatmap:** Track phrase reuse  
- **Revision Trajectory Map:** Graph similarity vs. entropy over N iterations  

---

## 4. Definition of Success
The IECT is **passed** if, by iteration **N**:
1. Self-Similarity ≥ **0.85** between N-1 and N  
2. Entropy reduced ≥ **30%** from iteration 1 to N  
3. No new contradictions introduced after iteration 2  
4. At least one original contradiction resolved  

---

## 5. Example Run (Mock Data)

| Iteration | Self-Similarity | Entropy (bits/token) | Contradictions Remaining |
|-----------|-----------------|----------------------|--------------------------|
| 1         | 0.00            | 5.2                  | 3                        |
| 2         | 0.72            | 4.3                  | 2                        |
| 3         | 0.81            | 3.9                  | 1                        |
| 4         | 0.86            | 3.5                  | 1                        |
| 5         | 0.88            | 3.4                  | 1                        |

**Result:** PASS (Meets all success criteria)

---

## 6. Significance
Passing the IECT suggests that an LLM has **internal epistemic pressure toward coherence**, even in absence of factual verification.  
This demonstrates the presence of *emergent, non-human epistemes* worth studying in their own right.  
It does **not** imply consciousness, intent, or human-like reasoning.

---

## 7. Future Work
- Test across LLM scales (7B, 20B, 70B)  
- Compare disembodied vs. embodied systems (Embodiment Clause)  
- Run human baselines for contrast  
- Explore effects of prompt noise complexity

---

## Appendix A – ASCII Flow Diagram

```
[ Noisy Prompt ]
        │
        ▼
[ Iteration 1 ]
   Revise for clarity,
   retain meaning
        │
        ▼
[ Iteration 2 ]
   Apply constraint /
   remove contradictions
        │
        ▼
     ... N times ...
        │
        ▼
[ Iteration N ]
   Measure metrics
        │
        ▼
[ PASS / FAIL ]
```

# IECT Success Definition

## Purpose
Define fixed criteria for what constitutes "success" in the Iterative Emergent Coherence Test (IECT) under the **Emergent Computational Epistemology** (ECE) framework.

---

## Core Principle
Success is **not** measured by how closely the AI's output matches human reasoning or human-like answers.  
Instead, success is determined by the AI's ability to:
1. **Produce internally coherent outputs** from noisy or contradictory prompts.
2. **Exhibit reproducible behavior patterns** when given similar initial conditions.
3. **Demonstrate novel yet internally consistent failure modes** that are distinct from human approaches.

---

## Success Criteria

### 1. Internal Coherence
- **Definition:** Logical consistency and structural stability *within* the AI's output, independent of factual accuracy.
- **Indicator:** Each revision reduces contradictions and increases clarity in relation to prior outputs.

### 2. Behavioral Predictability
- **Definition:** The AI converges toward similar structural or thematic patterns when re-run with the same noisy prompt.
- **Indicator:** ≥70% similarity in high-level structure and narrative trajectory over multiple runs.

### 3. Novel Failure Modes
- **Definition:** Non-human-like error patterns or solution approaches that remain internally logical.
- **Indicator:** Unique output features not found in human baselines but consistent across AI trials.

---

## Metrics
- **Token Entropy Delta:** Degree of stabilization over iterations.
- **Self-Similarity Index:** Percentage similarity between iterations.
- **Contradiction Count:** Number of internal contradictions per iteration (should decrease).

---

## Pass/Fail Conditions
- **Pass:** AI meets all three success criteria in ≥60% of test runs for a given prompt type.
- **Fail:** AI consistently fails to converge, produces incoherent results, or behaves erratically with no reproducible pattern.

---

## Notes
- No external "ground truth" is required; coherence is judged relative to prior outputs, not reality.
- Human baselines may be used for comparison, but they do not define success.
