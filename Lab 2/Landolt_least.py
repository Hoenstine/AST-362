#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 19:37:44 2026

@author: jameshoenstine
"""


import matplotlib.pyplot as plt
import numpy as np
from nice_imshow_function import implot
from nice_imshow_function import strip_SIP
from astropy.io import fits
from astropy.modeling.functional_models import Gaussian2D
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


C1 = 5.506 + 14.674287 # del 18
C2 = 3.68 + 18.79    # thuban
C3 = 8.83 +10.79  # HD 206488
C4  = 9.0974 + 8.868 # right
C5 = 8.831 + 9.22 # left
C6 = 9.0974+ 12.274# right v2
C7 = 8.831 + 9.8427 # left v2
C8 = 7.65 + 10.349 # third land

#C9 = 21.5 # Vega




c4 = .03
c5 = .027
c6 = .006
c7 = .017
c8 = .019
#c9 = .0002


#C = np.array([C1, C2, C3, C4, C5, C6, C7, C8])

C = np.array([ C4, C5, C6, C7, C8])
c = np.array([c4, c5, c6, c7, c8])

x1 = 1/np.cos(np.radians(90 - 52)) # Del 
x2 = 1/np.cos(np.radians(90 - 39)) # Thuban
x3 = 1/np.cos(np.radians(90 - 41)) # HD 206488
x4 = 1/np.cos(np.radians(90 - 42)) # right
x5 = 1/np.cos(np.radians(90 - 42)) # left
x6 = 1/np.cos(np.radians(90 - 43)) # right v2
x7 = 1/np.cos(np.radians(90 - 43)) # left v2
x8 = 1/np.cos(np.radians(90 - 52)) # third land
#x9 = 1/np.cos(np.radians(90 - 44)) # VEGA


#sec = np.array([x1, x2, x3, x4, x5, x6, x7, x8])


sec = np.array([ x4, x5, x6, x7, x8])


m = sec
mdub =  m**2
l = C
#l_err = np.array([0.1, 0.3, 0.2, 0.07, 0.7, 0.4, 0.5, 0.2])
l_err = c

#plt.plot(sec,C)

m_fit = np.linspace(np.min(sec), np.max(sec), 100)









msum = m.sum()
msumsqueared = mdub.sum()
lsum = l.sum()
lmsum = (m*l).sum()

'''
w = 1 / l_err **2
s = np.sum(w)
s_m = np.sum(w*m)
s_l = np.sum(w*l)
smm = np.sum(w*m**2)
sml = np.sum(w*m*l)
'''

N = len(m)

triangle = (N * msumsqueared - (msum)**2  )
#ntriangle = s * smm - s_m**2

A = (msumsqueared  * lsum - msum * lmsum)/triangle
B = (N * lmsum  -  msum * lsum)/ triangle

#new_A = (smm * s_l - s_m * sml)/ ntriangle
#new_B = ( s* sml - s_m * s_l) / ntriangle


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


#plt.scatter(m,l, label='Data Points')
plt.title('Landolt Least Squares')
plt.ylabel("Magnitude ")
plt.xlabel('Airmass')
#plt.scatter(C,sec)
plt.plot(m_fit, l_fit, label='fit')
plt.errorbar(m,l,yerr=l_err, fmt='o', label=' Data Points')

plt.legend()

#%%
############# EXPONENTIAL #############
'''
import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit


t = np.array([10, 20 , 30, 40 , 50 ])
tdub = np.array([100, 20**2, 30**2, 40**2, 50**2])
nu = np.array([409, 304, 260, 192, 170])
enu = np.log(nu)
N = len(nu)

t_fit = np.linspace(10, 50, 100)

tsum = t.sum()
tsumsqueared = tdub.sum()
enusum = enu.sum()
tenusum = (t*enu).sum()

triangle = (N * tsumsqueared.sum()) - (t.sum())**2  

Ae = ((tsumsqueared  * enusum - tsum * tenusum)/triangle)
Be = ((N * tenusum  -  tsum * enusum)/ triangle)
Aee = np.exp(Ae)

nu_fit =  Aee * np.exp(Be*t_fit)

nu_p = Ae + Be * t

rest = enu - nu_p

salle = np.sum(rest **2) 


un_ye = (np.sqrt( salle/( N-2) ))

un_Ae = (un_ye *  (tsumsqueared/triangle)** .5)
un_Be = (un_ye * ( N / triangle)**.5)


chie = np.sum((rest **2)/ (un_ye**2))
reduced_chie = chie / (N-2)


plt.title('Residuals')
plt.xlabel("t(minuets)")
plt.ylabel('v(counts)')
#plt.scatter(m,res)
#plt.plot(t_fit, nu_fit, label='fit')
#plt.errorbar(t,rest, yerr=un_ye, fmt='o', label=' Data Points')

plt.legend()



def func(x, A, B):
    return A * np.exp(-B * x) 



popt, pcov = curve_fit(func, t, nu,p0=(493,0.022))
er = (np.diag(pcov))**.5

t_fit = np.linspace(10, 50, 100)

perr = np.sqrt(np.diag(pcov))
chie = np.sum((rest **2)/ (un_ye**2))
reduced_chie = chie / (N-2)


plt.figure()
#plt.errorbar(t,rest, yerr=nu**.5, fmt='o', label=' Data Points')
plt.title('Residuals')
plt.xlabel("t(minuets)")
plt.ylabel('v(counts)')
#plt.plot(t_fit, func(t_fit, *popt))
plt.legend()
plt.show()

'''
