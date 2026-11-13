# Defect Classes — what goes wrong in titles and descriptions, with one generic example each

Load triggers: writing the writer brief (step 4 of the core); reading a review's findings (steps 5 and 7); before the correction pass (step 6)

Reference file for `title-meta-gap-fill`. This is the checklist a writer
applies to every row, kept and rewritten, and the grading scale the blind
reviewer uses. The list is open: every review that finds a class not
listed here adds it, and every correction pass writes its check against
these names so the counts are comparable between runs and locales.

The same classes recur across languages. A run over many locales finds
the same handful in each, so the correction pass is written once per
class and run per locale, not reinvented per writer.

## The classes

### 1. Wrong service or product type

The value names a sibling offer instead of the page's own: a "repair"
page titled as "replacement"; a "hire" page titled as "sale"; a
"course" page titled as "exam"; an "inspection" page titled as
"installation". The nouns are near each other in the writer's mind and
far apart for the reader, who lands on a page that does not offer what
the title promised.

- Example: a page whose copy describes bicycle hire by the day carries
  the title "Bicycles for sale".
- Check: a per-locale term list of the offer types the site
  distinguishes, matched against the page copy's own type word.

### 2. Claims beyond the page copy

The value asserts something the page does not say: an award, a
number, "market leader", "official retailer", "free delivery", a
registration number credited to the wrong entity. Keywords and
competitor snippets are where these come from; the page is the only
place they may come from.

- Example: the description says "official retailer with free delivery"
  on a page whose copy mentions neither.
- Check: a list of claim words per locale (accredited, certified,
  official, leading, award, numbers with units) matched against the
  page copy; a hit in the value with no support in the copy is a
  defect.

### 3. Calques

A word-for-word transfer from the source language that is grammatical
and unidiomatic: the reader understands it and knows it was translated.
Machine translation and non-native writers produce these at the same
rate; a native reader spots them in a second.

- Example: a phrasal construction native to the source language
  rendered literally, where the target language says it with a single
  verb.
- Check: no mechanical test. The blind reviewer's native read is the
  check, which is why the reviewer is native-level and blind.

### 4. Inflected brand names

The brand name carries a case ending, a possessive suffix or a plural
marker that the brand's own convention forbids. Languages with case
systems inflect every noun in a sentence, and a fluent writer inflects
the brand with them; the brand's style says it stays invariant.

- Example: a genitive or dative ending attached to the brand name in a
  title, where the brand writes itself the same in every case.
- Check: a pattern for the brand name followed by anything other than a
  space, punctuation or the end of the value; the intake records which
  convention the client follows, since some brands do inflect.
- Where the brand does take a suffix, the second shape is a suffix
  chosen by the wrong pronunciation: a name read letter by letter in the
  local alphabet when the market says it the English way, so harmony and
  voicing come out wrong. Writers and blind reviewers both miss it, so
  record the correct forms at intake and put the wrong ones on the term
  list the correction pass searches for in every row.

### 5. Meaning lost when shortening

A value cut to fit the width limit dropped the qualifier that made it
accurate: "for masonry" gone, so the title now claims a general-purpose
tool; "used" gone, so the listing reads as new. Width fixing is where
accurate values become wrong ones, and it happens last, after the
accuracy check.

- Example: "Cordless hammer drill for masonry, 18 V" shortened to
  "Cordless drill", losing both the tool class and the material.
- Check: every row the width checker reported as over the limit before
  the final pass is re-read for meaning after it; a diff of the two
  values shows what was cut.

### 6. Wrong register

The value addresses the reader in the wrong form (informal where the
client's style is formal, or the reverse), or in a tone the page does
not use. One wrong register in a set of formal pages reads as a
different company.

- Example: the informal second-person form in a locale whose style
  guide prescribes the formal one.
- Check: a per-locale pattern for the forms of address and their verb
  endings, matched against the intake's register.

### 7. Wrong page subject

The value describes a different page: a neighbouring product, the
category instead of the item, the parent service instead of the
variant. The join key was right and the writer's eye slipped a row, or
the copy column held another page's text.

- Example: the title of the 200-litre variant on the 50-litre
  variant's row.
- Check: the page's subject term (the heading's head noun, the model or
  variant identifier) must appear in the title.

### 8. Duplicate values

Two or more pages in the same locale carry the same final title or the
same final description. Templates produce this on purpose and the keep
rule may have preserved it; the result page shows one of them.

- Example: every variant page of a product keeps the parent product's
  title.
- Check: group by locale and value; any group larger than one is
  listed with its keys.

### 9. Wrong language

A value in a language other than the locale's: an untranslated source
value kept because it existed and fit, or a writer's slip into the
source language for a term.

- Example: the source-language title retained on the translated page
  because the keep rule checked existence and width but not language.
- Check: a language-identification pass over every final value, with
  short values (under five words) read by hand where the identifier is
  unsure.

### 10. Template artefacts

Placeholders, separators and pipe characters left from a template, a
doubled brand suffix, a trailing separator where the generator ran out
of values.

- Example: "Garden hose reel | | Brand".
- Check: a pattern for doubled separators, leading or trailing
  separators, braces and placeholder tokens.

### 11. Written for another market

The value carries a claim the page supports that is written for another
market: another country's regulator or trade body, a sister entity of
another market, a regional law where that region's law does not apply,
an approval every provider in the market must hold, sold as an
advantage. Local pages are often translated from the head-office
language without being adapted, so the copy itself carries these. The
page copy is the upper limit on facts, not the list of what to use:
every claim must mean something to a buyer in the locale's market
(intake 2). A reference stays only where the offer itself is defined by
it, such as a regional regulation the product exists to comply with.

- Example: a description on one country's site that closes with "your
  partner across the region" and names a sister entity of another
  market, both lifted from the translated copy.
- Check: a per-locale list of the bodies, entity names and laws the
  final values cite, matched against that locale's market. Writers run
  it in the writing pass, not as a late extra round.

### 12. Impartiality wording

A provider says it "supports", "helps with" or "guides you to" an
approval, grade or decision it issues itself — an examiner, an inspector,
a notary, an assessor — so the verb claims a service the role forbids.

- Check: a per-locale list of advisory verbs, run over every value of a
  page whose offer is a decision the provider makes.

### 13. Regional variant against the page copy

A locale serving several markets is written in one market's variety
while the page copy uses another. The rule is recorded at intake:
neutral where the varieties share a term, the main market's where they
do not.

- Check: the variety's marker words against the page copy, per locale.

### 14. Generic term for an official standard

A regulated thing is named by its everyday word where the market searches
for its official title or local acronym — a qualification, a vehicle
class, a tax form, a safety rating.

- Check: a per-locale glossary of official names, collected at intake.

### 15. Audit term of the wrong kind

A term with two professional meanings taken from the wrong profession: an
inspection written with the accountant's "audit", a medical appointment
written as a "consultation", a software "licence" written as a permit. The
page's own H1 and copy decide per page, unless they are obviously wrong.

- Check: the term in each value against the term in its page's H1.

## Using the list

- **Writers** read the list before the first row and apply every class
  to every row, kept rows included; the brief in
  `references/writer-brief.md` says so in its own words.
- **Reviewers** grade each row they receive with the class numbers above and
  add a named class for anything the list lacks; the brief in
  `references/reviewer-brief.md` carries the grading form.
- **The correction pass** (step 6 of the core) writes one check per
  class found, using the "Check" line of that class as its starting
  point, runs it over every row in every locale, and records the count
  per class and locale. The checks are kept with the run: they are the
  regression suite for the next one.
- **A country reviewer finds classes, not rows.** A class one reviewer
  finds in one locale is checked in every locale before the corrected
  file goes back, and a value changed after review gets a regenerated
  Why explanation, never the old one.

Title & Meta Gap Fill: Eoghan Henn and contributors | CC BY 4.0
