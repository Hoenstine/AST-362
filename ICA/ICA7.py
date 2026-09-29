#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
REPEATED MEASUREMENTS & DISTROBUTIONS 1

In-Class Assignment 7

Gabe Hoenstine

"""
############################### PART 1-2 ###############################
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import glob

sample_data = np.loadtxt('/Users/jameshoenstine/Desktop/AST_362/Lab0/different_niter/n100_t10ms/n100_t10ms_001.dat')

############################### PART 3 ###############################

mean_sample = sum(sample_data) / len(sample_data) # 0.57

x = 0
for i in range(len(sample_data)):
    x = x + (( (sample_data[i] - mean_sample) **2) )
             
standard_dev = (x /(len(sample_data)) ) **.5 # Value: 1.32 Orginally had - 1 but that did not match
standard_mean = standard_dev/(len(sample_data))**.5


############################### PART 4 ###############################

sample_std = np.std(sample_data) # Value: 1.32
sample_mean = np.mean(sample_data) # Value 0.57

############################### PART 5 ############################### 
plt.title('Histograms of N=100, t=10ms data')
plt.ylabel('frequency')
plt.xlabel('number of counts')
plt.hist(sample_data,bins=10) # Sqrt of total counts = bin quantity 

############################### PART 6 ############################### 

list_of_files = sorted(glob.glob('/Users/jameshoenstine/Desktop/AST_362/Lab0/different_niter/n100_t10ms/*.dat'))

npoints = 100

############################### PART 7 ###############################
data_array = np.zeros([len(list_of_files), npoints])
for i in range(len(list_of_files)):
    data_array[i,:] = np.loadtxt(list_of_files[i])


############################### PART 8 ###############################

rows = []
data = {'Mean':1, 
        'Standard Devation':1,
        'Standard Devation of the mean':1
        }


for i in range(len(data_array)):
    mean = data_array[i].mean()
    std = data_array[i].std()
    std_mean = std/10
    print(f" FILE {i} Mean:{mean} , Standard Deviation: {std}, Mean of Standard Deviation: {std_mean}")
    rows.append({'Mean':mean, 
            'Standard Devation':std,
            'Standard Devation of the mean':std_mean
            })
df = pd.DataFrame(rows)


############################### PART 9 ###############################
"""
                                     N = 100 T = 10MS 

 FILE 0 Mean:0.57 , Standard Deviation: 1.32102233137824, Mean of Standard Deviation: 0.13210223313782402
 FILE 1 Mean:0.58 , Standard Deviation: 1.5567915724335097, Mean of Standard Deviation: 0.15567915724335096
 FILE 2 Mean:0.85 , Standard Deviation: 2.471335671251479, Mean of Standard Deviation: 0.24713356712514792
 FILE 3 Mean:0.47 , Standard Deviation: 1.2996538000559996, Mean of Standard Deviation: 0.12996538000559996
 FILE 4 Mean:0.94 , Standard Deviation: 2.855941175864797, Mean of Standard Deviation: 0.2855941175864797
 FILE 5 Mean:0.54 , Standard Deviation: 1.3146862743635837, Mean of Standard Deviation: 0.13146862743635837
 FILE 6 Mean:0.52 , Standard Deviation: 1.8410866356584092, Mean of Standard Deviation: 0.18410866356584094
 FILE 7 Mean:0.64 , Standard Deviation: 1.5589740215924064, Mean of Standard Deviation: 0.15589740215924064
 FILE 8 Mean:0.49 , Standard Deviation: 1.0908253755757609, Mean of Standard Deviation: 0.10908253755757609
 FILE 9 Mean:0.63 , Standard Deviation: 2.524499950485244, Mean of Standard Deviation: 0.2524499950485244

"""

############################### PART 10 ###############################

nbins= 10

plt.figure(figsize=[10,10])
plt.subplot(321)
plt.hist(data_array[0],nbins)
plt.title('Histograms of N=100, t=10ms data')
plt.ylabel('frequency')
plt.subplot(322)
plt.hist(data_array[1],nbins)
plt.subplot(323)
plt.hist(data_array[2],nbins)
plt.ylabel('frequency')
plt.subplot(324)
plt.hist(data_array[3],nbins)
plt.subplot(325)
plt.ylabel('frequency')
plt.hist(data_array[4],nbins)
plt.xlabel('number of counts')
plt.subplot(326)
plt.hist(data_array[5],nbins)
plt.xlabel('number of counts')


#%%

########## N = 1000 t = 10 ###################

sample_data = np.loadtxt('/Users/jameshoenstine/Desktop/AST_362/Lab0/different_niter/n1000_t10ms/n1000_t10ms_001.dat')
list_of_files = sorted(glob.glob('/Users/jameshoenstine/Desktop/AST_362/Lab0/different_niter/n1000_t10ms/*.dat'))

mean = sum(sample_data) / len(sample_data) # 0.57

npoints = 1000
data_array = np.zeros([len(list_of_files), npoints])
for i in range(len(list_of_files)):
    data_array[i,:] = np.loadtxt(list_of_files[i])


rows = []
data = {'Mean':1, 
        'Standard Devation':1,
        'Standard Devation of the mean':1
        }


for i in range(len(data_array)):
    mean = data_array[i].mean()
    std = data_array[i].std()
    std_mean = std/100
    print(f" FILE {i} Mean:{mean} , Standard Deviation: {std}, Mean of Standard Deviation: {std_mean}")
    rows.append({'Mean':mean, 
            'Standard Devation':std,
            'Standard Devation of the mean':std_mean
            })
df = pd.DataFrame(rows)

"""
                                     N = 1000 T = 10MS 
 FILE 0 Mean:0.68 , Standard Deviation: 1.8214280112043957, Mean of Standard Deviation: 0.018214280112043957
 FILE 1 Mean:0.614 , Standard Deviation: 1.9618878663165231, Mean of Standard Deviation: 0.01961887866316523
 FILE 2 Mean:0.636 , Standard Deviation: 1.6862692548937728, Mean of Standard Deviation: 0.016862692548937727
 FILE 3 Mean:0.623 , Standard Deviation: 1.8030171934842993, Mean of Standard Deviation: 0.018030171934842992
 FILE 4 Mean:0.578 , Standard Deviation: 1.4852326417097088, Mean of Standard Deviation: 0.014852326417097089
 FILE 5 Mean:0.538 , Standard Deviation: 1.6243632598652311, Mean of Standard Deviation: 0.016243632598652313
 FILE 6 Mean:0.588 , Standard Deviation: 1.6340917966870772, Mean of Standard Deviation: 0.01634091796687077
 FILE 7 Mean:0.662 , Standard Deviation: 1.7993765587002628, Mean of Standard Deviation: 0.01799376558700263
 FILE 8 Mean:0.572 , Standard Deviation: 1.593366247916655, Mean of Standard Deviation: 0.01593366247916655
 FILE 9 Mean:0.749 , Standard Deviation: 1.9308026828239078, Mean of Standard Deviation: 0.019308026828239077
"""
nbins= 32

plt.figure(figsize=[10,10])
plt.subplot(321)
plt.hist(data_array[0],nbins)
plt.title('Histograms of N=1000, t=10ms data')
plt.ylabel('frequency')
plt.subplot(322)
plt.hist(data_array[1],nbins)
plt.subplot(323)
plt.hist(data_array[2],nbins)
plt.ylabel('frequency')
plt.subplot(324)
plt.hist(data_array[3],nbins)
plt.subplot(325)
plt.ylabel('frequency')
plt.hist(data_array[4],nbins)
plt.xlabel('number of counts')
plt.subplot(326)
plt.hist(data_array[5],nbins)
plt.xlabel('number of counts')

"""
These results have slightly differnt values. I assume due to variation of the data.

"""
