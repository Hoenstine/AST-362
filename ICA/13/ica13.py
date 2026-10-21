#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
                    Created on Sun Oct 18 10:41:40 2026
                            Gabe Hoenstine
                            Code for ICA 13
                            
                        FINAL ANSWER FOR MAGNITUDE IS -4.56


"""

import matplotlib.pyplot as plt
import numpy as np
from nice_imshow_function import implot
from nice_imshow_function import strip_SIP
from astropy.io import fits
from astropy.modeling.functional_models import Gaussian2D


fit = '/Users/jameshoenstine/Desktop/AST_362/ica13/image_ZTF-sci-20180331471019-zg-size-600.0arcsec.fits'
image = fits.getdata(fit)


height, width = image.shape[:2]

x = width / 2.0 
y = height / 2.0 



ztf_cutout = image[300-50:300+50, 300-50:300+50]

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
    
    normal = ev / np.sum(ev)
    
    
    return normal

xvals, yvals = np.meshgrid(np.arange(300-50, 300+50), np.arange(300-50, 300+50))

x_std  = 50
y_std  = 50
x_mean = x
y_mean = y


g2d = gauss2d(xvals, yvals, x_std, y_std, x_mean, y_mean)

convolve = ztf_cutout * g2d

sum_count = np.sum(convolve)


##################### step 13 #####################


blank_sky = image[500-20:500+20, 300-20:300+20]
n = 40 * 40


height_bs, width_bs = blank_sky.shape[:2]

x_bs = width_bs  / 2.0
y_bs = height_bs / 2.0


xvalsbs, yvalsbs = np.meshgrid(np.arange(500-20, 500+20), np.arange(300-20, 300+20))

x_stdbs  = 20
y_stdbs  = 20
x_meanbs = x_bs
y_meanbs = y_bs


g2dbs = gauss2d(xvalsbs, yvalsbs, x_std, y_std, x_mean, y_mean)

convolvebs = blank_sky * g2dbs

sky_count = np.median(convolvebs)

######################

net =    sum_count -  n *  sky_count

m = -2.5 * np.log10(net/30)

#################### MAGNITDUE = -4.56 #################### 


#plt.imshow(image, cmap='gray')
#plt.imshow(ztf_cutout, cmap='gray')
plt.title('Postition of Star')
plt.xlabel('Pixels')
plt.ylabel('Pixels')
#plt.contour(xvals,yvals,g2d)
#plt.plot(x, y, 'rx') #Part 3




#plt.imshow(image, cmap='gray')
#plt.contour(xvalsbs,yvalsbs,g2dbs)
