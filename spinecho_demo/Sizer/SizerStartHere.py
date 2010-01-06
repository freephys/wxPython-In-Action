# -*- coding: iso-8859-1 -*-
#--------------------------------------------------------------------
# Name:      SizerStartHere.py
# Purpose:   An application to learn sizers
# Author:    Jean-Michel Fauth, Switzerland
# Copyright: (c) 2007-2008 Jean-Michel Fauth
# Licence:   None
# os dev:    winXP sp2
# py dev:    Python 2.5.4
# wx dev:    wxPython 2.8.9.1-ansi
# Revision:  30 December 2008
#--------------------------------------------------------------------

# This application describes how the miscellaneous standalone
# applications of the LearnSizers bundle are designed.

#--------------------------------------------------------------------

import wx

# The ColWin class from the module colourwindow is a wx.Window widget
# used as a "standard" item for the miscellaneous application.
from colourwindow import ColWin

#--------------------------------------------------------------------

# The simpliest sizer, a single item in a wx.BoxSizer.
# The sizer is laid out in a panel.

class MyPanel1(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        
        # A green ColWin as sizer item.
        wgreen = ColWin(self, wx.ID_ANY, wx.GREEN)
        
        # Setup the sizer
        b = 20
        vsizer1 = wx.BoxSizer(orient=wx.VERTICAL)
        vsizer1.Add(item=wgreen, proportion=1, flag=wx.EXPAND | wx.ALL, border=b)
        self.SetSizer(vsizer1)

#-------------------------------------------------------------------

class MyPanel2(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        
        # Define and setup your sizer(s) here.
        pass

#-------------------------------------------------------------------

if __name__ == "__main__":

    # The module baseframe contains a default wx.Frame widget, the MyFrame
    # class, hosting the panel created in *this* module.
    import baseframe
    
    # The wx application
    app = wx.PySimpleApp()
    
    # The frame hosting the panel.
    # frame   : an instance of MyFrame
    # MyFrame : default frame
    # None    : std wx stuff
    # panel=MyPanel1 : pass the MyPanel1 class as the panel of MyFrame.
    frame = baseframe.MyFrame(None, panel=MyPanel1)
    
    # Variants

    # Full defined MyFrame
    #~ frame = baseframe.MyFrame(None, \
                    #~ id=wx.ID_ANY, \
                    #~ title='A new title', \
                    #~ pos=(200, 400), \
                    #~ size=(200, 100), \
                    #~ style=wx.DEFAULT_FRAME_STYLE, \
                    #~ panel=MyPanel1, \
                    #~ showmenu=False)
    
    # No panel is passed to MyFrame, a default panel is used.
    #~ frame = baseframe.MyFrame(None)
    
    # Pass MyPanel2 to MyFrame
    #~ frame = baseframe.MyFrame(None, panel=MyPanel2)
    
    # The showmenu argument, False as default, shows a dummy menu
    # in MyFrame.
    #~ frame = baseframe.MyFrame(None, panel=MyPanel1, showmenu=True)
    
    # Show and run the wx application.
    frame.Show()
    app.MainLoop()

#eof-----------------------------------------------------------------

