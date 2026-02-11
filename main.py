from anthropic import Anthropic
from config import ANTHROPIC_API_KEY
from prompts import SYSTEM_PROMPT
from search import search_books, format_results
import json


client = Anthropic()


def get_search_params(user_input):
    response = client.messages.create(
        model="claude-sonnet-4-20250514",
        max_tokens=200,
        system=SYSTEM_PROMPT,
        messages=[{"role": "user", "content": user_input}]
    )
    return json.loads(response.content[0].text)


user_input = "I want a book for a romantic candlelight dinner vibe"
params = get_search_params(user_input)
print(f"Search params: {params}\n")

results = search_books(params)
books = format_results(results)

for book in books:
    print(f"{book['title']} — {', '.join(book['authors'])}")
    print(f"  {book['description'][:100]}...")
    print()
