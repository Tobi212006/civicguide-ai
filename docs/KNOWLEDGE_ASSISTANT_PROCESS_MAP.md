# CivicGuide Knowledge Assistant — End-to-End Process Map

```mermaid
flowchart TD
    A[User enters a question] --> B[GET /search?q=...]
    B --> C[Trim and tokenise query]
    C --> D[Load reviewed catalogue]
    D --> E[Compare query terms with each entry]
    E --> F[Rank matching entries deterministically]
    F --> G{Any useful match?}
    G -->|Yes| H[Return ranked result and official source URL]
    G -->|No| I[Return empty results and abstention message]
    H --> J[User verifies information on official portal]
    I --> J
```

## Developer workflow

```mermaid
flowchart LR
    A[Issue or improvement idea] --> B[Update catalogue or API]
    B --> C[Add or update tests]
    C --> D[Run pytest]
    D --> E{Tests pass?}
    E -->|No| B
    E -->|Yes| F[Run evaluation script]
    F --> G[Review diff and documentation]
    G --> H[Commit with clear message]
```

## How to explain it in an interview

"I built a small source-grounded retrieval API. It normalises a query, ranks a reviewed catalogue using deterministic token overlap, and returns the official source with each match. When it cannot find a match, it abstains. I added unit tests and a small labelled evaluation set so the behaviour is measurable. It is a retrieval baseline, not an LLM, and I documented where semantic search could improve it."
