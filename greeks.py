import numpy as np
from scipy.stats import norm
from black_scholes import calculate_d1, calculate_d2

def delta_call(S, K, T, r, sigma):
    '''Calculate the delta of a European Call option'''
    d1 = calculate_d1(S, K, T, r, sigma)
    return norm.cdf(d1)

def delta_put(S, K, T, r, sigma):
    '''Calculate the delta of a European Put option'''
    d1 = calculate_d1(S, K, T, r, sigma)
    return norm.cdf(d1) - 1

def gamma(S, K, T, r, sigma):
    "Calculate the gamma of a European Option"
    d1 = calculate_d1(S, K, T, r, sigma)
    return norm.pdf(d1)/(S * sigma * np.sqrt(T))

def vega(S, K, T, r, sigma):
    "Calculate the vega of a European Option"
    d1 = calculate_d1(S, K, T, r, sigma)
    return S * norm.pdf(d1) * np.sqrt(T)

def theta_call(S, K, T, r, sigma):
    d1 = calculate_d1(S, K, T, r, sigma)
    d2 = calculate_d2(S, K, T, r, sigma)
    term1 = -(S * norm.pdf(d1) * sigma) / (2 * np.sqrt(T))
    term2 = r * K * np.exp(-r * T) * norm.cdf(d2)
    return term1 - term2

def theta_put(S, K, T, r, sigma):
    d1 = calculate_d1(S, K, T, r, sigma)
    d2 = calculate_d2(S, K, T, r, sigma)
    term1 = -(S * norm.pdf(d1) * sigma) / (2 * np.sqrt(T))
    term2 = r * K * np.exp(-r * T) * norm.cdf(-d2)
    return term1 + term2

def rho_call(S, K, T, r, sigma):
    d2 = calculate_d2(S, K, T, r, sigma)
    return K * T * np.exp(-r * T) * norm.cdf(d2)

def rho_put(S, K, T, r, sigma):
    d2 = calculate_d2(S, K, T, r, sigma)
    return -K * T * np.exp(-r * T) * norm.cdf(-d2)

if __name__ == "__main__":
    S, K, T, r, sigma = 100, 100, 1, 0.05, 0.2

    print(f"Delta (call): {delta_call(S, K, T, r, sigma):.4f}")
    print(f"Delta (put):  {delta_put(S, K, T, r, sigma):.4f}")
    print(f"Gamma:        {gamma(S, K, T, r, sigma):.4f}")
    print(f"Vega:         {vega(S, K, T, r, sigma):.4f}")
    print(f"Theta (call): {theta_call(S, K, T, r, sigma):.4f}")
    print(f"Rho (call):   {rho_call(S, K, T, r, sigma):.4f}")
    print(f"Theta (put):  {theta_put(S, K, T, r, sigma):.4f}")
    print(f"Rho (put):    {rho_put(S, K, T, r, sigma):.4f}")