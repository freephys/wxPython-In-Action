#!/bin/env python
#----------------------------------------------------------------------------
# Name:         toolbar.py
# Author:       XXXX
# Created:      XX/XX/XX
# Copyright:    
#----------------------------------------------------------------------------

import wx

from toolbar_wdr import *


# WDR: classes

class MyFrame(wx.Frame):
    def __init__(self, parent, id, title,
        pos = wx.DefaultPosition, size = wx.DefaultSize,
        style = wx.DEFAULT_FRAME_STYLE ):
        wx.Frame.__init__(self, parent, id, title, pos, size, style)
        
        self.CreateMyMenuBar()
        
        self.CreateMyToolBar()
        
        self.CreateStatusBar(1)
        self.SetStatusText("Welcome!")
        
        # insert main window here
        
        # WDR: handler declarations for MyFrame
        wx.EVT_MENU(self, wx.ID_ABOUT, self.OnAbout)
        wx.EVT_MENU(self, wx.ID_EXIT, self.OnQuit)
        wx.EVT_CLOSE(self, self.OnCloseWindow)
        
    # WDR: methods for MyFrame
    
    def CreateMyMenuBar(self):
        self.SetMenuBar( MyMenuBarFunc() )
    
    def CreateMyToolBar(self):
        tb = self.CreateToolBar(wx.TB_HORIZONTAL|wx.NO_BORDER)
        MyToolBarFunc( tb )
    
    # WDR: handler implementations for MyFrame
    
    def OnAbout(self, event):
        dialog = wx.MessageDialog(self, "Welcome to SuperApp 1.0\n(C)opyright Joe Hacker",
            "About SuperApp", wx.OK|wx.ICON_INFORMATION )
        dialog.CentreOnParent()
        dialog.ShowModal()
        dialog.Destroy()
    
    def OnQuit(self, event):
        self.Close(True)
    
    def OnCloseWindow(self, event):
        self.Destroy()
    

#----------------------------------------------------------------------------

class MyApp(wx.App):
    
    def OnInit(self):   
        wx.InitAllImageHandlers()
        frame = MyFrame(None, -1, "SuperApp", [20,20], [500,340])
        frame.Show(True)
        return True

#----------------------------------------------------------------------------

app = MyApp(True)
app.MainLoop()

