#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Oct  2 14:54:42 2017

@author: horas

Program ini ditulis untuk mengkonversi suatu deret waktu dengan interval time
1/20 detik. Deret waktu dalam detik dikonversi ke menit. Deret waktu yang
dihasilkan digunakan sebagai syarat data untuk memperoleh data konversi ke 
format MSEED.
"""

time = open ('time.ascii','r')
read_lines = time.readlines()
len_data = len (read_lines)
time.close()
for i in range (len_data):
    time2minute = open ('time2minute.ascii','a+')
    readline = read_lines[i]
    readline = float (readline)
        
    if readline < 10:
        date = '1970-01-09T11:00:'
        time2minute.write("%s%0d%.6f\n"%(date,0,readline))
        

    elif readline < 60:
        date = '1970-01-09T11:00:'
        time2minute.write("%s%.6f\n"%(date,readline))
            
    elif readline < 120:
        x = readline - 60.
        date = '1970-01-09T11:01:'
        if x < 10:
            time2minute.write("%s%0d%.6f\n"%(date,0,x))
        else: 
            if x < 60:
                time2minute.write("%s%.6f\n"%(date,x))

    elif readline < 180:
        x = readline - 120.
        date = '1970-01-09T11:02:'
        if x < 10:
            time2minute.write("%s%0d%.6f\n"%(date,0,x))
        else: 
            if x < 60:
                time2minute.write("%s%.6f\n"%(date,x))
                            
    elif readline < 240:
        x = readline - 180.
        date = '1970-01-09T11:03:'
        if x < 10:
            time2minute.write("%s%0d%.6f\n"%(date,0,x))
        else: 
            if x < 60:
                time2minute.write("%s%.6f\n"%(date,x))
                                
    elif readline < 300:
        x = readline - 240.
        date = '1970-01-09T11:04:'
        if x < 10:
            time2minute.write("%s%0d%.6f\n"%(date,0,x))
        else: 
            if x < 60:
                time2minute.write("%s%.6f\n"%(date,x))
                        
    elif readline < 360:
        x = readline - 300.
        date = '1970-01-09T11:05:'
        if x < 10:
            time2minute.write("%s%0d%.6f\n"%(date,0,x))
        else: 
            if x < 60:
                time2minute.write("%s%.6f\n"%(date,x))
                                        
    elif readline < 420:
        x = readline - 360.
        date = '1970-01-09T11:06:'
        if x < 10:
            time2minute.write("%s%0d%.6f\n"%(date,0,x))
        else: 
            if x < 60:
                time2minute.write("%s%.6f\n"%(date,x))
            
    elif readline < 480:
        x = readline - 420.
        date = '1970-01-09T11:07:'
        if x < 10:
            time2minute.write("%s%0d%.6f\n"%(date,0,x))
        else: 
            if x < 60:
                time2minute.write("%s%.6f\n"%(date,x))
                                    
    elif readline < 540:
        x = readline - 480.
        date = '1970-01-09T11:08:'
        if x < 10:
            time2minute.write("%s%0d%.6f\n"%(date,0,x))
        else: 
            if x < 60:
                time2minute.write("%s%.6f\n"%(date,x))
                                       
    elif readline < 600:
        x = readline - 540.
        date = '1970-01-09T11:09:'
        if x < 10:
            time2minute.write("%s%0d%.6f\n"%(date,0,x))
        else: 
            if x < 60:
                time2minute.write("%s%.6f\n"%(date,x))
                                             
    elif readline < 660:
        x = readline - 600.
        date = '1970-01-09T11:10:'
        if x < 10:
            time2minute.write("%s%0d%.6f\n"%(date,0,x))
        else: 
            if x < 60:
                time2minute.write("%s%.6f\n"%(date,x))
                                                        
    elif readline < 720:
        x = readline - 660.
        date = '1970-01-09T11:11:'
        if x < 10:
            time2minute.write("%s%0d%.6f\n"%(date,0,x))
        else: 
            if x < 60:
                time2minute.write("%s%.6f\n"%(date,x))

    elif readline < 780:
        x = readline - 720.
        date = '1970-01-09T11:12:'
        if x < 10:
            time2minute.write("%s%0d%.6f\n"%(date,0,x))
        else: 
            if x < 60:
                time2minute.write("%s%.6f\n"%(date,x))
                
    elif readline < 840:
        x = readline - 780.
        date = '1970-01-09T11:13:'
        if x < 10:
            time2minute.write("%s%0d%.6f\n"%(date,0,x))
        else: 
            if x < 60:
                time2minute.write("%s%.6f\n"%(date,x))
        
    elif readline < 900:
        x = readline - 840.
        date = '1970-01-09T11:14:'
        if x < 10:
            time2minute.write("%s%0d%.6f\n"%(date,0,x))
        else: 
            if x < 60:
                time2minute.write("%s%.6f\n"%(date,x))
                
    elif readline < 960:
        x = readline - 900.
        date = '1970-01-09T11:15:'
        if x < 10:
            time2minute.write("%s%0d%.6f\n"%(date,0,x))
        else: 
            if x < 60:
                time2minute.write("%s%.6f\n"%(date,x))
    elif readline < 1020:
        x = readline - 960.
        date = '1970-01-09T11:16:'
        if x < 10:
            time2minute.write("%s%0d%.6f\n"%(date,0,x))
        else: 
            if x < 60:
                time2minute.write("%s%.6f\n"%(date,x))
time2minute.close()

##############################################################################