#!/bin/env python
#----------------------------------------------------------------------------
# Name:         foreign.py
# Author:       XXXX
# Created:      XX/XX/XX
# Copyright:    
#----------------------------------------------------------------------------

import wx
from foreign_wdr import *

# constants

ID_ABOUT = 100
ID_QUIT = 101
ID_TEST = 102

# WDR: classes

class MyFrame(wx.Frame):
    def __init__(self, parent, id, title,
        pos = wx.DefaultPosition, size = wx.DefaultSize,
        style = wx.DEFAULT_FRAME_STYLE ):
        wx.Frame.__init__(self, parent, id, title, pos, size, style)
        
        self.CreateMyMenuBar()
        
        self.CreateStatusBar(1)
        self.SetStatusText("Welcome to Foreign!")
        
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
        dialog = wx.MessageDialog(self, "Welcome to Foreign\n(C)opyright 2000 Robert Roebling",
            "About Foreign", wx.OK|wx.ICON_INFORMATION )
        dialog.CentreOnParent()
        dialog.ShowModal()
        dialog.Destroy()
    
    def OnTest(self, event):
        dialog = wx.Dialog( self, -1, "Test foreign control" );
        listctrl = wx.ListCtrl( dialog, ID_LISTCTRL, wx.DefaultPosition, [370,150], wx.LC_REPORT|wx.SUNKEN_BORDER )
        listctrl.InsertColumn( 0, "Column 1", width=110 )
        listctrl.InsertColumn( 1, "Column 2", width=110 )
        listctrl.InsertColumn( 2, "Column 3", width=110 )
        for i in range(80):
            listctrl.InsertStringItem(i,"This is item %d" % i)
            listctrl.SetStringItem(i, 1, "Col 2, item %d" % i)
            listctrl.SetStringItem(i, 2, "Col 3, item %d" % i)
            
        MyDialogFunc( dialog, True )
            
        dialog.CentreOnParent()
        dialog.ShowModal()
        dialog.Destroy()
    
    def OnQuit(self, event):
        self.Close(true)
    
    def OnCloseWindow(self, event):
        self.Destroy()
    

#----------------------------------------------------------------------------

class MyApp(wx.App):
    
    def OnInit(self):
        frame = MyFrame(None, -1, "Foreign", [20,20], [500,340] )
        frame.Show(True)
        return True

#----------------------------------------------------------------------------

app = MyApp(True)
app.MainLoop()

