#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 19:48:27 2017

@author: horas
"""

#with open('DUM') as file:
#    for line in file:
#        print (line, end='')


'''
normal_list=[1,2,3,5]

class CustomSequence():
    def __len__(self):
        return 5
    
    def __getitem__(self, index):
        return "x{0}".format(index)
    
class FunkyBackwards():
    
    def __reversed__(self):
        return "BACKWARDS"
    
for seq in normal_list, CustomSequence(), FunkyBackwards():
    print("{}: ".format(seq.__class__.__name__))
    for item in reversed(seq):
        
        print (item)
'''


'''
#I/O
contents = "Some contents"

file = open("DUM", "a")
file.write(contents)
file.close()
'''

#read and do math operation
read = open("DUM_Y", "ra")
base_val = read.readline(20)
base_val = float (base_val)
file_nod = read.readlines()
nod = len (file_nod)
#x = 0
for x in range (nod):
    dim = open("CORRECTED.txt", "a+")
    
    #for i in file_nod:
        #i=float(i)
        
    #dim.write(file_nod[x])
    c = file_nod[x]
    d = float(c)
    #e = d - base_val
    f = str(d)
    #g = str(d)+" "+str(base_val)+" "+f
    h = str(x)
    i = h +" "+ f
    dim.write(i)
    dim.write("\n")
    #print d, base_val, f
        #dim.close()
        
        #corr_ = open("CORRECTED", "w+")
        #corr_value = corr_.readlines()
    #for z in corr_value[x]:
        #corrected = float (z)
        #corr = ((z) - (base_val))
        #corr = str(corrected)
        
    #print file_nod[x]
    x=x+1
    #i=str(i)
    #print base_val, file_nod[1], nod
    
    #lis = file_nod[i]
    
    
    
    #lis = str(lis)
    #list_ = float (list)
    
    #dim_base = (list_ - base_val)
    
    #dim.close()
    #print i
    #x=x+1
   
    #i = i + 1
    
#str2float = float(base_var)
#base_float = str2float + 1
#print len(base_var)
dim.close()
read.close()








