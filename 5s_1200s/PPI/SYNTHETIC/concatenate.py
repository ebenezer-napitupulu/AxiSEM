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
read_disp = open ('synt_disp.ascii','r')
disp_lines = read_disp.readlines()
disp_len = len (disp_lines)
read_disp.close()

#open the synt_time.ascii
read_synt_time = open('synt_time.ascii','r')
read_synt = read_synt_time.readlines()
read_synt_time.close()
delta_time = float(read_synt[1000])-float(read_synt[999])

#set the variable
header = 'TIMESERIES'
station_name = 'INATEWS_PPI_SYNT_Z_R,'   #Net_Sta_Loc_Chan_Qual
samples = time_len-1
samples = str(samples)+' samples,'
sps = (1./delta_time)                      #denominator input manual from delta time 
sps = ("%.20s"%(sps))+' sps,'
time_start = time_lines[0]
format_ = 'TSPAIR,'                   #'TSPAIR' or 'SLIST'   
type_ = 'FLOAT,'                    #'INTEGER', 'FLOAT' or 'ASCII'
unit = 'M'                      #Counts, M/S, etc.

concatenate = open ('synt_full.ascii','a+')
concatenate.write("%s %s %s %s %.27s, %s %s %s\n"%(header, station_name, samples, sps, time_start, format_, type_, unit))
for i in range (time_len):
    disp_line = disp_lines[i]
    disp_line = float (disp_line)
    concatenate.write("%.27s\t%E\n"%(time_lines[i],disp_line))
    #concatenate.write("%"%)

concatenate.close()
######################################################################
#step selanjutnya adalah convert ascii to MSEED
#run in terminal
'''
ascii2mseed nama_file.ascii -o nama_file.mseed
'''
#then check the disk usage for the file.MSEED
#with run this code 'du -sh file.MSEED' without quotes

#nex, run the read_data.py to compare the synthetic and observation data
