#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Sun Sep 17 23:18:50 2017

@author: horas
"""

#read and do math operation
read = open("DUM_Y", "r")
base_val = read.readline(20)
base_val = float (base_val)
file_nod = read.readlines()
nod = len (file_nod)
#x = 0
for x in range (nod):
    dim = open("CORRECTED.txt", "a+")
    
    c = file_nod[x]
    d = float(c)
    #e = d - base_val
    f = str(d)
    #g = str(d)+" "+str(base_val)+" "+f
    h = str(x)
    i = h +" "+ f
    dim.write(i)
    dim.write("\n")
    
    x=x+1
    
dim.close()
read.close()
