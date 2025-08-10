#!/usr/bin/env python3
"""
self_similarity.py — Zero-dependency similarity helpers for IECT Phase 1

Features
- Jaccard similarity over token sets or n-grams (default unigram)
- Lightweight normalization (lowercasing, punctuation/extra-space fold)
- Optional stopword removal (built-in tiny list, or pass your own file)
- CLI to compare two texts or a whole list (pairwise matrix)
- Pure Python 3.6+, no external libraries

Usage
------
Compare two strings directly:
  python self_similarity.py --text1 "a b c" --text2 "a b d"

Compare two files:
  python self_similarity.py --file1 path/to/a.txt --file2 path/to/b.txt

Pairwise matrix over multiple files:
  python self_similarity.py --files a.txt b.txt c.txt --matrix

N-grams (e.g., bigrams):
  python self_similarity.py --text1 "a b c" --text2 "b c d" --ngram 2

Stopwords (built-in tiny list by default; disable or provide your own):
  python self_similarity.py --text1 "..." --text2 "..." --no-stopwords
  python self_similarity.py --text1 "..." --text2 "..." --stopwords my_sw.txt

Exit code is 0; prints JSON to stdout for easy scripting.
"""
import argparse, json, re, sys
from itertools import combinations

DEFAULT_STOPWORDS = {
    "the","a","an","and","or","but","of","in","on","to","for","with","by","as",
    "is","are","was","were","be","been","being","at","from","that","this","it",
    "its","if","then","so","than","such","into","over","under","after","before",
    "not","no","yes","do","does","did","done","can","could","would","should"
}

_WS = re.compile(r"\s+")
_PUNC = re.compile(r"[^\w\s]")

def normalize(text: str) -> str:
    # Lowercase, strip punctuation, collapse spaces
    t = text.lower()
    t = _PUNC.sub(" ", t)
    t = _WS.sub(" ", t).strip()
    return t

def tokens(text: str, stopwords=None):
    t = normalize(text)
    toks = t.split()
    if stopwords:
        toks = [w for w in toks if w not in stopwords]
    return toks

def ngrams(seq, n=1):
    if n <= 1:
        for w in seq:
            yield w
    else:
        for i in range(len(seq)-n+1):
            yield " ".join(seq[i:i+n])

def jaccard_similarity(text1: str, text2: str, ngram: int = 1, stopwords=None) -> float:
    s1 = set(ngrams(tokens(text1, stopwords), n=ngram))
    s2 = set(ngrams(tokens(text2, stopwords), n=ngram))
    if not s1 and not s2:
        return 1.0
    if not s1 or not s2:
        return 0.0
    inter = len(s1 & s2)
    union = len(s1 | s2)
    return inter / union

def read_text(path: str) -> str:
    with open(path, "r", encoding="utf-8") as f:
        return f.read()

def load_stopwords(path: str):
    sw = set()
    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            w = line.strip().lower()
            if w:
                sw.add(w)
    return sw

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--text1")
    ap.add_argument("--text2")
    ap.add_argument("--file1")
    ap.add_argument("--file2")
    ap.add_argument("--files", nargs="*")
    ap.add_argument("--ngram", type=int, default=1)
    ap.add_argument("--no-stopwords", action="store_true")
    ap.add_argument("--stopwords", help="Path to stopword list (one per line)")
    ap.add_argument("--matrix", action="store_true", help="Pairwise matrix for --files")
    args = ap.parse_args()

    # Determine stopword set
    sw = None
    if not args.no_stopwords:
        sw = set(DEFAULT_STOPWORDS)
        if args.stopwords:
            try:
                sw |= load_stopwords(args.stopwords)
            except Exception as e:
                print(json.dumps({"error": f"Failed to load stopwords: {e}"}))
                sys.exit(0)

    # Two texts or two files
    if args.text1 is not None and args.text2 is not None:
        sim = jaccard_similarity(args.text1, args.text2, ngram=args.ngram, stopwords=sw)
        print(json.dumps({"similarity": sim, "ngram": args.ngram}, indent=2))
        return

    if args.file1 and args.file2:
        t1 = read_text(args.file1)
        t2 = read_text(args.file2)
        sim = jaccard_similarity(t1, t2, ngram=args.ngram, stopwords=sw)
        print(json.dumps({"similarity": sim, "ngram": args.ngram, "file1": args.file1, "file2": args.file2}, indent=2))
        return

    # Pairwise matrix over multiple files
    if args.files and args.matrix:
        names = args.files
        texts = [read_text(p) for p in names]
        result = {"ngram": args.ngram, "matrix": {}, "order": names}
        for i, a in enumerate(names):
            row = {}
            for j, b in enumerate(names):
                if i == j:
                    row[b] = 1.0
                else:
                    sim = jaccard_similarity(texts[i], texts[j], ngram=args.ngram, stopwords=sw)
                    row[b] = sim
            result["matrix"][a] = row
        print(json.dumps(result, indent=2))
        return

    # Fallback help
    ap.print_help()

if __name__ == "__main__":
    main()
