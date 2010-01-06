# -*- coding: iso-8859-1 -*-
#--------------------------------------------------------------------
# Name:      WithBoxSizersTwo.py
# Purpose:   An application to learn sizers
# Author:    Jean-Michel Fauth, Switzerland
# Copyright: (c) 2007-2008 Jean-Michel Fauth
# Licence:   None
# os dev:    winXP sp2
# py dev:    Python 2.5.4
# wx dev:    wxPython 2.8.9.1-ansi
# Revision:  27 December 2008
#--------------------------------------------------------------------

# Mainly BoxSizers, part two

#--------------------------------------------------------------------


import wx
from colourwindow import ColWin

#--------------------------------------------------------------------

# Three ColWins. The B width is fixed. A and C are expanded.
# AAAAAA | BBB
# AAAAAA | BBB
# -------+-----
# CCCCCCCCCCCC
# CCCCCCCCCCCC

class MyPanel1(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.parent = parent
        
        wred = ColWin(self, wx.ID_ANY, wx.RED)
        wblue = ColWin(self, wx.ID_ANY, wx.BLUE)
        #The B width is fixed to 200 pix
        wblue.SetSize((200, -1))
        wgreen = ColWin(self, wx.ID_ANY, wx.GREEN)
        
        b = 4
        
        hsizer1 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer1.Add(wred, 1, wx.EXPAND | wx.RIGHT, b)
        hsizer1.Add(wblue, 0, wx.GROW, b)

        vsizer1 = wx.BoxSizer(wx.VERTICAL)
        vsizer1.Add(hsizer1, 2, wx.EXPAND | wx.ALL, b)
        vsizer1.Add(wgreen, 3, wx.EXPAND | wx.LEFT | wx.RIGHT | wx.BOTTOM, b)

        self.SetSizerAndFit(vsizer1)
        self.parent.SetClientSize((500, 400))
        self.parent.SetMinSize((250, 100))
        self.parent.CenterOnScreen()

#-----------------------------------------------------------------

# Three ColWins. The a width is fixed. B and C are expanded.
# AAA | BBBBBBBB
# AAA | BBBBBBBB
# AAA + --------
# AAA | CCCCCCCC
# AAA | CCCCCCCC

class MyPanel2(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.parent = parent
        
        wred = ColWin(self, wx.ID_ANY, wx.RED)
        #The a width is fixed at 200 pix
        wred.SetSize((200, -1))
        wblue = ColWin(self, wx.ID_ANY, wx.BLUE)
        wgreen = ColWin(self, wx.ID_ANY, wx.GREEN)
        
        b = 4
        
        vsizer1 = wx.BoxSizer(wx.VERTICAL)
        vsizer1.Add(wblue, 1, wx.EXPAND | wx.BOTTOM, b)
        vsizer1.Add(wgreen, 2, wx.EXPAND, b)

        hsizer1 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer1.Add(wred, 0, wx.GROW | wx.LEFT | wx.TOP | wx.BOTTOM, b)
        hsizer1.Add(vsizer1, 1, wx.EXPAND | wx.ALL, b)

        self.SetSizerAndFit(hsizer1)
        self.parent.SetClientSize((500, 400))
        self.parent.SetMinSize((250, 100))
        self.parent.CenterOnScreen()

#-----------------------------------------------------------------

# A item (ColWin) with a fixed size, centered in the panel.
# Or "flexible" borders.
# Use a vertical boxsizer.

class MyPanel3(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.parent = parent

        ItemSize = (200, 100)
        wblue2 = ColWin(self, wx.ID_ANY, wx.BLUE)
        #A item (ColWin) with a fixed size
        wblue2.SetSize(ItemSize)

        vsizer1 = wx.BoxSizer(wx.VERTICAL)
        b = 0
        vsizer1.AddStretchSpacer()
        #~ vsizer1.Add((-1, -1), 1) #old
        #centered 
        vsizer1.Add(wblue2, 0, wx.ALIGN_CENTER | wx.ALL, b)
        vsizer1.AddStretchSpacer()
        #~ vsizer1.Add((-1, -1), 1) #old

        self.SetSizer(vsizer1)
        self.parent.SetClientSize((400, 400))
        self.parent.CenterOnScreen()

#-----------------------------------------------------------------

# Same as MyPanel3, but with an horizontal boxsizer.

class MyPanel4(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.parent = parent

        ItemSize = (200, 100)
        wblue2 = ColWin(self, wx.ID_ANY, wx.BLUE)
        wblue2.SetSize(ItemSize)

        hsizer1 = wx.BoxSizer(wx.HORIZONTAL)
        b = 0
        hsizer1.AddStretchSpacer()
        hsizer1.Add(wblue2, 0, wx.ALIGN_CENTER | wx.ALL, b)
        hsizer1.AddStretchSpacer()

        self.SetSizer(hsizer1)
        self.parent.SetClientSize((400, 400))
        self.parent.CenterOnScreen()

#-----------------------------------------------------------------

# Two separated items (ColWin) with fixed sized centered in the panel.
# Seems to need refreshing if the main frame is too narrow.

class MyPanel5(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.parent = parent

        ItemSize = (100, 100)
        wblue = ColWin(self, wx.ID_ANY, wx.BLUE)
        wblue.SetSize(ItemSize)
        wred = ColWin(self, wx.ID_ANY, wx.RED)
        wred.SetSize(ItemSize)

        hsizer1 = wx.BoxSizer(wx.HORIZONTAL)
        b = 0
        hsizer1.AddStretchSpacer()
        hsizer1.Add(wblue, 0, wx.ALL, b)
        hsizer1.AddStretchSpacer()
        hsizer1.Add(wred, 0, wx.ALL, b)
        hsizer1.AddStretchSpacer()

        vsizer1 = wx.BoxSizer(wx.VERTICAL)
        b = 0
        vsizer1.AddStretchSpacer()
        vsizer1.Add(hsizer1, 0, wx.EXPAND | wx.ALL, b)
        vsizer1.AddStretchSpacer()

        self.SetSizer(vsizer1)
        self.parent.SetClientSize((400, 400))
        self.parent.CenterOnScreen()

#-----------------------------------------------------------------

# Pairs of "labels" - "text entries" widgets with different styles.

class MyPanel6(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.parent = parent

        self.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, \
            wx.FONTWEIGHT_NORMAL, False, ''))
        
        col1 = '#ffff80'
        col2 = '#80ffff'
        s1 = 'abc pqlt ABC WMQ'
        s2 = s1 + ' :'
        ch = [s1, 'alpha', 'beta', 'gamma']

        #widgets and sizers for each couple
        
        lab1 = wx.StaticText(self, wx.ID_ANY, s2)
        lab1.SetBackgroundColour(col1)
        txt1 = wx.TextCtrl(self, wx.ID_ANY, s1)
        
        b = 5
        hsizer1 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer1.Add(lab1, 0, wx.RIGHT, b)
        hsizer1.Add(txt1, 1, wx.GROW)
        
        #-----
        sty = wx.SUNKEN_BORDER
        lab2 = wx.StaticText(self, wx.ID_ANY, s2, style=sty)
        lab2.SetBackgroundColour(col1)
        txt2 = wx.TextCtrl(self, wx.ID_ANY, s1)
        
        b = 5
        hsizer2 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer2.Add(lab2, 0, wx.RIGHT, b)
        hsizer2.Add(txt2, 1, wx.GROW)
        
        #-----
        sty = wx.SUNKEN_BORDER
        lab3 = wx.StaticText(self, wx.ID_ANY, s2, style=sty)
        lab3.SetBackgroundColour(wx.WHITE)
        lab3.SetBackgroundColour(col1)
        txt3 = wx.TextCtrl(self, wx.ID_ANY, s1)
        
        b = 5
        hsizer3 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer3.Add(lab3, 0, wx.RIGHT | wx.ALIGN_CENTRE_VERTICAL, b)
        hsizer3.Add(txt3, 1, wx.GROW)

        #-----
        lab4 = wx.StaticText(self, wx.ID_ANY, s2)
        lab4.SetBackgroundColour(col1)
        txt4 = wx.TextCtrl(self, wx.ID_ANY, s1)
        
        b = 5
        hsizer4 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer4.Add(lab4, 0, wx.RIGHT | wx.ALIGN_CENTRE_VERTICAL, b)
        hsizer4.Add(txt4, 1, wx.GROW)
        
        #-----
        lab5 = wx.StaticText(self, wx.ID_ANY, s2)
        lab5.SetBackgroundColour(col1)
        sty = wx.NO_BORDER
        txt5 = wx.TextCtrl(self, wx.ID_ANY, s1, style=sty)
        
        b = 5
        hsizer5 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer5.Add(lab5, 0, wx.RIGHT | wx.ALIGN_CENTRE_VERTICAL, b)
        hsizer5.Add(txt5, 1, wx.GROW)
        
        #-----
        lab6 = wx.StaticText(self, wx.ID_ANY, s2, style=wx.SIMPLE_BORDER)
        lab6.SetBackgroundColour(col1)
        sty = wx.NO_BORDER
        txt6 = wx.TextCtrl(self, wx.ID_ANY, s1, style=sty)
        
        b = 5
        hsizer6 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer6.Add(lab6, 0, wx.RIGHT | wx.ALIGN_CENTRE_VERTICAL, b)
        hsizer6.Add(txt6, 1, wx.GROW)
        
        #-----
        sty = wx.TE_READONLY
        txt77 = wx.TextCtrl(self, wx.ID_ANY, s2, style=sty)
        txt77.SetBackgroundColour(col2)
        realsi = txt77.GetTextExtent(txt77.GetValue())
        txt7 = wx.TextCtrl(self, wx.ID_ANY, s1)
        
        b = 5
        hsizer7 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer7.Add(txt77, 0, wx.RIGHT | wx.ALIGN_CENTRE_VERTICAL, b)
        hsizer7.Add(txt7, 1, wx.GROW)
        hsizer7.SetItemMinSize(txt77, realsi)
        
        #-----
        sty = wx.TE_READONLY | wx.SIMPLE_BORDER
        txt88 = wx.TextCtrl(self, wx.ID_ANY, s2, style=sty)
        txt88.SetBackgroundColour(col2)
        realsi = txt88.GetTextExtent(txt88.GetValue())
        txt8 = wx.TextCtrl(self, wx.ID_ANY, s1)
        
        b = 5
        hsizer8 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer8.Add(txt88, 0, wx.RIGHT | wx.ALIGN_CENTRE_VERTICAL, b)
        hsizer8.Add(txt8, 1, wx.GROW)
        hsizer8.SetItemMinSize(txt88, realsi)

        #-----
        lab9 = wx.StaticText(self, wx.ID_ANY, s2)
        lab9.SetBackgroundColour(col1)
        combo9 = wx.ComboBox(self, wx.ID_ANY, ch[0], choices=ch)
        
        b = 5
        hsizer9 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer9.Add(lab9, 0, wx.RIGHT | wx.ALIGN_CENTRE_VERTICAL, b)
        hsizer9.Add(combo9, 1, wx.GROW)

        # sizer and layout

        b = 8
        vsizer1 = wx.BoxSizer(wx.VERTICAL)
        vsizer1.Add(hsizer1, 0, wx.EXPAND | wx.ALL, b)
        vsizer1.Add(hsizer2, 0, wx.EXPAND | wx.ALL, b)
        vsizer1.Add(hsizer3, 0, wx.EXPAND | wx.ALL, b)
        vsizer1.Add(hsizer4, 0, wx.EXPAND | wx.ALL, b)
        vsizer1.Add(hsizer5, 0, wx.EXPAND | wx.ALL, b)
        vsizer1.Add(hsizer6, 0, wx.EXPAND | wx.ALL, b)
        vsizer1.Add(hsizer7, 0, wx.EXPAND | wx.ALL, b)
        vsizer1.Add(hsizer8, 0, wx.EXPAND | wx.ALL, b)
        vsizer1.Add(hsizer9, 0, wx.EXPAND | wx.ALL, b)
        
        self.SetSizer(vsizer1)

#-----------------------------------------------------------------

if __name__ == "__main__":

    import baseframe
    
    app = wx.PySimpleApp()
    frame = baseframe.MyFrame(None, panel=MyPanel1)
    frame.Show()
    app.MainLoop()

#eof-----------------------------------------------------------------
