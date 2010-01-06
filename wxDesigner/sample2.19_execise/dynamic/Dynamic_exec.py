#!/bin/env python
#----------------------------------------------------------------------------
# Name:         Dynamic_exec.py
# Author:       XXXX
# Created:      XX/XX/XX
# Copyright:    
#----------------------------------------------------------------------------

import wx

from Dynamic_exec_wdr import *


# WDR: classes

class MyDialog(wx.Dialog):
    def __init__(self, parent, id, title,
        pos = wx.DefaultPosition, size = wx.DefaultSize,
        style = wx.DEFAULT_DIALOG_STYLE ):
        wx.Dialog.__init__(self, parent, id, title, pos, size, style)
        
        # WDR: handler declarations for MyDialog
        wx.EVT_CHOICE(self, ID_CHOICE, self.OnChoice)
        self.sizer = TestDialogFunc(self)
        self.SetSizer(self.sizer)
        self.GetSizer().Fit( self )
    # WDR: methods for MyDialog

    # WDR: handler implementations for MyDialog

    def OnChoice(self, event):
        # Test to see if sefl.newSizer already exists 
        if hasattr(self,'newSizer'):
            #Destroy all windows managed by the sizer
            self.newSizer.DeleteWindows() 
            self.sizer.Remove(self.newSizer)
        if event.GetInt() == 1:
            self.newSizer = PageDialogFunc1(self,False,False)
        else:
            self.newSizer = PageDialogFunc2(self,False,False)
        self.sizer.Add(self.newSizer,0,wx.CENTER)
        self.GetSizer().Fit( self )



class DynamicFrame(wx.Frame):
    def __init__(self, parent, id, title,
        pos = wx.DefaultPosition, size = wx.DefaultSize,
        style = wx.DEFAULT_FRAME_STYLE ):
        wx.Frame.__init__(self, parent, id, title, pos, size, style)
        
        # insert main window here
        self.menuBar = FileMenuBarFunc()
        self.SetMenuBar(self.menuBar)
        # WDR: handler declarations for DynamicFrame
        wx.EVT_MENU(self, ID_MENU_Test, self.OnTest)
        wx.EVT_MENU(self, wx.ID_ABOUT, self.OnAbout)
        wx.EVT_MENU(self, wx.ID_EXIT, self.OnQuit)
        wx.EVT_CLOSE(self, self.OnCloseWindow)
        
    # WDR: methods for DynamicFrame
    
    # WDR: handler implementations for DynamicFrame
    
    def OnTest(self, event):
        dialog = MyDialog(self,-1,"dynamic demo")
        dialog.CenterOnParent()
        dialog.ShowModal()
        dialog.Destroy()


    def OnAbout(self, event):
        dialog = wx.MessageDialog(self, "Welcome to wxDesigner 1.0",
            "About WxDesigner", wx.OK|wx.ICON_INFORMATION )
        dialog.CentreOnParent()
        dialog.ShowModal()
        dialog.Destroy()
    
    def OnQuit(self, event):
        self.Close(True)
    
    def OnCloseWindow(self, event):
        self.Destroy()
    

#----------------------------------------------------------------------------

class Dynamic(wx.App):
    
    def OnInit(self):
        wx.InitAllImageHandlers()
        frame = DynamicFrame( None, -1, "SuperApp", [20,20], [500,340] )
        frame.Show(True)
        
        return True

#----------------------------------------------------------------------------

app = Dynamic(True)
app.MainLoop()

