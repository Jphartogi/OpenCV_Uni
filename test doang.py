# -*- coding: utf-8 -*-
"""
Created on Thu Feb 15 21:02:10 2018

@author: MSI
"""

import matplotlib.pyplot as plt

line_up, = plt.plot([1,2,3], label='Line 2')
line_down, = plt.plot([3,2,1], label='Line 1')
plt.legend(handles=[line_up, line_down])
