from fastapi import FastAPI, HTTPException
from app.retrieval import search_documents
from app.caching import cache_document, get_cached_document
from app.user_manager import manage_user_requests

app = FastAPI()

@app.get("/health")
async def health_check():
    return {"status": "API is up and running"}

@app.get("/search")
async def search(text: str, top_k: int = 5, threshold: float = 0.8, user_id: str = None):
    # Check rate limiting for the user
    if not manage_user_requests(user_id):
        raise HTTPException(status_code=429, detail="Too many requests")

    # Check cache first
    cached_result = get_cached_document(text)
    if cached_result:
        return {"results": cached_result}

    results = search_documents(text, top_k, threshold)

    cache_document(text, results)

    return {"results": results}
