import time
import numpy as np
import matplotlib.pyplot as plt

def puissanceN(q, n):
    tps_debut = time.time()
    x=1
    for k in range(1, n+1):
        x=x*q
    tps_fin = time.time()
    return tps_fin - tps_debut

def puissanceR(q, n):
    tps_debut = time.time()
    r, x, e = 1, q, n
    while e!=0:
        if e%2==0:
            x=x*x
            e=e//2
        else:
            r=r*x
            e=e-1
    tps_fin = time.time()
    return tps_fin - tps_debut

q = 1.2345
puissances = np.linspace(0, 5000000, 5)
N = []
R = []
for elt in puissances:
    N.append(puissanceN(q, int(elt)))
    R.append(puissanceR(q, int(elt)))

plt.plot(puissances, N, label= "Naïf")
plt.plot(puissances, R, label= "Rapide")
plt.legend()
plt.show()
