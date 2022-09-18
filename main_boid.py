# -*- coding: utf-8 -*-

import os
import sys
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation
from BOID import BOID
import math

width = 1000
height = 1000
nb_boids = 50

flock = []
for n in range(0, nb_boids):
    flock.append(BOID(np.random.randint(width), np.random.randint(height), 0, 0, width, height))


fig_test = plt.figure()
plt.xlim(0, width)
plt.ylim(0, height)
points, = plt.plot([], [], 'bo')

def Boids_animation(frame):
    x_data = []
    y_data = []
    for n in range(0, np.size(flock)):
        flock[n].update(flock)
        x_data.append(flock[n].position[0])
        y_data.append(flock[n].position[1])
    points.set_data(x_data, y_data)
    return points,
    
anim = animation.FuncAnimation(fig_test, Boids_animation)

plt.show()
