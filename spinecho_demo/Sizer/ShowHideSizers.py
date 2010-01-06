# -*- coding: iso-8859-1 -*-
#--------------------------------------------------------------------
# Name:      ShowHideSizers.py
# Purpose:   An application to learn sizers
# Author:    Jean-Michel Fauth, Switzerland
# Copyright: (c) 2007-2008 Jean-Michel Fauth
# Licence:   None
# os dev:    winXP sp2
# py dev:    Python 2.5.4
# wx dev:    wxPython 2.8.9.1-ansi
# Revision:  27 December 2008
#--------------------------------------------------------------------

# Show and hide items in sizers.

#--------------------------------------------------------------------

import os
import wx
from colourwindow import ColWin

#--------------------------------------------------------------------

# 2 Buttons and 2 ColWins. Show/hide the ColWins.
# Buttons as "toolbar" on the top.

class MyPanel1(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        self.wred = ColWin(self, wx.ID_ANY, wx.RED)
        self.wblue = ColWin(self, wx.ID_ANY, wx.BLUE)

        b1 = wx.Button(self, wx.ID_ANY, 'Show / Hide wred', wx.DefaultPosition, wx.DefaultSize)
        b2 = wx.Button(self, wx.ID_ANY, 'Show / Hide wblue', wx.DefaultPosition, wx.DefaultSize)

        b1.Bind(wx.EVT_BUTTON, self.OnClick1)
        b2.Bind(wx.EVT_BUTTON, self.OnClick2)

        hsizer1 = wx.BoxSizer(wx.HORIZONTAL)
        b = 8
        hsizer1.Add(b1, 0, wx.RIGHT, b)
        hsizer1.Add(b2, 0, border=b)

        b = 4
        hsizer2 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer2.Add(self.wred, 1, wx.EXPAND | wx.RIGHT, b)
        hsizer2.Add(self.wblue, 1, wx.EXPAND | wx.LEFT, b)

        b = 4
        vsizer1 = wx.BoxSizer(wx.VERTICAL)
        vsizer1.Add(hsizer1, 0, wx.ALL, b)
        vsizer1.Add(hsizer2, 1, wx.ALL | wx.EXPAND, b)

        self.SetSizer(vsizer1)

    def OnClick1(self, event):
        if self.wred.IsShown():
            self.wred.Show(False)
            self.Layout()
        elif not self.wred.IsShown():
            self.wred.Show(True)
            self.Layout()
        else:
            pass

    def OnClick2(self, event):
        if self.wblue.IsShown():
            self.wblue.Show(False)
            self.Layout()
        elif not self.wblue.IsShown():
            self.wblue.Show(True)
            self.Layout()
        else:
            pass

#-------------------------------------------------------------------

# 6 Buttons and 3 ColWins. Show/hide the ColWins.
# Buttons as "tool bar" at the right of the frame.

class MyPanel2(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        self.wred = ColWin(self, wx.ID_ANY, wx.RED)
        self.wwhite = ColWin(self, wx.ID_ANY, wx.WHITE)
        self.wgreen = ColWin(self, wx.ID_ANY, wx.GREEN)

        b1 = wx.Button(self, wx.ID_ANY, 'Show / Hide wred', wx.DefaultPosition, wx.DefaultSize)
        b2 = wx.Button(self, wx.ID_ANY, 'Show / Hide wwhite', wx.DefaultPosition, wx.DefaultSize)
        b3 = wx.Button(self, wx.ID_ANY, 'Show / Hide wgreen', wx.DefaultPosition, wx.DefaultSize)

        b1.Bind(wx.EVT_BUTTON, self.OnClick1)
        b2.Bind(wx.EVT_BUTTON, self.OnClick2)
        b3.Bind(wx.EVT_BUTTON, self.OnClick3)

        vsizer1 = wx.BoxSizer(wx.VERTICAL)
        b = 8
        vsizer1.Add(b1, 0, wx.BOTTOM, b)
        vsizer1.Add(b2, 0, wx.BOTTOM, b)
        vsizer1.Add(b3, 0, border=b)

        b = 4
        hsizer2 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer2.Add(self.wred, 1, wx.EXPAND | wx.ALL, b)
        hsizer2.Add(self.wwhite, 2, wx.EXPAND | wx.ALL, b)
        hsizer2.Add(self.wgreen, 3, wx.EXPAND | wx.ALL, b)
        hsizer2.Add(vsizer1, 0, wx.ALL, b)
        
        self.SetSizer(hsizer2)

    def OnClick1(self, event):
        if self.wred.IsShown():
            self.wred.Show(False)
            self.Layout()
            self.Refresh() #does not work properly without this !?
        elif not self.wred.IsShown():
            self.wred.Show(True)
            self.Layout()
            self.Refresh()
        else:
            pass
            
    def OnClick2(self, event):
        if self.wwhite.IsShown():
            self.wwhite.Show(False)
            self.Layout()
            self.Refresh()
        elif not self.wwhite.IsShown():
            self.wwhite.Show(True)
            self.Layout()
            self.Refresh()
        else:
            pass

    def OnClick3(self, event):
        if self.wgreen.IsShown():
            self.wgreen.Show(False)
            self.Layout()
            self.Refresh()
        elif not self.wgreen.IsShown():
            self.wgreen.Show(True)
            self.Layout()
            self.Refresh()
        else:
            pass

#-------------------------------------------------------------------

class MyPanel3(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        self.wred = ColWin(self, wx.ID_ANY, wx.RED)
        self.wyellow = ColWin(self, wx.ID_ANY, (255, 255, 0))
        self.wgreen = ColWin(self, wx.ID_ANY, wx.GREEN)
        self.wblue = ColWin(self, wx.ID_ANY, wx.BLUE)

        b1 = wx.Button(self, wx.ID_ANY, 'Show / Hide sizer2 (wred, wyellow)', wx.DefaultPosition, wx.DefaultSize)
        b2 = wx.Button(self, wx.ID_ANY, 'Show sizer3 (wgreen, wblue)', wx.DefaultPosition, wx.DefaultSize)

        b1.Bind(wx.EVT_BUTTON, self.OnClick1)
        b2.Bind(wx.EVT_BUTTON, self.OnClick2)

        hsizer1 = wx.BoxSizer(wx.HORIZONTAL)
        b = 8
        hsizer1.Add(b1, 0, wx.RIGHT, b)
        hsizer1.Add(b2, 0, border=b)

        b = 4
        self.hsizer2 = wx.BoxSizer(wx.HORIZONTAL)
        self.hsizer2.Add(self.wred, 2, wx.EXPAND | wx.RIGHT, b)
        self.hsizer2.Add(self.wyellow, 1, wx.EXPAND | wx.LEFT, b)

        b = 4
        self.hsizer3 = wx.BoxSizer(wx.HORIZONTAL)
        self.hsizer3.Add(self.wgreen, 1, wx.EXPAND | wx.RIGHT, b)
        self.hsizer3.Add(self.wblue, 2, wx.EXPAND | wx.LEFT, b)

        b = 4
        self.vsizer1 = wx.BoxSizer(wx.VERTICAL)
        self.vsizer1.Add(self.hsizer2, 1, wx.ALL | wx.EXPAND, b)
        self.vsizer1.Add(self.hsizer3, 1, wx.ALL | wx.EXPAND, b)
        self.vsizer1.Add(hsizer1, 0, wx.ALL | wx.ALIGN_CENTRE, b)

        self.SetSizer(self.vsizer1)

    def OnClick1(self, event):
        if self.vsizer1.IsShown(self.hsizer2):
            self.vsizer1.Hide(self.hsizer2)
            self.Layout()
        elif not self.vsizer1.IsShown(self.hsizer2):
            self.vsizer1.Show(self.hsizer2)
            self.Layout()
        else:
            pass

    def OnClick2(self, event):
        if self.vsizer1.IsShown(self.hsizer3):
            self.vsizer1.Hide(self.hsizer3)
            self.Layout()
        elif not self.vsizer1.IsShown(self.hsizer3):
            self.vsizer1.Show(self.hsizer3)
            self.Layout()
        else:
            pass
            
#-------------------------------------------------------------------

if __name__ == "__main__":

    import baseframe
    
    app = wx.PySimpleApp()
    frame = baseframe.MyFrame(None, panel=MyPanel3)
    frame.Show()
    app.MainLoop()

#eof-----------------------------------------------------------------

