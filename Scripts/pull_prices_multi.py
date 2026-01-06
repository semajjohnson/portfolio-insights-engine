import yfinance as yf
import pandas as pd

START = "2025-01-01"
END   = "2025-01-31"
tickers_df = pd.read_csv("/Users/mahji/Desktop/Investment Project/Investment_Tracker/Data/Raw/ticker.csv")
tickers = tickers_df["ticker"].dropna().unique().tolist()

dfs = []

for t in tickers:
    tk = yf.Ticker(t)
    hist = tk.history(start=START, end=END)

    # Date is usually the index -> make it a column
    hist = hist.reset_index()

    # Standardize column names
    hist = hist.rename(columns={"Date": "date"})

    # Add ticker column
    hist["ticker"] = t

    # Keep a controlled schema (add more later if you want)
    keep_cols = ["date", "ticker", "Open", "High", "Low", "Close", "Volume"]
    # Some tickers include Dividends/Splits; ignore for now
    hist = hist[[c for c in keep_cols if c in hist.columns]]

    dfs.append(hist)
    
prices = pd.concat(dfs, ignore_index=True)

# Sort for sanity
prices = prices.sort_values(["ticker", "date"])

filename = f"prices_{START}_to_{END}.csv"
output_path = f"data/processed/{filename}"

prices.to_csv(output_path, index=False)

print(prices.head())

print(f"Saved: {output_path}")