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
        self.frame.box = wx.TextCtrl(panel_ui, -1, pos=(10, 30))
        # button        
        btn = wx.Button(panel_ui, -1, 'OK', pos=(10, 60))
        btn.Bind(wx.EVT_BUTTON, self.Clicked)

        self.frame.Show(True)
    
    def Clicked(self,event):
        self.text = self.frame.box.GetValue()
        self.frame.Close(True)



class Controller(wx.Frame):

    def __init__(self,comport):
        #super(GUI, self).__init__(*args, **kw) #init using the definition of the super class
        super(Controller, self).__init__(None,-1,"Title",size=(300,400))
        # form GUI
        # Define 
        self.dmx = PyDMX(comport)
        self.InitUI()

    def InitUI(self):

        panel = wx.Panel(self, wx.ID_ANY)

        # statusbar
        self.CreateStatusBar()

        # sliders
        self.slider1 = wx.Slider(panel, style=wx.SL_LABELS, pos=(10, 30), maxValue=255)
        self.slider2 = wx.Slider(panel, style=wx.SL_LABELS, pos=(10, 100), maxValue=255)
        self.slider3 = wx.Slider(panel, style=wx.SL_LABELS, pos=(10, 170), maxValue=255)
        # text
        self.sltx1  = wx.StaticText(panel, -1, 'Red Slider', pos=(10, 10))
        self.sltx2  = wx.StaticText(panel, -1, 'Green Slider', pos=(10, 80))
        self.sltx3  = wx.StaticText(panel, -1, 'Blue Slider', pos=(10, 150))

        # Button1: Close and end 
        closeButton = wx.Button(panel, label='Quit this program',pos=(10,220))

        # BIND
        closeButton.Bind(wx.EVT_BUTTON, self.OnClose)
        self.slider1.Bind(wx.EVT_SLIDER, self.slider_value_change)
        self.slider2.Bind(wx.EVT_SLIDER, self.slider_value_change)
        self.slider3.Bind(wx.EVT_SLIDER, self.slider_value_change)


    def OnClose(self, e):
        del self.dmx
        self.Close(True)

    
    def slider_value_change(self,event):
        R = self.slider1.GetValue()
        G = self.slider2.GetValue()
        B = self.slider3.GetValue()
        self.dmx.set_data(1,R)
        self.dmx.set_data(2,G)
        self.dmx.set_data(3,B)
        self.dmx.send()
        self.SetStatusText('Slider value is ' + str(R)+ ', '+str(G)+ ', '+str(B))


if __name__=='__main__':
    app = wx.App()
    #txt = GUIinput()
    #app.MainLoop()
    #comport = txt.text

    ex = Controller('COM11')
    ex.Show()
    app.MainLoop()
    print('finish')
