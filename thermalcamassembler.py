#this will take a folder full of csv files from the ThermalCam python script and convert them into individual jpg files in a folder
#called ThermalCamPics on the desktop.  It will also extract the maximum and minimum values from each csv file and save them to two
#new csv files called Maxy and Miny on the desktop.
import time,board,busio
import numpy as np
import adafruit_mlx90640
import matplotlib.pyplot as plt
from PIL import Image as im
numberofpics = 12
#You need to enter the number of individual csv files that are in the target folder above as numberofpics
n=0
maxarray = np.array([0])
minarray = np.array([0])

#scd30 is the C02 detector that is still in development
#SCDTempdataarray = np.array([0])
#SCDCO2dataarray = np.array([0])
#SCDHumdataarray = np.array([0])
while True:

    #SCDarr = np.loadtxt("/home/pi/Desktop/SCD/read" + str(n) + ".csv",delimiter=",")
    arr = np.loadtxt("/home/pi/Desktop/All data from experiment 2/ThermalCam/thermo" + str(n) + ".csv",delimiter=",")
    #you need to make sure the loadtxt command above is aimed at the correct folder that contains all of the csv files.  To aim it, right
    #click on the ThermalCam folder and copy the file path, then paste this as a replacement for "/home/pi/Desktop/All data from experiment 2/ThermalCam"
    #print(arr)
    img = im.fromarray(arr.astype('uint8'), mode='L')
    maxy = np.max(arr)
    miny = np.min(arr)
    #scdy = np.max(SCDarr)
    print(n)
    #print(maxy)
    #print(miny)
    maxarray = np.append(maxarray,[maxy])
    minarray = np.append(minarray,[miny])
    #SCDCO2dataarray = np.append(SCDCO2dataarray,[scdy])
    if n == numberofpics-1:
        np.savetxt("/home/pi/Desktop/Maxy" ,maxarray, delimiter=",")
        np.savetxt("/home/pi/Desktop/Miny" ,minarray, delimiter=",")
        #np.savetxt("/home/pi/Desktop/CO2y" ,SCDCO2dataarray, delimiter=",")
    else:
        pass
    img.save('/home/pi/Desktop/ThermalCamPics/picture'+ str(n) + '.tif')

    n +=1
