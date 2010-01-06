#!/bin/env python
#----------------------------------------------------------------------------
# Name:         menu.py
# Author:       XXXX
# Created:      XX/XX/XX
# Copyright:    
#----------------------------------------------------------------------------

import wx

from menu_wdr import *


# WDR: classes

class MyFrame(wx.Frame):
    def __init__(self, parent, id, title,
        pos = wx.DefaultPosition, size = wx.DefaultSize,
        style = wx.DEFAULT_FRAME_STYLE ):
        wx.Frame.__init__(self, parent, id, title, pos, size, style)
        
        self.CreateMyMenuBar()
        
        self.CreateStatusBar(1)
        self.SetStatusText("Welcome!")
        
        # insert main window here
        
        # WDR: handler declarations for MyFrame
        wx.EVT_UPDATE_UI(self, ID_TEST3, self.OnUpdateTest3)
        wx.EVT_MENU_HIGHLIGHT(self, ID_TEST2, self.OnHightlightTest2)
        wx.EVT_MENU(self, ID_TEST1, self.OnTest1)
        wx.EVT_MENU(self, wx.ID_ABOUT, self.OnAbout)
        wx.EVT_MENU(self, wx.ID_EXIT, self.OnQuit)
        wx.EVT_CLOSE(self, self.OnCloseWindow)
        
    # WDR: methods for MyFrame
    
    def CreateMyMenuBar(self):
        self.SetMenuBar( MyMenuBarFunc() )
    
    # WDR: handler implementations for MyFrame
    
    def OnUpdateTest3(self, event):
        event.Enable( False );

    def OnHightlightTest2(self, event):
        self.SetStatusText( "Test 2 hightlighted !!" )

    def OnAbout(self, event):
        dialog = wx.MessageDialog(self, "Welcome to SuperApp 1.0\n(C)opyright Joe Hacker",
            "About SuperApp", wx.OK|wx.ICON_INFORMATION )
        dialog.CentreOnParent()
        dialog.ShowModal()
    
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

