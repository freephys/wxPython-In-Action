#!/bin/env python
#----------------------------------------------------------------------------
# Name:         events.py
# Author:       XXXX
# Created:      XX/XX/XX
# Copyright:    
#----------------------------------------------------------------------------

import wx
from events_wdr import *

# constants

ID_ABOUT = 100
ID_QUIT = 101
ID_TEST = 102

# WDR: classes

class MyDialog(wx.Dialog):
    def __init__(self, parent, id, title,
        pos = wx.DefaultPosition, size = wx.DefaultSize,
        style = wx.DEFAULT_DIALOG_STYLE ):
        wx.Dialog.__init__(self, parent, id, title, pos, size, style)
        
        # WDR: dialog function MyDialogFunc for MyDialog
        MyDialogFunc( self, True )
        
        self.CentreOnParent()
        
        # WDR: handler declarations for MyDialog
        wx.EVT_SLIDER(self, ID_SLIDER, self.OnSlider)

    # WDR: methods for MyDialog

    def GetGauge(self):
        return self.FindWindowById( ID_GAUGE )

    def GetSlider(self):
        return self.FindWindowById( ID_SLIDER )

    # WDR: handler implementations for MyDialog

    def OnSlider(self, event):
        self.GetGauge().SetValue( self.GetSlider().GetValue() )
        
        # self.GetGauge().SetValue( event.GetInt() )


class MyFrame(wx.Frame):
    def __init__(self, parent, id, title,
        pos = wx.DefaultPosition, size = wx.DefaultSize,
        style = wx.DEFAULT_FRAME_STYLE ):
        wx.Frame.__init__(self, parent, id, title, pos, size, style)
        
        self.CreateMyMenuBar()
        
        self.CreateStatusBar(1)
        self.SetStatusText("Welcome to Events!")
        
        # insert main window here
        
        # WDR: handler declarations for MyFrame
        wx.EVT_MENU(self, ID_ABOUT, self.OnAbout)
        wx.EVT_MENU(self, ID_QUIT, self.OnQuit)
        wx.EVT_MENU(self, ID_TEST, self.OnTest)
        wx.EVT_CLOSE(self, self.OnCloseWindow)
        
    # WDR: methods for MyFrame
    
    def CreateMyMenuBar(self):
        file_menu = wx.Menu()
        file_menu.Append(ID_ABOUT, "About...", "Program info")
        file_menu.Append(ID_TEST, "Test dialog...", "Test dialog")
        file_menu.Append(ID_QUIT, "Quit...", "Quit program")
        
        menu_bar = wx.MenuBar()
        menu_bar.Append(file_menu, "File")
        
        self.SetMenuBar(menu_bar)
    
    # WDR: handler implementations for MyFrame
    
    def OnAbout(self, event):
        dialog = wx.MessageDialog(self, "Welcome to Events\n(C)opyright 2000 Robert Roebling",
            "About Events", wx.OK|wx.ICON_INFORMATION )
        dialog.CentreOnParent()
        dialog.ShowModal()
    
    def OnTest(self, event):
        dialog = MyDialog(self, -1, "Events test" )
        dialog.ShowModal()
    
    def OnQuit(self, event):
        self.Close(true)
    
    def OnCloseWindow(self, event):
        self.Destroy()
    

#----------------------------------------------------------------------------

class MyApp(wx.App):
    
    def OnInit(self):
        frame = MyFrame(None, -1, "Events", [20,20], [500,340])
        frame.Show(True)
        return True

#----------------------------------------------------------------------------

app = MyApp(True)
app.MainLoop()

