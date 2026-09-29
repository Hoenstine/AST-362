#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""

@author: jameshoenstine
"""
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
        
        ra_total  = ra_total + del_ra 
        dec_total = dec_total + del_dec
        
        print(dec_total)
        return (ra_total)
        return(dec_total)
        if j == year:
            break

        
    #new_ra = (((year - 2000) * del_ra) / 3600) + ra
    
   # new_dec = (((year - 2000) * del_dec) /3600 )+ dec
    
    
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
