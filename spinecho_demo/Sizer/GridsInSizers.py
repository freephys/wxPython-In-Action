# -*- coding: iso-8859-1 -*-
#--------------------------------------------------------------------
# Name:      GridsInSizers.py
# Purpose:   An application to learn sizers
# Author:    Jean-Michel Fauth, Switzerland
# Copyright: (c) 2007-2008 Jean-Michel Fauth
# Licence:   None
# os dev:    winXP sp2
# py dev:    Python 2.5.4
# wx dev:    wxPython 2.8.9.1-ansi
# Revision:  27 December 2008
#--------------------------------------------------------------------

# Grids in Sizers

#--------------------------------------------------------------------

import wx
import wx.grid as gridlib

#--------------------------------------------------------------------

class MyGrid(gridlib.Grid):

    def __init__(self, parent, nrows, ncols):
        gridlib.Grid.__init__(self, parent, wx.ID_ANY, style=wx.SUNKEN_BORDER)
        self.parent = parent

        self.nrows, self.ncols = nrows, ncols
        self.CreateGrid(self.nrows, self.ncols)

        #populate
        for r in xrange(self.nrows):
            for c in xrange(self.ncols):
                s = str(r) + ', ' + str(c)
                self.SetCellValue(r, c, s)
        
#--------------------------------------------------------------------

# A Panel containing 1 Grid.

class MyPanel1(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        grid = MyGrid(self, 30, 10)
        
        b = 10
        vsizer = wx.BoxSizer(wx.VERTICAL)
        vsizer.Add(grid, 1, wx.EXPAND | wx.ALL, b)
        self.SetSizer(vsizer)

#-------------------------------------------------------------------

# A Panel containing 2 Grids, horizontally.

class MyPanel2(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        grid1 = MyGrid(self, 30, 10)
        grid2 = MyGrid(self, 10, 10)
        
        b = 10
        hsizer = wx.BoxSizer(wx.HORIZONTAL)
        hsizer.Add(grid1, 1, wx.EXPAND | wx.ALL, b)
        hsizer.Add(grid2, 2, wx.EXPAND | wx.ALL, b)
        self.SetSizer(hsizer)

#-------------------------------------------------------------------

# A Panel containing 3 Grids.

class MyPanel3(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        grid1 = MyGrid(self, 30, 10)
        grid2 = MyGrid(self, 1, 1)
        grid3 = MyGrid(self, 10, 10)
        
        b = 10
        hsizer = wx.BoxSizer(wx.HORIZONTAL)
        hsizer.Add(grid1, 1, wx.EXPAND | wx.RIGHT, b)
        hsizer.Add(grid2, 1, wx.EXPAND, b)
        
        b = 10
        vsizer = wx.BoxSizer(wx.VERTICAL)
        vsizer.Add(hsizer, 1, wx.EXPAND | wx.ALL, b)
        vsizer.Add(grid3, 1, wx.EXPAND | wx.ALL, b)
        
        self.SetSizer(vsizer)

#-------------------------------------------------------------------

if __name__ == "__main__":

    import baseframe
    
    app = wx.PySimpleApp()
    frame = baseframe.MyFrame(None, panel=MyPanel3)
    frame.Show()
    app.MainLoop()

#eof----------------------------------------------------------------
