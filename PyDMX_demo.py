import serial
import time
import numpy as np

from PyDMX import *
import wx

class GUIinput:
    def __init__(self):
        self.frame = wx.Frame(None, -1, "textbox")
        self.frame.SetTitle('Write Text Here')
        panel_ui = wx.Panel(self.frame, -1, pos=(50, 50), size=(100, 50)) 

        # message
        self.frame.label = wx.StaticText(panel_ui, -1, 'Write your device: (example: "COM8" or "/dev/ttyUSB0")', pos=(10, 10))
        # text box
        self.frame.box = wx.TextCtrl(panel_ui, -1, pos=(10, 30),style=wx.TE_PROCESS_ENTER)
        # button        
        btn = wx.Button(panel_ui, -1, 'OK', pos=(10, 60))
        # Bind
        btn.Bind(wx.EVT_BUTTON, self.Clicked) # button
        self.frame.box.Bind(wx.EVT_TEXT_ENTER, self.Clicked) #text enter
        self.frame.Show(True)
    
    def Clicked(self,event):
        self.text = self.frame.box.GetValue()
        self.frame.Close(True)



class Controller(wx.Frame):

    def __init__(self,comport,federnum=3):
        #super(GUI, self).__init__(*args, **kw) #init using the definition of the super class
        super(Controller, self).__init__(None,-1,"Title",size=(300,600))
        # form GUI
        #self.dmx = PyDMX(comport)
        if federnum > 512:
            federnum = 511
        self.fnum = federnum
        self.InitUI()

    def make_position(self):
        self.sliderhei = 50
        self.txthei = 20
        self.inihei = 10

        self.hpos = []
        for i in range(self.fnum):
            # message
            base = self.inihei+i*(self.sliderhei+self.txthei)
            self.hpos.append((10,base))
            # slider
            self.hpos.append((10,base+self.txthei))
        # for button
        self.hpos.append((150,self.inihei))

    def InitUI(self):
        self.make_position()

        panel = wx.Panel(self, wx.ID_ANY)

        # statusbar
        self.CreateStatusBar()

        # sliders
        self.sliders = []
        self.sltxs = []

        for i in range(self.fnum):
            self.sltxs.append(wx.StaticText(panel, -1, 'DMX Address: '+str(i+1), pos=self.hpos[2*i]))
            self.sliders.append(wx.Slider(panel, style=wx.SL_LABELS, pos=self.hpos[2*i+1], maxValue=255))
            # bind
            self.sliders[i].Bind(wx.EVT_SLIDER, self.slider_value_change)
        # button
        closeButton = wx.Button(panel, label='Quit this program',pos=self.hpos[-1])
        closeButton.Bind(wx.EVT_BUTTON, self.OnClose)


    def OnClose(self, e):
        #del self.dmx
        self.Close(True)

    
    def slider_value_change(self,event):
        nums = []
        for i in range(self.fnum):
            nums.append( self.sliders[i].GetValue() )
            #self.dmx.set_data(i+1,nums[i])
        #self.dmx.send()
        #self.SetStatusText('Slider value is ' + str(R)+ ', '+str(G)+ ', '+str(B))
        print(nums)

if __name__=='__main__':
    import sys
    args = sys.argv

    try:
        federnum = int(args[1])
    except:
        federnum = 3

    print('Feder number is = '+ str(federnum))
    # init
    app = wx.App()
    # catch the input of device
    txt = GUIinput()
    app.MainLoop()
    comport = txt.text

    # feder
    ex = Controller(comport,federnum)
    ex.Show()
    app.MainLoop()
    print('finish')
