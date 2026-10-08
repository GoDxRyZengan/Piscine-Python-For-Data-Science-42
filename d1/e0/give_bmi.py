import numpy as np

def give_bmi(height: list[int | float], weight: list[int | float]) -> list[int | float]:
    if (type(height) is not list or type(weight) is not list):
        raise TypeError('Arguement must be of type list')
    if (len(height) != len(weight)):
        raise ValueError('Different size of list')
    h = np.array(height)
    w = np.array(weight)
    if not(np.all(h > 0) and np.all(w > 0)):
        raise ValueError('Int or float must be positive')
    bmi = w / (h ** 2)
    return bmi.tolist()

def apply_limit(bmi: list[int | float], limit: int) -> list[bool]:
    bmi_np = np.array(bmi)
    is_above = np.array(bmi_np > limit)
    return is_above.tolist()