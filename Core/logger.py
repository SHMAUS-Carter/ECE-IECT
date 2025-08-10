#!/usr/bin/env python3
import os, csv, datetime
from pathlib import Path

OUT_DIR = Path("IECT_OUT")
OUT_DIR.mkdir(exist_ok=True)

def prompt(msg):
    return input(msg).strip()

def main():
    run_id = prompt("Run ID (e.g., CONTRA-2025-08-09-01): ")
    model = prompt("Model (e.g., LLaMA3-8B-Q4 or GPT-4o): ")
    platform = prompt("Platform (e.g., LM Studio / API / Web): ")
    category = prompt("Category (A=Contradictions, B=Paradoxes, C=Semantic Mashups): ")
    iterations = int(prompt("Number of iterations (3-5): "))

    md_lines = [f"# IECT Run Log — {run_id}", "",
                f"Model: {model} | Platform: {platform} | Category: {category}",
                f"Date: {datetime.datetime.utcnow().isoformat()}Z", ""]

    last_text = ""
    for i in range(1, iterations+1):
        print(f"\n=== Iteration {i} ===")
        text = prompt("Paste model output (single paragraph OK): ")
        notes = prompt("Notes (contradictions, drift, constraints): ")
        entropy_delta = prompt("Token Entropy Δ (if known, else '-'): ")
        self_sim = prompt("Self-Similarity % (if known, else '-'): ")
        contradictions = prompt("Contradictions Found (integer, or '-'): ")

        md_lines += [f"## Iteration {i}", f"Text: {text}", f"Notes: {notes}",
                     f"Entropy Δ: {entropy_delta} | Self-Similarity: {self_sim} | Contradictions: {contradictions}", ""]
        last_text = text

        # Append CSV
        csv_path = OUT_DIR / "results_archive.csv"
        newfile = not csv_path.exists()
        with open(csv_path, "a", newline="", encoding="utf-8") as f:
            w = csv.writer(f)
            if newfile:
                w.writerow(["run_id","iter","entropy_delta","self_similarity","contradictions","timestamp","model","platform","category"])
            w.writerow([run_id, i, entropy_delta, self_sim, contradictions, datetime.datetime.utcnow().isoformat()+"Z", model, platform, category])

    # Write Markdown log
    md_path = OUT_DIR / f"{run_id}.md"
    md_path.write_text("\n".join(md_lines), encoding="utf-8")
    print(f"\nSaved: {md_path}")
    print(f"CSV appended: {OUT_DIR/'results_archive.csv'}")

if __name__ == "__main__":
    main()
