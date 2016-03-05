# -*- coding: utf-8 -*-
"""
Created on Sat Mar 05 21:21:06 2016

@author: fedel_000
"""

import matplotlib.pyplot as plt
import numpy as np


x = np.arange(-3, 3, 0.01)

fig = plt.figure()#figsize=(20,10))
ax = fig.add_subplot(111)
plt.ion()
j = 0
y = []
Time = 0.5

while j < 10:
    y = y + [ (np.sin(np.pi*x*j)  / (np.pi*x*j) )**2 ]
    line, = ax.plot(x, y[j], 'b')
    plt.draw()
    plt.pause(0.5)
    line.remove()
    j = j + 1

