import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from funkcija_6_1 import generate_data

X = generate_data(500, 1)

inercije = []
K_raspon = range(1, 21)

for k in K_raspon:
    kmeans = KMeans(n_clusters=k, n_init=10, random_state=42)
    kmeans.fit(X)
    inercije.append(kmeans.inertia_)

plt.figure()
plt.plot(K_raspon, inercije, 'bo-')
plt.xlabel('Broj klastera K')
plt.ylabel('Kriterijska funkcija (inercija)')
plt.title('Elbow metoda - odabir optimalnog K')
plt.xticks(K_raspon)
plt.grid(True)
plt.show()

#Graf prikazuje pad kriterijske funkcije (inercije) kako raste broj klastera.
#Optimalno K je tocka gdje se graf naglo lomi (izgleda kao lakat).