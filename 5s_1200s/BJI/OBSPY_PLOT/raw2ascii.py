#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 15:29:03 2017

@author: horas
"""
##############################################################################
'''program ini akan mengubah data dengan sifat data raw ke data dengan
format ascii. Dimana data ascii tersebut akan bisa di conversi 
ke data dengan format MSEED.'''

'''ada dua bentuk data ascii yang bisa di konversi ke MSEED
yaitu bentuk SLIST dan TSPAIR. Data raw yang dimiliki merupakan bentuk yang 
bisa diubah kedalam bentuk TSPAIR format ascii.'''

'''bentuk data TSPAIR
TIMESERIES XX_TEST__BHZ, 12 samples, 40 sps, 2003-05-29T02:13:22.043400, TSPAIR, INTEGER, Counts
2003-05-29T02:13:22.043400  2787
2003-05-29T02:13:22.068400  2776

line pertama merupakan HEADER
#HEADER field description
SourceName: "Net_Sta_Loc_Chan_Qual", no spaces, quality code optional
# samples:  Number of samples following header
# sps:      Sampling rate in samples per second
Time:       Time of first sample in ISO YYYY-MM-DDTHH:MM:SS.FFFFFF format
Format:     'SLIST' (sample list) or 'TSPAIR' (time-sample pair)
Type:       Sample type 'INTEGER' or 'FLOAT' or 'FLOAT64'
Units:      Units of time-series, optional (will not be present in miniSEED)
Headers:    miniSEED header values and flags, optional
'''
##############################################################################
from obspy import UTCDateTime #as utc
#from obspy import read

##############################################################################
raw_data = open('BJI.DAT','r')

raw_line = raw_data.readlines()
len_data = len (raw_line)
 
raw_data.close()
##############################################################################

raw_data = open('BJI.DAT','r')

for i in raw_data:
    write_ascii = open('BJI_displacement.ascii','a+')
    
    split = i.strip().split()   #atribut ini berfungsi mendefenisikan data dalam kolom
    k, v = split[0], split[1]   #argumen 0 = kolom pertama (k), 1 = kolom kedua (v)
    k = float (k)
    v = float (v)
    time = UTCDateTime(k)
    write_ascii.write("%.f\n"%v)
            
raw_data.close()
write_ascii.close()

##############################################################################
