# Options Pricing & Volatility Analysis

A from-scratch implementation of options pricing models in Python, built as a way to
combine quantitative finance theory with practical software engineering.

This is an early, in-progress checkpoint. More models, analysis, and tooling are being
added incrementally.

## Current status (Phase 1)

- Black-Scholes pricing for European **call** and **put** options
- Put price derived from the call price via put-call parity
- `d1` / `d2` factored into shared helper functions (`calculate_d1`, `calculate_d2`) so
  other modules can reuse them
- Greeks: delta, gamma, vega, theta, rho (call and put where applicable)
- A couple of plots looking at how call delta behaves (see [Plots](#plots) below)
- Verified against hand calculations

Everything else (implied volatility, additional models, tests, CLI, etc.) is planned
but not yet implemented — this README will be updated as those land.

## Usage

```bash
pip install -r requirements.txt
python black_scholes.py
python greeks.py
python plot_greeks.py
```

```python
from black_scholes import black_scholes_call, black_scholes_put
from greeks import delta_call, gamma, vega, theta_call, rho_call

call_price = black_scholes_call(S=100, K=100, T=1, r=0.05, sigma=0.2)
put_price = black_scholes_put(S=100, K=100, T=1, r=0.05, sigma=0.2)
call_delta = delta_call(S=100, K=100, T=1, r=0.05, sigma=0.2)
```

## Plots

![Call and put delta vs stock price](plots/delta_vs_price.png)

![Call delta vs stock price for different times to expiry](plots/delta_vs_price_multi_T.png)

Call delta plotted against stock price, for four different times to expiry. For the
short-dated option (T = 0.1) delta jumps quite sharply from 0 to 1 around the strike —
with so little time left, the option is close to knowing whether it'll finish in or out
of the money. The longer-dated curves (T = 1, T = 2) are much more gradual, since
there's more time for the stock price to move around before expiry, so it's harder to
say which way it'll end up.

**Parameters**

| Symbol | Meaning |
|--------|---------|
| `S` | Current price of the underlying asset |
| `K` | Strike price |
| `T` | Time to expiration, in years |
| `r` | Risk-free interest rate (annualized) |
| `sigma` | Volatility of the underlying (annualized) |

## Requirements

- Python 3.9+
- numpy
- scipy
- matplotlib

## License

MIT — see [LICENSE](LICENSE).
