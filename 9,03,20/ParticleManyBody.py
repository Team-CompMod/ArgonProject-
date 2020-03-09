"""
CompMod Lennard Jones Project --
Describes N-body systems interacting through Lennard-Jones pair potential.

"""

import sys
import math
import numpy as np
import matplotlib.pyplot as pyplot
from Particle3D import Particle3D
import Lennard_Jones as LJ
import MDUtilities
import matplotlib.pyplot as plt
#from tqdm import tqdm


#Begin main code
def main():
    #for i in tqdm(range(1000)):
        if len(sys.argv)!=3:
            print("Wrong number of arguments.")
            print("Usage: " + sys.argv[0] + "  <parameters file> <xyz output file>")
            quit()
        else:
            params_filename = sys.argv[1]
            outfile_name = sys.argv[2]
        
    #setup simulation parameters
    
        #particle_num = input("Enter your preferred number of particles: ")
        #particle_num = int(particle_num)
        #temp = input("Enter simulation temperature (in Kelvin): ")
        #temp = float(temp)
    
    # get parameters from text file
        paramsfile = open(params_filename, "r")
        paramslines = paramsfile.readlines()
        paramsfile.close()
        
        particle_num = int(paramslines[0])
        rho = float(paramslines[1])
        temp = float(paramslines[2])
        cutoff = float(paramslines[3])
        step_num = int(paramslines[4])
        dt = float(paramslines[5])

        mass = 1.0
    #setup particles
        particles = []
        for x in range(int(particle_num)):
            particles.append(Particle3D("p%d" % x, mass))
        
        box = MDUtilities.set_initial_positions(rho, particles)
        MDUtilities.set_initial_velocities(temp, particles)
 
    #open output file
        outfile = open(outfile_name, "w")

    #write initial conditions to file
        outfile.write(str(particle_num)+  "\n")
        outfile.write("Point = 0\n")
        for particle in particles:
                outfile.write(str(particle)+ '\n')
        
    
    #get initial force and potential
        forces = LJ.LJ_force(particles, box[0], cutoff)
        potential = LJ.LJ_potential(particles, box[0], cutoff)
        kinetic = LJ.LJ_kinetic(particles)
        print(particles[0].velocity)
        print(particles[0].kinetic_energy())
        print(kinetic)
    #initalise information to data lists
        time = 0
        time_list = [time]
        potential_list = [potential]
        kinetic_list = [kinetic]

        #start the time integration loop
        for i in range(step_num):
            #update particle positions are write new positions to file
            outfile.write(str(particle_num)+  "\n")
            outfile.write("Point = " + str(i+1)+  "\n")
            for j in range(len(particles)):
                particles[j].update_position2(dt, forces[j])
                outfile.write(str(particles[j])+ '\n')
        
        # update force
            new_kinetic = LJ.LJ_kinetic(particles)
            new_forces = LJ.LJ_force(particles, box[0], cutoff)
            new_potential = LJ.LJ_potential(particles,box[0],cutoff)

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
            potential_list.append(new_potential)
            kinetic_list.append(new_kinetic)
            
    #Post-simulation:
    #close output file
        outfile.close()
        energy_list  = np.add(potential_list,kinetic_list)
        
        # create three subplots
    
        fig, axs = plt.subplots(3, 1, constrained_layout = True)
        axs[0].plot(time_list, potential_list,'-')
        axs[0].set_title('Time vs. Potential Energy')
        axs[0].set_xlabel('Time')
        axs[0].set_ylabel('Potential Energy')
        fig.suptitle('ParticleManyBody data', fontsize=16)

        # plot time and energy to second subplot
        axs[1].plot(time_list, kinetic_list, '-')
        axs[1].set_xlabel('Time')
        axs[1].set_title('Time vs. Kinetic Energy')
        axs[1].set_ylabel('Kinetic Energy')
    
        axs[2].plot(time_list, energy_list, '-')
        axs[2].set_xlabel('Time')
        axs[2].set_title('Time vs. Total Energy')
        axs[2].set_ylabel('Total Energy')
        plt.show()
 
# Execute main method, but only when directly invoked
if __name__ == "__main__":
    main()
