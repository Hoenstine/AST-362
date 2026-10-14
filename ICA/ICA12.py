#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Oct 13 15:01:11 2026

@author: jameshoenstine
"""
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit



m = np.array([200, 300, 400, 500, 600, 700, 800, 900])
mdub =  np.array([200 **2, 300**2, 400**2, 500**2, 600**2, 700**2, 800**2, 900**2])
l = np.array([5.1, 5.5, 5.9, 6.8, 7.8, 7.5, 8.6, 9.4])
l_err = np.array([0.1, 0.3, 0.2, 0.07, 0.7, 0.4, 0.5, 0.2])


m_fit = np.linspace(200, 900, 100)

#sigma_m = sigma_y = ( )
#sigma_l

w = 1 / l_err
s = np.sum(w)
s_m = np.sum(w*m)
s_l = np.sum(w*l)
smm = np.sum(w*m**2)
sml = np.sum(w*m*l)

ntriangle = s * smm - s_m**2
new_A = (smm * s_l - s_m * sml)/ ntriangle
new_B = ( s* sml - s_m * s_l) / ntriangle
uA = (smm/ntriangle) **.5
uB = (s/ntriangle) **.5


msum = m.sum()
msumsqueared = mdub.sum()
lsum = l.sum()
lmsum = (m*l).sum()
N = len(m)

triangle = (N * mdub.sum()) - (m.sum())**2  

A = ((msumsqueared  * lsum ) - (msum * lmsum))/triangle

B = ((N * lmsum ) - ( msum * lsum))/ triangle

l_fit = B*m_fit + A

l_p = A + B * m
res = l - l_p


res2 = l - new_A + new_B*m
############# A for loop would have been easier ################
y0 = A + B * m[0]
y1 = A + B * m[1]
y2 = A + B * m[2]
y3 = A + B * m[3]
y4 = A + B * m[4]
y5 = A + B * m[5]
y6 = A + B * m[6]
y7 = A + B * m[7]



s0 = (y0 - A - B*m[0])**2
s1 = (y1 - A - B*m[1])**2
s2 = (y2 - A - B*m[2])**2
s3 = (y3 - A - B*m[3])**2
s4 = (y4 - A - B*m[4])**2
s5 = (y5 - A - B*m[5])**2
s6 = (y6 - A - B*m[6])**2
s7 = (y7 - A - B*m[7])**2

sall = np.sum(res **2) 

yabx = ((l - B * m) - A)**2

su =( 1/6 - yabx.sum()) **(1/2)

un_y = np.sqrt( sall/( N-2) )

un_A = un_y *  (msumsqueared/triangle)** .5
un_B = un_y * ( N / triangle)**.5

#slope, intercept = np.polyfit(m,l, deg=1)


chi = np.sum(res **2)/ (un_y**2)

chi2 = np.sum(res2 **2)/ (un_y**2)

#plt.scatter(m,l, label='Data Points')
plt.title('Weighted Residual')
plt.ylabel("legth (cm)")
plt.xlabel('Mass(g)')
#plt.scatter(m,res)
#plt.plot(m_fit, l_fit, label='fit')
plt.errorbar(m,res, yerr=l_err, fmt='o', label=' Data Points')

plt.legend()




