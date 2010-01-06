#!/bin/env python
#----------------------------------------------------------------------------
# Name:         Derived.py
# Author:       XXXX
# Created:      XX/XX/XX
# Copyright:    
#----------------------------------------------------------------------------

import wx

from Derived_wdr import *



# WDR: classes

class MyDialog(wx.Dialog):
    def __init__(self, parent, id, title,
        pos = wx.DefaultPosition, size = wx.DefaultSize,
        style = wx.DEFAULT_DIALOG_STYLE ):
        wx.Dialog.__init__(self, parent, id, title, pos, size, style)
        
        # WDR: dialog function MyDialogFunc for MyDialog
        MyDialogFunc( self, True )
        self.CenterOnParent()
    
        # WDR: handler declarations for MyDialog
        wx.EVT_BUTTON(self, ID_BUTTON_TEST, self.OnButtonTest)

    # WDR: methods for MyDialog

    def GetTextCtrl2(self):
        return self.FindWindowById( ID_TEXTCTRL2 )

    def GetTextCtrl1(self):
        return self.FindWindowById( ID_TEXTCTRL1 )

    # WDR: handler implementations for MyDialog

    
    def OnButtonTest(self, event):
        text_Ctrl1 = self.GetTextCtrl1()
        text_Ctrl2 = self.GetTextCtrl2()
        text1 = text_Ctrl1.GetValue()
        text_Ctrl2.SetValue(text1)
        

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
        wx.EVT_MENU(self, ID_MENU_TEST, self.OnMenuTest)
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
    
    def OnMenuTest(self, event):
        dialog = MyDialog(self,-1,"Derived Control")
        dialog.ShowModal()
        


    def OnAbout(self, event):
        dialog = wx.MessageDialog(self, "Welcome to Demo of wxDesigner\n(C)opyright Leo Shen",
            "About wxDesigner", wx.OK|wx.ICON_INFORMATION )
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
        frame = MyFrame( None, -1, "SuperApp", [20,20], [500,340] )
        frame.Show(True)
        
        return True

#----------------------------------------------------------------------------

app = MyApp(True)
app.MainLoop()

