import sqlite3
import pandas as pd

from pathlib import Path

# --- Ensure required directories exist ---
Path("db").mkdir(exist_ok=True)
Path("Data/Processed").mkdir(parents=True, exist_ok=True)

DB_PATH = "db/portfolio.db"

# Update this to your auto-named output path:
START = "2025-01-01"
END   = "2025-01-31"

CSV_PATH  = f"Data/Processed/prices_{START}_to_{END}.csv"
print("Looking for:", CSV_PATH)

df = pd.read_csv(CSV_PATH)

# Basic sanity: ensure required columns exist
required = {"date", "ticker"}
missing = required - set(df.columns.str.lower())
# Normalize column names to match table schema
df = df.rename(columns={c: c.strip() for c in df.columns})

with sqlite3.connect(DB_PATH) as conn:
    # append will insert rows; PRIMARY KEY prevents duplicates only if you handle conflicts
    df.to_sql("prices", conn, if_exists="replace", index=False)

print(f"Loaded {len(df):,} rows into prices from {CSV_PATH}.")
