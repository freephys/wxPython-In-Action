# -*- coding: iso-8859-1 -*-
#--------------------------------------------------------------------
# Name:      AddressBook.py
# Purpose:   An application to learn sizers
# Author:    Jean-Michel Fauth, Switzerland
# Copyright: (c) 2007-2008 Jean-Michel Fauth
# Licence:   None
# os dev:    winXP sp2
# py dev:    Python 2.5.4
# wx dev:    wxPython 2.8.9.1-ansi
# Revision:  28 December 2008
#--------------------------------------------------------------------

# AddressBook is a wxPython port of an pyQt application found
# at http://dosimple.ch/articles/Python-PyQt/
# This module contains only the layout of the gui part.

#--------------------------------------------------------------------

import wx

#--------------------------------------------------------------------

class MyListCtrl(wx.ListCtrl):
    
    def __init__(self, parent, id):
        sty = wx.LC_REPORT | wx.LC_HRULES | wx.LC_VRULES
        wx.ListCtrl.__init__(self, parent, id, style=sty)

        self.ClearAll()

        #header
        self.InsertColumn(0, "Name")
        self.InsertColumn(1, "First name")
        self.InsertColumn(2, "City")
        self.InsertColumn(3, "zip")
        self.InsertColumn(4, "email")
        self.SetColumnWidth(0, 100)
        self.SetColumnWidth(1, 100)
        self.SetColumnWidth(2, 100)
        self.SetColumnWidth(3, 100)
        self.SetColumnWidth(4, 100)

#-------------------------------------------------------------------

class PanelLeft(wx.Panel):
    
    def __init__(self, parent, id):
        wx.Panel.__init__(self, parent, id, wx.DefaultPosition, wx.DefaultSize)
        self.parent = parent
        self.SetBackgroundColour(wx.RED)

        #widgets
        self.lc = MyListCtrl(self, wx.ID_ANY)
        self.b1 = wx.Button(self, wx.ID_ANY, 'Remove')
        self.b2 = wx.Button(self, wx.ID_ANY, 'Sort')

        hsizer1 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer1.Add(self.b1, 0)
        hsizer1.Add(self.b2, 0, wx.LEFT, 10)
        
        b = 10
        vsizer1 = wx.BoxSizer(wx.VERTICAL)
        vsizer1.Add(self.lc, 1, wx.EXPAND | wx.ALL, b)
        vsizer1.Add(hsizer1, 0, wx.ALIGN_LEFT | wx.ALL, b)
        
        self.SetSizer(vsizer1)
        #~ self.SetSizerAndFit(vsizer1)
        #very important
        self.SetMinSize(self.GetBestSize())

#-------------------------------------------------------------------

class PanelRight(wx.Panel):
    
    def __init__(self, parent, id):
        wx.Panel.__init__(self, parent, id, wx.DefaultPosition, wx.DefaultSize)
        self.parent = parent
        self.SetBackgroundColour(wx.GREEN)

        #widgets
        lab1 = wx.StaticText(self, wx.ID_ANY, 'Name', style=wx.ALIGN_RIGHT)
        lab2 = wx.StaticText(self, wx.ID_ANY, 'First name', style=wx.ALIGN_RIGHT)
        lab3 = wx.StaticText(self, wx.ID_ANY, 'City', style=wx.ALIGN_RIGHT)
        lab4 = wx.StaticText(self, wx.ID_ANY, 'zip', style=wx.ALIGN_RIGHT)
        lab5 = wx.StaticText(self, wx.ID_ANY, 'email', style=wx.ALIGN_RIGHT)
        self.txt1 = wx.TextCtrl(self, wx.ID_ANY, '')
        self.txt2 = wx.TextCtrl(self, wx.ID_ANY, '')
        self.txt3 = wx.TextCtrl(self, wx.ID_ANY, '')
        self.txt4 = wx.TextCtrl(self, wx.ID_ANY, '')
        self.txt5 = wx.TextCtrl(self, wx.ID_ANY, '')
        self.b1 = wx.Button(self, wx.ID_ANY, 'Add')
        self.b2 = wx.Button(self, wx.ID_ANY, 'Update')

        #sizers
        b = 10
        fgsizer1 = wx.FlexGridSizer(4, 2, b, b)
        fgsizer1.AddMany([ 
            (lab1, 1, wx.EXPAND | wx.ALL),
            (self.txt1, 1, wx.EXPAND | wx.ALL),
            (lab2, 1, wx.EXPAND | wx.ALL),
            (self.txt2, 1, wx.EXPAND | wx.ALL),
            (lab3, 1, wx.EXPAND | wx.ALL),
            (self.txt3, 1, wx.EXPAND | wx.ALL),
            (lab4, 1, wx.EXPAND | wx.ALL),
            (self.txt4, 1, wx.EXPAND | wx.ALL),
            (lab5, 1, wx.EXPAND | wx.ALL),
            (self.txt5, 1, wx.EXPAND | wx.ALL),
            ])
        fgsizer1.AddGrowableCol(1)

        hsizer1 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer1.Add(self.b1, 0)
        hsizer1.Add(self.b2, 0, wx.LEFT, 10)
        
        b = 10
        vsizer1 = wx.BoxSizer(wx.VERTICAL)
        vsizer1.Add(fgsizer1, 0, wx.EXPAND | wx.ALL, b)
        vsizer1.Add(hsizer1, 0, wx.ALIGN_LEFT | wx.ALL, b)

        self.SetSizer(vsizer1)
        self.SetMinSize(self.GetBestSize())

#-------------------------------------------------------------------

class MySplitterWindow(wx.SplitterWindow):
    
    def __init__(self, parent, id):
        #~ sty = wx.SP_3D | wx.SP_3DSASH #not ok
        sty = wx.SP_3D #not ok
        #~ sty = wx.SP_LIVE_UPDATE #ok
        #~ sty = wx.SP_3D | wx.SP_LIVE_UPDATE #not ok
        #~ sty = wx.SP_3DSASH #ok
        #~ sty = wx.SP_3DSASH | wx.SP_LIVE_UPDATE #ok
        #~ sty = wx.SP_3D | wx.SP_3DSASH | wx.SP_LIVE_UPDATE #not ok
        #~ sty = wx.SP_BORDER #ok
        #~ sty = wx.SP_BORDER | wx.SP_LIVE_UPDATE #ok
        wx.SplitterWindow.__init__(self, parent, id, style=sty)

        self.pl = PanelLeft(self, wx.ID_ANY)
        self.pr = PanelRight(self, wx.ID_ANY)
        self.SplitVertically(self.pl, self.pr, sashPosition=300)
        #~ self.SplitHorizontally(self.pl, self.pr, sashPosition=-1)
        self.SetMinimumPaneSize(10)
        self.UpdateSize()

        #~ grandparent = self.GetGrandParent()
        #~ print grandparent
        #~ grandparent.SendSizeEvent() #does not help

#-------------------------------------------------------------------

class MyPanel1(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.parent = parent
        
        self.sp = MySplitterWindow(self, wx.ID_ANY)
        self.sp.SetSashPosition(500)

        b = 4
        hsizer1 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer1.Add(self.sp, 1, wx.EXPAND | wx.ALL, b)
        
        self.SetSizer(hsizer1)
        self.parent.CentreOnScreen()

#-------------------------------------------------------------------

if __name__ == "__main__":

    import baseframe
    
    app = wx.PySimpleApp()
    frame = baseframe.MyFrame(None, panel=MyPanel1)
    frame.Show()
    app.MainLoop()

#eof----------------------------------------------------------------
