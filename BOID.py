# -*- coding: utf-8 -*-

import numpy as np
import matplotlib.pyplot as plt
import math

class BOID():
    
    def __init__(self, x, y, vx, vy, width, height):
        self.position = [x, y]
        self.velocity = [vx, vy]
        self.acceleration = (np.random.rand(2) - 0.5)*10
        self.acceleration = (self.acceleration / np.linalg.norm(self.acceleration))* 10
        self.width = width
        self.height = height
        
    def show(self):
        plt.plot( self.position[0] , self.position[1], 'b*')
        
    def update(self, flock):
        
        self.flock_mind(flock)
        
        self.velocity = [self.velocity[0] + self.acceleration[0], self.velocity[1] + self.acceleration[1]]
        self.position = [self.position[0] + self.velocity[0], self.position[1] + self.velocity[1]]
        
        # world's limts
        if self.position[0] > self.width:
            self.position[0] = 0
        elif self.position[0] < 0:
            self.position[0] = self.width

        if self.position[1] > self.height:
            self.position[1] = 0
        elif self.position[1] < 0:
            self.position[1] = self.height
            
    def flock_mind(self, flock):
        # Radius of neighbourhood
        radius = 100
        local_velocity = []
        local_position = []
        
        for boid in flock:
            if math.dist(np.array(self.position) , np.array(boid.position)) < radius:
                local_velocity.append(np.array(boid.velocity))
                local_position.append(np.array(boid.position))
                     
        
        local_position = np.array(local_position)
        
        # Let's move together
        if np.size(local_velocity) > 0:
            local_velocity = np.array(local_velocity)
            local_mean_mvt = np.mean(local_velocity, 0)
            deviation = local_mean_mvt - self.velocity
            self.acceleration = self.acceleration + deviation
        else:
            self.acceleration = (np.random.rand(2) - 0.5)*10

        
        ## center of gravity
        n_radius = 50
        center_gravity = np.mean(local_position, 0)
        
        if math.dist(np.array(self.position), center_gravity) > n_radius:
            # Cohesion
            vect = center_gravity - self.position
            self.acceleration = self.acceleration + vect
        else:
            # Separation
            vect = self.position - center_gravity
            self.acceleration = self.acceleration + vect

        self.acceleration = (self.acceleration / np.linalg.norm(self.acceleration))* 10

        
        
        
        
        
        
