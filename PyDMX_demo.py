import serial
import time
import numpy as np

#start serial
ser = serial.Serial('COM8',baudrate=250000,bytesize=8,stopbits=2)

# make data
data = np.zeros([513],dtype='uint8')
data[0] = 0 # StartCode

for i in range(1,60): # 3sec
    # Set Random Data
    data[1:513]= np.random.rand(512)*255
    
    # Send Break : 88us - 1s
    ser.break_condition = True
    time.sleep(176.0/1000000.0)
    
    # Send MAB : 8us - 1s
    ser.break_condition = False
    time.sleep(16.0/1000000.0)
    
    # Send Data
    ser.write(bytearray(data))
    
    # Sleep
    time.sleep(50.0/1000.0) # between 0 - 1 sec