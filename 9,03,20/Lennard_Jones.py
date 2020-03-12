"""

Contains function finding potential and force between N particles due to Lennard-Jones interactions.
Also finds total kinetic energy of a list of particles

"""

from Particle3D import *
import numpy as np
from numpy import linalg as LA
from observables import *

def LJ_force(particle,box_size,cutoff):

    """
    Calculates force due to Lennard-Jones interactions
     
    :param particle: list of Particle3D objects
    :param box_size: length of side of box created by MDUtilities
    :param cutoff: radius at which we set distance between two particles to zero value
   
    """
    
    N = len(particle)
    force = np.zeros(N, dtype = object)
    for i in range(N):
        for j in range(i+1,N):
            rij = (particle[i].position - particle[j].position)
            mic_rij = mic(rij,box_size)
            norm_rij = LA.norm(mic_rij)
            if norm_rij > cutoff:
                force_i = 0
            else:
                force_i = 48*((1/norm_rij)**14 - ((1/2)*((1/norm_rij)**8)))*(mic_rij)
            force[i] += force_i
            force[j] += -force_i
    
    return(force)
        

         
def LJ_potential(particle,box_size,cutoff):

    """
    Calculates Lennard-Jones potential.
        
        :param particle: list of Particle3D objects
        :param box_size: length of side of box created by MDUtilities
        :param cutoff: radius at which we set distance between two particles to zero value

    """
    N = len(particle)
    potential = 0.0
    
    for i in range(N):
        for j in range (i+1, N):
        
            rij = (particle[i].position - particle[j].position)
            mic_rij = mic(rij,box_size)
            norm_rij = LA.norm(mic_rij)
            #print(norm_rij)
            if norm_rij > cutoff:
                potential += 0
            else:
                potential += 4*((1/norm_rij)**12 - (1/norm_rij)**6)
        
    return(potential)
               
def LJ_kinetic(particle):

    """
    Calculates total kinetic energy of list of particles
    :param particle: list of Particle3D objects
    
    """
    N = len(particle)
    new_kinetic = 0
    for i in range(N):
        kinetic = particle[i].kinetic_energy()
        new_kinetic += kinetic
    
    return(new_kinetic)
        
