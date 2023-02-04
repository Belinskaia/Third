import numpy as np
import imageio
import matplotlib.pyplot as plt

img = imageio.imread()
a = np.array([0.299, 0.587, 0.114, 1])
s = img.dot(a)
plt.imshow(s)
plt.show()
