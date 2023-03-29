##########################################
# MLX90640 Thermal Camera w Raspberry Pi
# -- 2Hz Sampling with Simple Routine
##########################################
#
import time,board,busio
import numpy as np
import adafruit_mlx90640
import matplotlib.pyplot as plt

#scd30 is the C02 detector that is still in development
#import adafruit_scd30

i2c = busio.I2C(board.SCL, board.SDA, frequency=400000) # setup I2C

mlx_shape = (24,32)

def camera_setup():
    mlx = adafruit_mlx90640.MLX90640(i2c, 0x33) # begin MLX90640 with I2C comm
    mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_8_HZ # set refresh rate
mlx = adafruit_mlx90640.MLX90640(i2c, 0x33) # begin MLX90640 with I2C comm
mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_8_HZ # set refresh rate

# setup the figure for plotting
plt.ion() # enables interactive plotting
fig,ax = plt.subplots(figsize=(12,7))
therm1 = ax.imshow(np.zeros(mlx_shape),vmin=0,vmax=60) #start plot with zeros
cbar = fig.colorbar(therm1) # setup colorbar for temps
cbar.set_label('Temperature [$^{\circ}$C]',fontsize=14) # colorbar label
frame = np.zeros((24*32,)) # setup array for storing all 768 temperatures
t_array = []
n=0
t1 = time.monotonic()

#scd30 is the C02 detector that is still in development
#scd=adafruit_scd30.SCD30(i2c, ambient_pressure = 0, address = 0x61)

while True:

    #camera_setuptry:
    try:
        mlx.getFrame(frame) # read MLX temperatures into frame var
    except:
        mlx = adafruit_mlx90640.MLX90640(i2c, 0x33) # begin MLX90640 with I2C comm
        mlx.refresh_rate = adafruit_mlx90640.RefreshRate.REFRESH_8_HZ # set refresh rate
        mlx.getFrame(frame)
    try:
        data_array = (np.reshape(frame,mlx_shape)) # reshape to 24x32
        therm1.set_data(np.fliplr(data_array)) # flip left to right
        therm1.set_clim(vmin=np.min(data_array),vmax=np.max(data_array)) # set bounds
        #cbar.on_mappable_changed(therm1) # update colorbar range
        plt.pause(0.001) # required

        #this is attempt to just make one huge array that doesn't really work
        #y = np.loadtxt("/home/pi/Desktop/ThermalCam/thermolistzeros.csv", delimiter=',', unpack=True)
        #print(y)
        #y=np.append(y, data_array, axis=0)
        #np.savetxt("/home/pi/Desktop/ThermalCam/thermolistzeros.csv",data_array, delimiter=",")

        # save the arrays
        np.savetxt("/home/pi/Desktop/ThermalCam/thermo" + str(n) + ".csv",data_array, delimiter=",")

        #unhash this to save the figures, but you can also use the assembler script to convert the arrays saved above to figures later
        #fig.savefig("mlx90640_test_fliplr" + str(n) + ".png",dpi=300,facecolor='#FCFCFC',
        #            bbox_inches='tight') # comment out to speed up

        #scd30 is the C02 detector that is still in development
        #SCD30 info adding to lists
        #print("CO2:", scd.CO2)
        #print("Temp:", scd.temperature)
        #print("Humidity:", scd.relative_humidity)
        #DAT = [scd.CO2]
        #DAT = [scd.temperature, scd.CO2, scd.relative_humidity]
        #unhash this to save the scd arrays
        #np.savetxt("/home/pi/Desktop/SCD/read" + str(n) + ".csv",DAT, delimiter=",")

        n +=1
        t_array.append(time.monotonic()-t1)
        print('Sample Rate: {0:2.1f}fps'.format(len(t_array)/np.sum(t_array)))
    except ValueError:
        camera_setup()
        continue # if error, just read again
