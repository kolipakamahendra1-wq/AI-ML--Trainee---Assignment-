import requests
import sqlite3

API_URL = "https://fakerapi.it/api/v1/books?_quantity=10"

response = requests.get(API_URL)
books = response.json()["data"]

conn = sqlite3.connect("database.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT,
    author TEXT,
    year INTEGER
)
""")

for book in books:
    cursor.execute(
        "INSERT INTO books (title, author, year) VALUES (?, ?, ?)",
        (book["title"], book["author"], book["published"])
    )

conn.commit()

cursor.execute("SELECT * FROM books")
for row in cursor.fetchall():
    print(row)

conn.close()
