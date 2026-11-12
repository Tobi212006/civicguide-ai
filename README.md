# CivicGuide

**A source-linked starting point for exploring official Indian public services.**

CivicGuide is an independent BSc Computer Science portfolio project. It helps visitors find official portals for scholarships, careers, Aadhaar services and digital government services.

## Project modules

### 1. Public-service directory
- Responsive single-page interface with keyword search and category filters.
- Curated links to official portals.
- No account or personal data collection.

### 2. Knowledge Assistant API
A Python/FastAPI extension that demonstrates a transparent retrieval workflow:
- Deterministic token-overlap ranking over a small reviewed catalogue.
- REST endpoints for health checks and search.
- Official source URL returned with each match.
- Abstention when the catalogue has no useful match.
- Unit tests and a small labelled evaluation script.

This is a retrieval baseline, **not an LLM-powered system**. See [Knowledge Assistant](knowledge-assistant/README.md), [architecture](docs/KNOWLEDGE_ASSISTANT_ARCHITECTURE.md), and [end-to-end process map](docs/KNOWLEDGE_ASSISTANT_PROCESS_MAP.md).

## Run the directory

Open `index.html` in a modern browser. The static directory requires no build step or API key.

## Run the Knowledge Assistant API

```bash
cd knowledge-assistant
python -m venv .venv
# Windows PowerShell: .venv\\Scripts\\Activate.ps1
# macOS/Linux: source .venv/bin/activate
python -m pip install -r requirements.txt
uvicorn app:app --reload
```

API documentation: `http://127.0.0.1:8000/docs`

Run verification:

```bash
python -m pytest -q
python evaluate.py
```

The included evaluation set is small and illustrative. Do not present its score as evidence of general accuracy.

## Official sources

- [National Scholarship Portal](https://scholarships.gov.in/Students)
- [National Career Service](https://www.ncs.gov.in/)
- [UIDAI](https://uidai.gov.in/en/)
- [UMANG](https://www.umang.gov.in/landing/)

Information and requirements may change; confirm details on each official portal.

## Responsible use and limitations

CivicGuide is not affiliated with the Government of India. The directory and retrieval API do not determine personal eligibility, submit applications, or provide official advice. The catalogue is small and manually maintained; keyword overlap is not semantic understanding. Never enter Aadhaar numbers, passwords, application IDs or other sensitive personal information into this demo.

## Development roadmap

- [x] Publish the existing static directory.
- [x] Add a deterministic source-grounded retrieval API baseline.
- [x] Add API tests, evaluation examples, architecture and process documentation.
- [ ] Expand the catalogue after reviewing each official source.
- [ ] Add source freshness checks and more labelled evaluation cases.
- [ ] Explore semantic retrieval and compare it against the baseline.
- [ ] Add accessible Marathi and Hindi interfaces.

## About

Built as a learning project to practise Python, API design, data handling, testing, documentation and responsible software development.
