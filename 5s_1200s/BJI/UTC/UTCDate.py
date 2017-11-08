#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Thu Sep 28 14:26:44 2017

@author: horas
"""
from obspy import UTCDateTime
a=7.3282395e+05

time=UTCDateTime(a)

print time
print time.date
print time.year
print time.month
print time.day
print time.time
print time.hour
print time.minute
print time.second
print time.microsecond
print '\n'
print time.julday
print time.timestamp
print time.weekday


a=2
b=3
print ("%f\t%f" %(a,b))