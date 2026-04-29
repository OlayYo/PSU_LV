import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
from sklearn import cluster

imageNew = mpimg.imread('example_grayscale.png')

if len(imageNew.shape) == 3:
    imageNew = np.mean(imageNew, axis=2)

X = imageNew.reshape((-1, 1))

n_clusters = 10
k_means = cluster.KMeans(n_clusters=n_clusters, n_init=1)
k_means.fit(X)

values = k_means.cluster_centers_.squeeze()
labels = k_means.labels_

face_compressed = np.choose(labels, values)
face_compressed.shape = imageNew.shape

plt.figure(1)
plt.imshow(imageNew, cmap='gray')
plt.title("Original")
plt.axis('off')

plt.figure(2)
plt.imshow(face_compressed, cmap='gray')
plt.title(f"Kvantizirano ({n_clusters} klastera)")
plt.axis('off')

plt.show()

#Sto je manje klustera to ima manje broj boja, pa slika izgleda jednostavinja (manje detalja).
#Smanjenjem broja boja štedimo prostor jer trebamo manje bita za prikaz svakog piksela.