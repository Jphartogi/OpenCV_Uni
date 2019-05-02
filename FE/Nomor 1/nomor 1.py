# -*- coding: utf-8 -*-
"""
Created on Sat Jun 02 12:05:52 2018

@author: MSI
"""

#Use a for statement to generate 10,000 random floating point numbers where the value is between 10 and 100 (not including 100); calculate the average; print the largest integer less than or equal to the average (hint: use the math.floor() function here). You will need to use the random module and the math module for this exercise. 

import numpy as np
import matplotlib.pyplot as plt

# Set the training data (x, y) coordinates
data = np.random.uniform(0,1,1000)
# generate 1000 float number from 0-1
print(data)

count, bins, ignored = plt.hist(data, 10, normed=True)
plt.plot(bins, np.ones_like(bins), linewidth=2, color='r')
plt.show()

