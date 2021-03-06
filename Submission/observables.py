"""
Contains functions for periodic boundary conditions, minimum image convention and mean squared displacement.

"""

import numpy as np #importing necessary libraries
import random
import math
from Particle3D import Particle3D

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
    compares inital particle positions to current positions and calculates a mean squared displacement
    :param particles:
    :param particle0:
    """

    final_msd = 0
    N = len(particles)
    for i in range(N):
        msd_sqrt = np.linalg.norm(particles[i].position - particle0[i].position)
        msd = ((msd_sqrt)**2)/N
        
        final_msd += msd
        
    return final_msd

def rdf(particles, bin_list, bin_size, box_size):
    #finds the separation between each particle pair nd increments the correct historgram bin based on this distnace
    N  = len(particles)
    for i in range (N):
        for j in range (i+1,N):
            displacement = particles[i].position - particles[j].position
            closest_displacement = mic(displacement, box_size)
            distance = np.linalg.norm(closest_displacement)
            for k in range(len(bin_list)):
                if distance>k*bin_size and distance<=(k+1)*bin_size:
                    bin_list[k]+= 1


    
        
    
