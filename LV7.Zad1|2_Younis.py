import numpy as np
from tensorflow import keras
from tensorflow.keras import layers
from matplotlib import pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay


# MNIST podatkovni skup
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()

# TODO: prikazi nekoliko slika iz train skupa
plt.figure(figsize=(10, 4))
for i in range(9):
    plt.subplot(3, 3, i+1)
    plt.imshow(x_train[i], cmap='gray')
    plt.title(f'Labela: {y_train[i]}')
    plt.axis('off')
plt.suptitle('Primjeri iz MNIST train skupa')
plt.tight_layout()
plt.show()

# Skaliranje vrijednosti piksela na raspon [0,1]
x_train_s = x_train.astype("float32") / 255
x_test_s = x_test.astype("float32") / 255

# Slike 28x28 piksela se predstavljaju vektorom od 784 elementa
x_train_s = x_train_s.reshape(60000, 784)
x_test_s = x_test_s.reshape(10000, 784)

# Kodiraj labele (0, 1, ... 9) one hot encoding-om
y_train_s = keras.utils.to_categorical(y_train, 10)
y_test_s = keras.utils.to_categorical(y_test, 10)


# TODO: kreiraj mrezu pomocu keras.Sequential(); prikazi njenu strukturu pomocu .summary()
model = keras.Sequential()
model.add(layers.Dense(units=100, activation='relu', input_shape=(784,)))
model.add(layers.Dense(units=50, activation='relu'))
model.add(layers.Dense(units=10, activation='softmax'))
model.summary()

# TODO: definiraj karakteristike procesa ucenja pomocu .compile()
model.compile(loss='categorical_crossentropy', optimizer='sgd', metrics=['accuracy'])

# TODO: provedi treniranje mreze pomocu .fit()
model.fit(x_train_s, y_train_s, epochs=25, batch_size=32)

# TODO: Izracunajte tocnost mreze na skupu podataka za ucenje i skupu podataka za testiranje
print("\n Tocnost na train skupu")
train_loss, train_acc = model.evaluate(x_train_s, y_train_s, verbose=0)
print(f"Tocnost: {train_acc:.4f}")

print("\n Tocnost na train skupu")
train_loss, train_acc = model.evaluate(x_test_s, y_test_s, verbose=0)
print(f"Tocnost: {train_acc:.4f}")

# TODO: Prikazite matricu zabune na skupu podataka za testiranje
y_pred = np.argmax(model.predict(x_test_s), axis=1)

cm = confusion_matrix(y_test, y_pred)
disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot(cmap=plt.cm.Blues)
plt.title('Matrica zabune - testni skup')
plt.show()

# TODO: Prikazi nekoliko primjera iz testnog skupa podataka koje je izgrađena mreza pogresno klasificirala
pogresni = np.where(y_pred != y_test)[0]

np.random.seed(42)
odabrani = np.random.choice(pogresni, size=9, replace=False)

plt.figure(figsize=(10, 10))
for i, idx in enumerate(odabrani):
    plt.subplot(3, 3, i+1)
    plt.imshow(x_test[idx], cmap='gray')
    plt.title(f'Stvarno: {y_test[idx]} Predvidjeno: {y_pred[idx]}', fontsize=9)
    plt.axis('off')
plt.suptitle('Pogresno klasificirani primjeri')
plt.tight_layout()
plt.show()

print(f"Ukupno pogresno klasificaranih: {len(pogresni)} of {len(y_test)}")
