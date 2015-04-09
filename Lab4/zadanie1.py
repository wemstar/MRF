import numpy as np
import scipy
import scipy.stats
import matplotlib.pyplot as plt
from matplotlib.patches import Ellipse
import math
n=10**5.0
a=2.0
b=-1.0
c=-1.0
d=1.0
e=0.5
f=2.0


x=np.zeros([2,n])

g1=np.random.normal(0.0,1.0,n)
g2=np.random.normal(0.0,1.0,n)
x[0,:]=a*g1+b*g2+c
x[1,:]=d*g1+e*g2+f

z=np.cov(x)
p=scipy.stats.pearsonr(x[0,:],x[1,:])
print("Rozklad 1 srednia: {0} wariancja {1}".format(np.mean(x[0,:]),np.std(x[0,:])**2.0))
print("Rozklad 2 srednia: {0} wariancja {1}".format(np.mean(x[1,:]),np.std(x[1,:])**2.0))

own,own1=np.linalg.eig(z)

fig = plt.figure()
ax = fig.add_subplot(111, aspect='equal')

ax.scatter(x[0,:],x[1,:])
ax.add_artist(Ellipse(xy=[c,f], width=own[0], height=own[1], angle=math.atan2(own1[0,1],own1[0,0])/(2.0*math.pi)*360.0))

print(z)
print(p)
print(own,own1)
plt.show()
