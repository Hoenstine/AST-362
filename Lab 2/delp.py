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


fit = '/Users/jameshoenstine/Desktop/AST_362/lab2_data/del/18del-fix.fit'

image = fits.getdata(fit)


height, width = image.shape[:2]

x = 1597
y = 2478


box = 20
ztf_cutout = image[ y - box: y + box, x - box: x + box ]

# 10000 pixels in the aperture
plt.imshow(ztf_cutout, cmap='gray')

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

convolve = ztf_cutout * g2d

sum_count = np.sum(convolve)


##################### step 13 #####################

x_bs = 1000
y_bs = 1000
bs_box = 20


blank_sky = image[y_bs - bs_box : y_bs + bs_box, x_bs - bs_box : x_bs + bs_box]
n = np.sum(g2d)


height_bs, width_bs = blank_sky.shape[:2]



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

m = -2.5 * np.log10(net/5)
Nr = 2.132599
g = 2.517

SNR = net / ( g * net + n * g * sky_count + n * Nr**2)**(1/2)

dm = 6.616 * 1/SNR

#################### MAGNITDUE = -4.56 #################### 


#plt.imshow(image, cmap='gray')

#plt.imshow(ztf_cutout, cmap='gray', origin='lower', extent=[3300-50,3300+50, 800-50,800+50])
#plt.imshow(blank_sky, cmap='gray', origin='lower', extent=[500-20,500+20, 300-20,300+20])
plt.title('2D Gaussian Overlay of Blank Sky')
plt.xlabel('Pixels')
plt.ylabel('Pixels')
#plt.contour(xvals, yvals, g2d)
#plt.plot(x, y, 'rx') #Part 3


1
#plt.imshow(blank_sky_sky, cmap='gray')
#plt.imshow(image, cmap='gray')
#plt.contour(xvalsbs,yvalsbs,g2dbs)
