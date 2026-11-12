# CivicGuide — Retrieval Research Plan

## Current implementation

The repository now contains two distinct components:

1. A static directory with keyword search and curated official links.
2. A Python/FastAPI Knowledge Assistant that ranks a small, manually reviewed catalogue using deterministic token overlap and returns official source URLs.

The API is a retrieval baseline. It does not call an LLM, crawl government websites, or make eligibility decisions.

## Research question

Can a source-linked retrieval interface help people find the correct official public-service information more reliably than a basic keyword-search directory?

## Baseline and comparison design

- **Baseline A:** static directory search and category filters.
- **Baseline B:** Knowledge Assistant token-overlap ranking.
- **Future experiment:** optionally compare a semantic retrieval approach against both baselines after implementing and testing it.

Use the same labelled questions for each approach. Record the query, expected official destination, observed result, correctness, coverage, and any unsupported answer. Report sample size and limitations.

## Evaluation criteria

- Correctness of the top official destination.
- Whether the linked source supports the information sought.
- Coverage of the labelled questions.
- Whether the system abstains when the catalogue does not contain an answer.
- Response time and usability.
- Accessibility of navigation and language choices.

The current `knowledge-assistant/evaluation_cases.json` is only a small demonstration dataset. Its output is not a broad performance claim.

## Safety, privacy and reliability

- Use public information from official government domains only.
- Keep a record of each source URL and the date it was checked as the catalogue grows.
- Do not collect Aadhaar numbers, passwords, application IDs or other sensitive personal details.
- Do not infer personal eligibility or submit forms on a user's behalf.
- Show uncertainty and direct users to the relevant agency for decisions.
- Clearly label the project as an independent student prototype.

## Next steps

- [x] Build a deterministic retrieval baseline.
- [x] Add a small labelled evaluation set and automated tests.
- [ ] Expand to 15–20 reviewed test questions.
- [ ] Record expected results and known failure cases for each baseline.
- [ ] Review and date-check every curated source.
- [ ] If semantic retrieval is added, document its model, data and evaluation method.
- [ ] Publish comparative results only after running the same test set across implementations.

## Research integrity

No formal study, publication, participant research or production deployment is claimed. Keep implementation status, measured results and future plans clearly separated.
