import sqlite3

DB_PATH = "db/portfolio.db"

create_transactions_sql = """
CREATE TABLE IF NOT EXISTS transactions (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    date   TEXT NOT NULL,
    ticker TEXT NOT NULL,
    action TEXT NOT NULL,
    shares REAL NOT NULL,
    price  REAL NOT NULL,
    fees   REAL DEFAULT 0
);
"""

with sqlite3.connect(DB_PATH) as conn:
    conn.execute(create_transactions_sql)
    conn.commit()

print("Initialized DB and ensured transactions table exists.")
