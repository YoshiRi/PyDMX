import serial
import time
import numpy as np

from PyDMX import *
import wx
import wx.lib.scrolledpanel as scrolled


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

    def __init__(self,comport, fadernum=3):
        #init using the definition of the super class
        super(Controller, self).__init__(None,-1,"DMX  fader",size=(300,600))
        #super(Controller, self).__init__(None)
        
        # form GUI
        #self.dmx = PyDMX(comport)
        if  fadernum > 512:
             fadernum = 511
        self.fnum =  fadernum
        self.InitUI()


    def InitUI(self):
        panel = scrolled.ScrolledPanel(self, wx.ID_ANY)
        panel.SetupScrolling()
        
        # statusbar
        #self.CreateStatusBar()

        # sliders
        self.sliders = []
        self.sltxs = []
        layout = wx.BoxSizer(wx.VERTICAL)

        for i in range(self.fnum):
            self.sltxs.append(wx.StaticText(panel, -1, 'DMX Address: '+str(i+1)))
            self.sliders.append(wx.Slider(panel, style=wx.SL_LABELS, maxValue=255))
            layout.Add(self.sltxs[i], 0, wx.EXPAND | wx.LEFT, 10)
            layout.Add(self.sliders[i], 0, wx.EXPAND | wx.LEFT, 10)
            layout.AddSpacer(5) 
            # bind
            self.sliders[i].Bind(wx.EVT_SLIDER, self.slider_value_change)
        # button
        closeButton = wx.Button(panel, label='Quit this program')
        layout.Add(closeButton)
        closeButton.Bind(wx.EVT_BUTTON, self.OnClose)

        panel.SetSizer(layout)
        # show after setup
        self.Show(True)


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
         fadernum = int(args[1])
    except:
         fadernum = 3

    print(' fader number is = '+ str( fadernum))
    # init
    app = wx.App()
    # catch the input of device
    txt = GUIinput()
    app.MainLoop()
    comport = txt.text

    #  fader
    ex = Controller(comport, fadernum)
    ex.Show()
    app.MainLoop()
    print('finish')
