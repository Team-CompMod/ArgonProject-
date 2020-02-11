from Particle3D import *
import numpy

xyz_file = open('xyz_data.txt', 'w')
def extract_xyz(particle_list,xyz_file,i): # possible  i+1

    N = len(particle_list)
    outfile.write(str(N) + '\n')
    outfile.write("Points = " + str(i))
    for i in range N:
        outfile.write(particle_list[i] +'\n')
    
