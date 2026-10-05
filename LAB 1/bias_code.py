# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import glob
from bias_fix import fix

import matplotlib.pyplot as plt
from astropy.io import fits
bias_files = sorted(glob.glob('/Users/jameshoenstine/Desktop/AST_362/EthanandGabe/*.fit'))

bias_images = np.array([fits.getdata(file) for file in bias_files])


def fix(bias_image):
    fixed_bias_image = bias_image / 16 + 1
    return fixed_bias_image

fixed_bias_image = [fix(bias_image) for bias_image in bias_images]

mean = np.mean(fix(bias_images), axis=0)

plt.imshow(mean)
plt.colorbar(label='Counts')
plt.title('Bias Mean Image: QHY 163M CMOS')