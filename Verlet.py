"""
CMod Ex2: velocity Verlet time integration of
two particles interacting via a Morse potential
Produces plots of the relative separation of the 2 particles and the total energy. Also
saves both to file.
The morse potential depends on several variables which are read in from a file.
"""

import sys
import math
import numpy as np
import matplotlib.pyplot as pyplot
from Particle3D import Particle3D
import Lennard_Jones as LJ
import MDUtilities

#Begin main code
def main():

    if len(sys.argv)!=3:
        print("Wrong number of arguments.")
        print("Usage: " + sys.argv[0] + "  <parameters file> <xyz output file>")
        quit()
    else:
        params_filename =sys.argv[1]
        outfile_name = sys.argv[2]
        
    
    #setup simulation parameters
    paramsfile = open(params_filename, "r")
    paramslines = paramsfile.readlines()
    paramsfile.close()
    mass = 1
    particle_num = float(paramslines[0])
    rho = float(paramslines[1])
    temp = float(paramslines[2])
    cutoff = float(paramslines[3])
    step_num = int(paramslines[4])
    dt = float(paramslines[5])
    
    #setup particles
    particles = []
    for x in range(int(particle_num)):
        particles.append(Particle3D("p%d" % x, mass))
        
    box = MDUtilities.set_initial_positions(rho, particles)
    MDUtilities.set_initial_velocities(temp, particles)
 
    #open output file
    outfile = open(outfile_name, "w")

    #write initial condtions to file
    outfile.write(str(particle_num)+  "\n")
    outfile.write("Point = 0\n")
    for particle in particles:
        outfile.write(str(particle)+ '\n')
        
    
    #get initial force
    forces = LJ.LJ_force(particles, box[0], cutoff)

    #initalise information to data lists
    time = 0
    time_list = [time]

    #start the time integration loop
    for i in range(step_num):
        #update particle positions are write new positions to file
        outfile.write(str(particle_num)+  "\n")
        outfile.write("Point = " + str(i+1)+  "\n")
        for j in range(len(particles)):
            particles[j].update_position2(dt, forces[j])
            outfile.write(str(particles[j])+ '\n')
        
        # update force
        new_forces = LJ.LJ_force(particles, box[0], cutoff)

        # update particle velocity by averaging
        # current and new forces
        for k in range(len(particles)):
            particles[k].update_velocity(dt, 0.5*(forces[k]+new_forces[k]))

        #re-define force value
        forces = new_forces
        #increase time
        time += dt

        #append data to lists
        time_list.append(time)

    #Post-simulation:
    #close output file
    outfile.close()


# Execute main method, but only when directly invoked
if __name__ == "__main__":
    main()
