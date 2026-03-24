import numpy as np
import matplotlib.pyplot as plt

img = plt.imread("D:/lmao/tiger.png")
img = img[:,:,0].copy()
print(img.shape)
print(img.dtype)
plt.figure()
plt.imshow(img, cmap="gray")
plt.show()

min_value = image.min()
max_value = image.max()
print('min value = ', min_value)
print('max value = ', max_value)

plt.imshow(img, cmap='gray', vmax=10000)
plt.colorbar()