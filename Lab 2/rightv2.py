#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 22:25:06 2026

@author: jameshoenstine
"""


import matplotlib.pyplot as plt
import numpy as np
from nice_imshow_function import implot
from nice_imshow_function import strip_SIP
from astropy.io import fits
from astropy.modeling.functional_models import Gaussian2D

fit = '/Users/jameshoenstine/Desktop/AST_362/lab2_data/lan2_again/94lan2x-fix.fit'


image = fits.getdata(fit)


height, width = image.shape[:2]

y = 2235
x = 3790

#plt.imshow(image, cmap='gray')

box = 20
ztf_cutout = image[ y - box: y + box, x - box: x + box ]

#plt.imshow(ztf_cutout, cmap='gray')

# 10000 pixels in the aperture

###################### SAVED THIS FUNCTION FOR FUTURE USE ###################### 
def gauss2d(x, y, x_std, y_std, x_mean, y_mean):
    '''
    

    Parameters
    ----------
    x : int
        X value of centriod
    y : int
        Y value of centriod
    x_std : int
        Standard devation in x
    y_std : int
        Standard devation in x
    x_mean : int
        Mean x value 
    y_mean : int
        Mean y value

    Returns
    -------
    normal :
        Normalized 2D Gaussian

    '''
    
    g2d = Gaussian2D(amplitude=1, x_mean=x_mean, y_mean=y_mean,x_stddev=x_std, y_stddev=y_std)
   
    ev = g2d(x,y)
    
    #normal = ev / np.sum(ev)
    
    
    return ev

xvals, yvals = np.meshgrid(np.arange(x - box, x + box), np.arange(y - box, y + box))

x_std  = 3
y_std  = 3
x_mean = x
y_mean = y


g2d = gauss2d(xvals, yvals, x_std, y_std, x_mean, y_mean)

convolve = ztf_cutout

sum_count = np.sum(convolve)


##################### step 13 #####################

x_bs = 300
y_bs = 300
bs_box = 20


blank_sky = image[y_bs - bs_box : y_bs + bs_box, x_bs - bs_box : x_bs + bs_box]
n = np.sum(g2d)


height_bs, width_bs = blank_sky.shape[:2]

plt.imshow(blank_sky, cmap='gray')

xvalsbs, yvalsbs = np.meshgrid(
    np.arange(x_bs - bs_box, x_bs + bs_box),
    np.arange(y_bs - bs_box , y_bs + bs_box))

x_stdbs  = 3
y_stdbs  = 3
x_meanbs = x_bs
y_meanbs = y_bs


g2dbs = gauss2d(
    xvalsbs, yvalsbs, x_stdbs, y_stdbs, x_meanbs, y_meanbs)

convolvebs = blank_sky * g2dbs

sky_count = np.median(convolvebs)



net = sum_count -  n *  sky_count

m = -2.5 * np.log10(net/10)
Nr = 2.132599
g = 2.517

SNR = net / ( g * net + n * g * sky_count + n * Nr**2)**(1/2)




dm = 6.588 * 1/SNR














