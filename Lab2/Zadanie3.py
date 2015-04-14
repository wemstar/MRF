__author__ = 'wemstar'
import numpy as np
import matplotlib.pyplot as plt
import cProfile, pstats, io

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

pr = cProfile.Profile()
pr.enable()
n, bins, patches = ax.hist(boxMullerNormal(), 100,normed=True)
pr.disable()
s = io.StringIO()
sortby = 'cumulative'
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print(s.getvalue())




ax = fig.add_subplot(1, 2, 2)
pr = cProfile.Profile()
pr.enable()

n, bins, patches = ax.hist(boxMullerPolar(), 100,normed=True)

pr.disable()
s = io.StringIO()
sortby = 'cumulative'
ps = pstats.Stats(pr, stream=s).sort_stats(sortby)
ps.print_stats()
print(s.getvalue())
plt.show()