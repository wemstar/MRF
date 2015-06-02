__author__ = 'wemstar'
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from projekt.Enums import OptionType, BarierType
from projekt.PriceFunction import normalOptionCall, normalOptionPut, BarierOprionModel
from projekt.BinomialImplementation import binomial

M=2000
strike=100.0
barierLevels = np.arange(80., 120.,2.)

priceCallOut = []
pricePutOut = []
priceCallIn = []
pricePutIn = []

for barierLevel in barierLevels:
    barierCallOut = BarierOprionModel(OptionType.Call, barierLevel, BarierType.Out)
    barierPutOut = BarierOprionModel(OptionType.Put, barierLevel, BarierType.Out)
    barierCallIn = BarierOprionModel(OptionType.Call, barierLevel, BarierType.In)
    barierPutIn = BarierOprionModel(OptionType.Put, barierLevel, BarierType.In)

    priceCallOut.append(binomial(S0=98.0, T=1., r=0.05, vola=0.2, M=M, strike=strike, function=barierCallOut))
    pricePutOut.append(binomial(S0=98.0, T=1., r=0.05, vola=0.2, M=M, strike=strike, function=barierPutOut))
    priceCallIn.append(binomial(S0=98.0, T=1., r=0.05, vola=0.2, M=M, strike=strike, function=barierCallIn))
    pricePutIn.append(binomial(S0=98.0, T=1., r=0.05, vola=0.2, M=M, strike=strike, function=barierPutIn))

priceCallV = binomial(S0=98.0, T=1., r=0.05, vola=0.2, M=M, strike=strike, function=normalOptionCall)
pricePutV = binomial(S0=98.0, T=1., r=0.05, vola=0.2, M=M, strike=strike, function=normalOptionPut)
priceCall = np.zeros(len(barierLevels))
pricePut = np.zeros(len(barierLevels))
priceCall.fill(priceCallV)
pricePut.fill(pricePutV)

priceCallOut = np.array(priceCallOut)
pricePutOut = np.array(pricePutOut)
priceCallIn = np.array(priceCallIn)
pricePutIn = np.array(pricePutIn)

fig = plt.figure()

ax = fig.add_subplot(221)

ax.plot(barierLevels, priceCallOut)
ax.plot(barierLevels, priceCall)
ax.set_title('Bariera Out opcji Call')
ax.set_xlabel(u'Wartosc bariery')
ax.set_ylabel('Cena opcji')


ax = fig.add_subplot(222)
ax.plot(barierLevels, pricePutOut)
ax.plot(barierLevels, pricePut)
ax.set_title('Bariera Out opcji Put')
ax.set_xlabel(u'Wartosc bariery')
ax.set_ylabel('Cena opcji')

ax = fig.add_subplot(223)
ax.plot(barierLevels, priceCallIn)
ax.plot(barierLevels, priceCall)
ax.set_title('Bariera In opcji Call')
ax.set_xlabel(u'Wartosc bariery')
ax.set_ylabel('Cena opcji')

ax = fig.add_subplot(224)
ax.plot(barierLevels, pricePutIn)
ax.plot(barierLevels, pricePut)
ax.set_title('Bariera In opcji Put')
ax.set_xlabel(u'Wartosc bariery')
ax.set_ylabel('Cena opcji')

plt.tight_layout()
plt.savefig('Opcje.png')
plt.show()
