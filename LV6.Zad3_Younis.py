import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import dendrogram, linkage
from funkcija_6_1 import generate_data

X = generate_data(500, 1)

Z = linkage(X, method='ward')

plt.figure(figsize=(12, 6))
dendrogram(Z, truncate_mode='lastp', p=20)
plt.title('Dendogram - hijerarhijsko grupiranje (ward)')
plt.xlabel('Klaster')
plt.ylabel('Udaljenost')
plt.show()

#Izgleda kao stablo koje pokazuje kako se podaci spajaju u veće grupe.
#Različite metode (poput ward) mijenjaju način i udaljenost na kojoj se grupe spajaju.