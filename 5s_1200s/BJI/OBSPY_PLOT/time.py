#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 14:54:42 2017

@author: horas

Program ini ditulis untuk membuat suatu deret waktu dengan interval sebesar 
samp_time pada program di bawah. Program ini akan menghasilkan deret waktu 
dengan unit detik sebanyak jumlah deret yang diinginkan sesuai variabel n_samples.
"""
##############################################################################
raw_data = open('BJI.DAT','r')
raw_line = raw_data.readlines()
len_data = len (raw_line)
raw_data.close()
##############################################################################

samp_freq = 20. #Hz
samp_time = 1./samp_freq
n_samples = len_data
d_samples = float(n_samples)/samp_freq

n = 0.
for n in range (int(n_samples)):
    time_read = open ('time.ascii','a+')
    
    series = n * samp_time
    
    time_read.write("%.5f\n"%(series))
    n = n + 1

time_read.close()

##############################################################################
