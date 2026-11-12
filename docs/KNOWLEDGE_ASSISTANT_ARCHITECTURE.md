# CivicGuide Knowledge Assistant — Architecture

## Purpose

This document describes the implemented deterministic retrieval baseline in `knowledge-assistant/`. It does not describe an LLM-powered system.

## Components

| Component | Responsibility |
|---|---|
| FastAPI | Exposes health and search endpoints |
| Query normaliser | Converts text to lowercase alphanumeric tokens |
| Catalogue loader | Reads the reviewed JSON catalogue |
| Ranking function | Scores entries by distinct query-term overlap |
| Response formatter | Returns matches, matched terms and official source links |
| Tests | Check supported, unsupported, empty and case-insensitive queries |
| Evaluation script | Measures top-1 match and coverage on the small labelled set |

## Request lifecycle

1. Client sends a query to `GET /search?q=...`.
2. The API trims the input and tokenises it.
3. Each catalogue entry is converted into searchable text.
4. Entries with at least one matching term are scored.
5. Results are sorted by score, then title for deterministic ordering.
6. The API returns source URLs and a reminder to verify official details.
7. If nothing matches, the API abstains instead of inventing an answer.

## Design choices

- Deterministic ranking makes the baseline easy to explain and test.
- The source URL travels with each result.
- The catalogue is deliberately small and manually curated.
- The API does not request or store personal information.
- The system does not make eligibility decisions or submit forms.

## Known limitations

Token overlap does not understand synonyms, context or meaning. A high score is not a guarantee that a source fully answers a question. The catalogue may become outdated. These limitations should be stated in any demo or interview.
