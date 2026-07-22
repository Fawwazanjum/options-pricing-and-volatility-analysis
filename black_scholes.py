import numpy as np
from scipy.stats import norm

def calculate_d1(S, K, T, r, sigma):
    return (np.log(S / K) + (r + (sigma**2 / 2)) * T) / (sigma * np.sqrt(T))

def calculate_d2(S, K, T, r, sigma):
    return calculate_d1(S, K, T, r, sigma) - sigma * np.sqrt(T)
 
def black_scholes_call(S, K, T, r, sigma):
    '''Calculate the Black-Scholes price of a European call option'''
    d1 = calculate_d1(S, K, T, r, sigma)
    d2 = calculate_d2(S, K, T, r, sigma)
    call_price = S * norm.cdf(d1) - (K * np.exp(-r * T) * norm.cdf(d2))
    return call_price


def black_scholes_put(S, K, T, r, sigma):
    '''Calculate the Black-Scholes price of a European put option, via put-call parity'''
    call_price = black_scholes_call(S, K, T, r, sigma)
    put_price = call_price + K * np.exp(-r * T) - S
    return put_price


if __name__ == "__main__":
    call_result = black_scholes_call(100, 100, 1, 0.05, 0.2)
    print(f"The Black-Scholes price of the call option is: {call_result:.2f}")

    put_result = black_scholes_put(100, 100, 1, 0.05, 0.2)
    print(f"The Black-Scholes price of the put option is: {put_result:.2f}")