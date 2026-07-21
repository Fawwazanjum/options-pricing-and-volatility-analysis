# Options Pricing & Volatility Analysis

A from-scratch implementation of options pricing models in Python, built as a way to
combine quantitative finance theory with practical software engineering.

This is an early, in-progress checkpoint. More models, analysis, and tooling are being
added incrementally.

## Current status (Phase 1)

- Black-Scholes pricing for European **call** and **put** options
- Put price derived from the call price via put-call parity
- Verified against hand calculations

Everything else (Greeks, implied volatility, additional models, tests, CLI, etc.) is
planned but not yet implemented — this README will be updated as those land.

## Usage

```bash
pip install -r requirements.txt
python black_scholes.py
```

```python
from black_scholes import black_scholes_call, black_scholes_put

call_price = black_scholes_call(S=100, K=100, T=1, r=0.05, sigma=0.2)
put_price = black_scholes_put(S=100, K=100, T=1, r=0.05, sigma=0.2)
```

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

## License

MIT — see [LICENSE](LICENSE).
