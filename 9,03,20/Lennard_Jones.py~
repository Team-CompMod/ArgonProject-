"""

Contains function finding potential and force between N particles due to Lennard-Jones interactions.
Also finds total kinetic energy of a list of particles

"""

from Particle3D import *
import numpy as np
from numpy import linalg as LA
from observables import *

def LJ_force(particle,box_size,cutoff,sigma):

    """
    Calculates force due to Lennard-Jones interactions
     
    :param particle: list of Particle3D objects
    :param box_size: length of side of box created by MDUtilities
    :param cutoff: distance at which r starts  to take zero value
    :param sigma: reduced unit

    """
    
    N = len(particle)
    force = np.zeros(N, dtype = object)
    for i in range(N-1):
        for j in range(i+1,N):
            rij = (particle[i].position - particle[j].position)/sigma
            mic_rij = mic(rij,box_size)
            norm_rij = LA.norm(mic_rij)
            if norm_rij > cutoff:
                force_i = 0
            else:
                force_i = 48*((1/norm_rij)**14 - ((1/2)*((norm_rij)**8)))*rij
            force[i] += force_i
            force[j] += -force_i
    
    return(force)
        

         
def LJ_potential(particle,box_size,cutoff,sigma):

    """
    Calculates Lennard-Jones potential.
        
        :param particle: list of Particle3D objects
        :param box_size: length of side of box created by MDUtilities
        :param cutoff:
        :param sigma: reduced unit

    """
    N = len(particle)
    potential = np.zeros(N)
# need to apply reduced units here
    for i in range(N):
        for j in range (i+1, N):
        
        # apply minimum image convention to both (what box size do we use?)
            rij = (particle[i].position - particle[j].position)/sigma
            mic_rij = mic(rij,box_size)
            norm_rij = LA.norm(mic_rij)
            #print(norm_rij)
            if norm_rij > cutoff:
                potential_i = 0
            else:
                potential_i = 4*((1/norm_rij)**12 - (1/norm_rij)**6)
            potential[i] += potential_i
            potential[j] += -potential_i
        potential_sum = np.sum(potential)
        
    return(potential_sum)
               
def LJ_kinetic(particle):

    """
    Calculates total kinetic energy of list of particles
    :param particle: list of particles
    :
    :
    """
    N = len(particle)
    new_kinetic = 0
    for i in range(N):
        kinetic = particle[i].kinetic_energy()
        new_kinetic += kinetic
    
    return(new_kinetic)
        
