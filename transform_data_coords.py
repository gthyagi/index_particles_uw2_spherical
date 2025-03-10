#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 11 13:43:56 2019

@author: G Thyagarajulu
"""

import numpy as np
import math

# Geographical max, min values of lon & lat in the region
lon_max = 122.0
lon_min = 57.0
lat_max = 35.0
lat_min = -52.0
# lon_max = 122.0
# lon_min = 87.0
# lat_max = 20.0
# lat_min = -15.0
diff_lon = lon_max - lon_min
diff_lat = lat_max - lat_min
# print ("Difference b/w max and min lon: ", diff_lon)
# print ("Difference b/w max and min lat: ", diff_lat)

# Converting lon range to [0,360], lat range to [0, 180]
if lon_min <= 0:
    trans_lon_min = 360 + lon_min
else:
    trans_lon_min = lon_min
if lon_max <= 0:
    trans_lon_max = 360 + lon_max
else:
    trans_lon_max = lon_max
    
if lat_min < 0:
    trans_lat_min = 90 - lat_min
else:
    trans_lat_min = 90 - lat_min
if lat_max < 0:
    trans_lat_max = 90 - lat_max
else:
    trans_lat_max = 90 - lat_max
    
# print ("Min of trans lon: ", trans_lon_min, " & Min of geo lon: ", lon_min)
# print ("Max of trans lon: ", trans_lon_max, " & Max of geo lon: ", lon_max)
# print ("Min of trans lat: ", trans_lat_max, " & Min of geo lat: ", lat_max)
# print ("Max of trans lat: ", trans_lat_min, " & Max of geo lat: ", lat_min)

def sphxyz2sphlonlatr(xyz):
    """
    Function to convert (x,y,z) pts in spherical region to (lon, lat, radius) values in spherical region.
    input data format = (x, y, z)
    output data format = (lon, lat, radius)
    """
    ptsnew = np.zeros((len(xyz[:,0]),3))
    x_tanlon = xyz[:,0]/xyz[:,2]
    y_tanlat = xyz[:,1]/xyz[:,2]
    factor = np.sqrt(x_tanlon**2 + y_tanlat**2 + 1)
    ptsnew[:,2] = xyz[:,2] * factor
    ptsnew[:,1] = np.arctan(y_tanlat) * (180/math.pi)
    ptsnew[:,0] = np.arctan(x_tanlon) * (180/math.pi)
    return ptsnew


def sphlonlatr2sphxyz(data):
    """
    Converts (lon, lat, radius) in spherical region to (x, y, z) in spherical region.
    input data format = (lon, lat, radius)
    output data format = (x, y, z)
    """
    newcoords = np.zeros((len(data[:,0]),3))
    (x,y) = (np.tan(data[:,0]*np.pi/180.0), np.tan(data[:,1]*np.pi/180.0))
    d = data[:,2] / np.sqrt( x**2 + y**2 + 1)
    newcoords[:,0] = d*x
    newcoords[:,1] = d*y
    newcoords[:,2] = d
    return newcoords


def geolonlat2translonlat(phitheta):
    """
    Converts geographical longitude range to [0,360], geographical latitude range to [0, 180]
    """
    lonlat = np.array(phitheta, dtype='float')
    indices1 = np.argwhere(phitheta[:,0] <= 0)
    lonlat[:,0][indices1] = phitheta[:,0][indices1] + 360
    indices2 = np.argwhere(np.logical_and(phitheta[:,1] >= 0, phitheta[:,1] <= 90))
    lonlat[:,1][indices2] = 90 - phitheta[:,1][indices2]
    indices3 = np.argwhere(phitheta[:,1] < 0 )
    lonlat[:,1][indices3] = 90 - phitheta[:,1][indices3]
    return lonlat

def translonlatr2sphlonlatr(lonlatrad):
    """
    Converts transformed (lon, lat, rad) into spherical domain (lon, lat, rad)
    Transformation is performed using spherical domain max, min values of lon, lat
    """
    mid_lon = (trans_lon_max + trans_lon_min)/2
    mid_lat = (trans_lat_max + trans_lat_min)/2
    newcoords = np.zeros((len(lonlatrad[:,0]),3))
    newcoords[:,0] = lonlatrad[:,0] - mid_lon
    newcoords[:,1] = mid_lat - lonlatrad[:,1]
    newcoords[:,2] = (6371.0 - lonlatrad[:,2])/6371.0
    return newcoords

def sphlonlatr2translonlatr(lonlatrad):
    """
    Converts spherical domain (lon, lat, rad) into transformed (lon, lat, rad)
    Transformation is performed using spherical domain max, min values of lon, lat
    """
    mid_lon = (trans_lon_max + trans_lon_min)/2
    mid_lat = (trans_lat_max + trans_lat_min)/2
    newcoords = np.zeros((len(lonlatrad[:,0]),3))
    newcoords[:,0] = lonlatrad[:,0] + mid_lon
    newcoords[:,1] = mid_lat - lonlatrad[:,1]
    newcoords[:,2] = (1.0 - lonlatrad[:,2])*6371.0
    return newcoords

def translonlat2geolonlat(phitheta):
    """
    Converts transformed longitude range to [-180,180], transformed latitude range to [-90, 90]
    """
    lonlat = np.array(phitheta, dtype='float')
    
    indices1 = np.argwhere(phitheta[:,0] >= 180)
    lonlat[:,0][indices1] = phitheta[:,0][indices1] - 360
    indices2 = np.argwhere(np.logical_and(phitheta[:,1] >= 0, phitheta[:,1] <= 90))
    lonlat[:,1][indices2] = 90 - phitheta[:,1][indices2]
    indices3 = np.argwhere(phitheta[:,1] > 90 )
    lonlat[:,1][indices3] = 90 - phitheta[:,1][indices3]
    return lonlat

class transform_coords(object):
	"""
	Transform coordinates in geo lon, lat, r to uw xyz and vice versa
	"""
	def __init__(self, lon_min, lon_max, lat_min, lat_max):
		"""
		Min and Max lon, lat of the model domain
		"""
		self.lon_min = lon_min
		self.lon_max = lon_max
		self.lat_min = lat_min
		self.lat_max = lat_max
		self.diff_lon = self.lon_max - self.lon_min
		self.diff_lat = self.lat_max - self.lat_min
		
		# Converting lon range to [0,360], lat range to [0, 180]
		if self.lon_min <= 0:
			self.trans_lon_min = 360 + self.lon_min
		else:
		    self.trans_lon_min = self.lon_min
		if self.lon_max <= 0:
		    self.trans_lon_max = 360 + self.lon_max
		else:
		    self.trans_lon_max = self.lon_max
		    
		if self.lat_min < 0:
		    self.trans_lat_max = 90 - self.lat_min
		else:
		    self.trans_lat_max = 90 - self.lat_min
		if self.lat_max < 0:
		    self.trans_lat_min = 90 - self.lat_max
		else:
		    self.trans_lat_min = 90 - self.lat_max

		# Mid point of the model
		self.mid_lon = (self.trans_lon_max + self.trans_lon_min)/2
		self.mid_lat = (self.trans_lat_max + self.trans_lat_min)/2

	def model_size_info(self):
		print ("Min of trans lon: ", self.trans_lon_min, " & Min of geo lon: ", self.lon_min)
		print ("Max of trans lon: ", self.trans_lon_max, " & Max of geo lon: ", self.lon_max)
		print ("Min of trans lat: ", self.trans_lat_min, " & Max of geo lat: ", self.lat_max)
		print ("Max of trans lat: ", self.trans_lat_max, " & Min of geo lat: ", self.lat_min)
		print ("Difference b/w max and min lon: ", self.diff_lon)
		print ("Difference b/w max and min lat: ", self.diff_lat)

	def geo_lonlatr2uw_xyz(self, geo_lonlatr_data):
		"""
		Step1: Converts geographical longitude range to [0,360], geographical latitude range to [0, 180]. \n
		Step2: Converts transformed (lon, lat, rad) into uw spherical domain (lon, lat, rad). \n
		Step3: Converts (lon, lat, radius) in uw spherical coordinates to (x, y, z) in uw cartesian coordinates. \n
		Transformation is performed using spherical domain max, min values of lon, lat
		"""
		# step1
		phi_theta_r = np.copy(geo_lonlatr_data)
		indices1 = np.argwhere(geo_lonlatr_data[:, 0] <= 0)
		phi_theta_r[:, 0][indices1] = geo_lonlatr_data[:, 0][indices1] + 360
		indices2 = np.argwhere(np.logical_and(geo_lonlatr_data[:, 1] >= 0, geo_lonlatr_data[:, 1] <= 90))
		phi_theta_r[:, 1][indices2] = 90 - geo_lonlatr_data[:, 1][indices2]
		indices3 = np.argwhere(geo_lonlatr_data[:, 1] < 0)
		phi_theta_r[:, 1][indices3] = 90 - geo_lonlatr_data[:, 1][indices3]

		# step2
		uw_lonlatr = np.zeros((len(geo_lonlatr_data[:, 0]), 3))
		uw_lonlatr[:, 0] = phi_theta_r[:, 0] - self.mid_lon
		uw_lonlatr[:, 1] = self.mid_lat - phi_theta_r[:, 1]
		uw_lonlatr[:, 2] = (6371.0 - phi_theta_r[:, 2]) / 6371.0

		# step3
		uw_xyz = np.zeros((len(uw_lonlatr[:, 0]), 3))
		(x, y) = (np.tan(uw_lonlatr[:, 0] * np.pi / 180.0), np.tan(uw_lonlatr[:, 1] * np.pi / 180.0))
		d = uw_lonlatr[:, 2] / np.sqrt(x ** 2 + y ** 2 + 1)
		uw_xyz[:, 0] = d * x
		uw_xyz[:, 1] = d * y
		uw_xyz[:, 2] = d
		return uw_xyz

	def uw_xyz2geo_lonlatr(self, uw_xyz_data):
		"""
		Step1: Converts (x,y,z) uw cartesian system to (lon, lat, radius) spherical system. \n
		Step2: Converts spherical domain (lon, lat, rad) into transformed (lon, lat, rad).
		       Transformation is performed using spherical domain max, min values of lon, lat \n
		Step3: Converts transformed longitude range to [-180,180], transformed latitude range to [-90, 90]
		"""
		# step1
		uw_lonlatr = np.zeros((len(uw_xyz_data[:, 0]), 3))
		x_tanlon = uw_xyz_data[:, 0] / uw_xyz_data[:, 2]
		y_tanlat = uw_xyz_data[:, 1] / uw_xyz_data[:, 2]
		factor = np.sqrt(x_tanlon ** 2 + y_tanlat ** 2 + 1)
		uw_lonlatr[:, 2] = uw_xyz_data[:, 2] * factor
		uw_lonlatr[:, 1] = np.arctan(y_tanlat) * (180 / math.pi)
		uw_lonlatr[:, 0] = np.arctan(x_tanlon) * (180 / math.pi)

		# step2
		phi_theta_r = np.zeros((len(uw_lonlatr[:, 0]), 3))
		phi_theta_r[:, 0] = uw_lonlatr[:, 0] + self.mid_lon
		phi_theta_r[:, 1] = self.mid_lat - uw_lonlatr[:, 1]
		phi_theta_r[:, 2] = (1.0 - uw_lonlatr[:, 2]) * 6371.0

		# step3
		geo_lonlatr = np.copy(phi_theta_r)
		indices1 = np.argwhere(phi_theta_r[:, 0] >= 180)
		geo_lonlatr[:, 0][indices1] = phi_theta_r[:, 0][indices1] - 360
		indices2 = np.argwhere(np.logical_and(phi_theta_r[:, 1] >= 0, phi_theta_r[:, 1] <= 90))
		geo_lonlatr[:, 1][indices2] = 90 - phi_theta_r[:, 1][indices2]
		indices3 = np.argwhere(phi_theta_r[:, 1] > 90)
		geo_lonlatr[:, 1][indices3] = 90 - phi_theta_r[:, 1][indices3]
		return geo_lonlatr
		
	def sphxyz2sphlonlatr(self, xyz):
		"""
		Function to convert (x,y,z) pts in spherical region to (lon, lat, radius) values in spherical region.
		input data format = (x, y, z)
		output data format = (lon, lat, radius)
		"""
		ptsnew = np.zeros((len(xyz[:,0]),3))
		x_tanlon = xyz[:,0]/xyz[:,2]
		y_tanlat = xyz[:,1]/xyz[:,2]
		factor = np.sqrt(x_tanlon**2 + y_tanlat**2 + 1)
		ptsnew[:,2] = xyz[:,2] * factor
		ptsnew[:,1] = np.arctan(y_tanlat) * (180/math.pi)
		ptsnew[:,0] = np.arctan(x_tanlon) * (180/math.pi)
		return ptsnew

	def sphlonlatr2translonlatr(self, lonlatrad):
		"""
		Converts spherical domain (lon, lat, rad) into transformed (lon, lat, rad)
		Transformation is performed using spherical domain max, min values of lon, lat
		"""
		mid_lon = (trans_lon_max + trans_lon_min)/2
		mid_lat = (trans_lat_max + trans_lat_min)/2
		newcoords = np.zeros((len(lonlatrad[:,0]),3))
		newcoords[:,0] = lonlatrad[:,0] + mid_lon
		newcoords[:,1] = mid_lat - lonlatrad[:,1]
		newcoords[:,2] = (1.0 - lonlatrad[:,2])*6371.0
		return newcoords

	def translonlat2geolonlat(self, phithetar):
		"""
		Converts transformed longitude range to [-180,180], transformed latitude range to [-90, 90]
		"""
		lonlatr = np.copy(phithetar)
		indices1 = np.argwhere(phithetar[:,0] >= 180)
		lonlatr[:,0][indices1] = phithetar[:,0][indices1] - 360
		indices2 = np.argwhere(np.logical_and(phithetar[:,1] >= 0, phithetar[:,1] <= 90))
		lonlatr[:,1][indices2] = 90 - phithetar[:,1][indices2]
		indices3 = np.argwhere(phithetar[:,1] > 90 )
		lonlatr[:,1][indices3] = 90 - phithetar[:,1][indices3]
		return lonlatr

	def geolonlat2translonlat(self, phithetar):
		"""
		Converts geographical longitude range to [0,360], geographical latitude range to [0, 180]
		"""
		lonlatr = np.copy(phithetar)
		indices1 = np.argwhere(phithetar[:,0] <= 0)
		lonlatr[:,0][indices1] = phithetar[:,0][indices1] + 360
		indices2 = np.argwhere(np.logical_and(phithetar[:,1] >= 0, phithetar[:,1] <= 90))
		lonlatr[:,1][indices2] = 90 - phithetar[:,1][indices2]
		indices3 = np.argwhere(phithetar[:,1] < 0 )
		lonlatr[:,1][indices3] = 90 - phithetar[:,1][indices3]
		return lonlatr

	def translonlatr2sphlonlatr(self, lonlatrad):
		"""
		Converts transformed (lon, lat, rad) into spherical domain (lon, lat, rad)
		Transformation is performed using spherical domain max, min values of lon, lat
		"""
		mid_lon = (trans_lon_max + trans_lon_min)/2
		mid_lat = (trans_lat_max + trans_lat_min)/2
		newcoords = np.zeros((len(lonlatrad[:,0]),3))
		newcoords[:,0] = lonlatrad[:,0] - mid_lon
		newcoords[:,1] = mid_lat - lonlatrad[:,1]
		newcoords[:,2] = (6371.0 - lonlatrad[:,2])/6371.0
		return newcoords

	def sphlonlatr2sphxyz(self, data):
		"""
		Converts (lon, lat, radius) in spherical region to (x, y, z) in spherical region.
		input data format = (lon, lat, radius)
		output data format = (x, y, z)
		"""
		newcoords = np.zeros((len(data[:,0]),3))
		(x,y) = (np.tan(data[:,0]*np.pi/180.0), np.tan(data[:,1]*np.pi/180.0))
		d = data[:,2] / np.sqrt( x**2 + y**2 + 1)
		newcoords[:,0] = d*x
		newcoords[:,1] = d*y
		newcoords[:,2] = d
		return newcoords

	

	




