"""
Contains functions for periodic boundary conditions, minimum image convention and mean squared displacement.

"""

import numpy as np #importing necessary libraries
import random
import math
from Particle3D import Particle3D
from numpy import linalg as LA

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

def msd(particles,particle0,box_size):
    """
    :param particles:
    :param particle0:
    """

    final_msd = 0
    N = len(particles)
    for i in range(N):
        msd_mic = mic(Particle3D.sep(particles[i], particle0[i]),box_size)
        msd = LA.norm(msd_mic)
        msd = ((msd)**2)/N
        
        final_msd += msd
        
    return final_msd
    
def rdf(particles,rho, bins, box_size):
    bins_list = np.zeros(bins)
    dist_list = []
    N  = len(particles)
    for i in range (N):
        for j in range (i+1,N):
            sep = Particle3D.sep(particles[i],particles[j])
            distances = LA.norm(mic(sep,box_size))/(N*rho)
            dist_list.append(distances)
    #compute the size of each bin
    bin_size = (max(dist_list)- min(dist_list))/bins
    # Compare the value of dist_list against the range of each bin
    dist_N = len(dist_list)
    for i in range (dist_N):
        for j in range (bins):
            if dist_list[i]>=j*bin_size and dist_list[i]<=(j+1)*bin_size:
                bins_list[j]=bins_list[j] + 1
    # normalise each of the bins
    for n in range (bins):
        r = (n*bin_size+(n+1)*bin_size)/2
        bins_list[n] = bins_list[n]/(4*bin_size*math.pi*rho*(r**2))
        
    dist_list2 = []
    for i in range(bins):
        r = (i*bin_size + (i +1)*bin_size)/2
        dist_list2.append(r)
        
    return bins_list, dist_list2
        
    # prepare for plotting
    
    
                
        

    
        
    
