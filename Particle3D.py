"""
CompMod Ex2: Particle3D, a class to describe a particle in 3D space

Callum Moore s1722906
"""
import numpy as np
 
class Particle3D(object):
    """
    Class to describe particles in 3D space

    Properties:
    label(str) - label of particle
    mass(float) - mass of particle
    position(array) - postion of particle in 3D space
    Velocity(array) - velocity in x, y and z directions

    Methods:
    *formatted output
    *kinetic energy
    *velocity update
    *first and second order position update
    """

    def __init__(self, lab, mass):
        """
        Initialise a Particle3D instance
        
        :param label: label as string
        :param mass: mass as float
        """
        self.label = lab
        self.mass = mass


    def __str__(self):
        """
        Define output format
        for particle p=(p1, [1.0, 2.0, 3.0], [velocity], mass) this will print
        "label = p1, x = 1.0, y = 2.0, z = 3.0"
        """
        return  self.label + " " + str(self.position[0]) + " " + str(self.position[1]) + " " + str(self.position[2])


    def kinetic_energy(self):
        """
        Return kinetic energy as
        1/2*mass*vel^2
        """
        print(self.mass)
        print(np.inner(self.velocity,self.velocity))
        return 0.5*self.mass*np.inner(self.velocity,self.velocity)


    def leap_velocity(self,dt, force):
        """
        First-order velocity update,
        v(t+dt) = v(t) + dt*F(t)

        :param dt: timestep as float
        :param force: force on particle as numpy array
        """
        self.velocity += dt*force/self.mass


    def leap_pos1st(self, dt):
        """
        First-order position update,
        x(t+dt) = x(t) + dt*v(t)

        :param dt: timestep as float
        """
        self.position += dt*self.velocity

        
    def leap_pos2nd(self, dt, force):
        """
        Second-order position update,
        x(t+dt) = x(t) + dt*v(t) + 1/2*dt^2*F(t)

        :param dt: timestep as float
        :param force: current force as numpy array
        """
        self.position += dt*self.velocity + 0.5*dt**2*force/self.mass
        
    

    @staticmethod
    def from_file(filename):
        """
        Creates particle from file
        
        :param filename: file name as string
        """
        
        file = open(filename, "r")
        
        lines = file.readlines()
        file.close()
        pos = np.array([float(lines[1]), float(lines[2]), float(lines[3])])
        vel = np.array([float(lines[4]), float(lines[5]), float(lines[6])])
        
        return Particle3D(lines[0], pos, vel, float(lines[7]))

    @staticmethod
    def separation(p1, p2):
        """
        Finds vector separtion between two vectors p1 and p2
        
        :param p1: 1st particle
        :param p2: 2nd particle 
        """
        return p1.position - p2.position
