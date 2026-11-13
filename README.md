# title-meta-gap-fill

Open-source skill that **completes title tags and meta descriptions across a large page set without rewriting what already works**: it defines the page population by URL shape, verified against the sitemaps, joins crawl widths, page copy, queries and keywords on a stable key, applies an explicit keep rule, runs one native-level writer per locale with a fixed brief and a pixel-width checker, then a blind read of every final value by one reviewer per locale (a stratified sample only on very large sets), a correction pass over every row for the classes found, and a blind re-review. Its one rule above the others: the review runs on final values, not on changes — a keep decision is a claim that the value is correct, and it needs the same check as a rewrite. Load it into any MCP-capable AI agent (Claude, Cursor, Codex, n8n, etc.).

Part of the [Open Skill Library](https://github.com/rebelytics/one-skill-to-rule-them-all/blob/main/OPEN-SKILL-LIBRARY.md), the open-source agent skills maintained with Task Observer.

## When it triggers

When the user wants titles or meta descriptions written, completed, fixed or localised for product, category, service or article pages; mentions missing, duplicate, truncated or machine-translated titles or descriptions; or asks for a multilingual metadata rewrite or SERP snippet work at scale. H1s and image alt text follow the same loop.

## What this repo contains

- `SKILL.md` — the intake parameters that change per run, the seven steps (population by URL shape, the stable-key join, the keep rule as a column, one writer per locale, the blind read, the correction pass, the blind re-review), the hand-off format, the pre-flight, and the pointer list for the reference files.
- `references/writer-brief.md` — the fixed brief every per-locale writer receives, and how the width checker is run.
- `references/reviewer-brief.md` — the blind reviewer's brief, the full-read default and the sampling rule for the fallback.
- `references/defect-classes.md` — the defect classes with one generic example each; the checklist writers apply to every row and reviewers grade against.
- `references/evals.md` — three evaluation scenarios for this skill.
- `references/ceilings.txt` — line ceilings for the reference files, read by the skill validator.
- `scripts/pixel_width.py` — the width checker: renders each value with a TrueType font at the size the limit assumes and reports pixels (requires Pillow).
- `LICENSE` — CC BY 4.0.

## Install

Install the whole skill directory — `SKILL.md`, `references/` and `scripts/` must travel together — into your MCP-capable agent's skills directory, following the client-specific path, and restart the client.

## Contributing

Open an issue or a PR at [github.com/rebelytics/title-meta-gap-fill](https://github.com/rebelytics/title-meta-gap-fill).

## Credits

- Original author: [Eoghan Henn](https://www.rebelytics.com) / [LinkedIn](https://www.linkedin.com/in/eoghanhenn)

## License

CC BY 4.0 — the licence text is in [LICENSE](./LICENSE): the full legal code, unmodified, as Creative Commons publishes it; the [human-readable summary](https://creativecommons.org/licenses/by/4.0/) says what it allows. Use it, fork it, adapt it, monetise it. Keep the attribution.

Copyright (c) 2026 Eoghan Henn / rebelytics.com
