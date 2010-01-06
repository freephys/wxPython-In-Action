# -*- coding: iso-8859-1 -*-
#--------------------------------------------------------------------
# Name:      SizersAndNotebook.py
# Purpose:   An application to learn sizers
# Author:    Jean-Michel Fauth, Switzerland
# Copyright: (c) 2007-2008 Jean-Michel Fauth
# Licence:   None
# os dev:    winXP sp2
# py dev:    Python 2.5.4
# wx dev:    wxPython 2.8.9.1-ansi
# Revision:  28 December 2008
#--------------------------------------------------------------------

# Note: some panels from other modules in this package are causing refreshing
# issue when they are used with a notebook.

# Workaround. They are copied and modified here with an added
# wx.FULL_REPAINT_ON_RESIZE style.

#--------------------------------------------------------------------

import wx
from colourwindow import ColWin

#--------------------------------------------------------------------

# A modified version of WithBoxSizers.MyPanel13, where the style wx.FULL_REPAINT_ON_RESIZE
# has been added. Refreshing issue.

class MyPanel13A(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, style=wx.FULL_REPAINT_ON_RESIZE)

        wgreen = ColWin(self, wx.NewId(), wx.NamedColour('green'))
        b1 = wx.Button(self, wx.NewId(), 'button1')
        b2 = wx.Button(self, wx.NewId(), 'button2')
        b3 = wx.Button(self, wx.NewId(), 'button3')
        
        b = 0
        vsizer1 = wx.BoxSizer(wx.VERTICAL)
        vsizer1.Add(b1, 0, wx.ALL, b)
        vsizer1.AddStretchSpacer()
        vsizer1.Add(b2, 0, wx.ALL, b)
        vsizer1.AddStretchSpacer()
        vsizer1.Add(b3, 0, wx.ALL, b)

        b = 5
        self.hsizer2 = wx.BoxSizer(wx.HORIZONTAL)
        self.hsizer2.Add(vsizer1, 0, wx.EXPAND | wx.ALL, b)
        self.hsizer2.Add(wgreen, 1, wx.EXPAND | wx.ALL, b)

        self.SetSizer(self.hsizer2)

#-------------------------------------------------------------------

# A serie of couples, StaticTexts-TextCtrls.
# Buttons ok and cancel.
# This is not elegant. A better way: FlexGridSizer.

# A modified version of WithBoxSizers.MyPanel16, where the style wx.FULL_REPAINT_ON_RESIZE
# has been added. Refreshing issue.

class MyPanel16A(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, style=wx.FULL_REPAINT_ON_RESIZE)
        self.parent = parent

        self.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False))

        lab1 = wx.StaticText(self, -1, 'hydrogen :', style=wx.ALIGN_RIGHT)
        lab2 = wx.StaticText(self, -1, 'tin :', style=wx.ALIGN_RIGHT)
        lab3 = wx.StaticText(self, -1, 'mendelevium :', style=wx.ALIGN_RIGHT)
        lab4 = wx.StaticText(self, -1, 'carbon :', style=wx.ALIGN_RIGHT)
        txt1 = wx.TextCtrl(self, -1, '')
        txt2 = wx.TextCtrl(self, -1, '')
        txt3 = wx.TextCtrl(self, -1, '')
        txt4 = wx.TextCtrl(self, -1, '')
        b1 = wx.Button(self, wx.NewId(), '&OK')
        b2 = wx.Button(self, wx.NewId(), '&Cancel')
        staline = wx.StaticLine(self, wx.NewId(), wx.DefaultPosition, (-1, 2), wx.LI_HORIZONTAL)
        
        b = 5
        w = 100
        hsizer1 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer1.Add(lab1, 0, wx.RIGHT, b)
        hsizer1.Add(txt1, 1, wx.GROW, b)
        hsizer1.SetItemMinSize(lab1, (w, -1))
        
        hsizer2 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer2.Add(lab2, 0, wx.RIGHT, b)
        hsizer2.Add(txt2, 1, wx.GROW, b)
        hsizer2.SetItemMinSize(lab2, (w, -1))

        hsizer3 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer3.Add(lab3, 0, wx.RIGHT, b)
        hsizer3.Add(txt3, 1, wx.GROW, b)
        hsizer3.SetItemMinSize(lab3, (w, -1))

        hsizer4 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer4.Add(lab4, 0, wx.RIGHT, b)
        hsizer4.Add(txt4, 1, wx.GROW, b)
        hsizer4.SetItemMinSize(lab4, (w, -1))

        hsizer5 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer5.Add(b1, 0)
        hsizer5.Add(b2, 0, wx.LEFT, 10)
        
        b = 5
        vsizer1 = wx.BoxSizer(wx.VERTICAL)
        vsizer1.Add(hsizer1, 0, wx.EXPAND | wx.ALL, b)
        vsizer1.Add(hsizer2, 0, wx.EXPAND | wx.ALL, b)
        vsizer1.Add(hsizer3, 0, wx.EXPAND | wx.ALL, b)
        vsizer1.Add(hsizer4, 0, wx.EXPAND | wx.ALL, b)
        vsizer1.Add(staline, 0, wx.GROW | wx.ALL, b)
        vsizer1.Add(hsizer5, 0, wx.ALIGN_RIGHT | wx.ALL, b)
        
        self.SetSizer(vsizer1)

#-------------------------------------------------------------------

#~ ???
#~ r = self.pa1.GetWindowStyleFlag()
#~ r = r | wx.FULL_REPAINT_ON_RESIZE
#~ print 'r:', r
#~ self.pa1.SetWindowStyleFlag(r)
#~ self.pa1.Refresh()
#~ self.Refresh()

class MyNotebook(wx.Notebook):
    
    def __init__(self, parent, id):
        sty = wx.NB_TOP | wx.NB_MULTILINE
        wx.Notebook.__init__(self, parent, id, style=sty)
        
        self.pa1 = MyPanel13A(self)
        self.AddPage(self.pa1, 'MyPanel112A')

        self.pa2 = MyPanel16A(self)
        self.AddPage(self.pa2, 'MyPanel115A')

#-------------------------------------------------------------------

class MyPanel1(wx.Panel):
    
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, wx.ID_ANY)

        self.nb = MyNotebook(self, wx.ID_ANY)

        vsizer = wx.BoxSizer(wx.VERTICAL)
        vsizer.Add(self.nb, 1, wx.EXPAND | wx.ALL, 0)
        self.SetSizer(vsizer)

#-------------------------------------------------------------------

class MyPanel2(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent, wx.ID_ANY)

        self.nb = MyNotebook(self, wx.ID_ANY)
        
        b1 = wx.Button(self, wx.NewId(), '&OK')
        b2 = wx.Button(self, wx.NewId(), '&Cancel')

        hsizer5 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer5.Add(b1, 0)
        hsizer5.Add(b2, 0, wx.LEFT, 10)

        b = 8
        vsizer = wx.BoxSizer(wx.VERTICAL)
        vsizer.Add(self.nb, 1, wx.EXPAND | wx.TOP, b)
        vsizer.Add(hsizer5, 0, wx.ALIGN_RIGHT | wx.ALL, b)
        
        self.SetSizer(vsizer)

#-------------------------------------------------------------------

if __name__ == "__main__":

    import baseframe
    
    app = wx.PySimpleApp()
    frame = baseframe.MyFrame(None, panel=MyPanel1)
    frame.Show()
    app.MainLoop()

#eof-----------------------------------------------------------------

