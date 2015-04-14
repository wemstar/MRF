__author__ = 'wemstar'
import numpy as np

n=10**5
C=[[1.0,0.4,-0.6],
   [0.4,1.0,0.0],
   [-0.6,0.0,4.0]]
L=np.linalg.cholesky(C)
g=np.random.normal(0.0,1.0,[3,n])
x=np.dot(L,g)
Cov=np.cov(x)
Pear=np.corrcoef(x)
np.set_printoptions(precision=4,suppress=True)
print(Cov)
print(Pear)
