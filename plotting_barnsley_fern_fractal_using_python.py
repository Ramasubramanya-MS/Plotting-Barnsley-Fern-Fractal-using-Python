# -*- coding: utf-8 -*-
"""Plotting-Barnsley-Fern-Fractal-using-Python.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XV0c8LquyXMJqyVSoVGBOQw3-Cq8Psu0
"""

#last edit : 31-10-2021

import numpy as np
import matplotlib.pyplot as plt

def function1(x,y):
  return (0.0, 0.16*y)
def function2(x,y):
  return (0.85*x + 0.04*y, -0.04*x + 0.85*y + 1.6)
def function3(x,y):
  return (0.2*x - 0.26*y, 0.23*x + 0.22*y + 1.6)
def function4(x,y):
  return (-0.15*x + 0.28*y, 0.26*x + 0.24*y + 0.44)

functions = [function1,function2,function3,function4] #list of functions

points = 100000
x,y = 0,0
x_list = []
y_list = []
for i in range(points):
  function = np.random.choice(functions, p=[0.01, 0.85, 0.07, 0.07])
  x,y = function(x,y)
  x_list.append(x)
  y_list.append(y)

plt.scatter(x_list, y_list, color = 'green')

plt.scatter(x_list, y_list, s =0.2, color = 'green')

#Method used by Christian Hill - using numpy arrays and output as an image

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm #color map

width, height = 300,300
fern_image = np.zeros((width,height))
x,y = 0, 0
for i in range(points):
  function = np.random.choice(functions, p=[0.01, 0.85, 0.07, 0.07])
  x, y = function(x,y)
  ix, iy = int(width / 2 + x*width / 10), int(y*height / 12)
  fern_image[iy,ix] = 1
plt.imshow(fern_image[::-1,:], cmap=cm.Greens)
plt.show()

