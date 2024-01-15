# -*- coding: utf-8 -*-
"""
Created on Wed Jan 10 16:44:56 2024

@author: Santosh
"""

import numpy as np
import matplotlib.pyplot as plt
import math

vel = float(input("velocity in m/s"))
ang = float(input("angle in degree"))
# Equation of range 
u_lim = ((vel ** 2) * math.sin((2 * math.pi * ang) / 180)) /  9.8
# Equation of max height
u_lim_h = (((vel ** 2) * (math.sin((math.pi * ang) / 180) ** 2)) / (2 * 9.8))
# y = xtan(theta) + (x^2)/(2(u^2)cos^2(theta)) equation of trajectory
x_list = np.linspace(0, u_lim, 20000)
y_list = - (9.8 * ((x_list * x_list) / (2 * (vel ** 2) * (math.cos((math.pi * ang) / 180) ** 2)))) + (x_list * math.tan((math.pi * ang) / 180))
plt.figure(num=0, dpi=120)
plt.plot(x_list,y_list)
plt.show()
print("range is " + str(u_lim) + " meters")
print("max height is " + str(u_lim_h) + " meters")
    