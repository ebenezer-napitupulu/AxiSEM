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
raw_data = open('synt_time.ascii','r')
raw_line = raw_data.readlines()
len_data = len (raw_line)
raw_data.close()
##############################################################################

t_n = float(raw_line[211])
t_n1 = float(raw_line[212])
delta_t = t_n1 - t_n
delta_t = float(delta_t)

##############################################################################
samp_time = delta_t
samp_freq = 1./samp_time
n_samples = len_data

n = 0.
for n in range (int(n_samples)):
    time_read = open ('time.ascii','a+')
    
    series = n * samp_time
    
    time_read.write("%.7f\n"%(series))
    n = n + 1

time_read.close()

##############################################################################
#jika anda menjalankan program ini maka jalankan program time2minute kemudian
