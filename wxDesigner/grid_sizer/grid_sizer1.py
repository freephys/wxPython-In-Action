#!/bin/env python
#----------------------------------------------------------------------------
# Name:         grid_sizer1.py
# Author:       XXXX
# Created:      XX/XX/XX
# Copyright:    
#----------------------------------------------------------------------------

import wx

from grid_sizer1_wdr import *


# WDR: classes

class BasicGridSizerFrame(wx.Frame):
    def __init__(self, parent, id, title,
        pos = wx.DefaultPosition, size = wx.DefaultSize,
        style = wx.DEFAULT_FRAME_STYLE ):
        wx.Frame.__init__(self, parent, id, title, pos, size, style)
        
        self.CreateMyMenuBar()
        
        self.CreateMyToolBar()
        
        self.CreateStatusBar(1)
        self.SetStatusText("Welcome!")

        # insert main window here
        MyDialogFunc(self)
        # WDR: handler declarations for BasicGridSizerFrame
        wx.EVT_BUTTON(self, ID_BUTTON_ITEM2, self.OnClickItem2)
        wx.EVT_MENU_HIGHLIGHT(self, ID_SUBMENU_ITEM1, self.OnItem1)
        wx.EVT_MENU(self, ID_MENU, self.OnAbout)
        wx.EVT_MENU(self, wx.ID_ABOUT, self.OnAbout)
        wx.EVT_MENU(self, wx.ID_EXIT, self.OnQuit)
        wx.EVT_CLOSE(self, self.OnCloseWindow)
        
    # WDR: methods for BasicGridSizerFrame
    
    def Getbuttonitem2(self):
        return self.FindWindowById( ID_BUTTON_ITEM2 )

    def Getbuttonitem1(self):
        return self.FindWindowById( ID_BUTTON_ITEM1 )

    def CreateMyMenuBar(self):
        self.SetMenuBar(MyMenuBarFunc())       
    
    def CreateMyToolBar(self):
        tb = self.CreateToolBar(wx.TB_HORIZONTAL|wx.NO_BORDER)
        
        # tb.AddSimpleTool( wx.ID_EXIT, wxNoRefBitmap(...,wx.BITMAP_TYPE_PNG), "Quit" )
        
        tb.Realize()
    
    # WDR: handler implementations for BasicGridSizerFrame

    def OnClickItem2(self, event):
        self.Getbuttonitem1().Enable()

    def OnItem1(self, event):
        self.Getbuttonitem1().Disable()

        

        

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

class BasicGridSizer(wx.App):
    
    def OnInit(self):
        wx.InitAllImageHandlers()
        frame = BasicGridSizerFrame( None, -1, "SuperApp", [20,20], [500,340] )
        frame.Show(True)
        
        return True

#----------------------------------------------------------------------------

app = BasicGridSizer(True)
app.MainLoop()

