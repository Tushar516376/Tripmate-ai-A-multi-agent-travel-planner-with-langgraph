import os
import psycopg
from dotenv import load_dotenv

load_dotenv()

url = os.getenv("DATABASE_URL")

print("URL loaded:", bool(url))

if not url:
    raise Exception("DATABASE_URL not found")

print("Connecting...")

conn = psycopg.connect(
    url,
    connect_timeout=10
)

print("SUCCESS: PostgreSQL connected!")

conn.close()