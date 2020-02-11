"""
CompMod Exercise 1: Periodic Boundary Conditions.
Creates 2 methods, one for finding the image of a particle inside simulation box
where 0 ≤ xi < l, and the second which finds the closest image to the origin.

Callum Moore s1722906
"""

import numpy as np

def originbox(x, l):
    """
    Finds the corresponding image of particle x which is located in 
    the original simulation box

    :param x: 3d numpy array
    :param l: simulation box size
    :return: 3d numpy array np.mod(x,l)
    """
    return np.mod(x,l)

def closestimage(x,l):
    """
    Finds the closest image, of particle x, to the origin 

    :param x: vector (v1, v2, v3)3d numpy array
    :param l: simulation box size
    :return: 3d numpy array corresponding to image closest to origin
    """
    halfbox = np.array([l/2,l/2,l/2])
    return np.mod(x + halfbox, l) - halfbox
