#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Tue Oct  3 12:44:51 2017

@author: horas
"""
#open the x series
read_time = open ('time2minute.ascii','r')
time_lines = read_time.readlines()
time_len = len (time_lines)
read_time.close()

#open the y series
read_disp = open ('CBJI_Velocity.ascii','r')
disp_lines = read_disp.readlines()
disp_len = len (disp_lines)
read_disp.close()
'''
#open the synt_time.ascii
read_synt_time = open('synt_time.ascii','r')
read_synt = read_synt_time.readlines()
read_synt_time.close()
delta_time = read_synt[1000]-read_synt[999]
'''
#set the variable
header = 'TIMESERIES'
station_name = 'InaTEWS_CBJI__Z_R,'   #Net_Sta_Loc_Chan_Qual
samples = time_len-1
samples = str(samples)+' samples,'
sps = (1./delta_time)                      #denominator input manual from delta time 
sps = str(sps)+' sps,'
time_start = time_lines[0]
format_ = 'TSPAIR,'                   #'TSPAIR' or 'SLIST'   
type_ = 'INTEGER,'                    #'INTEGER', 'FLOAT' or 'ASCII'
unit = 'Counts'                      #Counts, M/S, etc.

concatenate = open ('CBJI_full.ascii','a+')
concatenate.write("%s %s %s %s %.26s, %s %s %s\n"%(header, station_name, samples, sps, time_start, format_, type_, unit))
for i in range (time_len):
    disp_line = disp_lines[i]
    disp_line = float (disp_line)
    concatenate.write("%.26s\t%d\n"%(time_lines[i],disp_line))
    #concatenate.write("%"%)

concatenate.close()
######################################################################
#step selanjutnya adalah convert ascii to MSEED
#run in terminal
'''
ascii2mseed nama_file.ascii -o nama_file.mseed
'''









