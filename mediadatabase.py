import wx 

class DemoPanel(wx.Panel):
    def __init__(self, parent, *args, **kwargs):
        wx.Panel.__init__(self, parent, *args, **kwargs)
 
        self.parent = parent
 
        VerbalButton = wx.Button(self, label="Verbal Mediums",size=(100,100))
        VerbalButton.Bind(wx.EVT_BUTTON, self.OnMsgBtn )
 
        VisualButton = wx.Button(self, label="Visual Mediums",size=(100,100))
        VisualButton.Bind(wx.EVT_BUTTON, self.OnMsgBtn )
 
        Sizer = wx.BoxSizer(wx.VERTICAL)
        Sizer.Add(VerbalButton, 0, wx.ALIGN_CENTER|wx.ALL, 25)
        Sizer.Add(VisualButton, 0, wx.ALIGN_CENTER|wx.ALL, 25)
 
        self.SetSizerAndFit(Sizer)
 
    def OnMsgBtn(self, event=None):
        """Bring up a wx.MessageDialog with a useless message."""
        dlg = wx.MessageDialog(self,
                                message='A completely useless message',
                                caption='A Message Box',
                                style=wx.OK|wx.ICON_INFORMATION
                                )
        dlg.ShowModal()
        dlg.Destroy()
 
class DemoFrame(wx.Frame):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
 
        # Build the menu bar
        MenuBar = wx.MenuBar()
 
        FileMenu = wx.Menu()
 
        #item = FileMenu.Append(wx.ID_EXIT, text="Quit")
        #self.Bind(wx.EVT_MENU, self.OnQuit, item)
 
        MenuBar.Append(FileMenu, "File")
        self.SetMenuBar(MenuBar)
 
        # Add the Widget Panel
        self.Panel = DemoPanel(self)
 
        self.Fit()
 
    def OnQuit(self, event=None):
        """Exit application."""
        self.Close()
 
if __name__ == '__main__':
    app = wx.App()
    frame = DemoFrame(None, title="Media Database")
    wx.Window.SetInitialSize(frame, size=(300,500))
    frame.Show()
    app.MainLoop()
