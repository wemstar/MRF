__author__ = 'wemstar'
import numpy as np
import matplotlib.pyplot as plt


def boxMullerNormal(n=10000):
    Z=np.random.random([2,n])
    Z0=np.sqrt(-2.0*np.log(Z[0,:]))*np.cos(2.0*np.pi*Z[1,:])
    Z1=np.sqrt(-2.0*np.log(Z[0,:]))*np.cos(2.0*np.pi*Z[1,:])
    return np.concatenate((Z0,Z1))

def boxMullerPolar(n=10000):
    Z=np.random.random([2,n])*2.0-1.0


    Z=Z[:,np.sum(Z**2.0,axis=0)<1.0]
    Z=Z[:,np.sum(Z**2.0,axis=0)!=0.0]
    S=np.sum(Z**2.0,axis=0)
    Z0=np.sqrt(-2.0*np.log(S)/S)*Z[0,:]
    Z1=np.sqrt(-2.0*np.log(S)/S)*Z[1,:]
    return np.concatenate((Z0,Z1))

fig = plt.figure(figsize=plt.figaspect(.5))
ax = fig.add_subplot(1, 2, 1)



n, bins, patches = ax.hist(boxMullerNormal(), 100,normed=True)









ax = fig.add_subplot(1, 2, 2)



n, bins, patches = ax.hist(boxMullerPolar(), 100,normed=True)






plt.show()
