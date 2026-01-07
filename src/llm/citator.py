def format_sources(docs):
    pages = sorted({d.metadata.get("page") for d in docs})
    return "Sources: " + ", ".join(f"Page {p}" for p in pages)
