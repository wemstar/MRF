__author__ = 'wemstar'
import numpy as np
import pylab as P

def generaterandomarray(n):
    return np.random.random(n)
def generateArray(n=10**6,m=2):
    return [np.sum(generaterandomarray(m)) for x in range(n)]
def gaussian(x, mu, sig):
    return np.exp(-np.power(x - mu, 2.) / 2 * np.power(sig, 2.))

fig, axes = P.subplots(nrows=2, ncols=1, figsize=(6, 6))

count, bins, ignored=axes[0].hist(generateArray(),100, normed=1, histtype='stepfilled', facecolor='g', alpha=0.75)
#axes[0].plot(gaussian(np.arange(0.0,2.0,0.05),1.0,1.0))
count, bins, ignored=axes[1].hist(generateArray(10**5,100),100, normed=1, histtype='stepfilled', facecolor='g', alpha=0.75)
axes[1].plot(0.14*gaussian(bins,50.0,1.0))
P.show()