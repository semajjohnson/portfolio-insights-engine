import sqlite3
import pandas as pd

conn = sqlite3.connect("db/portfolio.db")

df = pd.read_sql("SELECT * FROM prices LIMIT 5;", conn)
print(df)

conn.close()