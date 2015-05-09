__author__ = 'wemstar'
import numpy as np
from projekt.PriceFunction import normalOption
def binomial(S0=100., T=1., r=0.05, vola=0.20, M=1000, strike=100, function=normalOption):
    """
    Wycena opcji za pomoca modelu binormalnego
    :param S0: float wartość pierwotna indeksu
    :param T: float czas ykonania opcji (Lata)
    :param r: float
    :param vola: float zmienność
    :param M: float ilośc kroków czaowych
    :param strike: float wartość wykonania
    :return: float wycena opcji

    """
    dt = T / M
    df = np.exp(-r * dt)
    u = np.exp(vola * np.sqrt(dt))
    d = 1 / u
    q = (np.exp(r * dt) - d) / (u - d)
    mu = np.arange(M + 1)
    mu = np.resize(mu, (M + 1, M + 1))
    md = np.transpose(mu)
    mu = u ** (mu - md)
    md = d ** md
    S = S0 * mu * md
    pv = function(S, strike)
    z = 0
    for t in range(M - 1, -1, -1):
        pv[0:M - z, t] = (q * pv[0:M - z, t + 1] + (1 - q) * pv[1:M - z + 1, t + 1]) * df
        z += 1
    return pv[0, 0]