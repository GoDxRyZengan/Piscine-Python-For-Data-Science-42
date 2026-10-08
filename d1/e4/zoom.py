import numpy as np
from PIL import Image
from load_image import ft_load
from matplotlib import pyplot as plt

def ft_zoom():
    try:
        img_ar = ft_load("animal.jpg")
        if img_ar is None:
            return
        img_ar = img_ar[100:500, 450:850, 0:1]
        print(f"The shape of image is: {img_ar.shape} "
              f"or ({len(img_ar)}, {len(img_ar[0])})")
        print(img_ar)
        return img_ar
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
    return None