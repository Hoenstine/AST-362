#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  4 19:19:33 2026

@author: jameshoenstine
"""

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 12:52:59 2026

@author: jameshoenstine
"""




import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import glob
from astropy.io import fits
import OBS_Lab_Functions as obs
import lab2_helper_functions as hp
from astropy.modeling.functional_models import Gaussian2D

#first get the flat array



bias_files = sorted(glob.glob('/Users/jameshoenstine/Desktop/AST_362/lab2_data/bias/*.fit'))

bias_images = np.array([fits.getdata(file) for file in bias_files])

fixed_bias_image = [obs.fix(bias_image) for bias_image in bias_images]

mean_bias = np.mean(obs.fix(bias_images), axis=0)
median_bias = np.median(mean_bias)

diff = fixed_bias_image[5] - fixed_bias_image[3] 
diff_mean = np.mean(diff) # MEAN IS 0.0024 


flats_files = sorted(glob.glob('/Users/jameshoenstine/Desktop/AST_362/lab2_data/flat/*.fit'))

flat_reduced = flats_files[::5]

flat_images = np.array([fits.getdata(file) for file in flat_reduced])

fixed_flat_image = [obs.fix(flat_image) for flat_image in flat_images]

ar = np.array([1700, 1300, 900, 500, 250])




A = fixed_flat_image[18] # 265
B = fixed_flat_image[19] # 250
A2 = fixed_flat_image[17] # 265
B2 = fixed_flat_image[18]
A3 = fixed_flat_image[16] # 265
B3 = fixed_flat_image[17]
A4 = fixed_flat_image[15] # 265
B4 = fixed_flat_image[16]
A5 = fixed_flat_image[14] # 265
B5 = fixed_flat_image[15]



Fa = A[300-50:300+50, 300-50:300+50]
Fb = B[300-50:300+50, 300-50:300+50]
Fa2 = A2[300-50:300+50, 300-50:300+50]
Fb2 = B2[300-50:300+50, 300-50:300+50]
Fa3 = A3[300-50:300+50, 300-50:300+50]
Fb3 = B3[300-50:300+50, 300-50:300+50]
Fa4 = A4[300-50:300+50, 300-50:300+50]
Fb4 = B4[300-50:300+50, 300-50:300+50]
Fa5 = A5[300-50:300+50, 300-50:300+50]
Fb5 = B5[300-50:300+50, 300-50:300+50]

r = np.mean(Fa) / np.mean(Fb)
r2 = np.mean(Fa2) / np.mean(Fb2)
r3 = np.mean(Fa3) / np.mean(Fb3)
r4 = np.mean(Fa4) / np.mean(Fb4)
r5 = np.mean(Fa5) / np.mean(Fb5)

Br = B * r
Br2 = B2 * r2
Br3 = B3* r3
Br4 = B4* r4
Br5 = B5 * r5

D = A - Br
D2 = A2 - Br2
D3 = A3 - Br3
D4 = A4 - Br4
D5 = A5 - Br5

sub_d = D[300-50:300+50, 300-50:300+50]
sub_d2 = D2[300-50:300+50, 300-50:300+50]
sub_d3= D3[300-50:300+50, 300-50:300+50]
sub_d4 = D4[300-50:300+50, 300-50:300+50]
sub_d5= D5[300-50:300+50, 300-50:300+50]

var_D = np.var(sub_d, ddof=1)
var_D2 = np.var(sub_d2, ddof=1)
var_D3 = np.var(sub_d3, ddof=1)
var_D4 = np.var(sub_d4, ddof=1)
var_D5 = np.var(sub_d5, ddof=1)





var_A  = var_D/2**.5
var_A2 = var_D2/2**.5
var_A3 = var_D3/2**.5
var_A4 = var_D4/2**.5
var_A5 = var_D5/2**.5

me_a = np.mean(Fa)
me_a2 = np.mean(Fa2)
me_a3 = np.mean(Fa3)
me_a4 = np.mean(Fa4)
me_a5 = np.mean(Fa5)

fa_arr = np.array([me_a,me_a2, me_a3,me_a4,me_a5])
var_A_arr = np.array([var_A, var_A2,var_A3,var_A4,var_A5])
plt.plot(fa_arr, var_A_arr)
plt.title('Average illumination and Variance for flat image')
plt.xlabel('Average illumination (ADU)')
plt.ylabel('Image Variance ( ADU^2)')





############################      LEAST SQUARES    ############################ 
############################ SLOPE = 2.517 +_ 0.06 ############################



m = fa_arr
mdub =  m**2
l = var_A_arr
#l_err = np.array([0.1, 0.3, 0.2, 0.07, 0.7, 0.4, 0.5, 0.2])




m_fit = np.linspace(200, 900, 100)




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
