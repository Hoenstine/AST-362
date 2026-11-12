# -*- coding: utf-8 -*-
"""
Gabe Hoenstine
10-5-26
This is the calculations and anaylis done on LAB 1 CALABRATIONS
The Plots are qouted out
"""
##### MEDIAN VALUE AVERGE BIAS  153.5 ##### 
##### READ NOISE 2.13                 #####




import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import glob
from astropy.io import fits
import OBS_Lab_Functions as obs
import lab2_helper_functions as hp
#import manual_centroid_finding as mcp

############### BIAS ############### 







bias_files = sorted(glob.glob('/Users/jameshoenstine/Desktop/AST_362/lab2_data/bias/*.fit'))

bias_images = np.array([fits.getdata(file) for file in bias_files])

fixed_bias_image = [obs.fix(bias_image) for bias_image in bias_images]

mean_bias = np.mean(obs.fix(bias_images), axis=0)
median_bias = np.median(mean_bias)

diff = fixed_bias_image[5] - fixed_bias_image[3] 
diff_mean = np.mean(diff) # MEAN IS 0.0024 


plt.hist(diff[1700:1900,2200:2400])
plt.title('Differnece image histogram')
plt.xlabel("Pixel value")
plt.ylabel('Number of pixels')

read_noise = np.std(diff)/ (2**.5) # 2.13


'''

plt.imshow(mean_bias,origin='lower', cmap="spring")
#plt.imshow(median_bias)
plt.colorbar(label='Counts')
plt.title('Bias Mean Image: QHY 163M CMOS')
'''
#%%

############### DARK ############### 

dark_files = sorted(glob.glob('/Users/jameshoenstine/Desktop/AST_362/lab2_data/darks/1/*.fit'))

dark_images = np.array([fits.getdata(file) for file in dark_files])




fixed_dark_image = [obs.fix(dark_image) for dark_image in dark_images]

mean_dark = np.mean(fixed_dark_image, axis=0)
median_dark = np.median(fixed_dark_image, axis=0)



plt.imshow(mean_dark)
plt.subplot()
plt.imshow(median_dark)
plt.colorbar(label='Counts')
plt.title('Bias Mean Dark Image 0.1: QHY 163M CMOS')

#%%f


############### FLATS ############### 


flats_files = sorted(glob.glob('/Users/jameshoenstine/Desktop/AST_362/lab2_data/flat/*.fit'))

flat_reduced = flats_files[::5]

flat_images = np.array([fits.getdata(file) for file in flat_reduced])

fixed_flat_image = [obs.fix(flat_image) for flat_image in flat_images]


median_flat = np.median(fixed_flat_image, axis=0)

normalized_flat = (flat_images - mean_bias) / median_flat # need to have subtrack from each


flat = np.median(normalized_flat , axis=0)
vmin, vmax = np.percentile(flat,[1,99])


plt.imshow(flat, origin='lower')
plt.title('Median Normalized Flat')
plt.colorbar(label='Counts')




#%%


########### DIFFERNECE IMAGE BIAS ##################

diff = fixed_bias_image[5] - fixed_bias_image[3] 
diff_mean = np.mean(diff) # MEAN IS 0.0024 SO BASICALLY 0 
#plt.hist(diff)


######### SCIENCE IMAGE ##########
'''

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

vmin, vmax = np.percentile(dub,[1,99])
#plt.imshow(dub, cmap='grey', origin='lower', vmin=vmin, vmax=vmax)
#plt.title('Reduced Dubhe')


vmin, vmax = np.percentile(arc,[1,99])
#plt.imshow(arc,cmap='grey')
#plt.imshow(arc, cmap='grey', origin='lower', vmin=vmin, vmax=vmax)
#plt.title('Reduced Arcturus')

#vmin, vmax = np.percentile(sad,[1,99])
#plt.imshow(sad, cmap='flag', origin='lower', vmin=vmin, vmax=vmax)
#plt.title('Reduced Sadalsuud')
plt.colorbar(label='ADU')

'''
                   ############################# MAG 8 STAR #############################
                   
                   
image_data1, mage_header1 = obs.load_fits('/Users/jameshoenstine/Desktop/AST_362/lab2_data/mag8/8magstar-0001.fit', ext=0)
#new_file = obs.fix(image_data1)
#fits.writeto('/Users/jameshoenstine/Desktop/AST_362/lab2_data/8magstar-fixed.fit',new_file,mage_header1,overwrite=True)
mag8_1 = hp.implot(obs.fix(image_data1))

'''

image_data2, mage_header2 = obs.load_fits('/Users/jameshoenstine/Desktop/AST_362/lab2_data/8magstar-0002.fit', ext=0)
mag8_2 = hp.implot(obs.fix(image_data2))

image_data3, mage_header3 = obs.load_fits('/Users/jameshoenstine/Desktop/AST_362/lab2_data/8magstar-0003.fit', ext=0)
mag8_3 = hp.implot(obs.fix(image_data3))

image_data4, mage_header4 = obs.load_fits('/Users/jameshoenstine/Desktop/AST_362/lab2_data/8magstar-0004.fit', ext=0)
mag8_4 = hp.implot(obs.fix(image_data4))

image_data5, mage_header5 = obs.load_fits('/Users/jameshoenstine/Desktop/AST_362/lab2_data/8magstar-0005.fit', ext=0)
mag8_5 = hp.implot(obs.fix(image_data5))

image_data6, mage_header6 = obs.load_fits('/Users/jameshoenstine/Desktop/AST_362/lab2_data/8magstar-0006.fit', ext=0)
mag8_6 = hp.implot(obs.fix(image_data6))

image_data7, mage_header7 = obs.load_fits('/Users/jameshoenstine/Desktop/AST_362/lab2_data/8magstar-0007.fit', ext=0)
mag8_7 = hp.implot(obs.fix(image_data7))

image_data8, mage_header8 = obs.load_fits('/Users/jameshoenstine/Desktop/AST_362/lab2_data/8magstar-0008.fit', ext=0)
mag8_8 = hp.implot(obs.fix(image_data8))

image_data9, mage_header9 = obs.load_fits('/Users/jameshoenstine/Desktop/AST_362/lab2_data/8magstar-0009.fit', ext=0)
mag8_9 = hp.implot(obs.fix(image_data9))

image_data10, mage_header10 = obs.load_fits('/Users/jameshoenstine/Desktop/AST_362/lab2_data/8magstar-0010.fit', ext=0)
mag8_10 = hp.implot(obs.fix(image_data10))

'''
                   ############################# THUBAN #############################
                   
                   
image_data11, mage_header11 = obs.load_fits('/Users/jameshoenstine/Desktop/AST_362/lab2_data/thuban/thuban-0002.fit', ext=0)
thuban_1 = hp.implot(obs.fix(image_data11))

new_file2 = obs.fix(image_data11)
fits.writeto('/Users/jameshoenstine/Desktop/AST_362/lab2_data/thuban/thuban-fix.fit',new_file2,mage_header11,overwrite=True)
'''

image_data12, mage_header12 = obs.load_fits('/Users/jameshoenstine/Desktop/AST_362/lab2_data/thuban-0002.fit', ext=0)
thuban_2 = hp.implot(obs.fix(image_data12))

image_data13, mage_header13 = obs.load_fits('/Users/jameshoenstine/Desktop/AST_362/lab2_data/thuban-0003.fit', ext=0)
thuban_3 = hp.implot(obs.fix(image_data13))

image_data14, mage_header14 = obs.load_fits('/Users/jameshoenstine/Desktop/AST_362/lab2_data/thuban-0004.fit', ext=0)
thuban_4 = hp.implot(obs.fix(image_data14))

image_data15, mage_header15 = obs.load_fits('/Users/jameshoenstine/Desktop/AST_362/lab2_data/thuban-0005.fit', ext=0)
thuban_5 = hp.implot(obs.fix(image_data15))

image_data16, mage_header16 = obs.load_fits('/Users/jameshoenstine/Desktop/AST_362/lab2_data/thuban-0006.fit', ext=0)
thuban_6 = hp.implot(obs.fix(image_data16))

image_data17, mage_header17 = obs.load_fits('/Users/jameshoenstine/Desktop/AST_362/lab2_data/thuban-0007.fit', ext=0)
thuban_7 = hp.implot(obs.fix(image_data17))

image_data18, mage_header18 = obs.load_fits('/Users/jameshoenstine/Desktop/AST_362/lab2_data/thuban-0008.fit', ext=0)
thuban_8 = hp.implot(obs.fix(image_data18))

image_data19, mage_header19 = obs.load_fits('/Users/jameshoenstine/Desktop/AST_362/lab2_data/thuban-0009.fit', ext=0)
thuban_9 = hp.implot(obs.fix(image_data19))

image_data20, mage_header20 = obs.load_fits('/Users/jameshoenstine/Desktop/AST_362/lab2_data/thuban-0010.fit', ext=0)
thuban_10 = hp.implot(obs.fix(image_data20))
'''

                   ############################# MYSTERY STAR #############################

image_data21, mage_header21 = obs.load_fits('/Users/jameshoenstine/Desktop/AST_362/lab2_data/mst/mysterystar-0001.fit', ext=0)
#mst_1 = hp.implot(obs.fix(image_data21))

new_file3 = obs.fix(image_data21)
fits.writeto('/Users/jameshoenstine/Desktop/AST_362/lab2_data/mst/mysterystar-fix.fit',new_file3,mage_header21,overwrite=True)

'''
image_data22, mage_header22 = obs.load_fits('/Users/jameshoenstine/Desktop/AST_362/lab2_data/mst/mysterystar-0002.fit', ext=0)
mst_2 = hp.implot(obs.fix(image_data22))

image_data23, mage_header23 = obs.load_fits('/Users/jameshoenstine/Desktop/AST_362/lab2_data/mst/mysterystar-0003.fit', ext=0)
mst_3 = hp.implot(obs.fix(image_data23))

image_data24, mage_header24 = obs.load_fits('/Users/jameshoenstine/Desktop/AST_362/lab2_data/mst/mysterystar-0004.fit', ext=0)
mst_4 = hp.implot(obs.fix(image_data24))

image_data25, mage_header25 = obs.load_fits('/Users/jameshoenstine/Desktop/AST_362/lab2_data/mst/mysterystar-0005.fit', ext=0)
mst_5 = hp.implot(obs.fix(image_data25))

image_data26, mage_header26 = obs.load_fits('/Users/jameshoenstine/Desktop/AST_362/lab2_data/mst/mysterystar-0006.fit', ext=0)
mst_6 = hp.implot(obs.fix(image_data26))

image_data27, mage_header27 = obs.load_fits('/Users/jameshoenstine/Desktop/AST_362/lab2_data/mst/mysterystar-0007.fit', ext=0)
mst_7 = hp.implot(obs.fix(image_data27))

image_data28, mage_header28 = obs.load_fits('/Users/jameshoenstine/Desktop/AST_362/lab2_data/mst/mysterystar-0008.fit', ext=0)
mst_8 = hp.implot(obs.fix(image_data28))

image_data29, mage_header29 = obs.load_fits('/Users/jameshoenstine/Desktop/AST_362/lab2_data/mst/mysterystar-0009.fit', ext=0)
mst_9 = hp.implot(obs.fix(image_data29))

image_data30, mage_header30 = obs.load_fits('/Users/jameshoenstine/Desktop/AST_362/lab2_data/mst/mysterystar-0010.fit', ext=0)
mst_10 = hp.implot(obs.fix(image_data30))

'''

                   ############################# LAN 2X STAR #############################
                   
                   
image_data31, mage_header31 = obs.load_fits('/Users/jameshoenstine/Desktop/AST_362/lab2_data/2xlan/2xlan_820-0001.fit', ext=0)
#lan2_1 = hp.implot(obs.fix(image_data31))
new_file4 = obs.fix(image_data31)
fits.writeto('/Users/jameshoenstine/Desktop/AST_362/lab2_data/2xlan/2xlan_820-fix.fit',new_file4,mage_header31,overwrite=True)


'''
image_data32, mage_header32 = obs.load_fits('/Users/jameshoenstine/Desktop/AST_362/lab2_data/2xlan_820-0002.fit', ext=0)
lan2_2 = hp.implot(obs.fix(image_data32))

image_data33, mage_header33 = obs.load_fits('/Users/jameshoenstine/Desktop/AST_362/lab2_data/2xlan_820-0003.fit', ext=0)
lan2_3 = hp.implot(obs.fix(image_data33))

image_data34, mage_header34 = obs.load_fits('/Users/jameshoenstine/Desktop/AST_362/lab2_data/2xlan_820-0004.fit', ext=0)
lan2_4 = hp.implot(obs.fix(image_data34))

image_data35, mage_header35 = obs.load_fits('/Users/jameshoenstine/Desktop/AST_362/lab2_data/2xlan_820-0005.fit', ext=0)
lan2_5 = hp.implot(obs.fix(image_data35))

image_data36, mage_header36 = obs.load_fits('/Users/jameshoenstine/Desktop/AST_362/lab2_data/2xlan_820-0006.fit', ext=0)
lan2_6 = hp.implot(obs.fix(image_data36))

image_data37, mage_header37 = obs.load_fits('/Users/jameshoenstine/Desktop/AST_362/lab2_data/2xlan_820-0007.fit', ext=0)
lan2_7 = hp.implot(obs.fix(image_data37))

image_data38, mage_header38 = obs.load_fits('/Users/jameshoenstine/Desktop/AST_362/lab2_data/2xlan_820-0008.fit', ext=0)
lan2_8 = hp.implot(obs.fix(image_data38))

image_data39, mage_header39 = obs.load_fits('/Users/jameshoenstine/Desktop/AST_362/lab2_data/2xlan_820-0009.fit', ext=0)
lan2_9 = hp.implot(obs.fix(image_data39))

image_data40, mage_header40 = obs.load_fits('/Users/jameshoenstine/Desktop/AST_362/lab2_data/2xlan_820-0010.fit', ext=0)
lan2_10 = hp.implot(obs.fix(image_data40))



                   ############################# LAN 3 STAR #############################
    '''               
                   
image_data41, mage_header41 = obs.load_fits('/Users/jameshoenstine/Desktop/AST_362/lab2_data/3land/3land-0002.fit', ext=0)
#lan3_1 = hp.implot(obs.fix(image_data41))
new_file5 = obs.fix(image_data41)
fits.writeto('/Users/jameshoenstine/Desktop/AST_362/lab2_data/3land/3land-fix.fit',new_file5,mage_header41,overwrite=True)


'''

image_data42, mage_header42 = obs.load_fits('/Users/jameshoenstine/Desktop/AST_362/lab2_data/3land-0002.fit', ext=0)
lan3_2 = hp.implot(obs.fix(image_data42))

image_data43, mage_header43 = obs.load_fits('/Users/jameshoenstine/Desktop/AST_362/lab2_data/3land-0003.fit', ext=0)
lan3_3 = hp.implot(obs.fix(image_data43))

image_data44, mage_header44 = obs.load_fits('/Users/jameshoenstine/Desktop/AST_362/lab2_data/3land-0004.fit', ext=0)
lan3_4 = hp.implot(obs.fix(image_data44))

image_data45, mage_header45 = obs.load_fits('/Users/jameshoenstine/Desktop/AST_362/lab2_data/3land-0005.fit', ext=0)
lan3_5 = hp.implot(obs.fix(image_data45))

image_data46, mage_header46 = obs.load_fits('/Users/jameshoenstine/Desktop/AST_362/lab2_data/3land-0006.fit', ext=0)
lan3_6 = hp.implot(obs.fix(image_data46))

image_data47, mage_header47 = obs.load_fits('/Users/jameshoenstine/Desktop/AST_362/lab2_data/3land-0007.fit', ext=0)
lan3_7 = hp.implot(obs.fix(image_data47))

image_data48, mage_header48 = obs.load_fits('/Users/jameshoenstine/Desktop/AST_362/lab2_data/3land-0008.fit', ext=0)
lan3_8 = hp.implot(obs.fix(image_data48))

image_data49, mage_header49 = obs.load_fits('/Users/jameshoenstine/Desktop/AST_362/lab2_data/3land-0009.fit', ext=0)
lan3_9 = hp.implot(obs.fix(image_data49))

image_data50, mage_header50 = obs.load_fits('/Users/jameshoenstine/Desktop/AST_362/lab2_data/3land-0010.fit', ext=0)
lan3_10 = hp.implot(obs.fix(image_data50))


'''
                   ############################# LAN 2x STAR ROUND 2 #############################
                   

image_data51, mage_header51 = obs.load_fits('/Users/jameshoenstine/Desktop/AST_362/lab2_data/lan2_again/94lan2x-0002.fit', ext=0)
lan2x_v2_1 = hp.implot(obs.fix(image_data51))
new_file6 = obs.fix(image_data51)
fits.writeto('/Users/jameshoenstine/Desktop/AST_362/lab2_data/lan2_again/94lan2x-fix.fit',new_file6,mage_header51,overwrite=True)

'''

image_data52, mage_header52 = obs.load_fits('/Users/jameshoenstine/Desktop/AST_362/lab2_data/94lan2x-0002.fit', ext=0)
lan2x_v2_2 = hp.implot(obs.fix(image_data52))

image_data53, mage_header53 = obs.load_fits('/Users/jameshoenstine/Desktop/AST_362/lab2_data/94lan2x-0003.fit', ext=0)
lan2x_v2_3 = hp.implot(obs.fix(image_data53))

image_data54, mage_header54 = obs.load_fits('/Users/jameshoenstine/Desktop/AST_362/lab2_data/94lan2x-0004.fit', ext=0)
lan2x_v2_4 = hp.implot(obs.fix(image_data54))

image_data55, mage_header55 = obs.load_fits('/Users/jameshoenstine/Desktop/AST_362/lab2_data/94lan2x-0005.fit', ext=0)
lan2x_v2_5 = hp.implot(obs.fix(image_data55))

image_data56, mage_header56 = obs.load_fits('/Users/jameshoenstine/Desktop/AST_362/lab2_data/94lan2x-0006.fit', ext=0)
lan2x_v2_6 = hp.implot(obs.fix(image_data56))

image_data57, mage_header57 = obs.load_fits('/Users/jameshoenstine/Desktop/AST_362/lab2_data/94lan2x-0007.fit', ext=0)
lan2x_v2_7 = hp.implot(obs.fix(image_data57))

image_data58, mage_header58 = obs.load_fits('/Users/jameshoenstine/Desktop/AST_362/lab2_data/94lan2x-0008.fit', ext=0)
lan2x_v2_8 = hp.implot(obs.fix(image_data58))

image_data59, mage_header59 = obs.load_fits('/Users/jameshoenstine/Desktop/AST_362/lab2_data/94lan2x-0009.fit', ext=0)
lan2x_v2_9 = hp.implot(obs.fix(image_data59))

image_data60, mage_header60 = obs.load_fits('/Users/jameshoenstine/Desktop/AST_362/lab2_data/94lan2x-0010.fit', ext=0)
lan2x_v2_10 = hp.implot(obs.fix(image_data60))

                   
                  
                   







                   ############################# DOLPHIN STAR #############################


'''

image_data61, mage_header61 = obs.load_fits('/Users/jameshoenstine/Desktop/AST_362/lab2_data/del/18del-0002.fit', ext=0)
del_1 = hp.implot(obs.fix(image_data61))
new_file7 = obs.fix(image_data61)
fits.writeto('/Users/jameshoenstine/Desktop/AST_362/lab2_data/del/18del-fix.fit',new_file7,mage_header61,overwrite=True)


'''
image_data62, mage_header62 = obs.load_fits('/Users/jameshoenstine/Desktop/AST_362/lab2_data/18del-0002.fit', ext=0)
del_2 = hp.implot(obs.fix(image_data62))

image_data63, mage_header63 = obs.load_fits('/Users/jameshoenstine/Desktop/AST_362/lab2_data/18del-0003.fit', ext=0)
del_3 = hp.implot(obs.fix(image_data63))

image_data64, mage_header64 = obs.load_fits('/Users/jameshoenstine/Desktop/AST_362/lab2_data/18del-0004.fit', ext=0)
del_4 = hp.implot(obs.fix(image_data64))

image_data65, mage_header65 = obs.load_fits('/Users/jameshoenstine/Desktop/AST_362/lab2_data/18del-0005.fit', ext=0)
del_5 = hp.implot(obs.fix(image_data65))

image_data66, mage_header66 = obs.load_fits('/Users/jameshoenstine/Desktop/AST_362/lab2_data/18del-0006.fit', ext=0)
del_6 = hp.implot(obs.fix(image_data66))

image_data67, mage_header67 = obs.load_fits('/Users/jameshoenstine/Desktop/AST_362/lab2_data/18del-0007.fit', ext=0)
del_7 = hp.implot(obs.fix(image_data67))

image_data68, mage_header68 = obs.load_fits('/Users/jameshoenstine/Desktop/AST_362/lab2_data/18del-0008.fit', ext=0)
del_8 = hp.implot(obs.fix(image_data68))

image_data69, mage_header69 = obs.load_fits('/Users/jameshoenstine/Desktop/AST_362/lab2_data/18del-0009.fit', ext=0)
del_9 = hp.implot(obs.fix(image_data69))

image_data70, mage_header70 = obs.load_fits('/Users/jameshoenstine/Desktop/AST_362/lab2_data/18del-0010.fit', ext=0)
del_10 = hp.implot(obs.fix(image_data70))










'''
fit = '/Users/jameshoenstine/Downloads/Vega_0016-0001.fit'

image_data71, mage_header71 = obs.load_fits('/Users/jameshoenstine/Downloads/Vega_0016-0001.fit', ext=0)
veg = hp.implot(obs.fix(image_data71))
new_file8 = obs.fix(image_data71)
fits.writeto('/Users/jameshoenstine/Downloads/Vega_0016-fix.fit',new_file8,mage_header71,overwrite=True)










