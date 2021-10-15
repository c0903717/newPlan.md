import wx
import wx.grid as gridlib

class PanelOne(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        st=wx.StaticText(self, label="Home Screen\n\nChoose super-medium in Medium tab in Menu")
        font = st.GetFont()
        font.PointSize += 5
        st.SetFont(font)

        Sizer = wx.BoxSizer(wx.VERTICAL)
        Sizer.Add(st, 0, wx.ALIGN_CENTER|wx.ALL, 15)
 
        self.SetSizerAndFit(Sizer)
class PanelTwo(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        st=wx.StaticText(self, label="Verbal Mediums\n")
        font = st.GetFont()
        font.PointSize += 5
        st.SetFont(font)
        Sizer = wx.BoxSizer(wx.VERTICAL)
        Sizer.Add(st, 0, wx.ALIGN_CENTER|wx.ALL, 15)
 
        self.SetSizerAndFit(Sizer)
class PanelThree(wx.Panel):
    newMedium1=None
    newMedium2=None
    newMedium3=None
    newMedium4=None
    newMedium5=None
    newMedium6=None
    newMedium7=None
    newMedium8=None
    newMedium9=None
    newMedium10=None
    buttonArr=[]
    counter=0
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        st=wx.StaticText(self, label="Visual Mediums\n")
        font = st.GetFont()
        font.PointSize += 5
        st.SetFont(font)
        txt=""
        PanelThree.newMedium1 = wx.Button(self, label="+new",size=(100,30))
        PanelThree.newMedium1.Bind(wx.EVT_BUTTON, self.GetMediumResponse)
        PanelThree.newMedium2 = wx.Button(self, label="+new",size=(100,30))
        PanelThree.newMedium2.Bind(wx.EVT_BUTTON, self.GetMediumResponse)
        PanelThree.newMedium3 = wx.Button(self, label="+new",size=(100,30))
        PanelThree.newMedium3.Bind(wx.EVT_BUTTON, self.GetMediumResponse)
        PanelThree.newMedium4 = wx.Button(self, label="+new",size=(100,30))
        PanelThree.newMedium4.Bind(wx.EVT_BUTTON, self.GetMediumResponse)
        PanelThree.newMedium5 = wx.Button(self, label="+new",size=(100,30))
        PanelThree.newMedium5.Bind(wx.EVT_BUTTON, self.GetMediumResponse)
        PanelThree.newMedium6 = wx.Button(self, label="+new",size=(100,30))
        PanelThree.newMedium6.Bind(wx.EVT_BUTTON, self.GetMediumResponse)
        PanelThree.newMedium7 = wx.Button(self, label="+new",size=(100,30))
        PanelThree.newMedium7.Bind(wx.EVT_BUTTON, self.GetMediumResponse)
        PanelThree.newMedium8 = wx.Button(self, label="+new",size=(100,30))
        PanelThree.newMedium8.Bind(wx.EVT_BUTTON, self.GetMediumResponse)
        PanelThree.newMedium9 = wx.Button(self, label="+new",size=(100,30))
        PanelThree.newMedium9.Bind(wx.EVT_BUTTON, self.GetMediumResponse)
        PanelThree.newMedium10 = wx.Button(self, label="+new",size=(100,30))
        PanelThree.newMedium10.Bind(wx.EVT_BUTTON, self.GetMediumResponse)
        Sizer = wx.BoxSizer(wx.VERTICAL)
        Sizer.Add(st, 0, wx.ALIGN_CENTER|wx.ALL, 15)
        Sizer.Add(PanelThree.newMedium1, 0, wx.ALIGN_CENTER|wx.ALL, 15)
        Sizer.Add(PanelThree.newMedium2, 0, wx.ALIGN_CENTER|wx.ALL, 15)
        Sizer.Add(PanelThree.newMedium3, 0, wx.ALIGN_CENTER|wx.ALL, 15)
        Sizer.Add(PanelThree.newMedium4, 0, wx.ALIGN_CENTER|wx.ALL, 15)
        Sizer.Add(PanelThree.newMedium5, 0, wx.ALIGN_CENTER|wx.ALL, 15)
        Sizer.Add(PanelThree.newMedium6, 0, wx.ALIGN_CENTER|wx.ALL, 15)
        Sizer.Add(PanelThree.newMedium7, 0, wx.ALIGN_CENTER|wx.ALL, 15)
        Sizer.Add(PanelThree.newMedium8, 0, wx.ALIGN_CENTER|wx.ALL, 15)
        Sizer.Add(PanelThree.newMedium9, 0, wx.ALIGN_CENTER|wx.ALL, 15)
        Sizer.Add(PanelThree.newMedium10, 0, wx.ALIGN_CENTER|wx.ALL, 15)
 
        self.SetSizerAndFit(Sizer)
    def GetMediumResponse(self, event=None):
        dlg = wx.TextEntryDialog(self, 'Enter the name of the medium you want to add:',"Medium Inputter","", 
                style=wx.OK)
        dlg.ShowModal()
        PanelThree.txt=(dlg.GetValue())
        print(PanelThree.txt)
        self.MediumButtonSetup()
        dlg.Destroy()
    def MediumButtonSetup(self,event=None):
        #then add reset button next to button, and make reset button functionality
        PanelThree.buttonArr = [self.newMedium1, self.newMedium2, self.newMedium3, self.newMedium4, self.newMedium5,self.newMedium6, self.newMedium7, self.newMedium8,self.newMedium9,self.newMedium10]        
        PanelThree.buttonArr[PanelThree.counter].SetLabelText(PanelThree.txt)
        PanelThree.newMedium1.Bind(wx.EVT_BUTTON, self.MediumOpener())
        if PanelThree.counter<9:
            PanelThree.counter+=1
    def MediumOpener(self, event=None):
        #make panel switch to the specific medium panel
        pass
class MyForm(wx.Frame):

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
    wx.Window.SetInitialSize(frame, size=(1300,800))
    frame.Show()
    app.MainLoop()
