#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: jameshoenstine
"""


################ PROBLEM 2 #################


import math 
import numpy as np






##### Input variables #######
hour = 14
ra_minute = 15
ra_seconds =  39.7
degree = 19
dec_minute = 10
dec_seconds =57
year = 2017.5

def precess(hour, ra_minute, ra_seconds, degree, dec_minute, dec_seconds, year):
    
    m = float(46.124)
    n = float(20.043)
    
    
    ra  = (hour + ra_minute/60 + ra_seconds/3600) * 15
    dec = degree + dec_minute/60 + dec_seconds/3600 
    
    del_dec = (n * math.cos(math.radians(ra)))/3600
    
    del_ra = (m + n * math.sin(math.radians(ra)) * math.tan(math.radians(dec))) / 3600
    j = 2000
    ra_total = ra
    dec_total = dec
    
    while year >= j:
        j = j + .5
        
        ra_total  = ra_total + del_ra/2
        dec_total = dec_total + del_dec/2
        

        if j == year:
            break

    
    ra_hours_dec = ra_total / 15
    ra_h = int(ra_hours_dec)
    ra_m_dec = (ra_hours_dec - ra_h) *60
    ra_m = int(ra_m_dec)
    ra_s = (ra_m_dec - ra_m) * 60
    
    
    dec_sign = -1 if dec_total < 0 else 1
    dec_abs = abs(dec_total)
    dec_deg = int(dec_abs) * dec_sign
    min_dec = (dec_abs - int(dec_abs)) * 60
    dec_min = int(min_dec)
    dec_sec = (min_dec - dec_min) * 60
    
    
    
    
    
    print(f"Adjusted Right Ascension: {ra_h}h {ra_m}m {ra_s:.2f}s")
    print(f"Adjusted Declination: {dec_deg} degree {dec_min} m {dec_sec:.2f} ")
 


attempt = precess(hour, ra_minute, ra_seconds, degree, dec_minute, dec_seconds, year)

print(attempt)


#%%
############### PROBLEM 3 ##############

import astropy as ap
from astropy import units as u
from astropy.coordinates import AltAz, EarthLocation, SkyCoord, get_body, get_sun
from astropy.time import Time
from astropy.visualization import quantity_support


############# ALDEBARAN ###################
aldebaran_ecliptic = SkyCoord.from_name("Aldebaran",frame = 'galactic')
aldebaran_galatic = SkyCoord.from_name("Aldebaran",frame = 'icrs')

ecliptic = SkyCoord(ra=68.98016279, dec=16.50930235, frame='icrs', unit='deg')
galactic = SkyCoord(ra=68.98016279, dec=16.50930235, frame='icrs', unit='deg')


############# ANDROMEDA ###################
m31_ast = SkyCoord.from_name('M31')
m31 = SkyCoord(10.68470833, 41.26875, unit="deg" )

missoula = EarthLocation(lat=46.8722 * u.deg, lon=-113.9940 * u.deg, height=978 * u.m)
utcoffset = -7 * u.hour  # EDT
time = Time("2026-10-1 23:00:00") - utcoffset
m31_alt_az = m31.transform_to(AltAz(obstime=time, location=missoula))


#m31_alt_az = m31.transform_to(AltAz(obstime=time, location=missoula))
#print(f"M33's Altitude = {m33altaz.alt:.2}")



print(aldebaran_ecliptic)
print(aldebaran_galatic)

print(f"M31's Altitude = {m31_alt_az.alt:.2}")
print(f"M31's Azimuth = {m31_alt_az.az:.2}")































