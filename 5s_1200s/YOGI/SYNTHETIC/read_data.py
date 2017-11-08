#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Fri Sep 29 12:19:56 2017

@author: horas
"""

import obspy
import numpy as np
import matplotlib.pylab as plt

st = obspy.read ("synt_full.MSEED")
obs = obspy.read("YOGI_full.MSEED")       #change file name of file.MSEED

#####################################figure 1######################################
plt.figure(1)                        
fig = plt.figure(1)
fig.suptitle('YOGI', fontsize=14)    #change the title of the each figure

plt.rc('xtick', labelsize=6)
plt.rc('ytick', labelsize=6)
plt.rc('legend',fontsize=8)
#------------------------------------subplot 1---------------------------
disp = plt.subplot(2,1,1)           
disp.plot(st[0].data, color='red', label='Seismogram sintetik', linewidth=0.5)
disp.set_ylabel('Pergeseran (m)', fontsize=7)
disp.legend()
#------------------------------------subplot 2---------------------------
vel_obs = plt.subplot(2,1,2)        
vel_obs.plot(obs[0].data, label='Seismogram observasi', linewidth=0.5)
vel_obs.set_ylabel('Kecepatan (counts)', fontsize=7)
vel_obs.set_xlabel('Sampel', fontsize=8)
vel_obs.legend()
#--------------------------------save figure-------------------------------
#plt.savefig('sintetik_YOGI', format='png', dpi=1200)
plt.savefig('YOGI sintetik and obervasi', format='png', dpi=1200)

###################################figure 2########################################
plt.figure(2)                       
fig2 = plt.figure(2)
fig2.suptitle("YOGI", fontsize=14)

plt.rc('xtick', labelsize=6)
plt.rc('ytick', labelsize=6)
plt.rc('legend', fontsize=8)
#-----------------------------subplot 1----------------------------------
st.resample(20)
st[0].data = np.gradient(st[0].data, st[0].stats.delta)     #gradient of synthetic seismogram
t_st = np.arange(0, st[0].stats.npts/st[0].stats.sampling_rate, obs[0].stats.delta)

vel = plt.subplot(2,1,1)            
vel.plot(t_st, st[0].data, label='Seismogram sintetik', linewidth=0.5)
vel.set_ylabel('Kecepatan (m/s)', fontsize=7)
plt.xlim(0,1000)
#plt.ylim(-0.002,0.002)
vel.legend()
#-----------------------------subplot 2----------------------------------
tr_obs = obs[0]
obs_filt = tr_obs.copy()
obs_filt.filter('lowpass', freq=0.3, corners=2, zerophase=True)
t_obs = np.arange(0, obs[0].stats.npts/obs[0].stats.sampling_rate, obs[0].stats.delta)

vel_obs = plt.subplot(2,1,2)
vel_obs.plot(t_obs, obs_filt.data, label='Seismogram observasi', linewidth=0.5)
vel_obs.set_ylabel('Kecepatan (counts)', fontsize=7)
vel_obs.set_xlabel('Waktu (s)', fontsize=8)
plt.xlim(0,1000)
#plt.ylim(-4E+05,4E+05)
vel_obs.legend()
#------------------------------------save figure---------------------------
plt.savefig('YOGI Filtered 0.3Hz-1000s', format='png', dpi=1200)

#####################################figure 3######################################
plt.figure(3)
fig3 = plt.figure(3)
fig3.suptitle("YOGI", fontsize=14)

plt.rc('xtick', labelsize=6)
plt.rc('ytick', labelsize=6)
plt.rc('legend', fontsize=8)
#------------------------------subplot 1---------------------------------
st.resample(20)
st[0].data = np.gradient(st[0].data, st[0].stats.delta)     #gradient of synthetic seismogram
str(st[0].data)
t_st = np.arange(0, st[0].stats.npts/st[0].stats.sampling_rate, st[0].stats.delta)

vel = plt.subplot(3,1,1)            
vel.plot(t_st, st[0].data, 'g', label='Seismogram sintetik', linewidth=0.5)
vel.set_ylabel('Kecepatan (m/s)', fontsize=7)
plt.xlim(7.2,42.2)
vel.legend()

#------------------------------subplot 2---------------------------------
tr_obs = obs[0]
obs_filt = tr_obs.copy()
obs_filt.filter('lowpass', freq=0.3, corners=2, zerophase=True)
t_obs = np.arange(0, obs[0].stats.npts/obs[0].stats.sampling_rate, obs[0].stats.delta)

vel_obs = plt.subplot(3,1,2)
vel_obs.plot(t_obs, obs_filt.data, label='Seismogram observasi', linewidth=0.5)
vel_obs.set_ylabel('Kecepatan (counts)', fontsize=7)
vel_obs.set_xlabel('Waktu (s)', fontsize=8)

plt.xlim(965,1000)
#plt.ylim(-4E+05,4E+05)         
vel_obs.legend()

#------------------------------------save figure---------------------------
plt.savefig('YOGI Filtered 0.3Hz-35s', format='png', dpi=1200)

#####################################figure 4######################################
plt.figure(4)
fig4 = plt.figure(4)
fig4.suptitle("YOGI", fontsize=14)

plt.rc('xtick', labelsize=6)
plt.rc('ytick', labelsize=6)
plt.rc('legend', fontsize=8)

plt.subplots_adjust(top=0.8)

#------------------------------graph 1---------------------------------
vel_obs = fig4.add_subplot(111, label="1")
vel_ = fig4.add_subplot(111, label="2", frame_on=False)

tr_obs = obs[0]
obs_filt = tr_obs.copy()
obs_filt.filter('lowpass', freq=0.3, corners=2, zerophase=True)
t_obs = np.arange(0, obs[0].stats.npts/obs[0].stats.sampling_rate, obs[0].stats.delta)

vel_obs.plot(t_obs, obs_filt.data, label='Seismogram observasi', linewidth=0.5)
vel_obs.set_ylabel('Kecepatan (counts)', fontsize=7)
vel_obs.set_xlabel('Waktu (s)', fontsize=8)
vel_obs.tick_params(axis='x', colors='b')
vel_obs.tick_params(axis='y', colors='b')

vel_obs.set_xlim(965,1000)
vel_obs.set_ylim(-40E+05,40E+05)
vel_obs.legend(bbox_to_anchor=(0.37,0.1), loc=1, borderaxespad=0.)

#------------------------------graph 2---------------------------------
vel_.plot(t_obs, st[0].data, 'g', label='Seismogram sintetik', linewidth=0.5)
vel_.set_ylabel('kecepatan (m/s)', color='g', fontsize=7)
vel_.set_xlabel('Waktu (s)', color='g', fontsize=8)
vel_.tick_params(axis='x', colors='g')
vel_.tick_params(axis='y', colors='g')
vel_.xaxis.tick_top()
vel_.yaxis.tick_right()
vel_.xaxis.set_label_position('top')
vel_.yaxis.set_label_position('right')

vel_.set_xlim(7.2,42.2)
vel_.set_ylim(-20E-03,20E-03)
vel_.legend()

#------------------------------save figure---------------------------------
plt.savefig('YOGI Filtered 0.3Hz-35s Merged', format='png', dpi=1200)
plt.show()

###########################################################################
#-------------BASIC OBSPY-------------------------------------------------#
###########################################################################
#st.sort(['starttime'])
#dt = st[0].stats.starttime.timestamp
'''
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
'''
##################################33#######################################