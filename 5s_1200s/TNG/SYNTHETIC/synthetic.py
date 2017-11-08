#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 17:47:29 2017

@author: horas
"""
#run this code if the time series is same from initial file time series

synt_read = open ('TNG_IA_disp_post_mij_conv0000_Z.dat','r')
synt_lines = synt_read.readlines()
synt_len = len (synt_lines)
synt_read.close()

n_time = 1200.          #based on time synthetic seismogram
n_samples = float(synt_len)
d_sample = float(n_samples/n_time)
dt = 1./d_sample

synt_read = open ('TNG_IA_disp_post_mij_conv0000_Z.dat','r')
for i in synt_read:
    
    #synt_write = open ('synt_time.ascii','a+')  #if you wanna write time
    synt_write = open ('synt_disp.ascii','a+')  #if you wanna wrtie displacement
    
    split = i.strip().split()
    k,v = split[0], split[1]
    k = float (k)
    v = float (v)
    
    #synt_write.write("%.7f\n"%k)           #write time
    synt_write.write("%E\n"%v)         #write displacement | check the float from the raw synthetic file 
    
synt_write.close()
synt_read.close()

############################################################################
#jika anda ingin menghasilkan timeseries yang baru, maka jalankan time.py
#kemudian jalankan time2minute.py, kemudian jalankan concatenate.py
#jika tidak run the code in the concatenate.py file then
