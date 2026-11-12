# CivicGuide Knowledge Assistant

A small, source-grounded retrieval API built as an engineering extension to CivicGuide. It demonstrates how to organise a knowledge catalogue, rank relevant entries, return source links, handle unsupported questions, and test expected behaviour.

## Why this project exists

The prototype is aligned with entry-level software engineering work involving Python, REST APIs, knowledge processing, retrieval workflows, and reliability testing. It is deliberately transparent: it uses a deterministic retrieval baseline, **not** an LLM. This makes the behaviour explainable and gives us a measurable baseline before experimenting with language models.

## Features

- FastAPI endpoints: `GET /health` and `GET /search?q=...`.
- Token-based relevance ranking over a small, curated catalogue.
- Official source URL returned with every match.
- Abstains when no useful catalogue match is found.
- Unit tests for relevant queries, unsupported queries, and empty input.
- A small evaluation dataset and script for repeatable top-1 accuracy / coverage checks.

## Run locally

Python 3.10+ is recommended.

```bash
cd knowledge-assistant
python -m venv .venv
# Windows PowerShell: .venv\\Scripts\\Activate.ps1
# macOS/Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
uvicorn app:app --reload
```

Open `http://127.0.0.1:8000/docs` for the interactive API documentation.

Example request:

```bash
curl "http://127.0.0.1:8000/search?q=student%20scholarship"
```

## Run tests and evaluation

```bash
python -m pytest -q
python evaluate.py
```

The evaluation script reports results only for the included sample cases. It is not evidence of broad real-world accuracy.

## API response behaviour

- A supported query returns ranked catalogue entries and their official source URLs.
- An unsupported query returns an empty result list and an explanatory message.
- The service does not determine eligibility, submit applications, or request personal identifiers.

## Architecture

```text
HTTP query
   |
   v
FastAPI route (/search)
   |
   v
Input normalisation
   |
   v
Token overlap ranking <---- reviewed catalogue (catalog.json)
   |
   +---- relevant match ----> result + official source URL
   |
   +---- no useful match ---> abstain / empty results
```

See [architecture](../docs/KNOWLEDGE_ASSISTANT_ARCHITECTURE.md) and [process map](../docs/KNOWLEDGE_ASSISTANT_PROCESS_MAP.md).

## Limitations and next steps

- The catalogue is intentionally small and manually maintained.
- Token overlap is a baseline, not semantic search.
- Source freshness must be checked by a maintainer.
- Add more reviewed sources and labelled evaluation cases before comparing retrieval methods.
- A future LLM experiment should preserve source citations, add refusal/uncertainty tests, and compare against this baseline.

## Responsible use

CivicGuide is an independent student prototype and is not affiliated with any government agency. Always verify information on the linked official portal. Never enter Aadhaar numbers, passwords, application IDs, or other sensitive personal information into this demo.
