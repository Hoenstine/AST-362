#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 12:24:23 2026

@author: jameshoenstine
"""
import math

import numpy as np
from scipy.special import factorial
import matplotlib.pyplot as plt

data = np.loadtxt('/Users/jameshoenstine/Desktop/AST_362/Lab0/different_niter/n1000_t10ms/n1000_t10ms_001.dat')
mu = np.mean(data) # 0.68
std = np.std(data) # 1.82

maxx = np.max(data) # 18
minn = np.min(data) # 0

def Poisson(mu,nuu):
    return math.e **(-mu) * ((mu ** nuu)/(factorial(nuu)))

nuu = data
possion_val = [Poisson(mu,i) for i in nuu]
    
def gaussian(mu, sigma, x):
    return ( 1 / ( sigma * ( 2 * math.pi)**.5)) * np.exp(-(x - mu)**2 /( 2 * sigma**2))

x = np.linspace(np.min(data), np.max(data), 100)

smooth_poisson = Poisson(mu, x)
smooth_gaussian = gaussian(mu, std, x)

plt.hist(data, bins='auto', label='Data', density=True)
plt.plot(x, smooth_poisson, label='Poisson' )
plt.plot(x, smooth_gaussian, label='Gaussian' )
plt.legend()

