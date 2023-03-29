# ThermalCam
# March 29, 2023
# Matt Lynes

# This is the set of scripts for ThermalCam system for non-invasively monitoring temperature in mice undergoing stress 
# at millisecond resolution.  I probably should have a good acronym for it, but I don't.

# Follow the instructions in reference 1 to hook up a MLX90640 Thermal Camera to a Raspberry Pi 4 2gb using a Stemma QT JST SH 4-pin Cable 
# with female sockets all purchased from Adafruit. 

# Use the ThermalCam (with array saving).py script to record .csv files to the desktop.

# Use the thermalcamassembler.py script to extract the mouse and ambient temperature from each .csv file and convert it into an image

# Use ImageJ to assemble the images into a video by opening them as an image sequence, converting them to a stack and saving them as an .avi file

# References
# 1. Hrisko, J. (2020). High Resolution Thermal Camera with Raspberry Pi and MLX90640. 
#    Maker Portal. https://makersportal.com/blog/2020/6/8/high-resolution-thermal-camera-with-raspberry-pi-and-mlx90640
# 2. 
#
# After the camera is hooked up to the Raspberry Pi and all of the required libraries are installed, 
