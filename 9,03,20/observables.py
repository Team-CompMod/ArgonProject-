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
    :param x: 3-component distance vector between 2 particles
    :param l: length of side of box

    """
    halfbox = np.array([l/2,l/2,l/2])
    return np.mod(x + halfbox, l) - halfbox

def msd(particles,particle0):
    """
    :param particles: list of Particle3D objects 
    :param particle0: reference list of Particle3D objects
    
    """

    final_msd = 0
    N = len(particles)
    for i in range(N):
        msd_sqrt = np.linalg.norm(particles[i].position - particle0[i].position)
        msd = ((msd_sqrt)**2)/N #needs cleaning up
        
        final_msd += msd
        
    return final_msd

def rdf(particles, bin_list, bin_size):
    
    """
    Finds number of instances of particles in certain regular radial distances and tallies results.
    :param particles: list of Particle3D objects.
    :param bin_list: 
    :param bin_size: 
    
    """
    N  = len(particles)
    for i in range (N):
        for j in range (i+1,N):
            distance = np.linalg.norm(particles[i].position - particles[j].position)
            for k in range(len(bin_list)):
                if distance>k*bin_size and distance<=(k+1)*bin_size:
                    bin_list[k]+= 1

        
    
