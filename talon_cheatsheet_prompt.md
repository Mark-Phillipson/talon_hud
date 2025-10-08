# Talon Cheatsheet Generator Prompt (Reusable)

Use this prompt with an AI assistant to generate a compact, widescreen-optimized cheatsheet for any Talon repository that contains voice commands. The prompt below is parameterized so it can be reused across different repositories and output formats.

---

## How to use

- Replace the parameter values in the "Parameters" section before running the prompt.
- Provide the repository files (or point the assistant to the repo) so the assistant can scan `.talon`, `.talon-list`, and accompanying Python list files.
- If you want a different output format (HTML, CSV, JSON, or Markdown), set `OUTPUT_FORMAT` accordingly.

---

## Parameters (replace as needed)

- EXCLUDE_FOLDERS: comma-separated folder names to skip (default: games)
- LANGUAGES: comma-separated programming languages to include (default: HTML, CSS, Razor, C#, Python)
- OUTPUT_FORMAT: markdown | html | csv | json (default: markdown)
- EXPORT_WEB_HTML: true | false (default: true) — when true, also generate a small browsable HTML export and per-repository JSON files under `web-export/data/` so the cheatsheet can be browsed in a browser. The Markdown file must still be produced.
- MAX_COLUMNS: number of columns to use for multi-column tables (default: 4)
- SHOW_GLOBAL_BADGE: true | false (default: true) — mark global commands with an emoji/badge
- INCLUDE_LIST_VALUES: true | false (default: true)

---

## Prompt (copy & paste; substitute parameters above)

You are an expert Talon documentation assistant. Scan the provided repository and generate a cheatsheet according to the rules below. Use these parameter values in your run:

- Exclude folders: {EXCLUDE_FOLDERS}
- Include only these programming languages/scopes: {LANGUAGES}
- Output format: {OUTPUT_FORMAT}
- Also produce a browsable web export: {EXPORT_WEB_HTML}
- Multi-column table max columns: {MAX_COLUMNS}
- Mark global commands: {SHOW_GLOBAL_BADGE}
- Include list/capture values: {INCLUDE_LIST_VALUES}

Rules for extraction and formatting:

1. Scan all `.talon`, `.talon-list`, and Python files that define `mod.list` / `ctx.lists` for voice commands and lists. Follow imports and context files in the repo root and subfolders except those in {EXCLUDE_FOLDERS}.
2. Only include commands and lists that are relevant to the languages/scopes listed in {LANGUAGES}. If a command has no explicit scope, include it as global.
3. For each Talon command, extract: spoken form (the capture), the action (the right-hand side), any scope/context (e.g., `app: code`, `code.language: python`), and a brief description when available from comments. Mark global (scope-less) commands clearly when {SHOW_GLOBAL_BADGE} is true.
4. For every list/capture referenced by commands, extract the available values and alphabetize them. Present list values adjacent to or immediately above the table of commands that use them. Use multi-column tables with up to {MAX_COLUMNS} columns to reduce vertical scrolling.
5. Present all commands in alphabetical order (by spoken form) within each section and grouped by scope/application (Global, VSCode, Edge, etc.).
6. Use compact tables for commands and lists. Avoid long vertical lists; use multi-column tables for long value sets. Keep rows concise; escape special characters in table cells.
7. Include a short "Tips" section with VS Code shortkeys for viewing markdown/HTML preview, full-screen, and Zen mode.
8. Include a short "Filtering" section showing a minimal Python snippet to search/filter registry lists (example using Talon registry or simple file parsing). Provide an example that runs in the Talon Python REPL and one that uses a plain Python snippet for local post-processing.
9. If OUTPUT_FORMAT is `html`, also include a small client-side search script (vanilla JS) and a downloadable CSV export of the commands. If OUTPUT_FORMAT is `csv` or `json`, return machine-readable output only.
10. If {EXPORT_WEB_HTML} is true, in addition to the primary output (markdown or the selected machine-readable format), produce a `web-export/` folder containing:
	- `index.html`, `styles.css`, and `main.js` (vanilla JS, no build step) implementing a simple per-repository browser UI with search/filter and individual command views.
	- `data/` directory with one JSON file per repository processed, named `{repo_name}.json` (or `{repo_name}-commands.json`) containing the full array of command objects (fields: scope, spoken_form, action, language_scope, lists_used, notes, description, source_path).
	- The HTML should load the JSON file dynamically (fetch) and provide a UI to browse commands by scope/repository, search spoken forms, and view actions and list values. Keep the client-side code dependency-free and small.
10. Keep output compact and widescreen-friendly; avoid unnecessary line breaks and long wrapped cells. For markdown output, prefer tables optimized for wide preview (minimize vertical height).

Deliverables (choose and generate according to OUTPUT_FORMAT):

- markdown: single `README`-style markdown file with sections: Overview, Commands (by scope), Lists & Captures (adjacent to commands), Tips, Filtering & REPL examples.
- markdown: single `README`-style markdown file with sections: Overview, Commands (by scope), Lists & Captures (adjacent to commands), Tips, Filtering & REPL examples. If {EXPORT_WEB_HTML} is true, also include the `web-export/` folder described above.
- html: `index.html` (responsive widescreen layout), `styles.css`, and `main.js` (client-side search/filter and CSV download). Use only vanilla JS and no build step.
 - html: `index.html` (responsive widescreen layout), `styles.css`, and `main.js` (client-side search/filter and CSV download). Use only vanilla JS and no build step. When producing an HTML export as part of `web-export/`, also include the `data/{repo_name}.json` file(s) as described above.
- csv: single CSV file with columns: scope, spoken_form, action, language_scope, lists_used, notes.
- json: JSON array of command objects with fields: scope, spoken_form, action, language_scope, lists_used, notes.

Additional constraints:

- Exclude any files/folders listed in EXCLUDE_FOLDERS.
- Respect comments for descriptions but do not execute any repository code.
- Do not include entries from folders with obvious non-Talon content (for example: large binary folders).

Output example (markdown snippet):

```
# Talon Voice Command Cheatsheet

## Global Commands 🌐
| Command       | Action     | Scope  | Notes |
| ------------- | ---------- | ------ | ----- |
| open settings | key(alt s) | Global | ...   |

## Lists and Captures
**Available widgets:**
| widget1 | widget2 | widget3 | widget4 |
| ------- | ------- | ------- | ------- |
```

---

## Tips for reuse

- Keep the parameter block at the top so the prompt can be reused for different repos.
- If you need a custom extractor for a repo with unusual patterns, add a short adaptor script to the repo and point the assistant to it.

---

This prompt is now repository-agnostic and ready to be used against other Talon voice-command repositories. Replace parameters at the top and run the prompt with your preferred AI assistant or automation.
