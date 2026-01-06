import yfinance as yf
import pandas as pd

tickersymbol = "AAPL"
ticker = yf.Ticker(tickersymbol)

#shows what metadata is pullable
#print(dir(ticker))

#test space to see what it looks like once pulled
hist = ticker.financials
#print(type(hist))      # confirm it's a DataFrame or a list
#if dataframe...
#print(hist.head())     # see first few rows
#print(hist.columns)    # inspect available fields
print(hist)
