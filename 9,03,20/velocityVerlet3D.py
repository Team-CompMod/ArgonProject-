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
import MDUtlities

#Begin main code
def main():
    '''
    if len(sys.argv)!=5:
        print("Wrong number of arguments.")
        print("Usage: " + sys.argv[0] + " <output file> <particle1 file> <particle2 file> <parameters file>")
        quit()
    else:
        outfile_name = sys.argv[1]
        p1_filename = sys.argv[2]
        p2_filename = sys.argv[3]
        params_filename =sys.argv[4]
    
    #setup morse potential parameters
    paramsfile = open(params_filename, "r")
    paramslines = paramsfile.readlines()
    paramsfile.close()
    a = float(paramslines[0])
    r = float(paramslines[1])
    d = float(paramslines[2])
    dt = float(paramslines[3])
    numstep = int(paramslines[4])
    '''
    if len(sys.argv)!=3:
        print("Wrong number of arguments.")
        print("Usage: " + sys.argv[0] + "  <parameters file> <xyz output file>")
        quit()
    else:
        outfile_name = sys.argv[2]
        params_filename =sys.argv[1]
    
    #setup simulation parameters
    paramsfile = open(params_filename, "r")
    paramslines = paramsfile.readlines()
    paramsfile.close()
    mass = 1
    particle_num = float(paramslines[])  
    rho = float(paramslines[1])
    temp = float(paramslines[2])
    cutoff = float(paramslines[3])
    step_num = float(paramslines[4])
    dt = float(paramslines[5])
    
    #setup particles
    particles = []
    for x in range(10):
        particles.append(Particle3D("p%d" % x, mass))
        
    set_initial_positions(rho, particles)
    set_initial_velocities(temp, particles)
    
    '''
    #open output file
    outfile = open(outfile_name, "w")

    #write initial condtions to file
    time = 0.0
    energy  = pot_energy(p1,p2,a,r,d) + p1.kinetic_energy() + p2.kinetic_energy()
    separation = np.linalg.norm(Particle3D.separation(p1,p2))
    outfile.write("{0:f} {1:12.8f} {2:12.8f}\n".format(time,separation,energy))

    #get initial force
    force = force_dw(p1, p2, a, r, d)

    #initalise information to data lists
    time_list = [time]
    sep_list = [separation]
    energy_list = [energy]
    

    #start the time integration loop
    for i in range(numstep):
        #update particle positions
        p1.leap_pos2nd(dt, force)
        p2.leap_pos2nd(dt, -force)

        # update force
        force_new = force_dw(p1, p2, a, r, d)
        # update particle velocity by averaging

        # current and new forces
        p1.leap_velocity(dt, 0.5*(force+force_new))
        p2.leap_velocity(dt, -0.5*(force+force_new))
        
        #re-define force value
        force = force_new        
        #increase time
        time += dt

        #output new data to file
        energy  = pot_energy(p1,p2,a,r,d) + p1.kinetic_energy() + p2.kinetic_energy()
        separation = np.linalg.norm(Particle3D.separation(p1,p2))
        outfile.write("{0:f} {1:12.8f} {2:12.15f}\n".format(time,separation,energy))

        #append data to lists
        time_list.append(time)
        sep_list.append(separation)
        energy_list.append(energy)

    #Post-simulation:
    #close output file
    outfile.close()
    '''
    #open output file
    outfile = open(outfile_name, "w")

    #write initial condtions to file
    outfile.write(str(particle_num))
    outfile.write("Point = " + 0))
    for particle in particles:
        outfile.write(particle)
        
    #get initial force
    force = force_dw(particles, size, cutoff)

    #initalise information to data lists
    time_list = [time]

    #start the time integration loop
    for i in range(step_num):
        #update particle positions are write new positions to file
        outfile.write(str(particle_num))
        outfile.write("Point = " + (i+1))
        for j in range(len(particles)):
            particles[j].leap_pos2nd(dt, forces[j])
            outfile.write(particles[j])
        
        # update force
        new_forces = force_dw(particles, size, cutoff)

        # update particle velocity by averaging
        # current and new forces
        for k in range(len(particles)):
            particles[k].leap_velocity(dt, 0.5*(forces[k]+new_forces[k]))

        #re-define force value
        forces = new_forces        
        #increase time
        time += dt

        #append data to lists
        time_list.append(time)

    #Post-simulation:
    #close output file
    outfile.close()
    '''
    # Plot particles separation to screen
    pyplot.title('Velocity Verlet: separation vs time')
    pyplot.xlabel('Time')
    pyplot.ylabel('separation')
    pyplot.plot(time_list, sep_list)
    pyplot.show()

    # Plot total energy to screen
    pyplot.title('Velocity Verlet: total energy vs time')
    pyplot.xlabel('Time')
    pyplot.ylabel('Energy')
    pyplot.plot(time_list, energy_list)
    pyplot.show()
    '''


# Execute main method, but only when directly invoked
if __name__ == "__main__":
    main()
