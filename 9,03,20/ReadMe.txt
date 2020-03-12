Computer Modelling Semester 2 Project Source Code

Phoebe O'Carroll-Moran - s1624742
Callum Moore - s1722906

This code can be used to simulate  N-body systems of particles interacting under a number of user-defined conditions. This file contains:
    - Lennard_Jones.py - contains function for finding force, potential and kinetic energy in an N-body system.
    - ParticleManyBody.py - our main function. 
    - observables.py - contains function for applying periodic bundary conditions and minimum image convention and for finding mean squared distance and radial distribution.
    - Particle3D.py - contains class that creates our particles
    - input parameter text files.

The command line takes the following arguments
- Input parameters text file
- trajectory data file traj.xyz

Input text files are formatted as follows:

Number of particles
Density
Temperature 
Cutoff distance
Step number 
Timestep 
Number of histogram bins

Users will need to convert regular units to reduced units. 

- Density: To convert from density (m^3), multiply by 5.95E-4.
- Temperature: to convert from Kelvin to reduced units, divide through by 119.8.
- Cutoff distance: convert from standard units of distance to reduced units, divide by 3.405E-10.
- Timestep: to convert from seconds to reduced units, multiply by 1.103E-5.

We hope you enjoy reading this as much as we did coding it!
