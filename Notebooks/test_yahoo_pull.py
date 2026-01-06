import yfinance as yf
import pandas as pd

#STEP 1: (Optional) Pull raw price data from Yahoo Finance
# This fetches daily OHLCV price data for AAPL in January 2025.
# In practice, this step is often separated into its own script.

# ---------------------------------------------------
df = yf.download("AAPL", start="2025-01-01", end="2025-01-31")
# Uncomment these lines if you want to inspect or save raw output
#print(df.head())
#df.to_csv("AAPL_January_2025raw.csv")
#print(df.columns)

# ---------------------------------------------------
# STEP 2: Read the raw CSV correctly
# Yahoo Finance exports multi-level headers (Price / Ticker),
# so we explicitly tell pandas there are two header rows.
# index_col=0 ensures the Date column is treated as the index.

df = pd.read_csv(
    "/Users/mahji/Desktop/Investment Project/Investment_Tracker/Data/Raw/AAPL_January_2025raw.csv",
    header=[0,1],
    index_col=0
)
# ---------------------------------------------------
# STEP 3: Flatten multi-level column headers
# Drops the ticker level (e.g., 'AAPL') so columns become:
# Open, High, Low, Close, Volume
# ---------------------------------------------------
df.columns = df.columns.droplevel(1)

# ---------------------------------------------------
# STEP 4: Convert Date from index into a regular column
# SQL databases and CSV-based workflows require Date
# to be an explicit column, not an index.
# ---------------------------------------------------
df = df.reset_index()

# STEP 5: Standardize column naming
# After reset_index(), pandas may name the column 'index'.
# We rename it to 'Date' for clarity and consistency.
df = df.rename(columns={"index": "Date"})
df["ticker"] = "AAPL"

# ---------------------------------------------------
# STEP 7: Select a clean, controlled schema
# This defines the canonical column set for price data
# across all tickers and dates.
keep_cols = ["Date", "ticker", "Open", "High", "Low", "Close", "Volume"]
df = df[keep_cols]

# ---------------------------------------------------
# STEP 8: Save cleaned data for downstream use
# This file is now ready for:
# - combining with other tickers
# - loading into SQLite
# - portfolio calculations
df.to_csv("data/processed/AAPL_January_2025_clean.csv", index=False)

#sanity check
print(df.head())
print("Saved: data/processed/AAPL_prices_clean.csv")
print(df.columns)
