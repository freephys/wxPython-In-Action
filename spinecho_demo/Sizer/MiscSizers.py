# -*- coding: iso-8859-1 -*-
#--------------------------------------------------------------------
# Name:      MiscSizers.py
# Purpose:   An application to learn sizers
# Author:    Jean-Michel Fauth, Switzerland
# Copyright: (c) 2007-2008 Jean-Michel Fauth
# Licence:   None
# os dev:    winXP sp2
# py dev:    Python 2.5.4
# wx dev:    wxPython 2.8.9.1-ansi
# Revision:  28 December 2008
#--------------------------------------------------------------------

# Mainly widgets other than Buttons, StaticTexts or TextCtrls

#--------------------------------------------------------------------


import os
import wx
from colourwindow import ColWin

#--------------------------------------------------------------------

# This exemple is coming from one of my application.
# The StaticTexts have either 5 or 2 lines, the sizes are forced.
# It may depends of the font size.

class MyPanel1(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.parent = parent

        self.SetFont(wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False))
        the = self.GetTextExtent('X')[1]
        he1 = 5 * the + 3
        he2 = 2 * the + 3
        
        nl = os.linesep
        txt1 = 'this' + nl + 'text' + nl + 'has' + nl + 'five' + nl + 'lines'
        txt2 = 'two' + nl + 'lines'

        staline = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, (-1, 2), wx.LI_HORIZONTAL)

        wwhite = ColWin(self, wx.ID_ANY, wx.WHITE)
        
        wcoral = wx.StaticText(self, wx.ID_ANY, txt1, wx.DefaultPosition, (-1, he1), wx.ST_NO_AUTORESIZE)
        wcoral.SetBackgroundColour(wx.NamedColour('coral'))
        
        wcyan = wx.StaticText(self, wx.ID_ANY, txt1, wx.DefaultPosition, (-1, he1), wx.ST_NO_AUTORESIZE)
        wcyan.SetBackgroundColour(wx.CYAN)

        wred = wx.StaticText(self, wx.ID_ANY, txt1, wx.DefaultPosition, (-1, he1), wx.ST_NO_AUTORESIZE)
        wred.SetBackgroundColour(wx.RED)

        wgreen = wx.StaticText(self, wx.ID_ANY, txt2, wx.DefaultPosition, (-1, he2), wx.ST_NO_AUTORESIZE)
        wgreen.SetBackgroundColour(wx.GREEN)

        wblue = wx.StaticText(self, wx.ID_ANY, txt2, wx.DefaultPosition, (-1, he2), wx.ST_NO_AUTORESIZE)
        wblue.SetBackgroundColour(wx.BLUE)

        vsizer1 = wx.BoxSizer(wx.VERTICAL)
        b = 4
        vsizer1.Add(wblue, 1, wx.EXPAND | wx.BOTTOM, b)
        vsizer1.Add(wgreen, 1, wx.EXPAND | wx.TOP, b)
        
        hsizer2 = wx.BoxSizer(wx.HORIZONTAL)
        b = 5
        hsizer2.Add(wcoral, 2, wx.EXPAND | wx.RIGHT, b)
        hsizer2.Add(wcyan, 3, wx.EXPAND | wx.RIGHT, b)
        hsizer2.Add(wred, 3, wx.EXPAND | wx.RIGHT, b)
        hsizer2.Add(vsizer1, 2, wx.EXPAND, border=b)
        
        vsizer3 = wx.BoxSizer(wx.VERTICAL)
        b = 5
        vsizer3.Add(staline, 0, wx.EXPAND | wx.ALL, 0)
        vsizer3.Add(wwhite, 1, wx.EXPAND | wx.TOP | wx.LEFT | wx.RIGHT, b)
        vsizer3.Add(hsizer2, 0, wx.EXPAND | wx.ALL, b)
        
        self.SetSizer(vsizer3)

#-------------------------------------------------------------------

# This shows the relation between the font size and the size of the
# widgets when sizers are used.

class MyPanel2(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.parent = parent
        
        fs = 20
        self.SetFont(wx.Font(fs, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False))

        statxt1 = wx.StaticText(self, wx.ID_ANY, 'one, two, three')
        statxt1.SetBackgroundColour(wx.WHITE)
        statxt2 = wx.StaticText(self, wx.ID_ANY, 'eins, zwei, drei')
        statxt2.SetBackgroundColour(wx.WHITE)
        statxt3 = wx.StaticText(self, wx.ID_ANY, 'un, deux, trois')
        statxt3.SetBackgroundColour(wx.WHITE)
        b1 = wx.Button(self, wx.ID_ANY, 'button1')
        b2 = wx.Button(self, wx.ID_ANY, 'button2')

        b = 5
        hsizer1 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer1.Add(b1, 1, wx.EXPAND | wx.ALL, b)
        hsizer1.Add(b2, 1, wx.EXPAND | wx.ALL, b)
        
        vsizer1 = wx.BoxSizer(wx.VERTICAL)
        vsizer1.Add(statxt1, 0, wx.ALL, b)
        vsizer1.Add(statxt2, 0, wx.ALL, b)
        vsizer1.Add(statxt3, 0, wx.ALL, b)
        vsizer1.Add(hsizer1, 0, wx.ALL |wx.ALIGN_CENTER, b)
        
        self.SetSizerAndFit(vsizer1)
        self.parent.SetClientSize(vsizer1.GetSize())

#-------------------------------------------------------------------

# 2 ColWins, 2 Buttons and 2 ComboBoxes.
# Important: the ComboBoxes have a wx.CB_DROPDOWN style. They behave like a TextCtrl.

# Q: is there a way to set a max size for an item? Problem: too long item
# in a ComboBox. SetMaxSize does not seem to work.

class MyPanel3(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.parent = parent

        #~ self.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False))

        wblue = ColWin(self, wx.ID_ANY, wx.BLUE)
        wred = ColWin(self, wx.ID_ANY, wx.RED)

        b1 = wx.Button(self, wx.ID_ANY, 'button1')
        b2 = wx.Button(self, wx.ID_ANY, 'button2')

        sty = wx.CB_DROPDOWN
        sty = wx.CB_READONLY
        maxsi = (100, -1)
        ch1 = ['alpha', 'beta', 'gamma']
        cb1 = wx.ComboBox(self, wx.ID_ANY, ch1[0], choices=ch1, style=sty)
        #~ cb1.SetMaxSize(maxsi)
        ch2 = ['aaa', 'bb bb', 'ccc ccc ccc']
        cb2 = wx.ComboBox(self, wx.ID_ANY, ch2[0], choices=ch2, style=sty)
        #~ cb2.SetMaxSize(maxsi)

        b = 5
        
        hsizer1 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer1.Add(b1, 0, wx.ALL, b)
        hsizer1.Add(wblue, 1, wx.EXPAND | wx.ALL, b)
        hsizer1.Add(cb1, 1, wx.EXPAND | wx.ALL, b)

        hsizer2 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer2.Add(cb2, 1, wx.EXPAND | wx.ALL, b)
        hsizer2.Add(b2, 0, wx.ALL, b)
        hsizer2.Add(wred, 1, wx.EXPAND | wx.ALL, b)

        vsizer1 = wx.BoxSizer(wx.VERTICAL)
        vsizer1.Add(hsizer1, 0, wx.EXPAND | wx.ALL, b)
        vsizer1.Add(hsizer2, 0, wx.EXPAND | wx.ALL, b)

        self.SetSizerAndFit(vsizer1)
        self.parent.SetClientSize(vsizer1.GetSize())

#-------------------------------------------------------------------

# 2 ColWins, 2 Buttons and 2 ComboBoxes.
# Important: the comboxes have a wx.CB_SIMPLE style.

# A lot of problems here? What's wrong?

class MyPanel4(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.parent = parent

        #~ self.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False))

        wblue = ColWin(self, wx.ID_ANY, wx.BLUE)
        wred = ColWin(self, wx.ID_ANY, wx.RED)

        b1 = wx.Button(self, wx.ID_ANY, 'button1')
        b2 = wx.Button(self, wx.ID_ANY, 'button2')

        sty = wx.CB_SIMPLE

        si = (-1, 50)
        ch1 = ['alpha', 'beta', 'gamma']
        cb1 = wx.ComboBox(self, wx.ID_ANY, ch1[0], size=si, choices=ch1, style=sty)
        #~ cb1.SetMaxSize((100, 200)) # does not help
        ch2 = ['aaa', 'bb bb', 'ccc ccc ccc']
        cb2 = wx.ComboBox(self, wx.ID_ANY, ch2[0], choices=ch2, style=sty)

        b = 5

        hsizer1 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer1.Add(b1, 0, wx.ALL, b)
        hsizer1.Add(wblue, 1, wx.EXPAND | wx.ALL, b)
        hsizer1.Add(cb1, 0, wx.EXPAND | wx.ALL, b)
        #~ hsizer1.Add(cb1, 0, wx.ALL, b)

        hsizer2 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer2.Add(cb2, 1, wx.EXPAND | wx.ALL, b)
        hsizer2.Add(b2, 0, wx.ALL, b)
        hsizer2.Add(wred, 1, wx.EXPAND | wx.ALL, b)

        vsizer1 = wx.BoxSizer(wx.VERTICAL)
        vsizer1.Add(hsizer1, 0, wx.EXPAND | wx.ALL, b)
        vsizer1.Add(hsizer2, 0, wx.EXPAND | wx.ALL, b)

        self.SetSizer(vsizer1)
        
        #~ self.SetSizerAndFit(vsizer1)
        #~ self.parent.SetClientSize(vsizer1.GetSize())

#--------------------------------------------------------------------

# Problem?

class MyPanel5(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.parent = parent

        wblue = ColWin(self, wx.ID_ANY, wx.BLUE)

        sty = wx.CB_SIMPLE
        ch1 = ['alpha', 'beta', 'gamma']
        #~ cb1 = wx.ComboBox(self, wx.ID_ANY, ch1[0], size=(100, 200), choices=ch1, style=sty)
        cb1 = wx.ComboBox(self, wx.ID_ANY, ch1[0], size=(-1, -1), choices=ch1, style=sty)

        b = 5
        vsizer1 = wx.BoxSizer(wx.VERTICAL)
        vsizer1.Add(cb1, 1, wx.EXPAND | wx.ALL, b)
        vsizer1.SetItemMinSize(cb1, (100, 100))
        vsizer1.Add((-1, 50))
        vsizer1.Add(wblue, 1, wx.EXPAND | wx.ALL, b)
        
        self.SetSizer(vsizer1)
        
        #~ self.SetSizerAndFit(vsizer1)
        #~ self.parent.SetClientSize(vsizer1.GetSize())

#-------------------------------------------------------------------

# 2 ColWins, 2 Buttons and 2 ListBoxes.

class MyPanel6(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.parent = parent
        
        #~ self.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False))

        wblue = ColWin(self, wx.ID_ANY, wx.BLUE)
        wred = ColWin(self, wx.ID_ANY, wx.RED)

        b1 = wx.Button(self, wx.ID_ANY, 'button1')
        b2 = wx.Button(self, wx.ID_ANY, 'button2')

        sty = wx.LB_SINGLE

        ch1 = ['alpha', 'beta', 'gamma']
        lb1 = wx.ListBox(self, wx.ID_ANY, size=(-1, 50), choices=ch1, style=sty)
        ch2 = ['aaa', 'bb bb', 'ccc ccc ccc', 'ddd', 'eee', 'fff', 'ggg', 'hhh', 'iii', 'jjj']
        lb2 = wx.ListBox(self, wx.ID_ANY, choices=ch2, style=sty)

        b = 5

        hsizer1 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer1.Add(b1, 0, wx.ALL, b)
        hsizer1.Add(wblue, 1, wx.EXPAND | wx.ALL, b)
        hsizer1.Add(lb1, 0, wx.EXPAND | wx.ALL, b)

        hsizer2 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer2.Add(lb2, 1, wx.EXPAND | wx.ALL, b)
        hsizer2.Add(b2, 0, wx.ALL, b)
        hsizer2.Add(wred, 1, wx.EXPAND | wx.ALL, b)

        vsizer1 = wx.BoxSizer(wx.VERTICAL)
        # Listbox1 is not expanded and keep its size.
        #~ vsizer1.Add(hsizer1, 0, wx.EXPAND | wx.ALL, b)
        # Listbox1 is expanded.
        vsizer1.Add(hsizer1, 1, wx.EXPAND | wx.ALL, b)
        vsizer1.Add(hsizer2, 1, wx.EXPAND | wx.ALL, b)

        self.SetSizer(vsizer1)

#-----------------------------------------------------------------

if __name__ == "__main__":

    import baseframe
    
    app = wx.PySimpleApp()
    frame = baseframe.MyFrame(None, panel=MyPanel1)
    frame.Show()
    app.MainLoop()

#eof----------------------------------------------------------------
