from tensorflow import keras
from tensorflow.keras import layers, models, callbacks
from tensorflow.keras.utils import to_categorical
from sklearn.metrics import confusion_matrix, accuracy_score
import numpy as np
import matplotlib.pyplot as plt

# MNIST podatkovni skup
(x_train, y_train), (x_test, y_test) = keras.datasets.mnist.load_data()
x_train_s = x_train.reshape(-1, 28, 28, 1) / 255.0
x_test_s = x_test.reshape(-1, 28, 28, 1) / 255.0

y_train_s = to_categorical(y_train, num_classes=10)
y_test_s = to_categorical(y_test, num_classes=10)

# TODO: strukturiraj konvolucijsku neuronsku mrezu

model = keras.Sequential()
model.add(layers.Conv2D(32, (3, 3), activation = "relu", input_shape=(28, 28, 1)))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Conv2D(64, (3, 3), activation="relu"))
model.add(layers.MaxPooling2D((2, 2)))
model.add(layers.Flatten())
model.add(layers.Dense(64, activation="relu"))
model.add(layers.Dense(10, activation="softmax"))
model.summary()

# TODO: definiraj karakteristike procesa ucenja pomocu .compile()

model.compile(loss="categorical_crossentropy", optimizer="sgd", metrics=["accuracy"])

# TODO: definiraj callbacks

my_callbacks = [keras.callbacks.TensorBoard(log_dir="logs", update_freq=100),
                keras.callbacks.ModelCheckpoint(filepath="best_model.h5", 
                                                monitor="val_accuracy", 
                                                mode="max", 
                                                save_best_only=True)]

# TODO: provedi treniranje mreze pomocu .fit()

model.fit(x_train_s, y_train_s, epochs=50, batch_size=64, callbacks=my_callbacks, validation_split=0.1)

#TODO: Ucitaj najbolji model

best_model = keras.models.load_model("best_model.h5")

# TODO: Izracunajte tocnost mreze na skupu podataka za ucenje i skupu podataka za testiranje

y_pred_train = np.argmax(best_model.predict(x_train_s), axis=1)
y_pred_test = np.argmax(best_model.predict(x_test_s), axis=1)

print("Tocnost na train skupu: ", accuracy_score(y_train, y_pred_train))
print("Tocnost na test skupu: ", accuracy_score(y_test, y_pred_test))

# TODO: Prikazite matricu zabune na skupu podataka za testiranje

cm = confusion_matrix(y_test, y_pred_test)
print("matrica zabune (testni skup): ")
print(cm)

plt.figure()
plt.imshow(cm, cmap="Blues")
plt.colorbar()
plt.xlabel("Predicted label")
plt.ylabel("True label")
plt.title("Matrica zabune (testni skup)")
plt.show()




