#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu May 16 01:12:51 2019

@author: G. Thyagarajulu

Creating uw (lon, lat, r) files
"""

import numpy as np
import transform_data_coords as tds
from matplotlib import pyplot as plt

def geolonlatr2sphxyz(lonlatr):
    """
    transforms layer (lon, lat, r) in geographical coordinates to uw (lon,lat,r) and (x, y, z) coordinates
    """
    lonlatr_noNaN = lonlatr[~np.isnan(lonlatr[:,2])]
    lonlatr_noNaN[:,2] = lonlatr_noNaN[:,2]
    lonlatr_noNaN[:,0:2] = tds.geolonlat2translonlat(lonlatr_noNaN[:,0:2])
    lonlatr_Slonlatr = tds.translonlatr2sphlonlatr(lonlatr_noNaN)
#    lonlatr_Sxyz = tds.sphlonlatr2sphxyz(lonlatr_Slonlatr)
    lonlatr_Slonlatr_cut = lonlatr_Slonlatr[np.logical_and(np.logical_and(lonlatr_Slonlatr[:,0] >= -32.5, lonlatr_Slonlatr[:,0] <= 32.5), \
                    np.logical_and(lonlatr_Slonlatr[:,1] >= -43.5, lonlatr_Slonlatr[:,1] <= 43.5))]
    lonlatr_Sxyz_cut = tds.sphlonlatr2sphxyz(lonlatr_Slonlatr_cut)
    return lonlatr_Sxyz_cut

#loading layers
sum_layer_org = np.loadtxt('../sum_slab2_dep_02.23.18.xyz', delimiter=',')
sum_layer_org[:,2] = -sum_layer_org[:,2]
sum_5up_layer_5 = np.loadtxt('../sum_5up_layer_5.txt', delimiter=',')
sum_5up_layer_var = np.loadtxt('../sum_5up_layer_var.txt', delimiter=',')
sum_layer_var = np.loadtxt('../sum_layer_var.txt', delimiter=',')

sum_5up_layer_10 = np.loadtxt('../sum_5up_layer_-10.txt', delimiter=',')
sum_5up_layer_20 = np.loadtxt('../sum_5up_layer_-20.txt', delimiter=',')
sum_5up_layer_30 = np.loadtxt('../sum_5up_layer_-30.txt', delimiter=',')
sum_5up_layer_50 = np.loadtxt('../sum_5up_layer_-50.txt', delimiter=',')
sum_5up_layer_15 = np.loadtxt('../sum_5up_layer_-15.txt', delimiter=',')

"""
# check negative depth (i.e., points whose radius is more thanb 6371 km). Note: In the current uw domain range all points are positive depth
sum_5up_layer_5_noNaN = sum_5up_layer_5[~np.isnan(sum_5up_layer_5[:,2])]
a = np.where(sum_5up_layer_5_noNaN[:,2] <= 0)
plt.figure(1)
plt.scatter(sum_5up_layer_5_noNaN[:,0], sum_5up_layer_5_noNaN[:,1])
plt.scatter(sum_5up_layer_5_noNaN[a][:,0], sum_5up_layer_5_noNaN[a][:,1],c='r')
"""
# transforming coordinates and saving to txt file
sum_layer_org_sxyz = geolonlatr2sphxyz(sum_layer_org)
np.savetxt('./sum_layer_org_sxyz.txt', np.c_[sum_layer_org_sxyz], fmt='%3.12f')

sum_5up_layer_5_sxyz = geolonlatr2sphxyz(sum_5up_layer_5)
np.savetxt('./sum_5up_layer_5_sxyz.txt', np.c_[sum_5up_layer_5_sxyz], fmt='%3.12f')

sum_5up_layer_var_sxyz = geolonlatr2sphxyz(sum_5up_layer_var)
np.savetxt('./sum_5up_layer_var_sxyz.txt', np.c_[sum_5up_layer_var_sxyz], fmt='%3.12f')

sum_layer_var_sxyz = geolonlatr2sphxyz(sum_layer_var)
np.savetxt('./sum_layer_var_sxyz.txt', np.c_[sum_layer_var_sxyz], fmt='%3.12f')

sum_5up_layer_10_sxyz = geolonlatr2sphxyz(sum_5up_layer_10)
np.savetxt('./sum_5up_layer_-10_sxyz.txt', np.c_[sum_5up_layer_10_sxyz], fmt='%3.12f')

sum_5up_layer_20_sxyz = geolonlatr2sphxyz(sum_5up_layer_20)
np.savetxt('./sum_5up_layer_-20_sxyz.txt', np.c_[sum_5up_layer_20_sxyz], fmt='%3.12f')

sum_5up_layer_30_sxyz = geolonlatr2sphxyz(sum_5up_layer_30)
np.savetxt('./sum_5up_layer_-30_sxyz.txt', np.c_[sum_5up_layer_30_sxyz], fmt='%3.12f')

sum_5up_layer_50_sxyz = geolonlatr2sphxyz(sum_5up_layer_50)
np.savetxt('./sum_5up_layer_-50_sxyz.txt', np.c_[sum_5up_layer_50_sxyz], fmt='%3.12f')

sum_5up_layer_15_sxyz = geolonlatr2sphxyz(sum_5up_layer_15)
np.savetxt('./sum_5up_layer_-15_sxyz.txt', np.c_[sum_5up_layer_15_sxyz], fmt='%3.12f')



