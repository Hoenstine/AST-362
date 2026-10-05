# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import glob

import matplotlib.pyplot as plt
from astropy.io import fits
bias_files = sorted(glob.glob('/Users/James/Desktop/AST_362/EthanandGabe/*.fit'))

bias_images = [fits.getdata(file) for file in bias_files]

def fix(bias_images):
    fixed_bias_image = bias_images / 16 + 1
    return fixed_bias_image
mean = np.mean(bias_images, axis=0)
#david = 36.49 + 36.49 + 18.24*3 + 150