#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 29 19:32:54 2026

@author: jameshoenstine

"""
from astropy.io import fits


def load_fits(filename, ext=0):
    '''
    

    Parameters
    ----------
    filename : str
        The file you wish to open.
    ext : int
        Extension parameter to specifie Header Data Unit

    Returns
    -------
    data : numpy.ndarray
        Multi-dimensional data array
    header : astropy.io.fits.Header
        Metadata of the selected file.

    '''
    data, header = fits.getdata(filename, ext=ext, header=True)
    
    
    return data, header

def fix(bias_image):
    fixed_bias_image = bias_image / 16 + 1
    return fixed_bias_image

def gauss2d(x, y, x_std, y_std, x_mean, y_mean, window, inner_rad):
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


def phot(data, centriod_x, centriod_y, sigma_x, sigma_y, window, inner_rad):
    '''
    
    

    Parameters
    ----------
    data : int
        values
    centriod_x : int
        x middle
    centriod_y : int
        y middle.
    sigma_x : int
        devation in x
    sigma_y : int
        Devation in y.
    window : array
        aperature
    inner_rad : int
        inner radius

    Returns
    -------



    '''

    return model, psf_convole, psf_flux

def least(m,l,l_err):
    
    msum = m.sum()
    msumsqueared = mdub.sum()
    lsum = l.sum()
    lmsum = (m*l).sum()


    N = len(m)
    
    triangle = (N * msumsqueared - (msum)**2  )

    A = (msumsqueared  * lsum - msum * lmsum)/triangle
    B = (N * lmsum  -  msum * lsum)/ triangle



    l_fit = B*m_fit + A
    #l_fit2 = new_B*m_fit + new_A

    #l_p2 = new_A + new_B*m
    l_p = A + B * m

    res = l - l_p
    #res2 = l - l_p2


    sall = np.sum(res **2) 


    un_y = np.sqrt( sall/( N-2) )

    un_A = un_y *  (msumsqueared/triangle)** .5
    un_B = un_y * ( N / triangle)**.5
    
    #uA = (smm/ntriangle) **.5
    #uB = (s/ntriangle) **.5


    chi = np.sum((res **2)/ (un_y**2))
    reduced_chi = chi / (N-2)

    #chi2 = np.sum((res2 **2)/ (un_y**2))
    #reduced_chi2 = chi2 / (N-2)
    return A
    return B    