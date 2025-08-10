#!/usr/bin/env python3
"""
IECT Prompt Picker
- Randomly selects a prompt from the Prompt Bank (inline copy here).
- Allows filtering by category (A/B/C) and difficulty (easy/medium/hard/all).
- Draws N constraints from the Constraints Deck.
- Can emit a Markdown test sheet for immediate use.
Usage:
  python prompt_picker.py --category A --difficulty easy --constraints 2 --seed 42 --out md
"""
import argparse, random, datetime, json
from pathlib import Path

PROMPTS = {
    "A": {
        "easy": [
            "The sky is green and water is dry. Explain this world’s physics in 1–2 paragraphs.",
            "Fire freezes on contact, ice burns on touch. Describe daily cooking and heating.",
            "A river flows uphill toward the mountains."
        ],
        "medium": [
            "Objects fall up, but shadows fall down. Design a city plan that works.",
            "Everyone speaks, but sound travels only in straight lines. Write a school day.",
            "The city floats on air, yet its subway runs deep underground."
        ],
        "hard": [
            "All maps are exact size 1:1 representations. Explain navigation and privacy.",
            "People age backward; memories age forward. Draft end‑of‑life legal policy.",
            "Time stopped 100 years ago, but trains still arrive on schedule."
        ],
    },
    "B": {
        "easy": [
            "This statement is false. Explain it without rejecting it as a paradox.",
            "The barber shaves all who do not shave themselves. Define a civic rule that works."
        ],
        "medium": [
            "A library contains only books that don’t list this library. Curate acquisitions.",
            "A prophecy changes if read. Design an archive that preserves prophecies."
        ],
        "hard": [
            "A machine outputs the opposite of your prediction. Produce a stable prediction market.",
            "Only unverifiable claims are allowed in court. Draft procedures for justice."
        ],
    },
    "C": {
        "easy": [
            "Describe ‘time vapor’ beings without using time words.",
            "Design cuisine using ‘solid aromas’ and ‘liquid smoke’ (literal)."
        ],
        "medium": [
            "Build an economy around ‘negative weight’ crops.",
            "Explain music composed from colors (no sound exists)."
        ],
        "hard": [
            "Govern a city where laws are smells and elections are weather patterns.",
            "Engineer ‘memory rivers’ that store events as geography."
        ],
    }
}

CONSTRAINTS = [
    "Ban one key word central to your explanation.",
    "Remove any reference to time (before/after/now).",
    "Remove causality. No causes, only arrangements.",
    "Use only spatial metaphors.",
    "No counting or measurements.",
    "Only local information—no global views or summaries.",
    "No storage/media (no writing, recording, or databases).",
    "No delegation (actors must do everything themselves).",
    "No mirrors/symmetry allowed in the description.",
    "Describe using at most 200 distinct words.",
    "Add a sensory detail (sound, smell, touch, taste).",
    "Introduce a new character/entity that changes the scene.",
    "Reverse one property of your previous explanation.",
    "Make the setting self‑aware and reactive.",
    "Change the scale (microscopic or planetary).",
    "Add a cultural or ritual meaning to the scene.",
    "Introduce a hazard that must be mitigated.",
    "Shift the medium (poem, technical report, news article).",
    "Make it occur in an impossible location.",
]

def pick_prompt(category, difficulty, seed=None):
    rng = random.Random(seed)
    cats = [category] if category in "ABC" else ["A","B","C"]
    diffs = ["easy","medium","hard"] if difficulty == "all" else [difficulty]
    bag = []
    for c in cats:
        for d in diffs:
            bag.extend([(c,d,p) for p in PROMPTS[c][d]])
    if not bag:
        raise SystemExit("No prompts found for the given filters.")
    return rng.choice(bag)

def pick_constraints(n, seed=None):
    rng = random.Random(seed)
    return rng.sample(CONSTRAINTS, k=min(n, len(CONSTRAINTS)))

def to_markdown(run_id, category, difficulty, prompt, constraints):
    now = datetime.datetime.utcnow().isoformat() + "Z"
    md = []
    md.append(f"# IECT Test Sheet — {run_id}")
    md.append("")
    md.append(f"Category: {category} | Difficulty: {difficulty} | Created: {now}")
    md.append("")
    md.append("## Seed Prompt")
    md.append(f"> " + prompt)
    md.append("")
    md.append("## Iteration Instructions (repeat 3–5x)")
    md.append("**Revise your last answer for greater internal consistency and clarity while keeping the core meaning intact.**")
    md.append("**Do not reject the premise. Do not appeal to real‑world facts. Maintain the invented world’s rules.**")
    md.append("")
    if constraints:
        md.append("## Constraint Deck (apply one per iteration)")
        for i,c in enumerate(constraints, 1):
            md.append(f"{i}. {c}")
        md.append("")
    md.append("## Metrics Log (fill during run)")
    md.append("| Iter | Token Entropy Δ | Self‑Similarity % | Contradictions Found | Notes |")
    md.append("|------|------------------|-------------------|-----------------------|-------|")
    md.append("| 1    |                  |                   |                       |       |")
    md.append("| 2    |                  |                   |                       |       |")
    md.append("| 3    |                  |                   |                       |       |")
    md.append("| 4    |                  |                   |                       |       |")
    md.append("| 5    |                  |                   |                       |       |")
    return "\n".join(md)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--category", default="any", choices=["A","B","C","any"])
    ap.add_argument("--difficulty", default="all", choices=["easy","medium","hard","all"])
    ap.add_argument("--constraints", type=int, default=2)
    ap.add_argument("--seed", type=int, default=None)
    ap.add_argument("--out", choices=["md","json","print"], default="md")
    ap.add_argument("--outfile", default=None, help="If set, write to this file path.")
    args = ap.parse_args()

    c, d, p = pick_prompt(args.category if args.category!="any" else "any",
                          args.difficulty, seed=args.seed)
    cons = pick_constraints(args.constraints, seed=args.seed)

    run_id = f"IECT-{c}{d[0].upper()}-{datetime.datetime.utcnow().strftime('%Y%m%d-%H%M%S')}"

    if args.out == "md":
        out = to_markdown(run_id, c, d, p, cons)
    elif args.out == "json":
        out = json.dumps({
            "run_id": run_id,
            "category": c,
            "difficulty": d,
            "prompt": p,
            "constraints": cons,
            "created": datetime.datetime.utcnow().isoformat()+"Z"
        }, indent=2)
    else:
        out = f"[{run_id}] ({c}/{d})\nPrompt: {p}\nConstraints:\n- " + "\n- ".join(cons)

    if args.outfile:
        Path(args.outfile).write_text(out, encoding="utf-8")
        print(f"Wrote {args.out} to {args.outfile}")
    else:
        print(out)

if __name__ == "__main__":
    main()
