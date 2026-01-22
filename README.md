# Quantitative Risk Lab 
**Current Status:** Active Sprint (Jan 2026)

## Objective
To build a production-grade Risk Management engine in Python that bridges the gap between academic theory and financial regulation (Basel III).

## Modules (The 60-Day Roadmap)
1. **Market Risk Engine:** Historical, Parametric, and Monte Carlo VaR. (In Progress)
2. **Volatility Forecasting:** GARCH(1,1) vs. EWMA. (Upcoming)
3. **Credit Risk:** Merton Model & Probability of Default. (Upcoming)
4. **Stress Testing:** Scenario Analysis for Macro-Economic Shocks. (Upcoming)

## Tech Stack
* **Language:** Python
* **Libraries:** Pandas, NumPy, Scikit-Learn, SciPy
* **Data Source:** Yahoo Finance (yfinance), FRED (Federal Reserve)

## Day 3: Monte Carlo Simulation 🎲
**Goal:** Predict future portfolio performance using stochastic simulations.

**What I built:**
- Implemented **Monte Carlo VaR** (Value at Risk) using 10,000 simulations.
- Used **Cholesky Decomposition** to apply accurate correlation between assets (e.g., ensuring AAPL and MSFT move together).
- **Result:** The model predicts a maximum loss of $X (replace with your number) at 95% confidence.

**Tech Stack:** Python, NumPy, Linear Algebra.
