__author__ = 'wemstar'
import numpy as np
import math
import random
import pylab as P

def rozklad(x):
        return 2.0/math.pi*(math.sqrt(1.0-x**2.0))

def generateValues(n=10**5):
        prawdziwe=np.zeros([n, 2])
        for b in range(n):
                x=(random.random()-0.5)*2.0
                y=(random.random())*2.0/math.pi
                if y <= rozklad(x):
                        prawdziwe[b,0]=x
                        prawdziwe[b,1]=y
        return prawdziwe


tablica=np.array(generateValues())

n, bins, patches = P.hist(tablica[:,0], 100,normed=True)
P.setp(patches, 'facecolor', 'g', 'alpha', 0.75)

y=[]
wart=np.arange(-0.9,0.9,0.01)
for x in wart:
        y.append(rozklad(x))
y=np.array(y)
l = P.plot(wart, y, 'k--', linewidth=1.5)
P.show()
