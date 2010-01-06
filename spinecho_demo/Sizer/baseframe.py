# -*- coding: iso-8859-1 -*-
#--------------------------------------------------------------------
# Name:      baseframe.py
# Purpose:   A generic Frame
# Author:    Jean-Michel Fauth, Switzerland
# Copyright: (c) 2007-2008 Jean-Michel Fauth
# Licence:   None
# os dev:    winXP sp2
# py dev:    Python 2.5.4
# wx dev:    wxPython 2.8.9.1-ansi
# Revision:  27 December 2008
#--------------------------------------------------------------------

# Base frame used in the different scripts of the LearnSizers package.

#--------------------------------------------------------------------

import os
import wx

#--------------------------------------------------------------------

# Note: panel has no id.
class DefaultPanel(wx.Panel):
    
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, wx.ID_ANY, wx.DefaultPosition, wx.DefaultSize)
        self.parent = parent

        txt = \
"""
-----

This is the default panel (class DefaultPanel) of the
class MyFrame in module baseframe.py.

-----

Are you sure you want to use this?

-----
"""

        sty = wx.ALIGN_CENTRE | wx.ST_NO_AUTORESIZE 
        label = wx.StaticText(self, wx.ID_ANY, txt, style=sty)
        label.SetBackgroundColour((255, 255, 200))
        label.SetForegroundColour((0, 0, 255))
        
        b = 20
        vsizer = wx.BoxSizer(orient=wx.VERTICAL)
        vsizer.Add(item=label, proportion=1, flag=wx.EXPAND | wx.ALL, border=b)
        
        self.SetSizer(vsizer)
        
#-------------------------------------------------------------------

# Note: wx.Frame does not like wx.DefaultPosition, (-1, -1)
class MyFrame(wx.Frame):

    def __init__(self, parent, id=wx.ID_ANY, title='LearnSizers 9 - Top frame', \
                 pos=(20, 20), size=wx.DefaultSize, style=wx.DEFAULT_FRAME_STYLE, \
                 panel=DefaultPanel, showmenu=False):
        id = id
        title = title
        pos = pos
        size = size
        style = style
        self.locpanel = panel
        self.showmenu = showmenu
        wx.Frame.__init__(self, parent, id, title, pos, size, style)
        
        # Cosmetic. Useful if the sizer in the panel has a static line on top.
        if self.showmenu:
            self.AddMenuBar()
        
        self.panel = self.locpanel(self)

        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)

    def OnCloseWindow(self, event):
        self.Destroy()

    def AddMenuBar(self):
        menu1 = wx.Menu()
        menu1.Append(101, '&File')
        menu2 = wx.Menu()
        menu2.Append(102, '&Edit')
        menu3 = wx.Menu()
        menu3.Append(104, '&Search')
        menuBar = wx.MenuBar()
        menuBar.Append(menu1, '&File')
        menuBar.Append(menu2, '&Edit')
        menuBar.Append(menu3, '&Search')
        self.SetMenuBar(menuBar)

#-------------------------------------------------------------------

if __name__ == "__main__":

    app = wx.PySimpleApp()
    frame = MyFrame(None, panel=DefaultPanel, showmenu=False)
    frame.Show()
    app.MainLoop()

#eof-----------------------------------------------------------------
