import math

__author__ = 'wemstar'
import scipy.stats as stats

def priceBuyOption(S,X,r,sigma,T):
    C1=S*stats.norm.cdf((math.log(S/X)+(r + (sigma**2.0)/2.0)*T)/(sigma*math.sqrt(T)))
    C2=X*math.exp(r*(-T))*stats.norm.cdf((math.log(S/X)+(r-(sigma**2.0)/2.0)*T)/(sigma*math.sqrt(T)))
    return C1-C2
def priceSellOption(S,X,r,sigma,T):
    P1=X*math.exp(r*(-T))*stats.norm.cdf(-(math.log(S/X)-(r-(sigma**2.0)/2.0)*T)/(sigma*math.sqrt(T)))
    P2=S*stats.norm.cdf((-math.log(S/X)-(r + (sigma**2.0)/2.0)*T)/(sigma*math.sqrt(T)))
    return P1-P2

print(priceBuyOption(98.0,100.0,0.05,0.2,0.25))
print(priceSellOption(98.0,100.0,0.05,0.2,0.25))
