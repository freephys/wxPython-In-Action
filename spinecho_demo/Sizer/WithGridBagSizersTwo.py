# -*- coding: iso-8859-1 -*-
#--------------------------------------------------------------------
# Name:      WithGridBagSizersTwo.py
# Purpose:   An application to learn sizers
# Author:    Jean-Michel Fauth, Switzerland
# Copyright: (c) 2007-2008 Jean-Michel Fauth
# Licence:   None
# os dev:    winXP sp2
# py dev:    Python 2.5.4
# wx dev:    wxPython 2.8.9.1-ansi
# Revision:  28 December 2008
#--------------------------------------------------------------------

# It seems wx.GridBagSizer has got some cleanup from 2.8.8.0.
# Especially the behaviour with wx.StaticLine's.
# From this, this new test module.

#--------------------------------------------------------------------

import wx
from colourwindow import ColWin

#--------------------------------------------------------------------

# a GridBagSizer with 3 x 3 coloured windows, 9 items

class MyPanel1(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        wwhite = ColWin(self, wx.ID_ANY, wx.WHITE)
        wblue = ColWin(self, wx.ID_ANY, wx.BLUE)
        wgreen = ColWin(self, wx.ID_ANY, wx.GREEN)
        wred = ColWin(self, wx.ID_ANY, wx.RED)
        wgrey = ColWin(self, wx.ID_ANY, '#a0a0a0')
        wpink = ColWin(self, wx.ID_ANY, wx.NamedColour('pink'))
        wyellow = ColWin(self, wx.ID_ANY, wx.NamedColour('yellow'))
        wcyan = ColWin(self, wx.ID_ANY, wx.NamedColour('cyan'))
        worange = ColWin(self, wx.ID_ANY, wx.NamedColour('orange'))

        vgap, hgap = 8, 4
        gbs = wx.GridBagSizer(vgap, hgap)

        b = 0
        f = wx.EXPAND | wx.ALL
        gbs.Add(wwhite,     (0, 0), (1, 1), f, b)
        gbs.Add(wblue,      (0, 1), (1, 1), f, b)
        gbs.Add(wgreen,     (0, 2), (1, 1), f, b)
        
        gbs.Add(wred,       (1, 0), (1, 1), f, b)
        gbs.Add(wgrey,      (1, 1), (1, 1), f, b)
        gbs.Add(wpink,      (1, 2), (1, 1), f, b)

        gbs.Add(wyellow,    (2, 0), (1, 1), f, b)
        gbs.Add(wcyan,      (2, 1), (1, 1), f, b)
        gbs.Add(worange,    (2, 2), (1, 1), f, b)

        gbs.AddGrowableRow(0)
        gbs.AddGrowableRow(1)
        gbs.AddGrowableRow(2)

        gbs.AddGrowableCol(0)
        gbs.AddGrowableCol(1)
        gbs.AddGrowableCol(2)
        
        self.SetSizer(gbs)

#-----------------------------------------------------------------

# a GridBagSizer with 3 x 3 coloured windows,  9 items
# and staticlines between rows and cols

class MyPanel2(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        wwhite = ColWin(self, wx.ID_ANY, wx.WHITE)
        wblue = ColWin(self, wx.ID_ANY, wx.BLUE)
        wgreen = ColWin(self, wx.ID_ANY, wx.GREEN)
        wred = ColWin(self, wx.ID_ANY, wx.RED)
        wgrey = ColWin(self, wx.ID_ANY, '#a0a0a0')
        wpink = ColWin(self, wx.ID_ANY, wx.NamedColour('pink'))
        wyellow = ColWin(self, wx.ID_ANY, wx.NamedColour('yellow'))
        wcyan = ColWin(self, wx.ID_ANY, wx.NamedColour('cyan'))
        worange = ColWin(self, wx.ID_ANY, wx.NamedColour('orange'))

        hstaline1 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, (-1, 2), wx.LI_HORIZONTAL)
        hstaline2 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, (-1, 2), wx.LI_HORIZONTAL)
        
        vstaline1 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, (2, -1), wx.LI_VERTICAL)
        vstaline2 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, (2, -1), wx.LI_VERTICAL)

        vgap, hgap = 4, 4
        gbs = wx.GridBagSizer(vgap, hgap)

        b = 0
        f = wx.EXPAND | wx.ALL
        b2 = 8
        f2 = wx.EXPAND | wx.TOP | wx.BOTTOM
        b3 = 8
        f3 = wx.EXPAND | wx.LEFT | wx.RIGHT
        
        gbs.Add(wwhite,     (0, 0), (1, 1), f, b)
        gbs.Add(vstaline1,  (0, 1), (5, 1), f3, b3)
        gbs.Add(wblue,      (0, 2), (1, 1), f, b)
        gbs.Add(vstaline2,  (0, 3), (5, 1), f3, b3)
        gbs.Add(wgreen,     (0, 4), (1, 1), f, b)

        gbs.Add(hstaline1,  (1, 0), (1, 5), f2, b2)

        gbs.Add(wred,       (2, 0), (1, 1), f, b)
        gbs.Add(wgrey,      (2, 2), (1, 1), f, b)
        gbs.Add(wpink,      (2, 4), (1, 1), f, b)

        gbs.Add(hstaline2,  (3, 0), (1, 5), f, b2)

        gbs.Add(wyellow,    (4, 0), (1, 1), f, b)
        gbs.Add(wcyan,      (4, 2), (1, 1), f, b)
        gbs.Add(worange,    (4, 4), (1, 1), f, b)

        gbs.AddGrowableRow(0)
        gbs.AddGrowableRow(2)
        gbs.AddGrowableRow(4)

        gbs.AddGrowableCol(0)
        gbs.AddGrowableCol(2)
        gbs.AddGrowableCol(4)
        
        self.SetSizer(gbs)

#-----------------------------------------------------------------

# a GridBagSizer with 3 x 3 coloured windows,  9 items
# and staticlines between rows and cols
# and staticlines as "borders"

class MyPanel3(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        wwhite = ColWin(self, wx.ID_ANY, wx.WHITE)
        wblue = ColWin(self, wx.ID_ANY, wx.BLUE)
        wgreen = ColWin(self, wx.ID_ANY, wx.GREEN)
        wred = ColWin(self, wx.ID_ANY, wx.RED)

        hstaline1 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, (-1, 2), wx.LI_HORIZONTAL)
        hstaline2 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, (-1, 2), wx.LI_HORIZONTAL)
        hstaline3 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, (-1, 2), wx.LI_HORIZONTAL)
        
        vstaline1 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, (2, -1), wx.LI_VERTICAL)
        vstaline2 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, (2, -1), wx.LI_VERTICAL)
        vstaline3 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, (2, -1), wx.LI_VERTICAL)

        vgap, hgap = 4, 4
        gbs = wx.GridBagSizer(vgap, hgap)

        b = 8
        f = wx.EXPAND | wx.ALL
        b2 = 8
        f2 = wx.EXPAND | wx.TOP | wx.BOTTOM
        b3 = 8
        f3 = wx.EXPAND | wx.LEFT | wx.RIGHT
        
        gbs.Add(hstaline1,  (0, 0), (1, 5), f, b)
        
        gbs.Add(vstaline1,  (1, 0), (3, 1), f, b)
        gbs.Add(wwhite,     (1, 1), (1, 1), f, b)
        gbs.Add(vstaline2,  (1, 2), (3, 1), f, b)
        gbs.Add(wblue,      (1, 3), (1, 1), f, b)
        gbs.Add(vstaline3,  (1, 4), (3, 1), f, b)

        gbs.Add(hstaline2,  (2, 1), (1, 3), f, b)

        gbs.Add(wgreen,     (3, 1), (1, 1), f, b)
        gbs.Add(wred,       (3, 3), (1, 1), f, b)

        gbs.Add(hstaline3,  (4, 0), (1, 5), f, b)


        gbs.AddGrowableRow(1)
        gbs.AddGrowableRow(3)

        gbs.AddGrowableCol(1)
        gbs.AddGrowableCol(3)
        
        self.SetSizer(gbs)

#-----------------------------------------------------------------

# Spacers in GridBagSizer

class MyPanel4(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.parent = parent
        
        wwhite = ColWin(self, wx.ID_ANY, wx.WHITE)
        wblue = ColWin(self, wx.ID_ANY, wx.BLUE)
        wgreen = ColWin(self, wx.ID_ANY, wx.GREEN)
        wred = ColWin(self, wx.ID_ANY, wx.RED)
        #~ wgrey = ColWin(self, wx.ID_ANY, '#aaaaaa')
        #~ wpink = ColWin(self, wx.ID_ANY, wx.NamedColour('pink'))
        #~ wyellow = ColWin(self, wx.ID_ANY, wx.NamedColour('yellow'))
        #~ wcyan = ColWin(self, wx.ID_ANY, wx.NamedColour('cyan'))
        #~ worange = ColWin(self, wx.ID_ANY, wx.NamedColour('orange'))
        #~ wbrown = ColWin(self, wx.ID_ANY, wx.NamedColour('brown'))

        hgap, vgap = 10, 10
        gbs = wx.GridBagSizer(vgap, hgap)

        b = 0
        f = wx.EXPAND | wx.ALL

        gbs.Add(wwhite,         (0, 0), (1, 1), f, b)
        gbs.Add(wblue,          (0, 1), (1, 1), f, b)
        gbs.AddSpacer((30, -1), (0, 2))

        gbs.AddSpacer((-1, 25), (1, 0))

        gbs.Add(wgreen,         (2, 0), (1, 1), f, b)
        gbs.Add(wred,           (2, 1), (1, 1), f, b)
        
        gbs.AddSpacer(          (-1, 50), (3, 0))
        #the line below also works
        #~ gbs.Add((-1, 50),       (3, 0))
        
        
        
        gbs.AddGrowableRow(0)
        gbs.AddGrowableRow(2)

        gbs.AddGrowableCol(0)
        gbs.AddGrowableCol(1)
        
        self.SetSizerAndFit(gbs)
        #~ self.SetSizer(gbs)
        
        #set a size
        self.parent.SetClientSize((300, 300))
        self.parent.CentreOnScreen()

#-----------------------------------------------------------------

if __name__ == "__main__":

    import baseframe
    
    app = wx.PySimpleApp()
    frame = baseframe.MyFrame(None, panel=MyPanel4)
    frame.Show()
    app.MainLoop()

#eof----------------------------------------------------------------
