#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri May 17 15:16:43 2019

@author: G. Thyagarajulu 
"""
"""
Note:
1. First original surface is shifted up 5km.
2. Then surface at particular depth are created using shifted surface.
"""

import numpy as np
import pointShift as pst

#loading depth, dip, strike and thickness datasets
sum_dep = np.loadtxt('./sum_slab2_dep_02.23.18.xyz', delimiter=',')
sum_dip = np.loadtxt('./sum_slab2_dip_02.23.18.xyz', delimiter=',')
sum_str = np.loadtxt('./sum_slab2_str_02.23.18.xyz', delimiter=',')
sum_thk = np.loadtxt('./sum_slab2_thk_02.23.18.xyz', delimiter=',')

# layer thickness is negative if it is shifted down and positive if it is shifted upward direction
#layer_thk = [5, -10, -20, -30, -40, -50, -90, 'var']
layer_thk = [5, 10, 15, 20]

sum_5_up = np.zeros((len(sum_dep), 3))

for i in layer_thk:
    store_data = np.zeros((len(sum_dep), 3))
    if i == 5:
        for count, value in enumerate(sum_dep):
            shift_pt = pst.pointShift(sum_dep[count][0], sum_dep[count][1], -sum_dep[count][2], sum_dip[count][2], sum_str[count][2], i)
            store_data[count][0] = shift_pt[0]
            store_data[count][1] = shift_pt[1]
            store_data[count][2] = shift_pt[2]
        
        sum_5_up = store_data
        indices = np.argwhere(np.isnan(store_data[:,2]))  
        store_data[indices] = np.around(sum_dep[indices], 6)
        np.savetxt('./sum_5up_layer_'+str(i)+'.txt', store_data, fmt='%3.6f,%3.6f,%3.12f', delimiter=',') 
        
    elif type(i) == str:
        for count, value in enumerate(sum_dep):
            shift_pt = pst.pointShift(sum_5_up[count][0], sum_5_up[count][1], sum_5_up[count][2], sum_dip[count][2], sum_str[count][2], -sum_thk[count][2])
            store_data[count][0] = shift_pt[0]
            store_data[count][1] = shift_pt[1]
            store_data[count][2] = shift_pt[2]
            
        indices = np.argwhere(np.isnan(store_data[:,2]))  
        store_data[indices] = np.around(sum_dep[indices], 6)
        np.savetxt('./sum_5up_layer_var.txt', store_data, fmt='%3.6f,%3.6f,%3.12f', delimiter=',')    
    else:
        for count, value in enumerate(sum_dep):
            shift_pt = pst.pointShift(sum_5_up[count][0], sum_5_up[count][1], sum_5_up[count][2], sum_dip[count][2], sum_str[count][2], i)
            store_data[count][0] = shift_pt[0]
            store_data[count][1] = shift_pt[1]
            store_data[count][2] = shift_pt[2]
            
        indices = np.argwhere(np.isnan(store_data[:,2]))  
        store_data[indices] = np.around(sum_dep[indices], 6)
        np.savetxt('./sum_5up_layer_'+str(i)+'.txt', store_data, fmt='%3.6f,%3.6f,%3.12f', delimiter=',')
        
# checking with the old values to make sure everything is right
# sum_new = np.loadtxt('./sum_5up_layer_var.txt', delimiter=',')
# sum_old = np.loadtxt('../sum_slab2_bot_var.txt', delimiter=',')
# a = np.isclose(sum_new, sum_old, equal_nan='True')
# b = np.where(a[:,2] == False)
# print(b)

"""
# Create variable layer thickness without shifting 5km upwards
store_data = np.zeros((len(sum_dep), 3))
for count, value in enumerate(sum_dep):
    shift_pt = pst.pointShift(sum_dep[count][0], sum_dep[count][1], -sum_dep[count][2], sum_dip[count][2], sum_str[count][2], -sum_thk[count][2])
    store_data[count][0] = shift_pt[0]
    store_data[count][1] = shift_pt[1]
    store_data[count][2] = shift_pt[2]
        
indices = np.argwhere(np.isnan(store_data[:,2]))  
store_data[indices] = np.around(sum_dep[indices], 6)
np.savetxt('./sum_layer_var.txt', store_data, fmt='%3.6f,%3.6f,%3.12f', delimiter=',')
"""




