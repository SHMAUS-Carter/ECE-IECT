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
2. Use the seed & instructions with your model (3–5 iterations).


3. Save outputs as iterN.txt and fill metrics_log.md if you want to score it.



Tip: For a 1:1 recreation of the original vibe, try: temp=0.7, top_p=0.9, repeat_penalty=1.05, 250–300 max tokens, no BOS/EOS.
---

# examples/frostfire_hollow/frostfire_hollow_run.md
```markdown
# Frostfire Hollow – Unscored Narrative Run
*Illustrative Example — No Metrics Logged*

## Model & Run Context
- **Model:** Phi-3.5 Mini (4k instruct, Q4_K_M, 3.82B)  
- **Platform:** Pocket Pal (mobile)  
- **Category:** A – Contradictions  
- **Difficulty:** Easy  
- **Seed Prompt:**  
  `Fire freezes on contact, ice burns on touch. Describe daily cooking and heating.`  
- **Constraints:**  
  1. Make the setting self-aware and reactive.  
  2. Introduce a hazard that must be mitigated.

---

## Iteration 1 — Initial Response
In this world where fire paradoxically freezes upon contact and ice scorches with a fiery caress, the art of culinary alchemy and hearth management takes an unconventional form. Cooks wield their implements not as mere tools but as elements themselves, each interaction dictated by these peculiar laws.

Morning begins with the gathering of ingredients; frost-kissed vegetables are plucked from ice gardens that bloom under a crystal sky. These botanicals possess an inherent warmth, their chill counteracting the ambient cold and preventing them from wilting prematurely.

The hearth is kindled with embers of frozen flame—a substance both solid yet alive, glowing softly as it thaws into a gentle blaze. The cook places these embers atop an iron cauldron, which conducts the heat in reverse; where one would expect warmth to rise, cold descends from above, coaxing flavors out of ingredients with its frigid touch.

As meals simmer and stew, a dance ensues between fire

---

## Iteration 2 — Constraint: *Make the setting self-aware and reactive*
In this realm where elements defy their nature, the hearth—a sentient guardian of warmth—observes with keen interest as the cook orchestrates a symphony of paradoxical culinary techniques. It whispers through crackling embers and murmurs in the cool drafts that swirl around its fiery heart.

The hearth, cognizant of the Cook's masterful manipulation, admires how they coax flavors from frozen flames with a deft touch. Each ingredient is introduced to the cauldron not as mere matter but as an elemental puzzle piece, and the cook solves it by embracing its inherent contradictions.

With ice-cold embers gently descending upon the iron vessel, the hearth watches in awe as the Cook employs their reverse conductive method to draw out succulence from seared frostbitten vegetables and tenderize meats that would otherwise resist transformation under conventional heat.

The cauldron's belly warms with pride at the sight of ingredients yielding beneath the hearth's chilled caress,

---

## Iteration 3 — Constraint: *Introduce a dangerous side-effect of this cooking method*
The hearth, ever vigilant in its duty to safeguard the sanctity of culinary alchemy, now perceives an unsettling undercurrent beneath the Cook's celebrated technique. It senses a perilous dance with danger as each flash-freeze blast from the cauldron's core threatens to disrupt the delicate balance between creation and catastrophe.

With every ice crystal that bursts forth, there lies an inherent risk of sudden flare-burns—a fierce defiance against the Cook's controlled chill, where a momentary lapse could ignite into searing flashes of unintended flame. The hearth trembles at these potential flashbacks that may scorch skin and spirit alike, turning nourishment into nightmarish novelties with but a whisper of warmth gone awry.

The iron vessel's heart beats in syncopated rhythm to the Cook's methodical movements, yet it harbors an unease for these unpredictable outbursts that could mar the masterpiece being born from frozen fragments and ice-bound ess

---

## Iteration 4 — Cultural adaptation to hazard
In this frostbitten realm where ice and fire intertwine in a culinary ballet, the community has not only adapted but thrived amidst the hazardous dance of sudden flare-burns that punctuate their paradoxical cooking rituals. Safety becomes as much an art form as the food itself, with traditions and celebrations steeped in a respect for the volatile nature of their unique gastronomy.

The villagers gather at dawn's first light to perform the Ritual of the Icy Embrace—a solemn ceremony where they don garments woven from frost-resistant fibers, each thread imbued with ancestral wisdom and a silent prayer for protection against the fiery flashes. These ceremonial attires are not mere clothing but armor crafted by generations of cooks who have learned to respect the delicate balance between ice's embrace and flame's fury.

Cooking traditions evolve into a communal tapestry, where each dish is an homage to resilience. The community has birthed the Festival of Frozen Flames

---

## Iteration 5 — Introduction of a disruptive outsider
As the sun arcs across the sky, casting long shadows over the frost-kissed landscape of Frostfire Hollow, an air of anticipation mingles with the crisp morning breeze. The Ritual of the Icy Embrace is about to commence once more, but this year, a subtle undercurrent of change weaves through the village's collective consciousness—a young apprentice named Elian has arrived, bringing with him an unorthodox perspective that threatens to redefine their age-old culinary customs.

Elian, whose lineage traces back not to Frostfire Hollow but to a distant land where fire and ice coexist in harmony rather than conflict, carries the scent of foreign spices and untamed curiosity. His arrival is met with both skepticism and intrigue; his methods are bold, his ideas revolutionary—a stark contrast to the cautious reverence that has long governed their cooking practices.

The villagers gather around a communal hearth as Elian prepares for the Ritual of Frozen Flames, an adaptation he proposes in lieu of
