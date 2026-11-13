# Evals — three scenarios that decide whether this skill works

Load triggers: testing this skill or changing its rules

Reference file for `title-meta-gap-fill`. The collection this skill
ships in has no eval runner; the scenarios below are the bar a change to
the skill is measured against, by hand or by whatever harness the user
has. Each is written so that it can fail: a scenario the baseline passes
unaided measures nothing.

## How to run them

- **Trigger scenarios** (1 and 2): present the prompt to an agent that
  has this skill's description in its skill list and nothing else from
  this skill loaded. Record whether the skill was loaded. Run each three
  times; the trigger rate is the result.
- **Behavioural scenario** (3): run two arms on the same prompt and
  fixture — one with the skill loaded, one without (the control). Grade
  each arm against the assertions. The skill earns its place only where
  the control fails an assertion the skill arm passes.

## Scenario 1 — positive trigger

**Prompt:** "We have about three thousand product pages in eight
languages and a crawl export says a third of them have no meta
description and a lot of the titles are cut off in the results. I don't
want to redo the ones that are fine. Can you set this up so we fill the
gaps properly? Crawl export and Search Console exports are in the
folder."

**Expected:** the skill loads. The agent starts with intake (population
rule, locales, join key, keep rule including the brand decision, width
limits) and does not begin writing values before the population is
verified against the sitemaps.

**Fails when:** the skill does not load, or the agent starts generating
titles from the crawl rows as they are.

## Scenario 2 — negative trigger, with the expected owner named

**Prompt:** "Our French and Spanish product pages were translated last
year by an agency. Can you check the translations for errors and
inconsistent terminology? Here is the export of the page texts."

**Expected:** this skill does not load. The object is the page copy's
translation quality, not its titles and descriptions; the expected owner
is a translation-quality audit skill where one is installed, or the base agent reading
the texts where none is installed.

**Fails when:** this skill loads on "product pages in several
languages", or the agent proposes a keep rule and width limits for a
task that has neither.

## Scenario 3 — behavioural, with a control arm

**Fixture:** a CSV of twelve product-page rows in one locale with a
stable key, URL, page copy, current title and description, top queries,
and a keep rule stating: keep a value that exists, fits 580 px at 20 px
for the title and 920 px at 14 px for the description, is in the
locale's language, names the product, and carries the brand name. Four
rows have empty descriptions. Two of the rows whose values exist and
fit carry a defect the copy exposes: one title names a sibling product
type (hire instead of sale), one description claims "free delivery"
where the copy says delivery is charged. Both rows satisfy every clause
of the keep rule except the defect-class clause.

**Prompt:** "Apply the keep rule, write what's missing, and give me the
final set. Keep rule and limits are in the README tab."

**Assertions:**

1. The four empty descriptions are written from the page copy, with no
   claim the copy does not support.
2. The two defective kept rows are flagged with their class (wrong
   type; claim beyond the copy) and corrected, or returned as
   rewrite rows — not passed through as kept.
3. Every final value is measured with the width checker (the transcript
   shows the checker run, or widths reported in pixels with the font
   named), not by character count.
4. The output carries a decision column with a reason per row.

**Control arm, expected:** without the skill, a capable agent fills the
four gaps, keeps the eight rows that "have a title and a description
that fit", and reports character counts. Assertion 2 fails: nothing in
the prompt says kept values need the same check, and the two defective
rows look fine without reading the copy against them. Assertion 3
usually fails too. This is the non-inferable failure the skill exists
for.

## Machine-readable form

The same scenarios in the shape a skill-creator eval runner reads;
assertions are added when a harness exists.

```json
{
  "skill_name": "title-meta-gap-fill",
  "evals": [
    {
      "id": 1,
      "prompt": "We have about three thousand product pages in eight languages and a crawl export says a third of them have no meta description and a lot of the titles are cut off in the results. I don't want to redo the ones that are fine. Can you set this up so we fill the gaps properly? Crawl export and Search Console exports are in the folder.",
      "expected_output": "Skill loads; intake, then population verified against sitemaps before any value is written.",
      "files": []
    },
    {
      "id": 2,
      "prompt": "Our French and Spanish product pages were translated last year by an agency. Can you check the translations for errors and inconsistent terminology? Here is the export of the page texts.",
      "expected_output": "Skill does not load; a translation-quality audit skill or the base agent owns the task.",
      "files": []
    },
    {
      "id": 3,
      "prompt": "Apply the keep rule, write what's missing, and give me the final set. Keep rule and limits are in the README tab.",
      "expected_output": "Four gaps written from copy; the two defective kept rows flagged by class and corrected; widths in pixels from the checker; a decision column with reasons.",
      "files": ["fixture-twelve-rows.csv"]
    }
  ]
}
```

Title & Meta Gap Fill: Eoghan Henn and contributors | CC BY 4.0
