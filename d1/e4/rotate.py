import numpy as np
from PIL import Image
from load_image import ft_load
from zoom import ft_zoom
from matplotlib import pyplot as plt

def main():
    try:
        img_ar = ft_zoom()
        if img_ar is None:
            return
        img_ar = img_ar.squeeze()
        new_img = np.zeros(img_ar.shape, dtype=img_ar.dtype)
        for x in range(img_ar.shape[0]):
            for y in range(img_ar.shape[1]):
                new_img[x][y] = img_ar[y][x]
        print(f"New shape after Transpose: {new_img.shape}")
        plt.imshow(new_img, cmap="gray")
        plt.show()
        print(new_img)
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
    return

if __name__ == "__main__":
    main()  