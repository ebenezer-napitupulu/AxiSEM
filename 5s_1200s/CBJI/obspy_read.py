#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Sep 18 13:57:29 2017

@author: horas
"""
import os
from obspy.core import read

st = read("/home/horas/AXISEM_v1.1_YOGYA_MT_FULL-GCMT-DATA-SOURCE_1800s/SOLVER/PREM_mrr_20s_gauss_1800s_MT_FULL-DATA-GCMT/Data_Postprocessing/SEISMOGRAMS/OBSERVASI/BJI/DUM_Y.dat", format="Y")

print (st)