import numpy as np
import matplotlib.pyplot as plt
from greeks import delta_call, delta_put, gamma, vega

stock_prices = np.linspace(50, 150, 200)
K, T, r, sigma = 100, 1, 0.05, 0.2

# Chart 1: Call and Put Delta vs Stock Price

deltas_call = [delta_call(S, K, T, r, sigma) for S in stock_prices]
deltas_put = [delta_put(S, K, T, r, sigma) for S in stock_prices]

plt.figure(figsize=(8, 5))
plt.plot(stock_prices, deltas_call, label="Delta (Call)")
plt.plot(stock_prices, deltas_put, label="Delta (Put)")
plt.axvline(x=K, color='gray', linestyle='--', label='Strike (K)')
plt.axhline(y=0, color='black', linewidth=0.5)
plt.xlabel("Stock Price (S)")
plt.ylabel("Delta")
plt.title("Call and Put Delta vs Stock Price")
plt.legend()
plt.grid(True)
plt.savefig("plots/delta_vs_price.png")
plt.show()

# Chart 2: Call Delta vs Stock Price for Different Times to Expiry
K, r, sigma = 100, 0.05, 0.2
T_values = [0.1, 0.5, 1, 2]
plt.figure(figsize=(8, 5))
for T in T_values:
    deltas = [delta_call(S, K, T, r, sigma) for S in stock_prices]
    plt.plot(stock_prices, deltas, label=f"T = {T}")

plt.axvline(x=K, color='gray', linestyle='--', label='Strike (K)')
plt.xlabel("Stock Price (S)")
plt.ylabel("Delta")
plt.title("Call Delta vs Stock Price, at Different Times to Expiry")
plt.legend()
plt.grid(True)
plt.savefig("plots/delta_vs_price_multi_T.png")
plt.show()

# Chart 3: Gamma vs Stock Price
K, T, r, sigma = 100, 1, 0.05, 0.2
gammas = [gamma(S, K, T, r, sigma) for S in stock_prices]
plt.figure(figsize=(8, 5))
plt.plot(stock_prices, gammas, label="Gamma")
plt.axvline(x=K, color='gray', linestyle='--', label='Strike (K)')
plt.xlabel("Stock Price (S)")
plt.ylabel("Gamma")
plt.title("Gamma vs Stock Price")
plt.legend()
plt.grid(True)
plt.savefig("plots/gamma_vs_price.png")
plt.show()

# Chart 4: Vega vs Stock Price
vegas = [vega(S, K, T, r, sigma) for S in stock_prices]
plt.figure(figsize=(8, 5))
plt.plot(stock_prices, vegas, label="Vega")
plt.axvline(x=K, color='gray', linestyle='--', label='Strike (K)')
plt.xlabel("Stock Price (S)")
plt.ylabel("Vega")
plt.title("Vega vs Stock Price")
plt.legend()
plt.grid(True)
plt.savefig("plots/vega_vs_price.png")
plt.show()
