#!/bin/env python
#----------------------------------------------------------------------------
# Name:         minimal.py
# Author:       XXXX
# Created:      XX/XX/XX
# Copyright:    
#----------------------------------------------------------------------------

import wx
from minimal_wdr import *

# constants

# WDR: classes

class MyFrame(wx.Frame):
    def __init__(self, parent, id, title,
        pos = wx.DefaultPosition, size = wx.DefaultSize,
        style = wx.DEFAULT_FRAME_STYLE ):
        wx.Frame.__init__(self, parent, id, title, pos, size, style)
        
        self.CreateMyMenuBar()
        
        self.CreateStatusBar(1)
        self.SetStatusText("Welcome to minimal!")
        
        # insert main window here
        
        # WDR: handler declarations for MyFrame
        wx.EVT_MENU(self, wx.ID_ABOUT, self.OnAbout)
        wx.EVT_MENU(self, wx.ID_EXIT, self.OnQuit)
        wx.EVT_CLOSE(self, self.OnCloseWindow)
        
    # WDR: methods for MyFrame
    
    def CreateMyMenuBar(self):
        file_menu = wx.Menu()
        file_menu.Append(wx.ID_EXIT, "&Quit...\tCtrl-Q", "Quit program")
        
        help_menu = wx.Menu()
        help_menu.Append(wx.ID_ABOUT, "&About...\tCtrl-A", "Program info")
        
        menu_bar = wx.MenuBar()
        menu_bar.Append(file_menu, "&File")
        menu_bar.Append(help_menu, "&Help")
        
        self.SetMenuBar(menu_bar)
    
    # WDR: handler implementations for MyFrame
    
    def OnAbout(self, event):
        dialog = wx.Dialog(self, -1, "About Minimal" )
        MyDialogFunc( dialog, True )
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
        frame = MyFrame(None, -1, "Minimal", [20,20], [500,340] )
        frame.Show(True)
        return True

#----------------------------------------------------------------------------

app = MyApp(True)
app.MainLoop()

