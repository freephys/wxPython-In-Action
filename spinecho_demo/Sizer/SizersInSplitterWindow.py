# -*- coding: iso-8859-1 -*-
#--------------------------------------------------------------------
# Name:      SizersInSplitterWindow.py
# Purpose:   An application to learn sizers
# Author:    Jean-Michel Fauth, Switzerland
# Copyright: (c) 2007-2008 Jean-Michel Fauth
# Licence:   None
# os dev:    winXP sp2
# py dev:    Python 2.5.4
# wx dev:    wxPython 2.8.9.1-ansi
# Revision:  28 December 2008
#--------------------------------------------------------------------

# Sizers in SplitterWindows

#--------------------------------------------------------------------

import wx
import wx.stc
from colourwindow import ColWin

from WithBoxSizers import MyPanel4 as pa1
from WithBoxSizers import MyPanel7 as pa2
from WithBoxSizers import MyPanel2 as pa3

#--------------------------------------------------------------------

# A panel containing a SplitterWindow with panels holding sizers inside.

class MyPanel1(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        
        #add a splitter windows containing two panels
        sty = wx.SP_3D #ok
        #~ sty = wx.SP_3D | wx.SP_3DSASH | wx.SP_LIVE_UPDATE #ok, but flickering
        self.splitwin = wx.SplitterWindow(self, wx.ID_ANY, style=sty)

        topw = pa1(self.splitwin)
        bottomw = pa2(self.splitwin)
        self.splitwin.SplitHorizontally(topw, bottomw, sashPosition=30)
        self.splitwin.SetMinimumPaneSize(100)

        b = 0
        vsizer = wx.BoxSizer(wx.VERTICAL)
        vsizer.Add(self.splitwin, 1, wx.EXPAND | wx.ALL, b)
        self.SetSizer(vsizer)

#-------------------------------------------------------------------

# A aizer containing 1 ColWin and SplitterWindow as defined in MyPanel1.

class MyPanel2(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        
        #add a splitter windows containing two panels
        sty = wx.SP_3D #ok
        self.splitwin = wx.SplitterWindow(self, wx.ID_ANY, style=sty)

        topw = pa1(self.splitwin)
        bottomw = pa2(self.splitwin)
        self.splitwin.SplitHorizontally(topw, bottomw, sashPosition=30)
        self.splitwin.SetMinimumPaneSize(50)

        wwhite = ColWin(self, wx.ID_ANY, wx.WHITE)

        b1, b2 = 10, 0
        vsizer = wx.BoxSizer(wx.VERTICAL)
        vsizer.Add(wwhite, 1, wx.EXPAND | wx.ALL, b1)
        vsizer.Add(self.splitwin, 1, wx.EXPAND | wx.ALL, b2)
        self.SetSizer(vsizer)

#--------------------------------------------------------------------

# A panel containing a SplitterWindow with two panels.
# Used in MyPanel3

class MyPanelTmp(wx.Panel):
    
    def __init__(self, parent, id):
        wx.Panel.__init__(self, parent, id, wx.DefaultPosition, wx.DefaultSize, wx.NO_BORDER)

        sty = wx.SP_3D
        sty = wx.SP_NOBORDER | wx.SP_3DSASH

        self.splitwin = wx.SplitterWindow(self, wx.ID_ANY, (-1, -1), (-1, -1), style=sty)
        topw1 = pa1(self.splitwin)
        bottomw1 = pa2(self.splitwin)
        self.splitwin.SplitHorizontally(topw1, bottomw1, sashPosition=30)
        self.splitwin.SetMinimumPaneSize(100)
        
        b = 0
        vsizer = wx.BoxSizer(wx.VERTICAL)
        vsizer.Add(self.splitwin, proportion=1, flag=wx.EXPAND | wx.ALL, border=b)
        self.SetSizer(vsizer)

#--------------------------------------------------------------------

# A panel containing a SplitterWindow with 2 panels: MyPanelTmp and pa2.
# It seems, this is the only way to set a SplitterWindow in a SplitterWindow:
# defining a SplitterWindow in a separate class.
# memo: wx.SashLayoutWindow

class MyPanel3(wx.Panel):
    
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize)

        sty = wx.SP_3D
        #~ sty = wx.SP_BORDER
        #~ sty = wx.SP_3DSASH
        #~ sty = wx.SP_LIVE_UPDATE
        self.splitwin = wx.SplitterWindow(self, wx.ID_ANY, style=sty)
        w1 = MyPanelTmp(self.splitwin, wx.ID_ANY)
        w2 = pa3(self.splitwin)
        self.splitwin.SplitVertically(w2, w1, sashPosition=300)
        self.splitwin.SetMinimumPaneSize(50)
        
        b = 10
        vsizer = wx.BoxSizer(wx.VERTICAL)
        vsizer.Add(self.splitwin, proportion=1, flag=wx.EXPAND | wx.ALL, border=b)
        self.SetSizer(vsizer)

#--------------------------------------------------------------------

# 2 STC widdgets in a SplitterWindow

class MyPanel4(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize)
        self.parent = parent

        # 1st splitter: 2 stc's
        sty = wx.SP_3D
        splitter1 = wx.SplitterWindow(self, wx.ID_ANY, style=sty)

        self.stc1 = wx.stc.StyledTextCtrl(splitter1, wx.ID_ANY,  style=wx.NO_BORDER)
        self.stc2 = wx.stc.StyledTextCtrl(splitter1, wx.ID_ANY,  style=wx.NO_BORDER)
    
        splitter1.SplitHorizontally(self.stc1, self.stc2, sashPosition=30)
        splitter1.SetMinimumPaneSize(100)

        b = 10
        vsizer = wx.BoxSizer(wx.VERTICAL)
        vsizer.Add(splitter1, proportion=1, flag=wx.EXPAND | wx.ALL, border=b)
        self.SetSizer(vsizer)

#--------------------------------------------------------------------

if __name__ == "__main__":

    import baseframe
    
    app = wx.PySimpleApp()
    frame = baseframe.MyFrame(None, panel=MyPanel1)
    frame.Show()
    app.MainLoop()

#eof----------------------------------------------------------------
