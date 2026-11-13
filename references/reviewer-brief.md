# Reviewer Brief — the blind review, the full-read default, its sampling fallback, and how to read the result

Load triggers: before the blind read (step 5 of the core); before the re-review (step 7)

Reference file for `title-meta-gap-fill`. The review's job is to find
the defects present in the final values, so that the correction pass
can remove each class from every row. It is not to fix the rows it
reads for their own sake, and it is not to compare old with new.

## Blind means three things

1. **Not the writer.** The reviewer did not write any of the values
   under review and has not seen the writer brief's reasoning for them.
   A writer re-reading its own rows re-reads its own decisions.
2. **No decision column.** The reviewer does not know which rows were
   kept and which rewritten. A reviewer who knows a row was kept reads
   it as "someone already checked this" and grades it lighter; the
   whole point of the run is that kept values get the same read.
3. **No old value.** The reviewer sees the final value and the page
   copy, nothing to compare against. "Better than before" is not the
   bar; "correct for this page in this language" is.

The orchestrator keeps the stratification and the decision column on
its side, joined back by key after the review returns.

## The default: every row, one reviewer per locale

The deliverable ships verbatim, so every final value gets a reviewer's
read: one native-level reviewer per locale, not the writer, reads all
rows of that locale with the brief below. The read is organised by
locale, never by class, so a row is graded once against every class.
Reviewers receive the rows in batches small enough to read with
attention; the batch size is recorded so a later run can repeat it. The
failure shape this closes: a clean second sample is reported as a clean
set, and a later full read finds a few percent of the values wrong,
most of them kept values no sample drew.

## The sampling rule (fallback for very large sets only)

Use this route only when a full read per locale does not fit the run's
budget — a judgement, recorded in the README with the row count.
Stratify by **locale × page subtype × decision (kept / rewritten)** and
draw within each cell, so that every locale, every subtype and both
decisions are represented in proportion to the set, with a floor so the
small cells are not skipped:

- at least 20 rows per locale, or every row where the locale has fewer;
- within a locale, kept and rewritten rows in proportion to their
  counts, with a floor of 5 of each where both exist;
- subtypes in proportion, with a floor of 3 each.

The sample is read for classes, so its size is set by how rare a class
must be to be missed: a class present in 5 % of rows is almost certain
to appear in a 100-row sample and about even odds in a 15-row one.
Record the size and the seed or selection method so the second sample
can be drawn as a disjoint set from the same population.

**Re-review (step 7):** after a full read, a reviewer who made none of
the corrections re-reads every corrected value plus a random sample of
untouched rows, same brief. After the sample route, a second sample:
same stratification, same floors, rows not in the first sample. Same
brief; the reviewer may be the same person or agent, since the rows are
new.

## The brief

```
You are reviewing title tags and meta descriptions for [page type]
pages in [locale], as a native-level reader serving [market]. For each
row you receive the page's URL, several thousand characters of the
page's own copy (heading, intro and the sections that carry its
claims), the final title and the final description. You do not receive
the previous values or any history, and you should not look for them.

Grade each row on the attached defect classes. For every defect, give
the class number and one line saying what is wrong. A row may carry
several. A row with none is marked OK.

Three things to hold to:
- The page copy is the only source of truth. A claim in the title or
  description that the copy does not support is a defect (class 2)
  even where it is probably true. One the copy supports but that is
  written for another market than [market] is a defect too (class 11).
- Read as the reader of a result page in this language would. A
  grammatical sentence that no native writer would produce is a defect
  (class 3). Register that does not match [formal / informal] is a
  defect (class 6).
- Do not fix anything. Your output is the grade and the reason; the
  fix runs over the whole set, not over your rows.
- Width is not your grade. Do not flag or shorten a value for its
  length; widths are measured elsewhere, and a value that reads a few
  pixels over on one instrument may be within the limit on the one
  that decided it.

If you find a defect that fits no listed class, name it (a short label
and one line) and grade it as class NEW-<label>.

Return the file with columns: key, title_grade, title_reason,
desc_grade, desc_reason. Grades are OK, or the class numbers separated
by commas.
```

Attach `references/defect-classes.md` as it stands. Fill the slots from
intake 1, 2 and 4.

## Reading the result

1. **Tabulate by class and locale**, not by row: a table with one row
   per class found, columns per locale, cells the count among the rows
   read. Append the class's rate (count over rows read in that locale).
2. **Every class with a non-zero cell goes to the correction pass**
   (step 6 of the core), including a class found once. The review is a
   detector; the whole set is where the class lives, and after a full
   read the class check still runs over every row, because a reader
   who found three cases is not proof there was no fourth.
3. **A `NEW-` class is added to `references/defect-classes.md`** with a
   generic example and a check line, before the correction pass, so
   the pass has a name and a check to run.
4. **Compare kept against rewritten** after joining the decision column
   back in. A class concentrated in kept rows means the keep rule
   admitted it; tighten the rule's wording in the README. A class
   concentrated in rewritten rows means the writer brief did not stop
   it; the brief changes for every locale.
5. **A locale with a clean read and a non-trivial count** is not
   exempt from the correction pass: the pass is written per class and
   runs over every locale, because a class the reviewer missed in one
   locale is found there by the check written from another.
6. **The re-review ships the run only when** every corrected class
   shows zero in it. Any non-zero cell for a corrected class means the
   check was too narrow — widen it, rerun step 6, re-review again. A
   new class means another correction pass and another re-review. A
   clean re-review is reported as "no defects in N re-read rows" (or "N
   sampled rows"), never as "0 wrong" for the set: only a full read of
   every row supports a claim about every row.

## What the review is not

- Not a comparison with the previous values; the previous values may
  have been worse, and that is not the bar.
- Not a keyword audit; whether a value carries the tracked keyword is a
  writer-brief question, checked mechanically, not a reviewer's grade.
- Not a hand-fix of the rows read; every finding is a class, and
  every class is corrected set-wide.
- Not a width check. A kept value is judged by the crawl's width and a
  rewrite by the checker's (core, step 4); a reviewer who rewrites a
  kept value for width alone changes a correct value for nothing.

Title & Meta Gap Fill: Eoghan Henn and contributors | CC BY 4.0
