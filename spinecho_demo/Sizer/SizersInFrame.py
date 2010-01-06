# -*- coding: iso-8859-1 -*-
#--------------------------------------------------------------------
# Name:      SizersInFrame.py
# Purpose:   An application to learn sizers
# Author:    Jean-Michel Fauth, Switzerland
# Copyright: (c) 2007-2008 Jean-Michel Fauth
# Licence:   None
# os dev:    winXP sp2
# py dev:    Python 2.5.4
# wx dev:    wxPython 2.8.9.1-ansi
# Revision:  28 December 2008
#--------------------------------------------------------------------

# Sizers can not only be used within panels they also can be packed in
# a frame. In this application, the frame has a sizer with two items,
# two panels from the module with_boxsizers.

import wx
from WithBoxSizers import MyPanel2
from WithBoxSizers import MyPanel3

#--------------------------------------------------------------------

class MyFrame(wx.Frame):

    def __init__(self, parent, id):
        title = 'sizers_in_frame'
        pos = wx.DefaultPosition
        size = (600, 400)
        sty = wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, parent, id, title, pos, size, sty)

        panel1 = MyPanel2(self)
        panel2 = MyPanel3(self)
        
        b = 20
        vsizer1 = wx.BoxSizer(wx.VERTICAL)
        vsizer1.Add(panel1, 1, wx.EXPAND | wx.ALL, b)
        vsizer1.Add(panel2, 1, wx.EXPAND | wx.ALL, b)
        
        self.SetSizer(vsizer1)

        self.Bind(wx.EVT_CLOSE, self.OnCloseWindow)

    def OnCloseWindow(self, event):
        self.Destroy()

#--------------------------------------------------------------------

if __name__ == "__main__":

    app = wx.PySimpleApp()
    frame = MyFrame(None, wx.ID_ANY)
    frame.Show()
    app.MainLoop()

#eof-----------------------------------------------------------------
