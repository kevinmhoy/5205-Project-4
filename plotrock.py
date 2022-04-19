# -*- coding: utf-8 -*-
"""
Created on Mon Apr 18 16:42:30 2022

@author: kevin
"""

import matplotlib.pyplot as plt
import pandas as pd

#Open data files
berf = pd.read_csv("Filename_Radius_1.91.csv")
earth = pd.read_csv("Filename_Radius_1.00.csv")

#These'll hold the names of the columns of significant contribution
berfpop = []
earthpop = []

#Remove the pure iron core nobody cares about
berfmantle = berf[berf["Fe"] < 100]
earthmantle = earth[earth["Fe"] < 100]

#Select for minerals that represent a significant portion of the mantle
for i in range(8, 57):
    berfmax = 0
    earthmax = 0
    
    for j in berfmantle[berf.columns[i]]:
        if j > berfmax:
            berfmax = j
    for j in earthmantle[earth.columns[i]]:
        if j > earthmax:
            earthmax = j
        
    if berfmax >= 10:
        berfpop.append(berf.columns[i])
        
    if earthmax >= 10:
        earthpop.append(earth.columns[i])

#Normalize to total thickness of mantle
deep = berfmantle["Depth"].iloc[1] - berfmantle["Depth"].iloc[-1]
berfmantle["Depth"] = berfmantle["Depth"].apply(lambda x: x / deep)
deep = earthmantle["Depth"].iloc[1] - earthmantle["Depth"].iloc[-1]
earthmantle["Depth"] = earthmantle["Depth"].apply(lambda x: x / deep)

#Plot junk
plt.rcParams.update({"font.size": 20})

axberf = berfmantle.plot(x = "Depth", y = berfpop, kind = "line", figsize = (12,12))
axearth = earthmantle.plot(x = "Depth", y = earthpop, kind = "line", figsize = (11,11))
axearth.set_title("Earth Minerology")
axearth.set_xlim([0.0001, 1])
axearth.set_ylim([0, 80])
axearth.set_ylabel("Fractional Composition")
axberf.set_title("Berf Minerology")
axberf.set_xlabel("Mantle Depth Fraction")
axberf.set_xlim([0.0001, 1])
axberf.set_ylim([0, 80])
axberf.set_ylabel("Fractional Composition")

plt.rcParams.update({"font.size": 22})

axearth = earthmantle.plot(x = "Depth", y = earthpop, kind = "line", figsize = (15,15))
axearth.set_title("Earth Minerology")
axearth.set_xlim([0.0001, 0.3])
axearth.set_ylim([0, 80])
axearth.set_ylabel("Fractional Composition")

axberf = berfmantle.plot(x = "Depth", y = berfpop, kind = "line", figsize = (16,16))
axberf.set_title("Berf Minerology")
axberf.set_xlim([0.0001, 0.1])
axberf.set_ylim([0, 80])
axberf.set_xlabel("Mantle Depth Fraction")
axberf.set_ylabel("Fractional Composition")
