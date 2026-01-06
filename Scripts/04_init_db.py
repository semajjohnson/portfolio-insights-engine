import sqlite3

# Path to the SQLite database file.
# If it doesn't exist yet, SQLite will create it the first time we connect.
DB_PATH = "db/portfolio.db"


# SQL statement to create a table named 'prices' if it does not already exist.
# This table stores daily market price data for each ticker.
create_prices_sql = """
CREATE TABLE IF NOT EXISTS prices (
    date   TEXT NOT NULL,
    ticker TEXT NOT NULL,
    Open   REAL,
    High   REAL,
    Low    REAL,
    Close  REAL,
    Volume REAL,
    PRIMARY KEY (ticker, date)
);
"""

# Open a connection to the database and run the CREATE TABLE statement.
# Using 'with' ensures the connection is safely closed even if something errors.
with sqlite3.connect(DB_PATH) as conn:
    conn.execute(create_prices_sql) # Execute the table creation query
    conn.commit()                   # Commit changes to the database

print("Initialized DB and ensured prices table exists.")
