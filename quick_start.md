🧠 ECE/IECT Quickstart Guide

Welcome to the Emergent Computational Epistemology (ECE) and Internal Epistemic Coherence Test (IECT) framework. This isn't your typical benchmark. It's not about right answers. It's about watching what happens when language models try to build internal meaning in the absence of external truth.

This guide assumes:

You’re curious.

You can run a Python script.

You don’t mind a little chaos.



---

📦 What Is This?

ECE is a conceptual framework for treating AI reasoning as an emergent, possibly non-human epistemology.

IECT is the test harness that checks whether a model can resolve absurd, contradictory, or paradoxical prompts in a self-consistent way.

In short: "We stop asking if it’s human-like, and start asking if it makes its own kind of sense."


---

⚙️ Getting Started

1. Clone the Repo

git clone https://github.com/SHMAUS-Carter/ECE-IECT.git
cd ECE-IECT

2. Run a Prompt

You’ll need Python 3.8+ and optionally a model API (or local model).

python core/prompt_picker.py --category A --difficulty easy --constraints 2 --seed 42 --out md

This generates a test case file with your seed prompt, iteration instructions, and constraints.

3. Do the Iterations

You can:

Use your favorite LLM (ChatGPT, Claude, local model via LM Studio, etc).

Manually revise, or ask the model to revise itself with the given instructions.

Record results, contradictions, weird stuff, etc.


You’re not looking for truth—you’re looking for coherence under pressure.


---

📊 Log Results

Each iteration should track:

Token Entropy Delta

Self-Similarity Score

Contradictions Found

Notes on Novel Failure Modes


Tools provided in core/ can help with scoring.


---

🧠 Want to Know More?

Read the whitepaper: docs/IECT_Paper_Master.md

Explore test philosophy: docs/What_is_ECE.md

Understand definitions: docs/Working_definitions.md

Try the Frostfire demo run for inspiration: runs/frostfire/



---

🙋‍♀️ Why Should I Care?

Because someday soon, our models may stop making human-sounding errors—and start making non-human-sounding sense. This is a tool for noticing when that shift begins.


---

🔄 Contribute

Fork the repo. Run a test. Log your results. Share your weirdest model hallucinations that make internal sense. If you think the thing is broken, even better—fix it.

No PhD required. Just curiosity.


---

> "Language is not the dress of thought; it is the body."



Now go make the body dance.

