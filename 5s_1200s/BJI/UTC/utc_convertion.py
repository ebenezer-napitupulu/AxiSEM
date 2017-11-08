#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 14:51:17 2017

@author: horas
"""

from obspy import UTCDateTime as utc

read_data = open('DUM_X', 'r')

data_reads = read_data.readlines()
len_x = len (data_reads)

print ('length of data is', len_x)

for list_x in range (len_x):
    formated_data = open('DUM_X_formated', 'a+')
    
    data_list = data_reads[list_x]
    #data_list = float (data_list)
    time = utc(data_list)
    '''
    formated_data.write('time\t','year\t','month\t',\
                        'day\t','hour\t','minute\t',\
                        'second\t','microsecond\t',\
                        'julday\t','timestamp')
    '''
    formated_data.write("%.2f\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f\t%.2f\n"%(time,time.year,time.month,time.day,time.hour,time.minute,time.second,time.microsecond))
                        
    #formated_data.write('\n')
    
    list_x = list_x + 1

formated_data.close()
read_data.close()

