import wx
import wx.grid as gridlib

########################################################################
class PanelOne(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        st=wx.StaticText(self, label="Home Screen\n\nChoose super-medium in Medium tab in Menu")
        font = st.GetFont()
        font.PointSize += 5
        st.SetFont(font)

########################################################################
class PanelTwo(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        st=wx.StaticText(self, label="Verbal Mediums")
        font = st.GetFont()
        font.PointSize += 5
        st.SetFont(font)

########################################################################
class PanelThree(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        st=wx.StaticText(self, label="Visual Mediums")
        font = st.GetFont()
        font.PointSize += 5
        st.SetFont(font)

########################################################################
class MyForm(wx.Frame):

    #----------------------------------------------------------------------
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)

        self.panel_one = PanelOne(self)
        self.panel_two = PanelTwo(self)
        self.panel_three = PanelThree(self)
        self.panel_two.Hide()
        self.panel_three.Hide()

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.panel_one, 1, wx.EXPAND)
        self.sizer.Add(self.panel_two, 1, wx.EXPAND)
        self.sizer.Add(self.panel_three, 1, wx.EXPAND)
        self.SetSizer(self.sizer)

        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        mediumMenu = wx.Menu()
        switch_panels_menu_home = mediumMenu.Append(wx.ID_ANY, 
                                                  "Home Screen", 
                                                  "Some text")
        switch_panels_menu_verbal = mediumMenu.Append(wx.ID_ANY, 
                                                  "Verbal Mediums", 
                                                  "Some text")
        switch_panels_menu_visual = mediumMenu.Append(wx.ID_ANY, 
                                                  "Visual Mediums", 
                                                  "Some text")
        self.Bind(wx.EVT_MENU, self.Home, 
                  switch_panels_menu_home)
        self.Bind(wx.EVT_MENU, self.Verbal, 
                  switch_panels_menu_verbal)
        self.Bind(wx.EVT_MENU, self.Visual, 
                  switch_panels_menu_visual)
        menubar.Append(fileMenu, '&File')
        menubar.Append(mediumMenu, '&Medium')
        self.SetMenuBar(menubar)

    #----------------------------------------------------------------------
    def Home(self, event):
        self.panel_one.Show()
        self.panel_two.Hide()
        self.panel_three.Hide()
        self.Layout()
    def Verbal(self, event):
        self.panel_one.Hide()
        self.panel_two.Show()
        self.panel_three.Hide()
        self.Layout()
    def Visual(self, event):
        self.panel_one.Hide()
        self.panel_two.Hide()
        self.panel_three.Show()
        self.Layout()

# Run the program
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyForm(None, title="Media Database")
    wx.Window.SetInitialSize(frame, size=(600,500))
    frame.Show()
    app.MainLoop()
