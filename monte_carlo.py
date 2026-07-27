import numpy as np

# Monte Carlo isn't strictly necessary for a European call like this one - Black-Scholes
# already gives an exact closed-form answer (10.45 for the parameters below). But Monte
# Carlo generalizes to option types where no closed-form solution exists (path-dependent
# payoffs, early exercise, etc.), so it's worth confirming here that it converges to the
# same 10.45 we already know to be correct before relying on it elsewhere.
def monte_carlo_option_pricing(S, K, T, r, sigma, num_simulations=10000):
    Z = np.random.standard_normal(num_simulations)
    S_T = S * np.exp((r - (sigma ** 2) / 2) * T + sigma * np.sqrt(T) * Z)

    payoffs = np.maximum(S_T - K, 0)

    option_price = np.exp(-r * T) * np.mean(payoffs)
    return option_price


if __name__ == "__main__":
    print(monte_carlo_option_pricing(100, 100, 1, 0.05, 0.2))
    for n in [100, 1000, 10000, 100000, 1000000]:
        price = monte_carlo_option_pricing(100, 100, 1, 0.05, 0.2, num_simulations=n)
        print(f"Simulations: {n:>8}, Price: {price:.4f}")