import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras
from PIL import Image

# Rječnik svih 43 klasa za ljepši ispis
klase = {
    0: '20 km/h', 1: '30 km/h', 2: '50 km/h', 3: '60 km/h',
    4: '70 km/h', 5: '80 km/h', 6: 'kraj 80 km/h', 7: '100 km/h',
    8: '120 km/h', 9: 'zabrana pretjecanja', 10: 'zabrana pretjecanja kamiona',
    11: 'raskrizje prioritet', 12: 'prioritetna cesta', 13: 'ustupite prolaz',
    14: 'stop', 15: 'zabrana prometa', 16: 'zabrana kamiona', 17: 'zabranjeni ulaz',
    18: 'opasnost', 19: 'lijeva krivina', 20: 'desna krivina',
    21: 'dvostruke krivine', 22: 'neravna cesta', 23: 'klizava cesta',
    24: 'suzenje s desna', 25: 'radovi', 26: 'semafor', 27: 'pješaci',
    28: 'djeca', 29: 'biciklisti', 30: 'led/snijeg', 31: 'divljac',
    32: 'kraj svih ogranicenja', 33: 'desno obavezno', 34: 'lijevo obavezno',
    35: 'ravno obavezno', 36: 'ravno ili desno', 37: 'ravno ili lijevo',
    38: 'drži desno', 39: 'drži lijevo', 40: 'kružni tok',
    41: 'kraj zabrane pretjecanja', 42: 'kraj zabrane pretjecanja kamiona'
}

# 1. Učitavanje modela sačuvanog u Zadatku 2
model = keras.models.load_model('best_model_gtsrb.h5')

# 2. Učitavanje i priprema proizvoljne slike s interneta
ime_slike = 'C:/Users/student/Downloads/znak4.png' # Promijenite ime ako se slika zove drugačije
img = Image.open(ime_slike).convert('RGB')
img_resized = img.resize((48, 48)) # Skaliranje na dimenziju 48x48 koju mreža očekuje

img_array = np.array(img_resized)
img_array = np.expand_dims(img_array, axis=0) # Dodavanje batch dimenzije (1, 48, 48, 3)

# 3. Predikcija
predikcija = model.predict(img_array)
indeks_klase = np.argmax(predikcija)
vjerojatnost = np.max(predikcija) * 100

# 4. Prikaz rezultata
plt.imshow(img_resized)
plt.title(f'Predvidjeno: {klase[indeks_klase]}')
plt.axis('off')
plt.show()

print(f"Mreža je prepoznala klasu {indeks_klase}: {klase[indeks_klase]} uz vjerojatnost od {vjerojatnost:.2f}%")
