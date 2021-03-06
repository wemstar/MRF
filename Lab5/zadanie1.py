import math
import numpy as np

__author__ = 'wemstar'
import scipy.stats as stats


def dt(S, X, r, sigma, T, wsp):
    return (math.log(S / X) + (r + wsp * ((sigma ** 2.0) / 2.0) * T)) / (sigma * math.sqrt(T))


def priceBuyOption(S, X, r, sigma, T):
    C1 = S * stats.norm.cdf(dt(S, X, r, sigma, T, 1.0))
    C2 = X * math.exp(r * (-T)) * stats.norm.cdf(dt(S, X, r, sigma, T, -1.0))
    return C1 - C2


def priceSellOption(S, X, r, sigma, T):
    P1 = X * math.exp(r * (-T)) * stats.norm.cdf(-dt(S, X, r, sigma, T, -1.0))
    P2 = S * stats.norm.cdf(-dt(S, X, r, sigma, T, 1.0))
    return P1 - P2


def funkcjaCenyKupno(S0, S):
    S = S - S0
    S[S < 0.0] = 0.0
    return S


def funkcjaCenySprzedaz(S0, S):
    S = S - S0
    S[S > 0.0] = 0.0
    return np.abs(S)


def monteOption(S, K, r, sigma, T, funkcjaCeny, n=10000000):
    m = r - (sigma ** 2.0) / 2.0
    R = np.random.normal(size=n) * sigma * np.sqrt(T) + m * T
    S0 = S * np.exp(R)
    B = funkcjaCeny(K, S0)
    return np.exp(-r * T) * np.mean(B)


print(priceBuyOption(100.0, 100.0, 0.0, 0.2, 0.5))
print(monteOption(100.0, 100.0, 0.0, 0.2, 0.5, funkcjaCenyKupno))
print(priceSellOption(100.0, 100.0, 0.0, 0.2, 0.5))
print(monteOption(100.0, 100.0, 0.0, 0.2, 0.5, funkcjaCenySprzedaz))
