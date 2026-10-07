# -*- coding: utf-8 -*-
"""
                       Gabe Hoenstine
                         10-5-26
This is the calculations and anaylis done on LAB 1 CALABRATIONS
                  The Plots are qouted out
      Values to be found in Variable Explorer as well
"""



import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import glob
from astropy.io import fits

############### BIAS ############### 


bias_files = sorted(glob.glob('/Users/jameshoenstine/Desktop/AST_362/EthanandGabe/*.fit'))

bias_images = np.array([fits.getdata(file) for file in bias_files])


def fix(bias_image):
    fixed_bias_image = bias_image / 16 + 1
    return fixed_bias_image

fixed_bias_image = [fix(bias_image) for bias_image in bias_images]



mean_bias = np.mean(fix(bias_images), axis=0) 

median_bias = np.median(mean_bias)# 153.5

std_bias = np.std(mean_bias) # .95

sigma_3max = median_bias + std_bias *3
sigma_3min = median_bias - std_bias *3

#val = (mean_bias >= sigma_3min) &  (mean_bias <= sigma_3max)
#excluded = val.size - val.sum() # 344814

diff = fixed_bias_image[5] - fixed_bias_image[3] 
diff_mean = np.mean(diff) # MEAN IS 0.0024 


read_noise = np.std(diff)/ (2**.5) # 2.13

'''
plt.hist(diff[1700:1900,2200:2400])
plt.title('Differnece image histogram')
plt.xlabel("Pixel value")
plt.ylabel('Number of pixels')
'''

'''

plt.imshow(mean_bias,origin='lower', cmap="spring")
#plt.imshow(median_bias)
plt.colorbar(label='Counts')
plt.title('Bias Mean Image: QHY 163M CMOS')
'''
#%%

############### DARK ############### 

dark_files = sorted(glob.glob('/Users/jameshoenstine/Desktop/AST_362/darks/30/*.fit'))# Switch between 10 and 30 exposure 

dark_images = np.array([fits.getdata(file) for file in dark_files])


def fix(dark_image):
    fixed_dark_image = dark_image / 16 + 1
    return fixed_dark_image


fixed_dark_image = [fix(dark_image) for dark_image in dark_images]

mean_dark = np.mean(fixed_dark_image, axis=0)
median_dark = np.median(fixed_dark_image, axis=0)


'''
plt.imshow(mean_dark)
plt.subplot()
plt.imshow(median_dark)
plt.colorbar(label='Counts')
plt.title('Darks Mean Image 30: QHY 163M CMOS')
'''

#%%f


############### FLATS ############### 


flats_files = sorted(glob.glob('/Users/jameshoenstine/Desktop/AST_362/flats/*.fit'))

flat_reduced = flats_files[::5]

flat_images = np.array([fits.getdata(file) for file in flat_reduced])

fixed_flat_image = [fix(flat_image) for flat_image in flat_images]


median_flat = np.median(fixed_flat_image, axis=0)

normalized_flat = (flat_images - mean_bias) / median_flat


flat = np.median(normalized_flat , axis=0)


'''
plt.imshow(flat, origin='lower')
plt.title('Median Normalized Flat')
plt.colorbar(label='Counts')
'''



#%%


########### DIFFERNECE IMAGE BIAS ##################

diff = fixed_bias_image[5] - fixed_bias_image[3] 

diff_mean = np.mean(diff) # MEAN IS 0.0024 
#plt.hist(diff)


######### SCIENCE IMAGE ##########


dubhe = '/Users/jameshoenstine/Desktop/AST_362/observations/dubhe_10sec_-0005.fit'
arctus = '/Users/jameshoenstine/Desktop/AST_362/observations/arcturus_10sec_-0008.fit'
sadalsuud = '/Users/jameshoenstine/Desktop/AST_362/observations/sadalsuud_30sec_-0001.fit'


dubhe_value = fits.getdata(dubhe)
arctus_value = fits.getdata(arctus)
sadalsuud_value = fits.getdata(sadalsuud)


fixed_dubhe_value = [fix(dubhe) for dubhe in dubhe_value]
fixed_arctus_value = [fix(arctus) for arctus in arctus_value]
fixed_sadalsuud_value = [fix(sadalsuud) for sadalsuud in sadalsuud_value]


correct_dubhe = (fixed_dubhe_value - mean_dark - mean_bias) / normalized_flat 
correct_arctus = (fixed_arctus_value - mean_dark - mean_bias) / normalized_flat 
correct_sadalsuud = (fixed_sadalsuud_value - mean_dark - mean_bias) / normalized_flat 


dub = np.median(correct_dubhe , axis=0)
arc = np.median(correct_arctus , axis=0)
sad = np.median(correct_sadalsuud , axis=0)

#vmin, vmax = np.percentile(dub,[1,99])
#plt.imshow(dub, cmap='grey', origin='lower', vmin=vmin, vmax=vmax)
#plt.title('Reduced Dubhe')
#plt.colorbar(label='ADU')

#vmin, vmax = np.percentile(arc,[1,99])
#plt.imshow(arc,cmap='grey')
#plt.imshow(arc, cmap='grey', origin='lower', vmin=vmin, vmax=vmax)
#plt.title('Reduced Arcturus')
#plt.colorbar(label='ADU')
#plt.imshow(fixed_sadalsuud_value, cmap='Greys', origin='lower', vmin=vmin, vmax=vmax)

#vmin, vmax = np.percentile(sad,[1,99])
#plt.imshow(sad, cmap='flag', origin='lower', vmin=vmin, vmax=vmax)
#plt.title('Sadalsuud Prior Calibration')
#plt.colorbar(label='ADU')













