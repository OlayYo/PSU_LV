import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from sklearn import cluster

imageNew = mpimg.imread('example.png')

visina, sirina, kanali = imageNew.shape
X = imageNew.reshape((-1, kanali))

n_colors = 64
k_means = cluster.KMeans(n_clusters=n_colors, n_init=5)
k_means.fit(X)

values = k_means.cluster_centers_
labels = k_means.labels_

imageNew_compressed = values[labels]
imageNew_compressed.shape = imageNew.shape

imageNew_compressed = np.clip(imageNew_compressed, 0, 1)

plt.figure(1)
plt.title('Originalna slika')
plt.imshow(imageNew)
plt.axis('off')

plt.figure(2)
plt.title(f'Kvantizirana slika ({n_colors} boja)')
plt.imshow(imageNew_compressed)
plt.axis('off')

plt.show()

#Sto je manje boja to ima manje broj boja, pa slika izgleda jednostavinja (manje detalja).
#Smanjenjem broja boja štedimo prostor jer trebamo manje bita za prikaz svakog piksela.