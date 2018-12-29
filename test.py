import wx
import wx.lib.scrolledpanel as scrolled
 
 
class Main(wx.Frame):
 
    def __init__(self, parent, id, title):
        """ Layout """
 
        wx.Frame.__init__(self, parent, id, title)
        panel = scrolled.ScrolledPanel(self, wx.ID_ANY)
        panel.SetupScrolling()
 
        v_layout = wx.BoxSizer(wx.VERTICAL)
 
        for i in range(30):
            text = wx.StaticText(panel, wx.ID_ANY, str(i))
            v_layout.Add(text)
 
        panel.SetSizer(v_layout)
        self.Show(True)
 
 
def main():
    app = wx.App()
    Main(None, wx.ID_ANY, "Title")
    app.MainLoop()
 
if __name__ == "__main__":
    main()