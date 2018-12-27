import wx

def slider_value_change(event):
    obj = event.GetEventObject()
    frame.SetStatusText('Slider value is ' + str(obj.GetValue()))

application = wx.App()
frame = wx.Frame(None, wx.ID_ANY, 'test', size=(300, 200))
frame.CreateStatusBar()
panel = wx.Panel(frame, wx.ID_ANY)
panel.SetBackgroundColour('#AFAFAF')


slider1 = wx.Slider(panel, style=wx.SL_LABELS)
slider2 = wx.Slider(panel, style=wx.SL_LABELS)
slider3 = wx.Slider(panel, style=wx.SL_LABELS)

sltx1  = wx.StaticText(panel, -1, 'Slider1',pos=(10, 50))
sltx2  = wx.StaticText(panel, -1, 'Slider2',pos=(10, 50))
sltx3  = wx.StaticText(panel, -1, 'Slider3',pos=(10, 50))

slider1.SetValue(0)
slider2.SetValue(0)
slider3.SetValue(0)

#print(slider1.GetValue())
 
layout = wx.BoxSizer(wx.VERTICAL)
layout.Add(sltx1)
layout.Add(slider1, flag=wx.GROW)
layout.Add(sltx2)
layout.Add(slider2, flag=wx.GROW)
layout.Add(sltx3)
layout.Add(slider3, flag=wx.GROW)

slider1.Bind(wx.EVT_SLIDER, slider_value_change)
slider2.Bind(wx.EVT_SLIDER, slider_value_change)
slider3.Bind(wx.EVT_SLIDER, slider_value_change)

panel.SetSizer(layout)
 
frame.Show()
application.MainLoop()