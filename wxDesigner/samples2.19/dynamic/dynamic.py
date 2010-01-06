#!/bin/env python
#----------------------------------------------------------------------------
# Name:         dynamic.py
# Author:       XXXX
# Created:      XX/XX/XX
# Copyright:    
#----------------------------------------------------------------------------

import wx

from dynamic_wdr import *


# WDR: classes

class MyDialog(wx.Dialog):
    def __init__(self, parent, id, title,
        pos = wx.DefaultPosition, size = wx.DefaultSize,
        style = wx.DEFAULT_DIALOG_STYLE ):
        wx.Dialog.__init__(self, parent, id, title, pos, size, style|wx.RESIZE_BORDER)
        
        # WDR: dialog function MyDialogFunc for MyDialog
        MyDialogFunc(self, True)
        
        self.sub_page = MyPageOneFunc( self, False, False )
        self.my_sizer.Add( self.sub_page )
        
        self.GetSizer().Fit( self )
        
        self.CentreOnParent()
        
        # WDR: handler declarations for MyDialog
        wx.EVT_CHOICE(self, ID_CHOICE, self.OnPage)

    # WDR: methods for MyDialog

    # WDR: handler implementations for MyDialog

    def OnPage(self, event):
        self.sub_page.DeleteWindows()
        self.my_sizer.Remove( self.sub_page )
        if event.GetInt() == 1:
            self.sub_page = MyPageTwoFunc( self, False, False )
        else:
            self.sub_page = MyPageOneFunc( self, False, False )
        self.my_sizer.Add( self.sub_page )
        self.GetSizer().Fit( self )

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
        wx.EVT_MENU(self, ID_TEST, self.OnTest)
        wx.EVT_MENU(self, wx.ID_ABOUT, self.OnAbout)
        wx.EVT_MENU(self, wx.ID_EXIT, self.OnQuit)
        wx.EVT_CLOSE(self, self.OnCloseWindow)
        
    # WDR: methods for MyFrame
    
    def CreateMyMenuBar(self):
        self.SetMenuBar( MyMenuBarFunc() )
    
    # WDR: handler implementations for MyFrame
    
    def OnTest(self, event):
        dialog = MyDialog( self, -1, "Test dialog" )
        dialog.ShowModal()
        dialog.Destroy()

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
        frame = MyFrame(None, -1, "SuperApp", [20,20], [500,340])
        frame.Show(True)
        return True

#----------------------------------------------------------------------------

app = MyApp(True)
app.MainLoop()

