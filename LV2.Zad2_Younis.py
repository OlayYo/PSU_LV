import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt(open("D:/lmao/mtcars.csv", "rb"), usecols=(1,2,3,4,5,6),
delimiter=",", skiprows=1)

mpg = data[:, 0] 
cyl = data[:, 1] 
hp = data[:, 3] 
wt = data[:, 5]

plt.figure()

scatter = plt.scatter(hp, mpg, s=wt*20, c='blue', alpha=0.7, edgecolors='black')

plt.xlabel('Konjske snage (hp)')
plt.ylabel('Potrošnja (mpg)')
plt.title('Ovisnost potrošnje o konjskim snagama')
plt.grid(True)


for tezina in [2, 3, 4, 5]:
    plt.scatter([], [], s=tezina*20, c='blue', alpha=0.7,
edgecolors='black', label=f'wt ≈ {tezina}')
plt.legend(title='Tezina (lb/1000)', loc='upper right')

plt.show()

print("Statistike potrošnje (svi automobili)")
print(f"Minimalna potrošnja (mpg): {mpg.min():.2f}")
print(f"Maksimalna potrošnja (mpg): {mpg.max():.2f}")
print(f"Srednja potrošnja (mpg): {mpg.mean():.2f}")

mpg_6cyl = mpg[cyl == 6]

print("\n e) Statistike potrošnje (samo 6-cilindarski automobili)")
print(f"Broj automobila sa 6 cilindara: {len(mpg_6cyl)}")
print(f"Minimalna potrošnja (mpg): {mpg_6cyl.min():.2f}")
print(f"Maksimalna potrošnja (mpg): {mpg_6cyl.max():.2f}")
print(f"Srednja potrošnja (mpg): {mpg_6cyl.mean():.2f}")




























