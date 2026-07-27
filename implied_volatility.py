import numpy as np
from scipy.stats import norm
from black_scholes import black_scholes_call
from greeks import vega

def implied_volatility(market_price, S, K, T, r, initial_guess = 1.5, tolerance = 0.0001, max_iterations = 100):
    """
    Calculate the implied volatility of a European call option using the Newton-Raphson method.

    Parameters:
    market_price: The market price of the option.
    S: Current stock price.
    K: Strike price of the option.
    T: Time to expiration in years.
    r: Risk-free interest rate.
    initial_guess: Initial guess for volatility. Default is 0.2 (20%).
    tolerance: The acceptable error margin for convergence. Default is 0.0001.
    max_iterations: Maximum number of iterations to perform. Default is 100.

    Returns:
    The implied volatility that matches the market price, or None if not found.
    """
    floor = max(S - K * np.exp(-r * T), 0)
    if market_price < floor:
        print(f"Warning: market_price ({market_price}) is below the arbitrage-free floor ({floor:.4f}) — no valid implied volatility exists.")
        return None
    
    sigma = initial_guess
    for i in range(max_iterations):
        price = black_scholes_call(S, K, T, r, sigma)
        difference = price - market_price
        
        if abs(difference) < tolerance:
            return sigma 
        
        v = vega(S, K, T, r, sigma)
        sigma = sigma - (difference / v)

    print("Warning: implied volatility did not converge")
    return sigma

# if __name__ == "__main__":
    # Test: use your known test case in reverse.
    # You know that S=100, K=100, T=1, r=0.05, sigma=0.2 gives a price of 10.45.
    # So feed 10.45 back in as the "market price" and check you recover sigma=0.2.
    true_sigma = 0.6
    test_price = black_scholes_call(100, 100, 1, 0.05, true_sigma)
    recovered_sigma = implied_volatility(test_price, 100, 100, 1, 0.05)
    print(f"True sigma: {true_sigma}, Recovered sigma: {recovered_sigma:.6f}")
    # --- Edge case test: arbitrage-violating price ---
    print("\n--- Testing an impossible (arbitrage-violating) market price ---")
    S, K, T, r = 100, 100, 1, 0.05
    floor = max(S - K * np.exp(-r * T), 0)
    print(f"Arbitrage floor for this option: {floor:.4f}")

    bad_price = 2.0  # deliberately below the floor
    result = implied_volatility(bad_price, S, K, T, r)
    print(f"Result when market_price = {bad_price}: {result}")