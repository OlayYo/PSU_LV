import numpy as np
import matplotlib.pyplot as plt

def sachovnica(velicina_kvadrata, broj_redaka, broj_stupaca):
    v = velicina_kvadrata
    bijeli = np.ones((v, v), dtype=np.uint8) * 255
    crni = np.zeros((v, v), dtype=np.uint8)

    redovi = []
    for i in range(broj_redaka):
        red = []
        for j in range(broj_stupaca):
            if (i + j) % 2 == 0:
                red.append(bijeli)
            else:
                red.append(crni)
        redovi.append(np.hstack(red))

    slika = np.vstack(redovi)
    return slika

img = sachovnica(25, 8, 9)

plt.imshow(img, cmap='gray', vmin=0, vmax=255)
plt.show()
