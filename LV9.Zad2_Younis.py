import numpy as np
import matplotlib.pyplot as plt
from tensorflow import keras
from tensorflow.keras import layers
from tensorflow.keras.preprocessing import image_dataset_from_directory
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay
from tensorflow.python.keras.layers import Dense


# 1. Učitavanje podataka
train_ds = image_dataset_from_directory(
    
    directory='C:/Users/student/Downloads/gtsrb/Train',
    labels='inferred',
    label_mode='categorical',
    batch_size=32,
    subset="training",
    seed=123,
    validation_split=0.2, # 20% podataka ide za validaciju
    image_size=(48, 48))

validation_ds = image_dataset_from_directory(
    directory='C:/Users/student/Downloads/gtsrb/Train',
    labels='inferred',
    label_mode='categorical',
    batch_size=32,
    subset="validation",
    seed=123,
    validation_split=0.2, # 20% podataka ide za validaciju
    image_size=(48, 48))

# Testni skup (shuffle=False je OBAVEZAN za ispravnu matricu zabune)
test_ds = image_dataset_from_directory(
    directory='C:/Users/student/Downloads/gtsrb/Test',
    labels='inferred',
    label_mode='categorical',
    batch_size=32,
    image_size=(48, 48),
    shuffle=False)

# 2. Izgradnja modela prema Slici 9.2
model = keras.Sequential()

# Normalizacija ulaza
model.add(layers.Rescaling(1./255, input_shape=(48, 48, 3)))

# BLOK 1: 32 filtara
model.add(layers.Conv2D(32, (3, 3), activation='relu', padding='same'))
model.add(layers.Conv2D(32, (3, 3), activation='relu', padding='valid'))
model.add(layers.MaxPooling2D((2, 2), strides=2))
model.add(layers.Dropout(0.2))

# BLOK 2: 64 filtara
model.add(layers.Conv2D(64, (3, 3), activation='relu', padding='same'))
model.add(layers.Conv2D(64, (3, 3), activation='relu', padding='valid'))
model.add(layers.MaxPooling2D((2, 2), strides=2))
model.add(layers.Dropout(0.2))

# BLOK 3: 128 filtara
model.add(layers.Conv2D(128, (3, 3), activation='relu', padding='same'))
model.add(layers.Conv2D(128, (3, 3), activation='relu', padding='valid'))
model.add(layers.MaxPooling2D((2, 2), strides=2))
model.add(layers.Dropout(0.2))

# Potpuno povezani slojevi
model.add(layers.Flatten())
model.add(layers.Dense(512, activation='relu'))
model.add(layers.Dropout(0.5))
model.add(layers.Dense(43, activation='softmax')) # 43 izlazna neurona za 43 klase

# Provjera broja parametara (Treba biti 1,358,155)
model.summary()

# 3. Kompiliranje
model.compile(loss='categorical_crossentropy',
              optimizer='adam',
              metrics=['accuracy'])

# 4. Callbacks: TensorBoard i ModelCheckpoint
my_callbacks = [
    keras.callbacks.TensorBoard(log_dir='logs', update_freq=100),
    keras.callbacks.ModelCheckpoint(filepath='best_model_gtsrb.h5',
                                    monitor='val_accuracy',
                                    mode='max',
                                    save_best_only=True)
]

# 5. Treniranje modela
history = model.fit(train_ds,
                    epochs=20, # Prilagodi po potrebi
                    callbacks=my_callbacks,
                    validation_data=validation_ds)

# 6. Učitavanje najboljeg modela i evaluacija na testnom skupu
best_model = keras.models.load_model('best_model_gtsrb.h5')

_, test_acc = best_model.evaluate(test_ds, verbose=0)
print(f"Tocnost na testnom skupu: {test_acc:.4f}")

# 7. Matrica zabune
y_true = np.concatenate([np.argmax(y.numpy(), axis=1) for x, y in test_ds])
y_pred = np.argmax(best_model.predict(test_ds), axis=1)

cm = confusion_matrix(y_true, y_pred)
fig, ax = plt.subplots(figsize=(15, 15)) # Veća slika radi 43 klase
disp = ConfusionMatrixDisplay(confusion_matrix=cm)
disp.plot(cmap=plt.cm.Blues, ax=ax, values_format='d')
plt.title('Matrica zabune - testni skup')
plt.xticks(rotation=90)
plt.show()



