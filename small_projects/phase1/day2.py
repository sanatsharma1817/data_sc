# load any image using matplotlib.image.imread()
# convert it to grayscale by averaging RGB channels
# increase/decrease brightness by adding/subtracting a constant
# flip the image horizontally and vertically
# crop a region using array slicing
# display all versions side-by-side
# apply a blur effect by averaging pixel values with neighbors

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.image as mpimg

img = mpimg.imread("image.jpg")

gray = np.mean(img[:, :, :3], axis=2)

bright = np.clip(gray + 50, 0, 255)

dark = np.clip(gray - 50, 0, 255)

horizontal_flip = np.fliplr(gray)

vertical_flip = np.flipud(gray)

cropped = gray[50:200, 50:200]

blur = (
    gray[:-2, :-2] +
    gray[1:-1, :-2] +
    gray[2:, :-2] +
    gray[:-2, 1:-1] +
    gray[1:-1, 1:-1] +
    gray[2:, 1:-1] +
    gray[:-2, 2:] +
    gray[1:-1, 2:] +
    gray[2:, 2:]
) / 9

fig, axes = plt.subplots(2, 4, figsize=(15, 8))

axes[0, 0].imshow(img)
axes[0, 0].set_title("original")

axes[0, 1].imshow(gray, cmap="gray")
axes[0, 1].set_title("gray")

axes[0, 2].imshow(bright, cmap="gray")
axes[0, 2].set_title("bright")

axes[0, 3].imshow(dark, cmap="gray")
axes[0, 3].set_title("dark")

axes[1, 0].imshow(horizontal_flip, cmap="gray")
axes[1, 0].set_title("horizontal")

axes[1, 1].imshow(vertical_flip, cmap="gray")
axes[1, 1].set_title("vertical")

axes[1, 2].imshow(cropped, cmap="gray")
axes[1, 2].set_title("cropped")

axes[1, 3].imshow(blur, cmap="gray")
axes[1, 3].set_title("blur")

plt.show()