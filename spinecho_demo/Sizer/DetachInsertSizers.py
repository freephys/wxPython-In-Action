# -*- coding: iso-8859-1 -*-
#--------------------------------------------------------------------
# Name:      DetachInsertSizers.py
# Purpose:   An application to learn sizers
# Author:    Jean-Michel Fauth, Switzerland
# Copyright: (c) 2007-2008 Jean-Michel Fauth
# Licence:   None
# os dev:    winXP sp2
# py dev:    Python 2.5.4
# wx dev:    wxPython 2.8.9.1-ansi
# Revision:  28 December 2008
#--------------------------------------------------------------------

# detach and insert items/sizers in sizers

#--------------------------------------------------------------------

import wx
from colourwindow import ColWin

#--------------------------------------------------------------------

class MyPanel1(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.parent = parent
        
        self.wred = ColWin(self, wx.ID_ANY, wx.RED)
        self.wgreen = ColWin(self, wx.ID_ANY, wx.GREEN)

        b1 = wx.Button(self, wx.ID_ANY, 'detach / insert wred', wx.DefaultPosition, wx.DefaultSize)
        b2 = wx.Button(self, wx.ID_ANY, 'detach / insert wgreen', wx.DefaultPosition, wx.DefaultSize)
        b3 = wx.Button(self, wx.ID_ANY, 'swap wrec / wgreen', wx.DefaultPosition, wx.DefaultSize)
        b4 = wx.Button(self, wx.ID_ANY, '4', wx.DefaultPosition, wx.DefaultSize)

        b1.Bind(wx.EVT_BUTTON, self.OnClick1)
        b2.Bind(wx.EVT_BUTTON, self.OnClick2)
        b3.Bind(wx.EVT_BUTTON, self.OnClick3)
        b4.Bind(wx.EVT_BUTTON, self.OnClick4)

        #toolbar
        hsizer1 = wx.BoxSizer(wx.HORIZONTAL)
        b = 8
        hsizer1.Add(b1, 0, wx.RIGHT, b)
        hsizer1.Add(b2, 0, wx.RIGHT, b)
        hsizer1.Add(b3, 0, wx.RIGHT, b)
        hsizer1.Add(b4, 0, border=b)

        #A horizontal sizer holding the green and red windows. Both windows
        #are visible at start.
        #note the same flag border for both windows (swapping)
        self.bb = 5
        self.hsizer2 = wx.BoxSizer(wx.HORIZONTAL)
        self.hsizer2.Add(self.wred, 1, wx.EXPAND | wx.ALL, self.bb)
        self.hsizer2.Add(self.wgreen, 1, wx.EXPAND | wx.ALL, self.bb)

        b = 5
        self.vsizer1 = wx.BoxSizer(wx.VERTICAL)
        self.vsizer1.Add(hsizer1, 0, wx.ALL, b)
        self.vsizer1.Add(self.hsizer2, 1, wx.ALL | wx.EXPAND, b)

        self.SetSizer(self.vsizer1)
        
        self.parent.SetClientSize((500, 300))
        self.parent.CentreOnScreen()
        
        #the two windows are shown
        assert self.wred.IsShown() == True
        assert self.wgreen.IsShown() == True

    # note: wred or wgreen win is always insert at "position 0" even if swapped.
    
    #wred
    def OnClick1(self, event):
        if self.wred.IsShown():
            #~ print 'wred is shown'
            self.hsizer2.Detach(self.wred)
            self.wred.Show(False)
            self.Layout()
        elif not self.wred.IsShown():
            #~ print 'wred is not shown'
            self.wred.Show(True)
            #same flag as in __init__
            self.hsizer2.Insert(0, self.wred, 1, wx.EXPAND | wx.ALL, self.bb)
            self.Layout()
        else:
            pass

    #wgreen 
    def OnClick2(self, event):
        if self.wgreen.IsShown():
            #~ print 'wgreen is shown'
            self.hsizer2.Detach(self.wgreen)
            self.wgreen.Show(False)
            self.Layout()
        elif not self.wgreen.IsShown():
            #~ print 'wgreen is not shown'
            self.wgreen.Show(True)
            #same flag as in __init__
            self.hsizer2.Insert(0, self.wgreen, 1, wx.EXPAND | wx.ALL, self.bb)
            self.Layout()
        else:
            pass

    #swap
    def OnClick3(self, event):
        if not self.wred.IsShown() or not self.wgreen.IsShown():
            #~ print 'wred *or* wgreen is/are not shown'
            return
        
        item0 = self.hsizer2.GetItem(0).GetWindow()
        item1 = self.hsizer2.GetItem(1).GetWindow()
        
        self.hsizer2.Detach(item0)
        self.hsizer2.Detach(item1)
        item0.Show(False)
        item1.Show(False)
        
        item1.Show(True)
        self.hsizer2.Insert(0, item1, 1, wx.EXPAND | wx.ALL, self.bb)
        self.Layout()
        
        item0.Show(True)
        self.hsizer2.Insert(1, item0, 1, wx.EXPAND | wx.ALL, self.bb)
        self.Layout()
        
    def OnClick4(self, event):
        pass

#-------------------------------------------------------------------

if __name__ == "__main__" :

    import baseframe
    
    app = wx.PySimpleApp()
    frame = baseframe.MyFrame(None, panel=MyPanel1)
    frame.Show()
    app.MainLoop()

#eof-----------------------------------------------------------------

