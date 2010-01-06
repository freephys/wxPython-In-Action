#!/bin/env python
#----------------------------------------------------------------------------
# Name:         scrolled.py
# Author:       XXXX
# Created:      XX/XX/XX
# Copyright:    
#----------------------------------------------------------------------------

import wx

from scrolled_wdr import *


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

    # WDR: methods for MyDialog

    # WDR: handler implementations for MyDialog


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
        EVT_MENU(self, ID_SCROLLED, self.OnScrolled)
        EVT_MENU(self, ID_QUIT, self.OnQuit)
        EVT_CLOSE(self, self.OnCloseWindow)
        
    # WDR: methods for MyFrame
    
    def CreateMyMenuBar(self):
        self.SetMenuBar( MyMenuBarFunc() )
    
    # WDR: handler implementations for MyFrame
    
    def OnScrolled(self, event):
        dialog = MyDialog(self, -1, "Test MyScrolledWindow")
        dialog.ShowModal()
    
    def OnQuit(self, event):
        self.Close(True)
    
    def OnCloseWindow(self, event):
        self.Destroy()
    

#----------------------------------------------------------------------------

class MyApp(wx.App):
    
    def OnInit(self):
        frame = MyFrame(None, -1, "SuperApp", [20,20], [500,340])
        frame.Show(True)
        return True

#----------------------------------------------------------------------------

app = MyApp(True)
app.MainLoop()

