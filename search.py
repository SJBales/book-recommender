import requests
from config import GOOGLE_BOOKS_API_KEY


def search_books(params):
    params["key"] = GOOGLE_BOOKS_API_KEY
    response = requests.get(
        "https://www.googleapis.com/books/v1/volumes",
        params=params
    )
    return response.json()


def format_results(data):
    books = []
    for item in data.get("items", []):
        info = item["volumeInfo"]
        books.append({
            "title": info.get("title", "Unknown"),
            "authors": info.get("authors", ["Unknown"]),
            "description": info.get("description", "No description available"),
            "categories": info.get("categories", []),
            "rating": info.get("averageRating", "N/A"),
            "preview": info.get("previewLink", "")
        })
    return books
