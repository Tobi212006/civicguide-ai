"""Source-grounded retrieval API for the CivicGuide student prototype."""
from __future__ import annotations

import json
import re
from pathlib import Path
from typing import Any

from fastapi import FastAPI, Query

CATALOG_PATH = Path(__file__).with_name("catalog.json")
MIN_MATCHED_TERMS = 1


def load_catalog() -> list[dict[str, Any]]:
    """Load the small, reviewed JSON catalogue shipped with this project."""
    with CATALOG_PATH.open("r", encoding="utf-8") as file:
        data = json.load(file)
    if not isinstance(data, list):
        raise ValueError("catalog.json must contain a JSON array")
    return data


def normalise_tokens(text: str) -> set[str]:
    """Return lowercase alphanumeric tokens; punctuation is treated as a separator."""
    return set(re.findall(r"[a-z0-9]+", text.lower()))


def search_catalog(query: str, catalog: list[dict[str, Any]] | None = None) -> list[dict[str, Any]]:
    """Rank entries by the number of distinct query terms they contain."""
    entries = catalog if catalog is not None else load_catalog()
    query_terms = normalise_tokens(query)
    if not query_terms:
        return []

    ranked: list[dict[str, Any]] = []
    for entry in entries:
        searchable_text = " ".join([
            entry.get("title", ""),
            entry.get("category", ""),
            entry.get("description", ""),
            " ".join(entry.get("keywords", [])),
        ])
        matched_terms = query_terms.intersection(normalise_tokens(searchable_text))
        if len(matched_terms) < MIN_MATCHED_TERMS:
            continue

        ranked.append({
            "id": entry["id"],
            "title": entry["title"],
            "category": entry["category"],
            "description": entry["description"],
            "matched_terms": sorted(matched_terms),
            "score": round(len(matched_terms) / len(query_terms), 3),
            "source": {
                "name": entry["source_name"],
                "url": entry["source_url"],
            },
        })

    return sorted(ranked, key=lambda item: (-item["score"], item["title"]))


app = FastAPI(
    title="CivicGuide Knowledge Assistant API",
    description="A transparent retrieval baseline over a small, reviewed public-service catalogue.",
    version="1.0.0",
)


@app.get("/health")
def health() -> dict[str, str]:
    return {"status": "ok", "service": "civicguide-knowledge-assistant"}


@app.get("/search")
def search(q: str = Query(default="", max_length=200)) -> dict[str, Any]:
    query = q.strip()
    if not query:
        return {"query": q, "count": 0, "results": [], "message": "Enter a search query."}

    results = search_catalog(query)
    if not results:
        return {
            "query": query,
            "count": 0,
            "results": [],
            "message": "No matching source was found in this reviewed catalogue. Check the relevant official portal directly.",
        }

    return {
        "query": query,
        "count": len(results),
        "results": results,
        "message": "Matches are ranked by keyword overlap. Verify details on the linked official source.",
    }
