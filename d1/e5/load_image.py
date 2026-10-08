from PIL import Image
import numpy as np

def ft_load(path: str) -> list:
    try:
        if not path.endswith((".jpg", ".jpeg")):
            raise ValueError('Image must be of .jpeg or .jpg extention')
        image = Image.open(path)
        if not image:
            raise FileNotFoundError(f"File not found at location: {path}")
        format = ["JPEG", "JPG"]
        if image.format not in format:  
            raise ValueError('File not in good format')
        image = image.convert('RGB')
        img_ar = np.array(image)
        print(f"The shape of image is: ({len(img_ar)}, {len(img_ar[0])}, {(img_ar.ndim)})")
        print(img_ar)
        return img_ar
    except Exception as e:
        print(f"{type(e).__name__}: {e}")
    return None