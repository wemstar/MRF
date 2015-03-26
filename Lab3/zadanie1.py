import pylab as P
import scipy
import scipy.stats
from scipy.stats import cauchy
import numpy as np

n=100000
wartosci=[]
srednia=[]
odchylenie=[]

wartosciCauchy=[]
sredniaCauchy=[]
odchylenieCauchy=[]


for x in range(n):
	wartosci.append(np.random.normal())
	srednia.append(np.mean(P.array(wartosci)))
	odchylenie.append(np.std(P.array(wartosci)))
	wartosciCauchy.append(cauchy.rvs())
	sredniaCauchy.append(np.mean(P.array(wartosciCauchy)))
	odchylenieCauchy.append(np.std(P.array(wartosciCauchy)))

fix, ax = P.subplots(4,1)
ax[0].plot(srednia)
zero=np.arange(len(srednia))
zero[:]=0.0
ax[0].plot(zero)
ax[0].set_title('Srednia Gauss')
ax[1].plot(odchylenie)
jeden=np.arange(len(srednia))
jeden[:]=1.0
ax[1].plot(jeden)
ax[1].set_title('Odchylenie Gauss')
ax[2].plot(sredniaCauchy)
ax[2].set_title('Srednia Cauchy')
ax[3].plot(odchylenieCauchy)
ax[3].set_title('Odchylenie Cauchy')

P.show()