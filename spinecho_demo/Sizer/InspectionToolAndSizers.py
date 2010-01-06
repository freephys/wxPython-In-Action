# -*- coding: iso-8859-1 -*-
#--------------------------------------------------------------------
# Name:      InspectionToolAndSizers.py
# Purpose:   An application to learn sizers
# Author:    Jean-Michel Fauth, Switzerland
# Copyright: (c) 2007-2008 Jean-Michel Fauth
# Licence:   None
# os dev:    winXP sp2
# py dev:    Python 2.5.4
# wx dev:    wxPython 2.8.9.1-ansi
# Revision:  28 December 2008
#--------------------------------------------------------------------

# Usage of the wxPython inspection tool with sizers.

#--------------------------------------------------------------------

import wx
from colourwindow import ColWin

#--------------------------------------------------------------------

# 3 ColWins, horizontally, height ratio 1:2:3.

class MyPanel1(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.parent = parent
        
        wred = ColWin(self, wx.ID_ANY, wx.RED)
        wblue = ColWin(self, wx.ID_ANY, wx.BLUE)
        wgreen = ColWin(self, wx.ID_ANY, wx.GREEN)
        
        b = 5
        hsizer1 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer1.Add(wred, 1, wx.EXPAND | wx.ALL, b)
        hsizer1.Add(wblue, 2, wx.EXPAND | wx.ALL, b)
        hsizer1.Add(wgreen, 3, wx.EXPAND | wx.ALL, b)
        
        self.SetSizer(hsizer1)

#-----------------------------------------------------------------

if __name__ == "__main__" :

    import baseframe
    import wx.lib.inspection #inspection tool

    app = wx.PySimpleApp()
    frame = baseframe.MyFrame(None, panel=MyPanel1)
    
    #set values to the parent frame to be easily recognized in the inspection tool.
    frame.SetPosition((33, 22))
    frame.SetSize((333, 222))
    
    frame.Show()
    
    #show the inspection frame of the inspection tool
    wx.lib.inspection.InspectionTool().Show()
    
    app.MainLoop()

#eof-----------------------------------------------------------------

