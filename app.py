from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from anthropic import Anthropic
from prompts import SYSTEM_PROMPT
from search import search_books, format_results
import json

app = FastAPI()
client = Anthropic()


class Query(BaseModel):
    message: str


@app.post("/api/recommend")
async def recommend(query: Query):
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=200,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": query.message}]
    )
    params = json.loads(response.content[0].text)
    results = search_books(params)
    books = format_results(results)
    return {"params": params, "books": books}

app.mount("/", StaticFiles(directory="static", html=True), name="static")
