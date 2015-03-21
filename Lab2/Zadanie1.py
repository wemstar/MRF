__author__ = 'wemstar'
import numpy as np



def wyliczPi(n=1000000):
        prawdziwe=0;
        for x in range(n):
                para=np.random.random(2)
                if para[0] ** 2.0 +para[1]**2.0 <1.0:
                        prawdziwe+=1
        return 4.0*float(prawdziwe)/float(n)
def err(dane):
        mean=np.mean(dane)
        sigma=np.sqrt(np.sum((dane-mean)**2.0))
        return sigma
def proby(p=10,n=1000000):
        z=[]
        for x in range(p):
                z.append(wyliczPi(n))
        z=np.array(z)
        print("Wartosc pi= {0} +- {1}".format(np.mean(z),err(z)))
proby(10,10**6)
proby(10,10**8)