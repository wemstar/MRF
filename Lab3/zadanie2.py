
import numpy as np
import random
import math
import scipy.stats as stats
def bootStrap(dane,estymator,n=20):
	wartosci=[]
	for x in range(n):
		tablica=[random.choice(dane) for z in range(len(dane))]
		wartosci.append(estymator(tablica))
	srednia=np.mean(wartosci)
	err=np.std(wartosci)*math.sqrt(n-1)
	return srednia, err
def jackKnife(dane,estymator):
	wartosci=[]
	for x in range(len(dane)):
		noweDane=np.delete(dane,x)
		wartosci.append(estymator(noweDane))
	srednia=np.mean(wartosci)
	err=np.std(wartosci)
	return srednia,err

gauss=bootStrap(np.random.normal(size=10000),stats.kurtosis)
flat=bootStrap(np.random.random(size=10000),np.mean)
print(" Wynik estymatora {:f} blad {:f}".format(*gauss))
print(stats.kurtosis(gauss))
print(" Wynik estymatora {:f} blad {:f}".format(*flat))

