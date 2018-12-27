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
        super(GUI, self).__init__(None)
        # form GUI
        # Define 
        self.dmx = PyDMX(comport)

    def InitUI(self):

        pnl = wx.Panel(self)

        # Button1: Close and end 
        closeButton = wx.Button(pnl, label='Quit this program', pos=(20, 20))
        closeButton.Bind(wx.EVT_BUTTON, self.OnClose)

        # Button2: Send Signal 
        closeButton = wx.Button(pnl, label='Send Signal', pos=(120, 20))
        closeButton.Bind(wx.EVT_BUTTON, self.senddmx)


        self.SetSize((350, 250)) # define box size
        self.SetTitle('wx.Button')
        self.Centre()

    def OnClose(self, e):

        self.Close(True)

    def senddmx(self,e):
        print('send')


if __name__=='__main__':
    app = wx.App()
    txt = GUIinput()
    comport = txt.text

    ex = Controller(None)
    ex.Show()
    app.MainLoop()
    print('finish')
