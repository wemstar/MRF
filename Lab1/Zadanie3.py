__author__ = 'wemstar'

import pylab as P
import math
import numpy as np
def funkcjaA(data):
    return 2.0 * data - 1.0

def funkcjaB(data):
    return data ** 2.0

def funkcjaC(data):
    return P.sqrt(data)

def funkcjaD(data):
    return P.log(data)

def funkcjaE(data):
    return P.tan(math.pi / 2.0 * funkcjaA(data))


def histogramuj(data,axes):
    pairs=P.zeros([len(data),2])
    for i,x in enumerate(data):
        pairs[i,1]=x
        pairs[i,0]=i/(len(data))
    axes.plot(pairs[:,1],pairs[:,0])

def histRange(data, rangeX, bins=100):
    hist = np.zeros(bins)
    xmin = rangeX[0]
    dx = (rangeX[1] - xmin) / (bins - 1)
    data = data[data > rangeX[0]]
    data = data[data < rangeX[1]]
    for x in data:
        hist[int(math.floor((x - xmin) / dx))] += 1
    return hist / len(data)

data = np.random.random(3000)

histogramA = P.sort(funkcjaA(data))
histogramB = P.sort(funkcjaB(data))
histogramC = P.sort(funkcjaC(data))
histogramD = P.sort(funkcjaD(data))
histogramE = P.sort(funkcjaE(data))

fig, axes = P.subplots(nrows=2, ncols=3, figsize=(6, 6))

histogramuj(histogramA,axes[0,0])
histogramuj(histogramB,axes[0,1])
histogramuj(histogramC,axes[0,2])
histogramuj(histogramD,axes[1,0])
histogramuj(histogramE,axes[1,1])
P.show()