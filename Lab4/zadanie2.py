__author__ = 'wemstar'
import numpy as np

n = 10 ** 5.0
m = 4
g = np.random.normal(0.0, 1.0, [m, n])
A = np.random.random([m, m])
mi = np.random.random(m)
x = np.dot(A, g)
for i in range(len(mi)):
    x[i, :] += mi[i]


print("Macierz koleralcji")
print(np.cov(x))
print("Wynik A* At")
print(np.dot(A,A.T))
print("Macierz korelacji persona")
print(np.corrcoef(x))



