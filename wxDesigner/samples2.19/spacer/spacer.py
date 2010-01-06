#!/bin/env python
#----------------------------------------------------------------------------
# Name:         spacer.py
# Author:       XXXX
# Created:      XX/XX/XX
# Copyright:    
#----------------------------------------------------------------------------

import wx
from spacer_wdr import *

# constants

ID_TEST = 100
ID_QUIT = 101

# WDR: classes

class MyFrame(wx.Frame):
    def __init__(self, parent, id, title,
        pos = wx.DefaultPosition, size = wx.DefaultSize,
        style = wx.DEFAULT_FRAME_STYLE ):
        wx.Frame.__init__(self, parent, id, title, pos, size, style)
        
        self.CreateMyMenuBar()
        
        self.CreateStatusBar(1)
        self.SetStatusText("Welcome to Spacers!")
        
        # insert main window here
        
        # WDR: handler declarations for MyFrame
        wx.EVT_MENU(self, ID_TEST, self.OnTest)
        wx.EVT_MENU(self, ID_QUIT, self.OnQuit)
        wx.EVT_CLOSE(self, self.OnCloseWindow)
        
    # WDR: methods for MyFrame
    
    def CreateMyMenuBar(self):
        file_menu = wx.Menu()
        file_menu.Append(ID_TEST, "Test dialog...", "Test dialog")
        file_menu.Append(ID_QUIT, "Quit...", "Quit program")
        
        menu_bar = wx.MenuBar()
        menu_bar.Append(file_menu, "File")
        
        self.SetMenuBar(menu_bar)
    
    # WDR: handler implementations for MyFrame
    
    def OnTest(self, event):
        dialog = wx.Dialog(self, -1, "Test spacers")
        MyDialogFunc( dialog, True )
        dialog.CentreOnParent()
        dialog.ShowModal()
    
    def OnQuit(self, event):
        self.Close(True)
    
    def OnCloseWindow(self, event):
        self.Destroy()
    

#----------------------------------------------------------------------------

class MyApp(wx.App):

    def OnInit(self):
        frame = MyFrame(None, -1, "Spacers", [20,20], [500,340])
        frame.Show(True)
        return True

#----------------------------------------------------------------------------

app = MyApp(True)
app.MainLoop()

