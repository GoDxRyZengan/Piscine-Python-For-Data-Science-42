import numpy as np
from matplotlib import pyplot as plt
from PIL import Image

def ft_invert(array):
    """Inverts the color of the image received"""
    inv_img = 255 - array
    plt.imshow(inv_img)
    plt.show()
    return inv_img

def ft_red(array):
    """Change image color to red"""
    red_array = array.copy()
    red_array[:,: ,1] = 0
    red_array[:,: ,2] = 0
    plt.imshow(red_array)
    plt.show()
    return red_array

def ft_green(array):
    """Change image color to green"""
    green_array = array.copy()
    green_array[:,: ,0] = 0
    green_array[:,: ,2] = 0
    plt.imshow(green_array)
    plt.show()
    return green_array

def ft_blue(array):
    """Change image color to blue"""
    blue_array = array.copy()
    blue_array[:,: ,0] = 0
    blue_array[:,: ,1] = 0
    plt.imshow(blue_array)
    plt.show()
    return blue_array

def ft_grey(array):
    """Change image color to grey"""
    grey_array = array.copy()
    grey = np.mean(grey_array, axis=2)
    grey_array[:, :, 0] = grey
    grey_array[:, :, 1] = grey
    grey_array[:, :, 2] = grey
    # for x in grey_array:
    #     for j in grey_array[x]:
    #         if (grey_array[x][j][0] >= grey_array[x][j][1] and grey_array[x][j][0] >= grey_array[x][j][2]):
    #             grey_array[x][j][1] = grey_array[x][j][0]
    #             grey_array[x][j][2] = grey_array[x][j][0]
    #         elif (grey_array[x][j][1] >= grey_array[x][j][0] and grey_array[x][j][1] >= grey_array[x][j][2]):
    #             grey_array[x][j][0] = grey_array[x][j][1]
    #             grey_array[x][j][2] = grey_array[x][j][1]
    #         else:
    #             grey_array[x][j][0] = grey_array[x][j][2]
    #             grey_array[x][j][1] = grey_array[x][j][2]
    plt.imshow(grey_array)
    plt.show()       
    return grey_array