import requests
import os
from dotenv import load_dotenv

load_dotenv()
API_KEY = os.getenv("GOOGLE_BOOKS_API_KEY")

response = requests.get(
    "https://www.googleapis.com/books/v1/volumes",
    params={"q": "italian travel fiction", "key": API_KEY, "maxResults": 5}
)

for book in response.json()["items"]:
    info = book["volumeInfo"]
    print(f"{info['title']} — {info.get('authors', ['Unknown'])[0]}")
