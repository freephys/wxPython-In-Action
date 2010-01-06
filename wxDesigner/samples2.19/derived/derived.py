#!/bin/env python
#----------------------------------------------------------------------------
# Name:         derived.py
# Author:       XXXX
# Created:      XX/XX/XX
# Copyright:    
#----------------------------------------------------------------------------

import wx
from derived2 import *
from derived_wdr import *

# constants

ID_ABOUT = 100
ID_QUIT = 101
ID_MYTEST = 102

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
        wx.EVT_BUTTON(self, ID_TEST, self.OnTest)

    # WDR: methods for MyDialog

    def GetTextctrl1(self):
        return self.FindWindowById( ID_TEXTCTRL1 )

    def GetTextctrl2(self):
        return self.FindWindowById( ID_TEXTCTRL2 )

    # WDR: handler implementations for MyDialog

    def OnTest(self, event):
        text1 = self.GetTextctrl1()
        text2 = self.GetTextctrl2()
        text = text1.GetValue()
        text2.SetValue( text )

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
        wx.EVT_MENU(self, ID_ABOUT, self.OnAbout)
        wx.EVT_MENU(self, ID_MYTEST, self.OnTest)
        wx.EVT_MENU(self, ID_QUIT, self.OnQuit)
        wx.EVT_CLOSE(self, self.OnCloseWindow)
        
    # WDR: methods for MyFrame
    
    def CreateMyMenuBar(self):
        file_menu = wx.Menu()
        file_menu.Append(ID_ABOUT, "About...", "Program info")
        file_menu.Append(ID_MYTEST, "Test dialog...", "Test dialog")
        file_menu.Append(ID_QUIT, "Quit...", "Quit program")
        
        menu_bar = wx.MenuBar()
        menu_bar.Append(file_menu, "File")
        
        self.SetMenuBar(menu_bar)
    
    # WDR: handler implementations for MyFrame
    
    def OnAbout(self, event):
        dialog = wx.MessageDialog(self, "Welcome to Derived\n(C)opyright 2000 Robert Roebling",
            "About SuperApp", wx.OK|wx.ICON_INFORMATION )
        dialog.CentreOnParent()
        dialog.ShowModal()
        dialog.Destroy()
    
    def OnTest(self, event):
        dialog = MyDialog(self, -1, "Derived controls")
        dialog.ShowModal()
        dialog.Destroy()
    
    def OnQuit(self, event):
        self.Close(True)
    
    def OnCloseWindow(self, event):
        self.Destroy()
    

#----------------------------------------------------------------------------
                                      
class MyApp(wx.App):
    
    def OnInit(self):
        frame = MyFrame(None, -1, "Derived", [20,20], [500,340])
        frame.Show(True)
        
        return True

#----------------------------------------------------------------------------

app = MyApp(True)
app.MainLoop()

