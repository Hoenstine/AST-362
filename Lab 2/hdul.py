#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 22:30:19 2026

@author: jameshoenstine
"""

from astropy.io import fits

file = '/Users/jameshoenstine/Desktop/AST_362/lab2_data/flat/flat-0097.fit'

with fits.open(file) as hdul:
    h = hdul[0].header
    print(repr(h))
    
    
"""
VEGA 5
2x lan 5
3lan 5
2xlanv2 = 10
8mag = 10
Mystery star 20
Thuban .1
del = 5
"""