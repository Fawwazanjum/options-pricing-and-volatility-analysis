import yfinance as yf
import pandas as pd
from datetime import datetime
from implied_volatility import implied_volatility
import matplotlib.pyplot as plt

# ============================================
# Setup: ticker, expiry, spot price
# ============================================

ticker = yf.Ticker("SPY")
expiry = "2026-09-18"

options_chain = ticker.option_chain(expiry)
calls = options_chain.calls

spot_price = ticker.history(period="1d")['Close'].iloc[-1]
print(f"Spot price: {spot_price}")

# ============================================
# Filtering: strike range + liquidity
# ============================================

lower_bound = spot_price * 0.8
upper_bound = spot_price * 1.2

filtered_calls = calls[
    (calls['strike'] >= lower_bound) &
    (calls['strike'] <= upper_bound) &
    (calls['bid'] > 0) &
    (calls['ask'] > 0) &
    (calls['volume'] >= 50)  # keep your liquidity filter too, worth retaining
]

filtered_calls = filtered_calls.copy()
filtered_calls['market_price'] = (filtered_calls['bid'] + filtered_calls['ask']) / 2

print(f"Number of usable strikes: {len(filtered_calls)}")

# ============================================
# Calculating T (time to expiry, in years)
# ============================================

today = datetime.now()
expiry_date = datetime.strptime(expiry, "%Y-%m-%d")

days_to_expiry = (expiry_date - today).days
T = days_to_expiry / 365

print(f"Days to expiry: {days_to_expiry}, T (years): {T:.4f}")

# ============================================
# Running the implied volatility solver across all strikes
# ============================================

S = spot_price
r = 0.05  # approximate risk-free rate

implied_vols = []
strikes = []

for index, row in filtered_calls.iterrows():
    K = row['strike']
    market_price = row['market_price']

    iv = implied_volatility(market_price, S, K, T, r)

    if iv is not None:
        implied_vols.append(iv)
        strikes.append(K)

print(f"Successfully calculated IV for {len(implied_vols)} out of {len(filtered_calls)} strikes")
for K, iv in zip(strikes, implied_vols):
    print(f"Strike: {K:.0f}, Implied Vol: {iv:.4f}")

plt.figure(figsize=(10, 6))
plt.plot(strikes, implied_vols, marker='o', linestyle='-')
plt.axvline(x=spot_price, color='gray', linestyle='--', label=f'Spot Price (S={spot_price:.2f})')
plt.xlabel("Strike Price (K)")
plt.ylabel("Implied Volatility")
plt.title(f"SPY Volatility Skew — Expiry {expiry}")
plt.legend()
plt.grid(True)
plt.savefig("plots/volatility_smile.png")
plt.show()

print(filtered_calls[filtered_calls['strike'].isin([730, 734, 735, 737, 820, 822, 823, 825])][['strike', 'lastPrice', 'volume', 'openInterest']])