#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 12:19:56 2017

@author: horas
"""

from obspy.core import read
#from scipy.integrate import simps
#import numpy as np
#import matplotlib.pylab as plt
#from obspy.core import stream

st = read ("KRK_full.MSEED")

print st
print '\n'
print st[0].data
print '\n'
print type(st)
print '\n'
print st.traces
print '\n'
print st[0].stats
print '\n'
print st[0].stats.delta, '|', st[0].stats.endtime
print '\n'
print st

print st[0]
print st[0].stats.delta

#jalankan yang dibawah ini untuk menemukan gradien
#st[0].data = np.gradient(st[0].data, st[0].stats.delta)
#print st[0].data

st.plot()

#st[0].data = np.array(st[0].data)
#
st.plot()
#############################################################################
#setelah program ini dijalankan maka lanjut ke data sintetik
#jangan lupa untuk menyalin file.MSEED ke folder SYNTHETIC