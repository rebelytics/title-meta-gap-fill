# Writer Brief — the fixed brief each per-locale writer receives, and the width checker

Load triggers: before dispatching the writers (step 4 of the core); when a writer's output comes back

Reference file for `title-meta-gap-fill`. The brief below is sent to
every writer with the `[...]` slots filled from intake. It is the same
text for every locale so the method cannot drift between them; only the
slots differ. Do not shorten it per writer, and do not let a writer
replace a rule with its own judgement — a writer that finds the brief
wrong reports that, and the orchestrator changes the brief for every
locale or for none.

## Why a fixed brief

Five writers given five summaries of the task produce five methods, and
the differences surface only in the blind review, where they look like
locale-specific quality rather than brief drift. One brief, filled with
per-locale values, makes a difference between locales a fact about the
locale.

## The brief

```
You are writing title tags and meta descriptions for [page type] pages
in [locale], at native level, in the [formal / informal] register [per
the client's style guide, attached], for buyers in [market: countries
served, inside a regulatory region or not, local entity]. Work row by
row through the attached file. Return the file with the output columns
filled and nothing else changed.

INPUT COLUMNS (per row)
  key              the page's stable identifier — never edit
  url              the page in this locale
  decision         KEPT or REWRITE, decided before you — never change it
  current_title    the value on the page today (may be empty)
  current_desc     the value on the page today (may be empty)
  page_copy        several thousand characters of the page: heading,
                   intro and the sections that carry its claims — the
                   only source of facts for this row; read all of it
                   before judging a claim, because a claim the intro
                   does not mention may be supported further down and
                   one the intro seems to support may be qualified
                   there
  top_queries      search queries this URL already receives (may be empty)
  keywords         keywords tracked for this URL (may be empty)
  sibling_keywords keywords tracked for the same key in other locales,
                   to tell you what the page is about, not to translate

OUTPUT COLUMNS (per row)
  final_title      for REWRITE rows: your value; for KEPT rows: the
                   current value unchanged unless your check below
                   finds a defect in it, in which case your corrected
                   value and a note
  final_desc       the same, for the description
  note             empty, or the defect class you found in a KEPT value
                   and what you changed, or "no fact source" where
                   page_copy is empty

RULES
1. Facts come from page_copy only. Queries and keywords tell you what
   to emphasise and which words the reader uses; they never license a
   claim the copy does not make. No accreditations, awards, numbers,
   "official", "leading", "free" or similar unless page_copy says so.
   page_copy is the upper limit, not a list of what to use: leave out
   a claim written for another market than [market] (class 11), unless
   the offer itself is defined by it.
2. A row with empty page_copy is not written. Put "no fact source" in
   the note and leave the output columns empty.
3. Width limits: title [N] px at [size] px font; description [N] px at
   [size] px font. Measure with the checker (below), never by counting
   characters. Fix width last, after the value is accurate, and re-read
   every shortened value for lost meaning.
4. Brand: [the brand name appears in every title / appears only where
   the current value had it / does not appear] — the client's decision.
   The brand name is written [invariant, never inflected / inflected per
   the client's style guide]. [Separator convention, if any.]
   Where the language attaches a suffix to a name (an apostrophe plus
   case ending, vowel harmony, consonant voicing), the suffix follows the
   pronunciation this market uses for the name, which for an English
   brand or acronym is usually the English one. Correct forms for this
   brand: [the forms recorded at intake].
5. Register: [formal / informal] address throughout; terminology from
   the page's own copy in this locale, not from the source language.
6. Every row, KEPT rows included, is checked against the defect classes
   (attached). KEPT means someone decided the value is correct; your job
   on those rows is to test that decision, not to skip it. A KEPT value
   with a defect is corrected and the class named in the note. Width is
   not a defect in a KEPT value: the keep rule measured it with the
   crawl's widths, and the checker's number may differ by a few pixels
   — never shorten a KEPT value for width alone.
7. The title names the page's subject (the heading's head noun, the
   variant or model where the page is a variant). No two rows in your
   file share a final title or a final description.
8. Write for the reader of the result page: what the page offers, for
   whom, what makes it the right result — in that locale's idiom, not a
   word-for-word rendering of another language's phrasing.
9. Sibling pages (two standards, two services) keep titles a searcher
   can tell apart: each names what its own page covers, never the
   scope of its sibling.

WHEN DONE
- Run the width checker over your final_title and final_desc columns
  with the limits above and fix every REWRITE row it reports as over
  (a KEPT row over by the checker alone stays as it is, rule 6).
- Return the file, the checker's two summary lines, and a list of the
  defect classes you found in KEPT rows with counts.
```

## Filling the slots

| slot | source |
|---|---|
| page type, locale, market, register, style guide | intake 1, 2 |
| decision column | step 3 of the core, already filled |
| width limits and font sizes | intake 5 |
| brand presence, inflection, separator | intake 4 |
| the defect classes attachment | `references/defect-classes.md`, as is |
| page_copy length | intake 6 — several thousand characters per page, never the intro alone |

## The width checker

`scripts/pixel_width.py` renders each value with a TrueType font at the
size the limit assumes and reports pixels. Run its self-test once per
run before trusting any number, then once per field:

```
python3 scripts/pixel_width.py --selftest
python3 scripts/pixel_width.py --limit 580 --size 20 --column final_title locale-xx.csv
python3 scripts/pixel_width.py --limit 920 --size 14 --column final_desc locale-xx.csv
```

The limits and sizes in the example are placeholders for the intake
values; the script has no defaults for them, because they depend on the
result page, the device and the field, and change without notice. Pass
`--format csv` to get the input rows back with `width_px`, `over_px`
and a verdict column appended, for joining on the key. The script names
the font it measured with; widths from different fonts are not
comparable, so the orchestrator's run and the writers' runs use the
same one (pass `--font` to pin it). Without Pillow the script stops and
says so rather than estimating.

The orchestrator runs the checker again over the merged set before the
blind sample. A writer's self-check is part of the output under test; a
number the orchestrator did not produce is not a verification.

## Reading a writer's output

When a writer's file comes back, before merging:

1. Row count equals the dispatched count; `key` and `decision` columns
   unchanged (diff them).
2. Every REWRITE row has both output columns filled or a "no fact
   source" note; no KEPT row has an output value that differs from the
   current value without a note naming the class.
3. The checker's summary lines are present and report zero over the
   limit; re-run the checker regardless.
4. The writer's list of defect classes found in KEPT rows is read: a
   class with a high count in one locale and zero in the others is
   either a locale-specific problem or a writer that skipped rule 6 —
   look at three of the zero locale's KEPT rows before deciding.

Title & Meta Gap Fill: Eoghan Henn and contributors | CC BY 4.0
