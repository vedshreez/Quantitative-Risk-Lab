# 1. Install Library
# 2. Import Libraries
import yfinance as yf
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import norm

# ==========================================
# PART 1: FRESH DATA INGESTION (The Fix)
# ==========================================
tickers = ['AAPL', 'MSFT', 'TLT', 'GLD', 'SPY']
start_date = '2020-01-01'
end_date = '2025-01-01'

print("Step 1: Downloading fresh data...")
# Download with auto-adjust to avoid the "Adj Close" error
data = yf.download(tickers, start=start_date, end=end_date, auto_adjust=True)

# Handle different yfinance versions (sometimes it returns 'Close' sometimes 'Adj Close')
if 'Close' in data.columns:
    prices = data['Close']
else:
    prices = data # Fallback

# Fill missing values to prevent dropping everything
prices = prices.ffill().bfill()

# Calculate Returns
returns = np.log(prices / prices.shift(1)).dropna()

# SAFETY CHECK: Stop if data is still empty
if returns.empty:
    raise ValueError("CRITICAL ERROR: Data download failed. The returns dataframe is empty.")

print(f"Success! Loaded {len(returns)} days of data.")

# ==========================================
# PART 2: THE RISK MODEL (VaR)
# ==========================================

# Create an "Equally Weighted" Portfolio (Average of all stocks)
returns['Portfolio'] = returns.mean(axis=1)

# Inputs
confidence_level = 0.95
investment_amount = 100000  # $100,000

def calculate_historical_var(returns, confidence=0.95):
    """
    Method 1: Historical Simulation
    """
    # Calculate the percentile (e.g., 5th percentile for 95% confidence)
    var_percentile = np.percentile(returns, (1 - confidence) * 100)
    return var_percentile

def calculate_parametric_var(returns, confidence=0.95):
    """
    Method 2: Parametric (Normal Distribution)
    """
    mu = np.mean(returns)
    sigma = np.std(returns)
    z_score = norm.ppf(1 - confidence)
    var_parametric = mu - (z_score * sigma)
    return var_parametric

# Run Calculations
var_hist = calculate_historical_var(returns['Portfolio'], confidence_level)
var_param = calculate_parametric_var(returns['Portfolio'], confidence_level)

# ==========================================
# PART 3: RESULTS
# ==========================================
print(f"\n--- RISK METRICS (1-Day, 95% Confidence) ---")
print(f"Portfolio Value: ${investment_amount:,.0f}")

print(f"\n1. Historical VaR: {var_hist:.2%}")
print(f"   Potential Loss: ${abs(var_hist * investment_amount):,.2f}")

print(f"\n2. Parametric VaR: {var_param:.2%}")
print(f"   Potential Loss: ${abs(var_param * investment_amount):,.2f}")

# Visualization
plt.figure(figsize=(10, 6))
plt.hist(returns['Portfolio'], bins=50, alpha=0.6, label='Portfolio Returns', color='blue')
plt.axvline(var_hist, color='red', linestyle='--', linewidth=2, label=f'Historical VaR ({var_hist:.2%})')
plt.axvline(var_param, color='green', linestyle='--', linewidth=2, label=f'Parametric VaR ({var_param:.2%})')
plt.title("Portfolio Returns & Value at Risk (VaR)")
plt.legend()
plt.grid(True, alpha=0.3)
plt.show()
