import numpy as np

def slice_me(family: list, start: int, end: int) -> list:
    if (type(start) != int or type(end) != int):
        raise TypeError('End and Start value must be of int type')
    if (type(family) != list):
        raise ValueError('The family argument must be a list')
    size = len(family[0])
    for x in family:
        if len(x) != size:
            raise ValueError('The array must have the same size')
    array = np.array(family)
    if array.ndim != 2:
        raise ValueError('The array must be 2D')
    print(f"\rMy shape is : ({len(family)}, {len(family[0])})")
    sliced_array = array[start:end]
    print(f"\rMy new shape is : ({len(sliced_array)}, {len(sliced_array[0])})")

    return sliced_array.tolist()