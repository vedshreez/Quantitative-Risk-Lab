# 1. Install the library 

# 2. Import libraries
import yfinance as yf
import pandas as pd
import numpy as np

# 3. Define the Portfolio (Tech, Bonds, Gold, S&P 500)
tickers = ['AAPL', 'MSFT', 'TLT', 'GLD', 'SPY']
start_date = '2020-01-01'
end_date = '2025-01-01'

def fetch_data(tickers, start, end):
    print(f"Fetching data for: {tickers}...")
    data = yf.download(tickers, start=start, end=end)['Adj Close']
    
    # Check for missing values
    if data.isnull().values.any():
        print("Missing values detected. Filling with forward fill...")
        data = data.ffill()
    
    print("Data fetched successfully!")
    return data

def calculate_returns(data):
    # Log Returns are additive (better for statistical modeling)
    log_returns = np.log(data / data.shift(1))
    
    # Drop the first row (NaN)
    log_returns = log_returns.dropna()
    return log_returns

# 4. Run the pipeline
prices = fetch_data(tickers, start_date, end_date)
returns = calculate_returns(prices)

# 5. Display the first few rows so you know it worked
print("\n--- HEAD OF RETURNS DATA ---")
print(returns.head())
