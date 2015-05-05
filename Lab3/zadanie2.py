import numpy as np
import random
import math
import scipy.stats as stats
#-*- coding: utf-8 -*-


def vonNeuman(pdf, n, xrange, yrange):
    x = np.random.uniform(xrange[0], xrange[1], 10.0 * n)
    y = np.random.uniform(yrange[0], yrange[1], 10.0 * n)
    mask = (y <= pdf(x))

    return x[mask]


def ekspotential(x):
    return np.exp(-x)


def flat(x):
    return np.ones(x.shape)


def cpdf(x, mi=0.0, sigma=1.0):
    return np.exp((-(np.log(x) - mi) ** 2.0) / 2.0 * sigma ** 2.0) / (np.sqrt(2.0 * np.pi * sigma ** 2.0) * x)


def dpdf(x, alpha=0.5, sigma=1.0):
    return alpha / (np.sqrt(2.0 * np.pi)) * np.exp(-(x ** 2.0) / 2.0) + (1. - alpha) / (
        np.sqrt(2.0 * np.pi * sigma ** 2.0)) * np.exp((-x ** 2.0) / (2.0 * sigma ** 2.0))


def bootStrap(dane, estymator, n=20):
    wartosci = np.random.choice(dane, [len(dane), n])
    wartosci = estymator(wartosci, axis=0)
    srednia = np.mean(wartosci)
    err = np.std(wartosci) * math.sqrt(n - 1)
    return srednia, err


def jackKnife(dane, estymator):
    wartosci = []
    for x in range(len(dane)):
        noweDane = np.delete(dane, x)
        wartosci.append(estymator(noweDane))
    srednia = np.mean(wartosci)
    err = np.std(wartosci)
    return srednia, err


flatPdf = vonNeuman(flat, 1000, [0.0, 1.0], [0.0, 1.0])
expPdf = vonNeuman(ekspotential, 10000, [0.0, 6.0], [0.0, 1.0])
cPdf = vonNeuman(cpdf, 10000, [0.0, 6.0], [0.0, 1.0])
dPdf = vonNeuman(dpdf, 10000, [0.0, 6.0], [0.0, 1.0])
for pdf,ops in zip([flatPdf,expPdf,cPdf,dPdf],["Rozkad A","Rozkad B","Rozkad C","Rozkad D"]):
    print(ops)
    for funkcje,opis in zip([np.mean,np.std,stats.skew,stats.kurtosis],["srednia","Odchylenie standarowe","Skonosc","Kurtoza"]):
        print(opis)
        jack = jackKnife(pdf, funkcje)
        boot=bootStrap(pdf,funkcje)
        print("Wartosc dla JackKnife {:f} niepewno {:f} wartoc dla BootStrap {:f} niepewnosc {:f}".format(jack[0],jack[1],boot[0],boot[1]))




