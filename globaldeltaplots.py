#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Apr 20 11:56:41 2020

@author: kchittur
"""

# import all of the functions, procedures
from jhu_github_analysis_functions import *
import sys
import os, glob, sys
import natsort

# there are three main data sets - deaths, confirmed and recovered 
# the recovered set seems iffy, buggy 
jhudatasetnames = [deathsGlobal,confirmedGlobal,recoveredGlobal]
jhudatasettitles = ['deaths','confirmed','recovered']

# you can get all of the countrynames using any one of the data sets 
allcountrynames = getlistofcountries(jhudatasetnames[0])

# you can choose to examine specific number of days from present - back
ndays = 578 

# creating twin y plots 
# in this case, deaths and confirmed on the same plot 
filename1 = deathsGlobal
filename2 = confirmedGlobal

prefix = 'B'

for i in range(len(allcountrynames)):
    cname = allcountrynames[i]
    x = getdates(filename2)
    y1 = getdelta(filename1,ndays,cname)
    y2 = getdelta(filename2,ndays,cname)
    outputname = prefix+cname+'.png'
    createtwinyplots(x,'Date',y1,'(daily difference) Deaths','r',y2,'(daily difference) Confirmed','b',ndays,outputname,cname)

#sys.exit()

# if you want, you can create mp4 files from the png files 
# create text slides that explain what the png files are
# here we have three sets of png files - 
# deaths, confirmed and recovered 
# specify the information for the slide, create the slide 
    
xpos = [1,1,1,1,1,1,1,1]
ypos = [9,8,7,6,5,4,3,2]
site = r'{https://github.com/CSSEGISandData/COVID-19}'
dset1 = r'{time\_series\_covid19\_deaths\_global.csv}'
dset2 = r'{time\_series\_covid19\_confirmed\_global.csv}'
cname='several countries'
info1 = 'The next few images will show '
info2 = 'the daily difference in deaths and confirmed cases in '
info3 = 'several countries (7 day smoothing) '
info4 = 'From the Hopkins Data set Named'
info5 = 'you can find it here'
thetexts = [info1,info2,info3,info4,dset1,dset2,info5,site]
slidename = 'Atextslide.png'   

createtextslide(thetexts,xpos,ypos,slidename)

# now assemble the png files into one mp4 

Xpngfiles = []
Xpngfiles.append('Atextslide.png')
for file in glob.glob("B*.png"):
    Xpngfiles.append(file)
pngfiles = natsort.natsorted(Xpngfiles)
createvideofile(pngfiles,0.2,'MP4V','differenceglobaldeathsandconfirmed.mp4')

sys.exit()
