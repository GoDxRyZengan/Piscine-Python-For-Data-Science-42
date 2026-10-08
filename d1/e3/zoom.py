import numpy as np
from PIL import Image
from load_image import ft_load
from matplotlib import pyplot as plt

def main():
    try:
        img_ar = ft_load("animal.jpg")
        if img_ar is None:
            return
        print(img_ar)
        img_ar = img_ar[100:500, 450:850, 0:1]
        print(img_ar)
        print(f"New shape after slicing: {img_ar.shape} "
              f"or ({len(img_ar)}, {len(img_ar[0])})")
        print(img_ar)
        plt.imshow(img_ar, cmap="gray")
        plt.show()
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
    return

if __name__ == "__main__":
    main()  