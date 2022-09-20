import numpy as np
import matplotlib.pyplot as plt
import math

class PREDOID():
    
    def __init__(self, x, y, vx, vy, width, height):
        self.position = [x, y]
        self.velocity = [vx, vy]
        self.acceleration = (np.random.rand(2) - 0.5)*10
        self.acceleration = (self.acceleration / np.linalg.norm(self.acceleration))* 10
        self.width = width
        self.height = height
        
    def show(self):
        plt.plot( self.position[0] , self.position[1], 'b*')
        
    def update(self, squad):
        
        self.squad_mind(squad)
        
        self.velocity = [self.velocity[0] + self.acceleration[0], self.velocity[1] + self.acceleration[1]]
        self.position = [self.position[0] + self.velocity[0], self.position[1] + self.velocity[1]]
        #self.acceleration = (np.random.rand(2) - 0.5)*10
        
        # world's limts
        if self.position[0] > self.width:
            self.position[0] = 0
        elif self.position[0] < 0:
            self.position[0] = self.width

        if self.position[1] > self.height:
            self.position[1] = 0
        elif self.position[1] < 0:
            self.position[1] = self.height
            
    def squad_mind(self, squad):
        # Radius of neighbourhood
        radius = 100
        local_velocity = []
        local_position = []
        
        self.acceleration = (np.random.rand(2) - 0.5)* 10
        self.acceleration = (self.acceleration / np.linalg.norm(self.acceleration))* 10
