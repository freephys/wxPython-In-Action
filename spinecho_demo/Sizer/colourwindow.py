# -*- coding: iso-8859-1 -*-
#--------------------------------------------------------------------
# Name:      colourwindow.py
# Purpose:   Item(s) for the miscellaneous LearnSizers package modules.
# Author:    Jean-Michel Fauth, Switzerland
# Copyright: (c) 2007-2008 Jean-Michel Fauth
# Licence:   None
# os dev:    winXP sp2
# py dev:    Python 2.5.4
# wx dev:    wxPython 2.8.9.1-ansi
# Revision:  27 December 2008
#--------------------------------------------------------------------

# Item(s) for the sizers of the LearnSizer package.

#--------------------------------------------------------------------

import wx

#-----------------------------------------------------------------

# A wx.Window with a coloured background.
# pos == wx.DefaultPosition and size == wx.DefaultSize since sizers are used.

class ColWin(wx.Window):
    
    def __init__(self, parent, id, BackColour):
        wx.Window.__init__(self, parent, id, wx.DefaultPosition, \
            wx.DefaultSize, wx.SIMPLE_BORDER)
        self.SetBackgroundColour(BackColour)

#eof-----------------------------------------------------------------
