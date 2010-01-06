# -*- coding: iso-8859-1 -*-
#--------------------------------------------------------------------
# Name:      WithStaticBoxsizers.py
# Purpose:   An application to learn sizers
# Author:    Jean-Michel Fauth, Switzerland
# Copyright: (c) 2007-2008 Jean-Michel Fauth
# Licence:   None
# os dev:    winXP sp2
# py dev:    Python 2.5.4
# wx dev:    wxPython 2.8.9.1-ansi
# Revision:  28 December 2008
#--------------------------------------------------------------------

# Mainly StaticBoxSizers

#--------------------------------------------------------------------

import wx
from colourwindow import ColWin

#--------------------------------------------------------------------

# 3 ColWins in a StaticBoxSizer, vertically.

class MyPanel1(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        wred = ColWin(self, wx.ID_ANY, wx.RED)
        wblue = ColWin(self, wx.ID_ANY, wx.BLUE)
        wgreen = ColWin(self, wx.ID_ANY, wx.GREEN)
        
        b = 10  #inside the staticbox
        vsbsizer1 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, 'StaticboxSizer with a caption'), wx.VERTICAL)
        vsbsizer1.Add(wred, 1, wx.EXPAND | wx.ALL, b)
        vsbsizer1.Add(wblue, 1, wx.EXPAND | wx.ALL, b)
        vsbsizer1.Add(wgreen, 1, wx.EXPAND | wx.ALL, b)
        self.SetSizer(vsbsizer1)

#-------------------------------------------------------------------

# 3 ColWins in a StaticBoxSizer, vertically.
# The StaticBoxSizer is in a sizer to enable a border.

class MyPanel2(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        wred = ColWin(self, wx.ID_ANY, wx.RED)
        wblue = ColWin(self, wx.ID_ANY, wx.BLUE)
        wgreen = ColWin(self, wx.ID_ANY, wx.GREEN)
        
        b = 10  #inside the staticbox
        vsbsizer1 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, 'StaticboxSizer with a caption'), wx.VERTICAL)
        vsbsizer1.Add(wred, 1, wx.EXPAND | wx.ALL, b)
        vsbsizer1.Add(wblue, 1, wx.EXPAND | wx.ALL, b)
        vsbsizer1.Add(wgreen, 1, wx.EXPAND | wx.ALL, b)
        
        b = 10
        hsizer1 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer1.Add(vsbsizer1, 1, wx.EXPAND | wx.ALL, b)
        
        self.SetSizer(hsizer1)

#-------------------------------------------------------------------

# 5 ColWin, vertically.
# The ColWins 2 and 4 are in StaticBoxSizers.

class MyPanel3(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        wred = ColWin(self, wx.ID_ANY, wx.RED)
        wblue = ColWin(self, wx.ID_ANY, wx.BLUE)
        wgreen = ColWin(self, wx.ID_ANY, wx.GREEN)
        wwhite = ColWin(self, wx.ID_ANY, wx.WHITE)
        wyellow = ColWin(self, wx.ID_ANY, wx.NamedColour('yellow'))
        
        b = 10
        vsbsizer1 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, 'blue'), wx.VERTICAL)
        vsbsizer1.Add(wblue, 1, wx.EXPAND | wx.ALL, b)
        
        vsbsizer2 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, 'white'), wx.VERTICAL)
        vsbsizer2.Add(wwhite, 1, wx.EXPAND | wx.ALL, b)
        
        b = 5
        vsizer1 = wx.BoxSizer(wx.VERTICAL)
        vsizer1.Add(wred, 1, wx.EXPAND | wx.ALL, b)
        vsizer1.Add(vsbsizer1, 1, wx.EXPAND | wx.ALL, b)
        vsizer1.Add(wgreen, 1, wx.EXPAND | wx.ALL, b)
        vsizer1.Add(vsbsizer2, 1, wx.EXPAND | wx.ALL, b)
        vsizer1.Add(wyellow, 1, wx.EXPAND | wx.ALL, b)
        
        self.SetSizer(vsizer1)

#-------------------------------------------------------------------

# 3 StaticBoxSizers with 1 ColWin in each.
# The StaticBoxSizers are arranged vertically.

class MyPanel4(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        wred = ColWin(self, wx.ID_ANY, wx.NamedColour('green'))
        wgreen = ColWin(self, wx.ID_ANY, wx.NamedColour('red'))
        wblue = ColWin(self, wx.ID_ANY, wx.NamedColour('blue'))
        
        b = 10
        sizer1 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, 'Staticbox'), wx.VERTICAL)
        sizer1.Add(wred, 1, wx.EXPAND | wx.ALL, b)

        sizer2 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, 'Staticbox'), wx.VERTICAL)
        sizer2.Add(wgreen, 1, wx.EXPAND | wx.ALL, b)

        sizer4 = wx.StaticBoxSizer(wx.StaticBox(self, wx.ID_ANY, 'Staticbox'), wx.VERTICAL)
        sizer4.Add(wblue, 1, wx.EXPAND | wx.ALL, b)
        
        #tricky: the 2nd and 3rd staticbox sizer are shifted one pixel to the
        #left, try with b2 = 0
        b1, b2 = 0, -1
        sizer3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer3.Add(sizer1, 1, wx.EXPAND, b1)
        sizer3.Add(sizer2, 1, wx.EXPAND | wx.LEFT, b2)
        sizer3.Add(sizer4, 1, wx.EXPAND | wx.LEFT, b2)
        
        self.SetSizer(sizer3)

#-----------------------------------------------------------------

if __name__ == "__main__":

    import baseframe
    
    app = wx.PySimpleApp()
    frame = baseframe.MyFrame(None, panel=MyPanel1)
    frame.Show()
    app.MainLoop()

#eof-----------------------------------------------------------------

