
import wx
import wx.grid as gridlib

class PanelOne(wx.Panel):
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        st=wx.StaticText(self, label="Home Screen")
        st2=wx.StaticText(self, label="Choose super-medium in Medium tab in Menu")
        font = st.GetFont()
        font.PointSize += 5
        st.SetFont(font)
        font = st2.GetFont()
        font.PointSize += 3
        st2.SetFont(font)

        Sizer = wx.BoxSizer(wx.VERTICAL)
        Sizer.Add(st, 0, wx.ALIGN_CENTER|wx.ALL, 15)
        Sizer.Add(st2, 0, wx.ALIGN_CENTER|wx.ALL, 15)
 
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
    resetter=None
    txt=""
    buttonArr=[]
    counter=0
    def __init__(self, parent):
        wx.Panel.__init__(self, parent=parent)
        st=wx.StaticText(self, label="Visual Mediums\n")
        font = st.GetFont()
        font.PointSize += 5
        st.SetFont(font)
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
        PanelThree.resetter = wx.Button(self, label="Reset",size=(100,30))
        PanelThree.resetter.Bind(wx.EVT_BUTTON, self.Reset)
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
        Sizer.Add(PanelThree.resetter, 0, wx.ALIGN_CENTER|wx.ALL, 15)

        self.SetSizerAndFit(Sizer)
    def GetMediumResponse(self, event=None):
        dlg = GetData1(parent = self)  
        dlg.ShowModal
        print(dlg.ShowModal())
        PanelThree.txt=(dlg.result_name)
        print(PanelThree.txt)
        if (dlg.result_name): 
            self.MediumButtonSetup()
        dlg.Destroy()
    def MediumButtonSetup(self,event=None):
        #make reset button functionality
        PanelThree.buttonArr = [self.newMedium1, self.newMedium2, self.newMedium3, self.newMedium4, self.newMedium5,self.newMedium6, self.newMedium7, self.newMedium8,self.newMedium9,self.newMedium10]        
        PanelThree.buttonArr[PanelThree.counter].SetLabelText(PanelThree.txt)
        PanelThree.newMedium1.Bind(wx.EVT_BUTTON, self.MediumOpener())
        if PanelThree.counter<9:
            PanelThree.counter+=1
        
    def MediumOpener(self, event=None):
        #make panel switch to the specific medium panel
        pass
    def Reset(self, event=None):
        #open new window to choose which button to reset
        pass

class GetData1(wx.Dialog):
    def __init__(self, parent):
        wx.Dialog.__init__(self, parent, wx.ID_ANY, "Medium Inputter", size= (800,220))
        self.panel = wx.Panel(self,wx.ID_ANY)

        self.lblname = wx.StaticText(self.panel, label="Name of medium:", pos=(20,20))
        self.name = wx.TextCtrl(self.panel, value="", pos=(120,18), size=(500,-1))
        self.lblsur = wx.StaticText(self.panel, label="Description of medium:", pos=(20,60))
        self.surname = wx.TextCtrl(self.panel, value="", pos=(148,58), size=(500,-1))
        self.saveButton =wx.Button(self.panel, label="Save", pos=(110,120))
        self.closeButton =wx.Button(self.panel, label="Cancel", pos=(210,120))
        self.saveButton.Bind(wx.EVT_BUTTON, self.SaveConnString)
        self.closeButton.Bind(wx.EVT_BUTTON, self.OnQuit)
        self.Bind(wx.EVT_CLOSE, self.OnQuit)
        self.Show()

    def OnQuit(self, event):
        self.result_name = None
        self.Destroy()

    def SaveConnString(self, event):
        self.result_name = self.name.GetValue()
        self.result_surname = self.surname.GetValue()
        self.Destroy()
class PanelFavorites(wx.Panel):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        st=wx.StaticText(self, label="Favorites")
        font = st.GetFont()
        font.PointSize += 5
        st.SetFont(font)

        self.btn = wx.Button(self, -1, "Go back home")

        Sizer = wx.BoxSizer(wx.VERTICAL)
        Sizer.Add(st, 0, wx.ALIGN_CENTER|wx.ALL, 15)
        Sizer.Add(self.btn, 0, wx.ALIGN_CENTER|wx.ALL, 15)

        
        self.SetSizerAndFit(Sizer)
class PanelDiary(wx.Panel):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        st=wx.StaticText(self, label="Diary")
        font = st.GetFont()
        font.PointSize += 5
        st.SetFont(font)

        self.btn = wx.Button(self, -1, "Go back home")

        Sizer = wx.BoxSizer(wx.VERTICAL)
        Sizer.Add(st, 0, wx.ALIGN_CENTER|wx.ALL, 15)
        Sizer.Add(self.btn, 0, wx.ALIGN_CENTER|wx.ALL, 15)
        
        self.SetSizerAndFit(Sizer)
class PanelSort(wx.Panel):
    
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        st=wx.StaticText(self, label="Sort")
        font = st.GetFont()
        font.PointSize += 5
        st.SetFont(font)

        self.btn = wx.Button(self, -1, "Go back home")

        Sizer = wx.BoxSizer(wx.VERTICAL)
        Sizer.Add(st, 0, wx.ALIGN_CENTER|wx.ALL, 15)
        Sizer.Add(self.btn, 0, wx.ALIGN_CENTER|wx.ALL, 15)
        
        self.SetSizerAndFit(Sizer)
class PanelVerbal1(wx.Panel):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        st=wx.StaticText(self, label="PanelVerbal1")
        font = st.GetFont()
        font.PointSize += 5
        st.SetFont(font)

        self.btn = wx.Button(self, -1, "Go back to Verbal mediums selection", (345, 100))

        Sizer = wx.BoxSizer(wx.VERTICAL)
        Sizer.Add(st, 0, wx.ALIGN_CENTER|wx.ALL, 15)
        Sizer.Add(PanelVerbal1.btn, 0, wx.ALIGN_CENTER|wx.ALL, 15)
        
        self.SetSizerAndFit(Sizer)
class PanelVerbal2(wx.Panel):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        st=wx.StaticText(self, label="PanelVerbal2")
        font = st.GetFont()
        font.PointSize += 5
        st.SetFont(font)

        self.btn = wx.Button(self, -1, "Change panel", (345, 100))

        Sizer = wx.BoxSizer(wx.VERTICAL)
        Sizer.Add(st, 0, wx.ALIGN_CENTER|wx.ALL, 15)
        
        self.SetSizerAndFit(Sizer)
class PanelVerbal3(wx.Panel):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        st=wx.StaticText(self, label="PanelVerbal3")
        font = st.GetFont()
        font.PointSize += 5
        st.SetFont(font)

        Sizer = wx.BoxSizer(wx.VERTICAL)
        Sizer.Add(st, 0, wx.ALIGN_CENTER|wx.ALL, 15)
        
        self.SetSizerAndFit(Sizer)
class PanelVerbal4(wx.Panel):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        st=wx.StaticText(self, label="PanelVerbal4")
        font = st.GetFont()
        font.PointSize += 5
        st.SetFont(font)

        Sizer = wx.BoxSizer(wx.VERTICAL)
        Sizer.Add(st, 0, wx.ALIGN_CENTER|wx.ALL, 15)
        
        self.SetSizerAndFit(Sizer)
class PanelVerbal5(wx.Panel):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        st=wx.StaticText(self, label="PanelVerbal5")
        font = st.GetFont()
        font.PointSize += 5
        st.SetFont(font)

        Sizer = wx.BoxSizer(wx.VERTICAL)
        Sizer.Add(st, 0, wx.ALIGN_CENTER|wx.ALL, 15)
        
        self.SetSizerAndFit(Sizer)
class PanelVerbal6(wx.Panel):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        st=wx.StaticText(self, label="PanelVerbal6")
        font = st.GetFont()
        font.PointSize += 5
        st.SetFont(font)

        Sizer = wx.BoxSizer(wx.VERTICAL)
        Sizer.Add(st, 0, wx.ALIGN_CENTER|wx.ALL, 15)
        
        self.SetSizerAndFit(Sizer)
class PanelVerbal7(wx.Panel):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        st=wx.StaticText(self, label="PanelVerbal7")
        font = st.GetFont()
        font.PointSize += 5
        st.SetFont(font)

        Sizer = wx.BoxSizer(wx.VERTICAL)
        Sizer.Add(st, 0, wx.ALIGN_CENTER|wx.ALL, 15)
        
        self.SetSizerAndFit(Sizer)
class PanelVerbal8(wx.Panel):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        st=wx.StaticText(self, label="PanelVerbal8")
        font = st.GetFont()
        font.PointSize += 5
        st.SetFont(font)

        Sizer = wx.BoxSizer(wx.VERTICAL)
        Sizer.Add(st, 0, wx.ALIGN_CENTER|wx.ALL, 15)
        
        self.SetSizerAndFit(Sizer)
class PanelVerbal9(wx.Panel):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        st=wx.StaticText(self, label="PanelVerbal9")
        font = st.GetFont()
        font.PointSize += 5
        st.SetFont(font)

        Sizer = wx.BoxSizer(wx.VERTICAL)
        Sizer.Add(st, 0, wx.ALIGN_CENTER|wx.ALL, 15)
        
        self.SetSizerAndFit(Sizer)
class PanelVerbal10(wx.Panel):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        st=wx.StaticText(self, label="PanelVerbal10")
        font = st.GetFont()
        font.PointSize += 5
        st.SetFont(font)

        Sizer = wx.BoxSizer(wx.VERTICAL)
        Sizer.Add(st, 0, wx.ALIGN_CENTER|wx.ALL, 15)
        
        self.SetSizerAndFit(Sizer)
class PanelVisual1(wx.Panel):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        st=wx.StaticText(self, label="PanelVisual1")
        font = st.GetFont()
        font.PointSize += 5
        st.SetFont(font)

        Sizer = wx.BoxSizer(wx.VERTICAL)
        Sizer.Add(st, 0, wx.ALIGN_CENTER|wx.ALL, 15)
        
        self.SetSizerAndFit(Sizer)
class PanelVisual2(wx.Panel):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        st=wx.StaticText(self, label="PanelVisual2")
        font = st.GetFont()
        font.PointSize += 5
        st.SetFont(font)

        Sizer = wx.BoxSizer(wx.VERTICAL)
        Sizer.Add(st, 0, wx.ALIGN_CENTER|wx.ALL, 15)
        
        self.SetSizerAndFit(Sizer)
class PanelVisuall3(wx.Panel):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        st=wx.StaticText(self, label="PanelVisual3")
        font = st.GetFont()
        font.PointSize += 5
        st.SetFont(font)

        Sizer = wx.BoxSizer(wx.VERTICAL)
        Sizer.Add(st, 0, wx.ALIGN_CENTER|wx.ALL, 15)
        
        self.SetSizerAndFit(Sizer)
class PanelVisuall4(wx.Panel):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        st=wx.StaticText(self, label="PanelVisual4")
        font = st.GetFont()
        font.PointSize += 5
        st.SetFont(font)

        Sizer = wx.BoxSizer(wx.VERTICAL)
        Sizer.Add(st, 0, wx.ALIGN_CENTER|wx.ALL, 15)
        
        self.SetSizerAndFit(Sizer)
class PanelVisuall5(wx.Panel):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        st=wx.StaticText(self, label="PanelVisual5")
        font = st.GetFont()
        font.PointSize += 5
        st.SetFont(font)

        Sizer = wx.BoxSizer(wx.VERTICAL)
        Sizer.Add(st, 0, wx.ALIGN_CENTER|wx.ALL, 15)
        
        self.SetSizerAndFit(Sizer)
class PanelVisuall6(wx.Panel):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        st=wx.StaticText(self, label="PanelVisual6")
        font = st.GetFont()
        font.PointSize += 5
        st.SetFont(font)

        Sizer = wx.BoxSizer(wx.VERTICAL)
        Sizer.Add(st, 0, wx.ALIGN_CENTER|wx.ALL, 15)
        
        self.SetSizerAndFit(Sizer)
class PanelVisuall7(wx.Panel):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        st=wx.StaticText(self, label="PanelVisual7")
        font = st.GetFont()
        font.PointSize += 5
        st.SetFont(font)

        Sizer = wx.BoxSizer(wx.VERTICAL)
        Sizer.Add(st, 0, wx.ALIGN_CENTER|wx.ALL, 15)
        
        self.SetSizerAndFit(Sizer)
class PanelVisuall8(wx.Panel):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        st=wx.StaticText(self, label="PanelVisual8")
        font = st.GetFont()
        font.PointSize += 5
        st.SetFont(font)

        Sizer = wx.BoxSizer(wx.VERTICAL)
        Sizer.Add(st, 0, wx.ALIGN_CENTER|wx.ALL, 15)
        
        self.SetSizerAndFit(Sizer)
class PanelVisuall9(wx.Panel):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        st=wx.StaticText(self, label="PanelVisual9")
        font = st.GetFont()
        font.PointSize += 5
        st.SetFont(font)

        Sizer = wx.BoxSizer(wx.VERTICAL)
        Sizer.Add(st, 0, wx.ALIGN_CENTER|wx.ALL, 15)
        
        self.SetSizerAndFit(Sizer)
class PanelVisuall10(wx.Panel):
    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)
        st=wx.StaticText(self, label="PanelVisual10")
        font = st.GetFont()
        font.PointSize += 5
        st.SetFont(font)

        Sizer = wx.BoxSizer(wx.VERTICAL)
        Sizer.Add(st, 0, wx.ALIGN_CENTER|wx.ALL, 15)
        
        self.SetSizerAndFit(Sizer)
class MyForm(wx.Frame):

    def __init__(self, *args, **kwargs):
        wx.Frame.__init__(self, *args, **kwargs)

        self.panel_one = PanelOne(self)
        self.panel_two = PanelTwo(self)
        self.panel_three = PanelThree(self)
        self.panel_four = PanelFavorites(self)
        self.panel_five = PanelDiary(self)
        self.panel_six = PanelSort(self)
        self.panel_two.Hide()
        self.panel_three.Hide()
        self.panel_four.Hide()
        self.panel_five.Hide()
        self.panel_six.Hide()

        self.panel_four.btn.Bind(wx.EVT_BUTTON, self.Home)
        self.panel_five.btn.Bind(wx.EVT_BUTTON, self.Home)
        self.panel_six.btn.Bind(wx.EVT_BUTTON, self.Home)

        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.sizer.Add(self.panel_one, 1, wx.EXPAND)
        self.sizer.Add(self.panel_two, 1, wx.EXPAND)
        self.sizer.Add(self.panel_three, 1, wx.EXPAND)
        self.sizer.Add(self.panel_four, 1, wx.EXPAND)
        self.sizer.Add(self.panel_five, 1, wx.EXPAND)
        self.sizer.Add(self.panel_six, 1, wx.EXPAND)
        self.SetSizer(self.sizer)

        menubar = wx.MenuBar()
        fileMenu = wx.Menu()
        mediumMenu = wx.Menu()
        panelsMenu = wx.Menu()
        switch_panels_menu_home = mediumMenu.Append(wx.ID_ANY, 
                                                  "Home Screen", 
                                                  "Some text")
        switch_panels_menu_verbal = mediumMenu.Append(wx.ID_ANY, 
                                                  "Verbal Mediums", 
                                                  "Some text")
        switch_panels_menu_visual = mediumMenu.Append(wx.ID_ANY, 
                                                  "Visual Mediums", 
                                                  "Some text")
        switch_panels_panels_favorites = panelsMenu.Append(wx.ID_ANY, 
                                                  "Favorites", 
                                                  "Some text")
        switch_panels_panels_diary = panelsMenu.Append(wx.ID_ANY, 
                                                  "Diary", 
                                                  "Some text")
        switch_panels_panels_sort = panelsMenu.Append(wx.ID_ANY, 
                                                  "Sort", 
                                                  "Some text")
        self.Bind(wx.EVT_MENU, self.Home, 
                  switch_panels_menu_home)
        self.Bind(wx.EVT_MENU, self.Verbal, 
                  switch_panels_menu_verbal)
        self.Bind(wx.EVT_MENU, self.Visual, 
                  switch_panels_menu_visual)
        self.Bind(wx.EVT_MENU, self.Favorites, 
                  switch_panels_panels_favorites)
        self.Bind(wx.EVT_MENU, self.Diary, 
                  switch_panels_panels_diary)
        self.Bind(wx.EVT_MENU, self.Sort, 
                  switch_panels_panels_sort)
        menubar.Append(fileMenu, '&File')
        menubar.Append(mediumMenu, '&Medium')
        menubar.Append(panelsMenu, '&Panels')
        self.SetMenuBar(menubar)

    #----------------------------------------------------------------------
    def Home(self, event):
        self.panel_one.Show()
        self.panel_two.Hide()
        self.panel_three.Hide()
        self.panel_four.Hide()
        self.panel_five.Hide()
        self.panel_six.Hide()
        self.Layout()
    def Verbal(self, event):
        self.panel_one.Hide()
        self.panel_two.Show()
        self.panel_three.Hide()
        self.panel_four.Hide()
        self.panel_five.Hide()
        self.panel_six.Hide()
        self.Layout()
    def Visual(self, event):
        self.panel_one.Hide()
        self.panel_two.Hide()
        self.panel_three.Show()
        self.panel_four.Hide()
        self.panel_five.Hide()
        self.panel_six.Hide()
        self.Layout()
    def Favorites(self, event):
        self.panel_one.Hide()
        self.panel_two.Hide()
        self.panel_three.Hide()
        self.panel_four.Show()
        self.panel_five.Hide()
        self.panel_six.Hide()
        self.Layout()
    def Diary(self, event):
        self.panel_one.Hide()
        self.panel_two.Hide()
        self.panel_three.Hide()
        self.panel_four.Hide()
        self.panel_five.Show()
        self.panel_six.Hide()
        self.Layout()
    def Sort(self, event):
        self.panel_one.Hide()
        self.panel_two.Hide()
        self.panel_three.Hide()
        self.panel_four.Hide()
        self.panel_five.Hide()
        self.panel_six.Show()
        self.Layout()
    def MediumButtonBinding(self, btn, num, v, event=None):
        pass

# Run the program
if __name__ == "__main__":
    app = wx.App(False)
    frame = MyForm(None, title="Media Database")
    wx.Window.SetInitialSize(frame, size=(1300,800))
    frame.Show()
    app.MainLoop()
