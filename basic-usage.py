#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 28 07:48:16 2021

@author: kchittur
"""


# import all of the functions, procedures
from jhu_github_analysis_functions import *

'''
this script contains a few examples of how to read data from the
Hopkins data set 
there are three data sets - deaths, confirmed and recovered 
for both global (countries) and states in the US 
the filenames refer to specific files in the JHU repository 
'''

globalfilenames = [deathsGlobal, confirmedGlobal, recoveredGlobal]
globaltitles = ['Deaths', 'Confirmed', 'Recovered']
statefilenames = [deathsUS, confirmedUS, recoveredUS]
statetitles = ['Deaths', 'Confirmed', 'Recovered']

# you can get a list of all of the countries in the repo
allcountrynames = getlistofcountries(deathsGlobal)
# and a list of all of the US states
allstatenames = statenames

# get the dates from the file 
x = getdates(deathsGlobal)   



# arbitrarily selected US and Alabama 
cname = 'US'
sname = 'Alabama'
sname = 'New York'

# you can get an array of deaths, confirmed, recovered country by country 
y1 = getcountrydata(deathsGlobal,cname)
y2 = getcountrydata(confirmedGlobal,cname)
y3 = getcountrydata(recoveredGlobal,cname)

# you can get array of deaths, confirmed, recovered for any state in the US
s1 = getstatedata(deathsUS,sname)
s2 = getstatedata(confirmedUS,sname)

'''
once you get the data arrays, you can process it anyway you want 
You can set the number of days to look at - present backwards 
so while the data arrays contain ALL of the data, you can choose to 
look at specific range
''' 
# you can get the size of the arrays (number of days for the data

ndaysmax = len(x)
print (ndaysmax)

# some of the data initially may be zero, so keep that in mind
      
ndays = 500

# plot the global and state data - on twin y axes - one y axis on each side 
# this displays the graph 
twinyplots(x,'Date',y1,'Deaths','r',y2,'Confirmed','b',ndays,cname)
twinyplots(x,'Date',s1,'Deaths','r',s2,'Confirmed','b',ndays,sname)

#sys.exit()

# take the log of the log - attempt at gompertz curves 
# in this case using deaths or confirmed data 

y1g = gompertz(y1[-ndays:])
y2g = gompertz(y2[-ndays:])
xg = x[-ndays+1:]

twinyplots(xg,'Date',y1g,'Deaths','r',y2g,'Confirmed','b',ndays,cname)

#sys.exit()

s1g = gompertz(s1[-ndays:])
s2g = gompertz(s2[-ndays:])
xg = x[-ndays+1:]

twinyplots(xg,'Date',s1g,'Deaths','r',s2g,'Confirmed','b',ndays,sname)
