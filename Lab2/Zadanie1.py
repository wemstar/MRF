__author__ = 'wemstar'
import numpy as np




def wyliczPi(n=1000000):
        para=np.random.random([2,n])
        return (np.sum(np.sum(para**2.0,axis=0) < 1.0))/float(n)*4.0

def err(dane):
        mean=np.mean(dane)
        sigma=np.sqrt(np.sum((dane-mean)**2.0))
        return sigma
def proby(p=10,n=1000000):
        z=[]
        for x in range(p):
             z.append(wyliczPi(n))
        print("Wartosc pi= {0} +- {1}".format(np.mean(z),err(z)))
proby(10,10**6)
proby(10,10**8)