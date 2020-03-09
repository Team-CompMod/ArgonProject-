"""
Contains functions for periodic boundary conditions, minimum image convention and mean squared displacement.

"""

import numpy as np #importing necessary libraries
import random
import math
from Particle3D import Particle3D

def pbc(x,scalar):

    """
    Applies periodic boundary conditions to particles
    :param x:
    :param scalar:
 
    """
    
    length  = len(x)
    x_image  = []
    for i in range(length):
        element = x[i] % scalar
        x_image.append(element)
    return(x_image)

def mic(x,l):

    """
    Finds nearest image of particle
    :param x:
    :param l:

    """
    halfbox = np.array([l/2,l/2,l/2])
    return np.mod(x + halfbox, l) - halfbox

def msd(particles,particle0):
    """
    :param particles:
    :param particle0:
    """

    final_msd = 0
    N = len(particles)
    for i in range(N):
        msd_sqrt = np.mod(particle[i].position - particle0.position)
        msd = ((msd_sqrt)**2)/N #needs cleaning up
        
        final_msd += msd
        
    return final_msd
    
        
    
