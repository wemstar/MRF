import pylab as P
import scipy
import scipy.stats
from scipy.stats import cauchy
import numpy as np

n = 10000000
wartosci = []
srednia = []
odchylenie = []

wartosciCauchy = np.random.standard_cauchy(n)
sredniaCauchy=np.cumsum(wartosciCauchy)/np.arange(1,n+1)
odchylenieCauchy = []

"""for x in range(n):
    #wartosci.append(np.random.normal())
    #srednia.append(np.mean(P.array(wartosci)))
    #odchylenie.append(np.std(P.array(wartosci)))
    sredniaCauchy.append(np.mean(P.array(wartosciCauchy[:x])))
    odchylenieCauchy.append(np.std(P.array(wartosciCauchy[:x])))"""

fix, ax = P.subplots(4, 1)
ax[0].plot(srednia)
zero = np.arange(len(srednia))
zero[:] = 0.0
ax[0].plot(zero)
ax[0].set_title('Srednia Gauss')
ax[1].plot(odchylenie)
jeden = np.arange(len(srednia))
jeden[:] = 1.0
ax[1].plot(jeden)
ax[1].set_title('Odchylenie Gauss')
ax[2].plot(sredniaCauchy)
ax[2].set_title('Srednia Cauchy')
ax[3].plot(odchylenieCauchy)
ax[3].set_title('Odchylenie Cauchy')

P.show()
