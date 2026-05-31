# PaperHub: Trusted and Efficient Computing Paper Notes

PaperHub is a MkDocs-based academic notes site focused on top systems and architecture conferences.
The current collection centers on trusted and efficient computing topics, including hardware security,
memory reliability, homomorphic encryption, LLM inference acceleration, PIM, and quantum architecture.

- Online site: https://xuanway.github.io/paperhub/
- Repo: https://github.com/xuanway/paperhub

## Current Coverage

- HPCA 2025: 19 papers
- HPCA 2026: 15 papers
- ISCA 2025: 8 papers
- MICRO 2025
- ASPLOS 2025
- DAC 2025
- NeurIPS 2025
- ICML 2025

## Main Features

- Two-row navigation experience:
  - Top header with a persistent Home button
  - Conference strip using compact format such as `HPCA (2025(19) | 2026(15))`
- English search experience:
  - Search placeholder in English
  - Focus suggestions show top 10 trending keywords from word cloud data
- Dynamic academic keyword word cloud on homepage:
  - Fully English keywords
  - Font size strictly follows keyword frequency
  - Hover shows conference source and paper count
  - Click triggers site search
  - Responsive redraw for desktop/mobile
  - Skeleton loading state before cloud render
- Theme polish:
  - Custom sun/moon toggle icons
  - Consistent visual styling for light/dark mode

## How Dynamic Word Cloud Works

Keyword data is generated from paper frontmatter tags in markdown files.

- Source generator: scripts/gen_wordcloud_data.py
- Output JSON: docs/assets/word_data.json
- Build hook: scripts/hooks.py (runs automatically on mkdocs build)

During each build, the hook regenerates word cloud data so newly added papers are reflected automatically.

## Add a New Paper

1. Create the markdown scaffold

```bash
bash scripts/new_paper.sh <conference> <track> <slug> "Paper Title"
```

2. Fill in the generated markdown content (metadata, summary, method, results).

3. Add the new page to `nav` in mkdocs.yml.

4. Commit and push:

```bash
git add -A
git commit -m "add: <paper title>"
git push origin master
```

## Local Development

Install dependencies and run local preview:

```bash
pip install -r requirements.txt
mkdocs serve
```

Open http://127.0.0.1:8000 to preview changes.

## Build

```bash
mkdocs build
```

The generated static site is written to `site/`.

## Tech Stack

- MkDocs
- Material for MkDocs
- wordcloud2.js
- Python (metadata extraction and build hooks)

## License

Content is distributed under CC BY-NC-SA 4.0 unless otherwise noted.
