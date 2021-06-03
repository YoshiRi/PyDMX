import serial
import time
import numpy as np


class PyDMX:
    def __init__(self,COM='COM8',Cnumber=512,Brate=250000,Bsize=8,StopB=2,use_prev_data=False,preserve_data_name="preserved_data.txt"):
        #start serial
        self.channel_num = Cnumber
        #self.ser = serial.Serial(COM,baudrate=Brate,bytesize=Bsize,stopbits=StopB)
        self.data = np.zeros([self.channel_num+1],dtype='uint8')
        self.data[0] = 0 # StartCode
        self.sleepms = 50.0
        self.breakus = 176.0
        self.MABus = 16.0
        # save filename
        self.preserve_data_name = preserve_data_name
        self.use_prev_data = use_prev_data
        # load preserved DMX data
        if use_prev_data:
            try:
                self.load_data()
            except:
                print("Something is wrong. please check data format!")
        
    def set_random_data(self):
        self.data[1:self.channel_num+1]= np.random.rand(self.channel_num)*255

    def set_data(self,id,data):
        self.data[id]=data

    def set_datalist(self,list_id,list_data):
        try:
            for id,data in zip(list_id,list_data):
                self.set_data(id,data)
        except:
            print('list of id and data must be the same size!')

    def send(self):
        # Send Break : 88us - 1s
        self.ser.break_condition = True
        time.sleep(self.breakus/1000000.0)
        
        # Send MAB : 8us - 1s
        self.ser.break_condition = False
        time.sleep(self.MABus/1000000.0)
        
        # Send Data
        self.ser.write(bytearray(self.data))
        
        # Sleep
        time.sleep(self.sleepms/1000.0) # between 0 - 1 sec

    def sendzero(self):
        self.data = np.zeros([self.channel_num+1],dtype='uint8')
        self.send()

    def load_data(self):
        self.data = np.loadtxt(self.preserve_data_name,dtype='int')        

    def preserve_data(self):
        np.savetxt(self.preserve_data_name,self.data)        

    def __del__(self):
        print('Close serial server!')
        # close with preserving current DMX data, I guess you may not need to reset DMX signal in this option.
        if self.use_prev_data:
            self.preserve_data()
        else:
            self.sendzero()
        self.ser.close()
    


if __name__ == '__main__':
    dmx = PyDMX('COM11')

    for i in range(0,10):
        dmx.set_random_data()
        dmx.send()
    
    del dmx
