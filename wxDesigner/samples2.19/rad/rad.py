#!/bin/env python
#----------------------------------------------------------------------------
# Name:         rad.py
# Author:       XXXX
# Created:      XX/XX/XX
# Copyright:    
#----------------------------------------------------------------------------

import wx
from rad_wdr import *

# constants

ID_TEST = 100

# WDR: classes

class MyDialog(wx.Dialog):
    def __init__(self, parent, id, title,
        pos = wx.DefaultPosition, size = wx.DefaultSize,
        style = wx.DEFAULT_DIALOG_STYLE ):
        wx.Dialog.__init__(self, parent, id, title, pos, size, style)
        
        MyDialogFunc( self, True )
        
        self.CentreOnParent()
        
        # WDR: handler declarations for MyDialog
    
    # WDR: methods for MyDialog
    
    def GetMyNumber(self):
        return self.FindWindowById(ID_MY_NUMBER)
    
    def GetMyText(self):
        return self.FindWindowById(ID_MY_TEXT)
    
    # WDR: handler implementations for MyDialog


class MyFrame(wx.Frame):
    def __init__(self, parent, id, title,
        pos = wx.DefaultPosition, size = wx.DefaultSize,
        style = wx.DEFAULT_FRAME_STYLE ):
        wx.Frame.__init__(self, parent, id, title, pos, size, style)
        
        self.CreateMyMenuBar()
        
        self.CreateStatusBar(1)
        self.SetStatusText("Welcome to RAD!")
        
        self.g_text = ""
        self.g_number = 0
        
        # insert main window here
        
        # WDR: handler declarations for MyFrame
        wx.EVT_MENU(self, wx.ID_ABOUT, self.OnAbout)
        wx.EVT_MENU(self, wx.ID_EXIT, self.OnQuit)
        wx.EVT_MENU(self, ID_TEST, self.OnTest)
        wx.EVT_CLOSE(self, self.OnCloseWindow)
        
    # WDR: methods for MyFrame
    
    def CreateMyMenuBar(self):
        file_menu = wx.Menu()
        file_menu.Append(ID_TEST, "&Test dialog...\tCtrl-T", "Test dialog")
        file_menu.Append(wx.ID_EXIT, "&Quit...\tCtrl-Q", "Quit program")
        
        help_menu = wx.Menu()
        help_menu.Append(wx.ID_ABOUT, "&About...\tCtrl-A", "Program info")
        
        menu_bar = wx.MenuBar()
        menu_bar.Append(file_menu, "&File")
        menu_bar.Append(help_menu, "&Help")
        
        self.SetMenuBar(menu_bar)
    
    # WDR: handler implementations for MyFrame
    
    def OnAbout(self, event):
        dialog = wx.MessageDialog(self, "Welcome to RAD\n(C)opyright 2000 Robert Roebling",
            "About RAD", wx.OK|wx.ICON_INFORMATION)
        dialog.CentreOnParent()
        dialog.ShowModal()
        dialog.Destroy()
    
    def OnTest(self, event):
        dialog = MyDialog(self, -1, "Testing Getters");
        
        dialog.GetMyNumber().SetValue( self.g_number )
        dialog.GetMyText().SetValue( self.g_text )
        
        if dialog.ShowModal() == wx.ID_OK:
            self.g_number = dialog.GetMyNumber().GetValue()
            self.g_text = dialog.GetMyText().GetValue()
        
        dialog.Destroy()
    
    def OnQuit(self, event):
        self.Close(True)
    
    def OnCloseWindow(self, event):
        self.Destroy()
    

#----------------------------------------------------------------------------

class MyApp(wx.App):
    
    def OnInit(self):
        frame = MyFrame(None, -1, "RAD", [20,20], [500,340])
        frame.Show(True)
        return True

#----------------------------------------------------------------------------

app = MyApp(True)
app.MainLoop()

