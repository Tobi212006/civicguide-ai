# CivicGuide — Research Exploration Plan

## Status and scope

This document is a proposed student research direction, not a report of completed experiments. The current CivicGuide application is a static directory with keyword search and curated links. It does not currently use an AI model, crawl government websites, or make eligibility decisions.

## Research question

Can a carefully source-linked, retrieval-based interface help people find the correct official public-service information more reliably than a basic keyword-search directory?

## Why this matters

People may encounter outdated links, confusing terminology, or multiple agencies while looking for public services. A useful system should make the source of each answer visible and avoid presenting uncertain information as official advice.

## Proposed comparison

1. **Baseline:** the current curated directory and keyword/category search.
2. **Possible extension:** a retrieval prototype using a small, manually reviewed collection of official public pages.
3. **Evaluation:** use a fixed set of representative questions and compare whether each approach returns the correct official destination and a relevant source.

Do not build the extension or claim results until the sources, implementation and tests are actually available.

## Evaluation criteria

- Correctness of the official destination selected.
- Whether the linked source directly supports the displayed information.
- Coverage of the test questions.
- Ability to recognize when the available sources do not answer a question.
- Response time and usability for first-time visitors.
- Accessibility of navigation and language choices.

A small labelled test set should be written before evaluation. Record the query, expected official source, observed result and any error. Report sample size and limitations rather than making broad claims from a small test.

## Safety, privacy and reliability

- Use public information from official government domains only.
- Keep a record of each source URL and the date it was checked.
- Do not collect Aadhaar numbers, passwords, application IDs or other sensitive personal details.
- Do not infer personal eligibility or submit forms on a user's behalf.
- Show uncertainty and direct users to the relevant agency for decisions.
- Clearly label the project as an independent student prototype.

## Next steps

- [ ] Define 15–20 test questions and their expected official destinations.
- [ ] Record the current baseline results.
- [ ] Review and date-check every curated source.
- [ ] If a retrieval prototype is built, document its source collection and retrieval method.
- [ ] Compare the prototype against the baseline using the same questions.
- [ ] Publish results, limitations and reproducible steps only after running the evaluation.

## Research integrity

No formal study, publication, participant research or experimental result is claimed in this repository. This plan is intended to guide future supervised work and should be updated with actual implementation and evidence.
