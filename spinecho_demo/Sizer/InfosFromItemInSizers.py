# -*- coding: iso-8859-1 -*-
#--------------------------------------------------------------------
# Name:      InfosFromItemInSizers.py
# Purpose:   An application to learn sizers
# Author:    Jean-Michel Fauth, Switzerland
# Copyright: (c) 2007-2008 Jean-Michel Fauth
# Licence:   None
# os dev:    winXP sp2
# py dev:    Python 2.5.4
# wx dev:    wxPython 2.8.9.1-ansi
# Revision:  28 December 2008
#--------------------------------------------------------------------

# Getting informations on the items in a sizer.
# Use print statement (sys.stdout).

#--------------------------------------------------------------------

import wx
from colourwindow import ColWin

#--------------------------------------------------------------------

class MyPanel1(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.parent = parent
        
        self.wblue = ColWin(self, wx.ID_ANY, wx.BLUE)
        self.wblue.SetName('wblue')
        
        b1 = wx.Button(self, wx.ID_ANY, 'Items infos', name='b1')

        b1.Bind(wx.EVT_BUTTON, self.OnClick1)

        #toolbar
        self.hsizer1 = wx.BoxSizer(wx.HORIZONTAL)
        b = 20
        self.hsizer1.Add(b1, 0, wx.ALL, b)
        self.hsizer1.Add(self.wblue, 1, wx.EXPAND | wx.ALL,b)
        self.hsizer1.SetItemMinSize(self.wblue, (100, 75))
        
        self.SetSizerAndFit(self.hsizer1)
        self.parent.SetClientSize(self.hsizer1.GetSize())

        #self.ShowItemsInfos()

    def OnClick1(self, event):
        self.ShowItemsInfos()

    #a few infos on the sizer items
    #see doc or dir(item)
    def ShowItemsInfos(self):
        r = self.hsizer1.GetChildren()
        for item in r:
            print '=' * 30
            print '<item>:', item
            print 'name of the <item>:', item.GetWindow().GetName()
            print '<item>.GetSize():', item.GetSize()
            print '<item>.GetMinSize():', item.GetMinSize()
            print '<item>.GetPosition():', item.GetPosition()
            print '<item>.IsWindow():', item.IsWindow()
            print '<item>.IsSpacer():', item.IsSpacer()

#-------------------------------------------------------------------

if __name__ == "__main__" :

    import baseframe
    
    app = wx.PySimpleApp()
    frame = baseframe.MyFrame(None, panel=MyPanel1)
    frame.Show()
    app.MainLoop()

#eof-----------------------------------------------------------------
