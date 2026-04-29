import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from funkcija_6_1 import generate_data

X = generate_data(500, 1)

kmeans = KMeans(n_clusters=3, n_init=10, random_state=42)
kmeans.fit(X)

oznake = kmeans.labels_
centri = kmeans.cluster_centers_

plt.figure()
plt.scatter(X[:, 0], X[:, 1], c=oznake, cmap='viridis', alpha=0.6)
plt.scatter(centri[:, 0], centri[:, 1], c='red', marker='X', s=200, label='Centri')
plt.title('KMeans grupiranje (flagc=1)')
plt.legend()
plt.show()

#KMeans super radi kad su podaci u grupama.
#Ako su podaci cudnih oblika (polumjesec), algoritam grijesi jer trazi samo okrugle grupe.