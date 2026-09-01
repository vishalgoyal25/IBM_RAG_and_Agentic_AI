# CLAUDE.md — working rules for this repo

Living document. We add to it as conventions emerge.

## What this repo is

Vishal's working repo for the **IBM RAG and Agentic AI Professional Certificate**
(10 courses, Coursera). It holds the course materials course by course — lab
notebooks, cheat sheets, glossaries, lecture PDFs, diagrams and datasets — plus
any experiments built on top of them.

Purpose is personal learning and recall.

**Do not spell that purpose out in `README.md`.** The README presents the repo as
a learning journey through the certificate. Keep archival/storage framing out of
it.

## Directory boundaries

- Work **only** inside `D:\CourseRa\IBM_RAG_and_Agentic_AI`.
- `D:\CourseRa\IBM_Generative_AI_Engineering` (the completed Gen AI certificate)
  is **read-only reference**. Read it to match conventions or copy patterns.
  Never edit, move, or delete anything in it.

## Folder convention

Mirrors the previous certificate repo:

```text
<N>. Course Name/
    <M>. Module Name/
        <lab name>.ipynb
        Cheat Sheet- <topic>.pdf
        Glossary- <topic>.pdf
        <diagram>.png
        <dataset>.txt
    Course Conclusion.pdf
```

- Course folders are numbered `1.` – `10.` in certificate order and already exist.
- Module folders are named after the **actual Coursera module titles** — create
  them only when the real names are known, never invent them.
- `:` is illegal in Windows paths; the repo uses `-` in its place
  (e.g. `2. Build RAG Applications- Get Started`).
- Files sit flat inside a module folder. No `Labs/` or `Notes/` sub-nesting.

## Environment

- Conda env lives at `./myvenv` (git-ignored), **Python 3.12** — CrewAI requires
  `<3.13`, so do not bump it.
- Activate: `conda activate D:\CourseRa\IBM_RAG_and_Agentic_AI\myvenv`
- Never install into `base` or into any other project's env.
- Adding a package means adding it to `requirements.txt` too — the file is the
  source of truth, `environment.yml` just points at it.
- The agentic stack (langgraph / crewai / ag2 / beeai / mcp) resolves each
  other's pins, so `requirements.txt` uses **lower bounds, not exact pins**.
  Exact pins belong in `requirements.lock.txt` (`pip freeze`).

## Secrets

- Real keys live in `.env`, which is git-ignored. Do not read it, print it, or
  copy its values into notebooks, logs, or commit messages.
- `.env.example` is the tracked template — when a lab needs a new key, add the
  empty slot there.

## Git

- Do not commit or push unless asked.
- Course materials (`.ipynb`, `.pdf`, `.png`, `.csv`, `.txt`, `.zip`) are meant
  to be tracked. If a `git add` skips one, the `.gitignore` is wrong — fix the
  rule rather than force-adding.
- Never `git add -A` from the repo root without checking what it picked up.

## Shared code

`common/config.py` holds the setup every lab repeats — `.env` loading,
`get_llm()`, `get_embeddings()`, `available_providers()`. Prefer extending it
over pasting provider boilerplate into individual notebooks. Provider imports
there are lazy on purpose: a missing package must only break its own path.

## Windows / environment gotchas

- Shell is PowerShell. Watch for Unix-only syntax.
- `WinError 32` during `pip install` means a stale `myvenv\python.exe` still
  holds files. Find it with `Get-CimInstance Win32_Process`, confirm it is an
  orphaned pip, kill it, then re-run the install — pip skips what is already
  installed. This has happened once already.
- Long installs go in the background and log to `myvenv\install.log`.

## Command execution — hard rule

**Never run shell commands.** No Bash, no PowerShell, no background jobs — not
even read-only ones like `git status` or `ls`.

Instead: write the command in the chat in a fenced ```bash block, one command per
block, so Vishal can run it with the Run button. He runs it in the terminal on
the right; read the output from there on the next turn.

Reading and writing files directly (Read / Write / Edit / Grep / Glob) is still
fine — that is not a command.

## Working style

- Notebooks are course artifacts. Do not reformat, re-run, or "clean up" a lab
  notebook unless asked — outputs are part of what is being kept.
- When a lab's API differs from current library versions, say so and show the
  current form; do not silently rewrite the course's code.
