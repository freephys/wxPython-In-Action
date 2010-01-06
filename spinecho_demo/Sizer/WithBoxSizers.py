# -*- coding: iso-8859-1 -*-
#--------------------------------------------------------------------
# Name:      WithBoxSizers.py
# Purpose:   An application to learn sizers
# Author:    Jean-Michel Fauth, Switzerland
# Copyright: (c) 2007-2008 Jean-Michel Fauth
# Licence:   None
# os dev:    winXP sp2
# py dev:    Python 2.5.4
# wx dev:    wxPython 2.8.9.1-ansi
# Revision:  27 December 2008
#--------------------------------------------------------------------

# Mainly BoxSizers
# Beginners: start here

#--------------------------------------------------------------------

import os
import wx
from colourwindow import ColWin

#--------------------------------------------------------------------

# The simpliest sizer, 1 ColWin.
# Use of named arguments in sizers.

class MyPanel1(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        
        wgreen = ColWin(self, wx.ID_ANY, wx.GREEN)
        
        b = 20
        vsizer1 = wx.BoxSizer(orient=wx.VERTICAL)
        # or
        # vsizer1 = wx.BoxSizer(orient=wx.HORIZONTAL)
        vsizer1.Add(item=wgreen, proportion=1, flag=wx.EXPAND | wx.ALL, border=b)
        self.SetSizer(vsizer1)

#-------------------------------------------------------------------

# 2 ColWins, vertically.

class MyPanel2(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        
        wred = ColWin(self, wx.ID_ANY, wx.RED)
        wblue = ColWin(self, wx.ID_ANY, wx.BLUE)
        
        b = 5
        vsizer1 = wx.BoxSizer(wx.VERTICAL)
        vsizer1.Add(wred, 1, wx.EXPAND | wx.ALL, b)
        vsizer1.Add(wblue, 1, wx.EXPAND | wx.ALL, b)
        self.SetSizer(vsizer1)

#-------------------------------------------------------------------

# 3 ColWins, horizontally.

class MyPanel3(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        
        wred = ColWin(self, wx.ID_ANY, wx.RED)
        wblue = ColWin(self, wx.ID_ANY, wx.BLUE)
        wgreen = ColWin(self, wx.ID_ANY, wx.GREEN)
        
        b = 5
        hsizer1 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer1.Add(wred, 1, wx.EXPAND | wx.ALL, b)
        hsizer1.Add(wblue, 1, wx.EXPAND | wx.ALL, b)
        hsizer1.Add(wgreen, 1, wx.EXPAND | wx.ALL, b)
        self.SetSizer(hsizer1)

#-------------------------------------------------------------------

# 3 ColWins, horizontally, height ratio 1:2:3.

class MyPanel4(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        
        wred = ColWin(self, wx.ID_ANY, wx.RED)
        wblue = ColWin(self, wx.ID_ANY, wx.BLUE)
        wgreen = ColWin(self, wx.ID_ANY, wx.GREEN)
        
        b = 5
        hsizer1 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer1.Add(wred, 1, wx.EXPAND | wx.ALL, b)
        hsizer1.Add(wblue, 2, wx.EXPAND | wx.ALL, b)
        hsizer1.Add(wgreen, 3, wx.EXPAND | wx.ALL, b)
        self.SetSizer(hsizer1)

#-------------------------------------------------------------------

# 2 ColWins, vertically, a fixed width of 50 pixels between the two items.

class MyPanel5(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        
        wred = ColWin(self, wx.ID_ANY, wx.RED)
        wblue = ColWin(self, wx.ID_ANY, wx.BLUE)
        
        b = 5
        vsizer1 = wx.BoxSizer(wx.VERTICAL)
        vsizer1.Add(wred, 1, wx.EXPAND | wx.ALL, b)
#add a fixed width of 50 pixels between the two items.        
        vsizer1.Add((-1, 50), 0,  wx.ALL, b)
        vsizer1.Add(wblue, 1, wx.EXPAND | wx.ALL, b)
        self.SetSizer(vsizer1)

#-------------------------------------------------------------------

# Two items, 1 ColWin and 1 Button, verically.
# The Button is either left/right aligned or centered.
# Comment / uncomment for testing the Button alignement.
# wx.ALIGN_LEFT is the default value.

class MyPanel6(wx.Panel):

    def __init__(self, parent):
        #~ wx.Panel.__init__(self, parent)
        wx.Panel.__init__(self, parent)

        wred = ColWin(self, wx.ID_ANY, wx.RED)
        b1 = wx.Button(self, wx.ID_ANY, 'button1')
        
        b = 5
        vsizer1 = wx.BoxSizer(wx.VERTICAL)
        vsizer1.Add(wred, 1, wx.EXPAND | wx.ALL, b)

        #~ vsizer1.Add(b1, 0, wx.ALIGN_LEFT | wx.ALL, b)
        #~ vsizer1.Add(b1, 0, wx.ALIGN_RIGHT | wx.ALL, b)
        vsizer1.Add(b1, 0, wx.ALIGN_CENTER | wx.ALL, b)
        self.SetSizer(vsizer1)

#-------------------------------------------------------------------

# 3 items, 1 ColWin and 2 Buttons.
# The Buttons are either left/right aligned or centered.

class MyPanel7(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        
        wred = ColWin(self, wx.ID_ANY, wx.RED)
        b1 = wx.Button(self, wx.ID_ANY, '&OK')
        b2 = wx.Button(self, wx.ID_ANY, '&Cancel')
        
        b = 10
        hsizer1 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer1.Add(b1, 0)
        hsizer1.Add(b2, 0, wx.LEFT, b)
        
        b = 5
        vsizer1 = wx.BoxSizer(wx.VERTICAL)
        vsizer1.Add(wred, 1, wx.EXPAND | wx.ALL, b)
#        vsizer1.Add(hsizer1, 0, wx.ALIGN_RIGHT | wx.ALL, b)
        vsizer1.Add(hsizer1, 0, wx.ALIGN_CENTER | wx.ALL, b)
        #~ vsizer1.Add(hsizer1, 0, wx.ALIGN_LEFT | wx.ALL, b)
        self.SetSizer(vsizer1)

#-------------------------------------------------------------------

# 4 items, 1 ColWin, 2 Buttons, 1 StaticLine.
# The Buttons are either left/right aligned or centered.
# The height of the static line == 2, the wx.GROW flag specifies an
# horizontal expansion, since the StaticLine is in a vertical sizer.

class MyPanel8(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        
        wred = ColWin(self, wx.ID_ANY, wx.RED)
        b1 = wx.Button(self, wx.ID_ANY, '&OK')
        b2 = wx.Button(self, wx.ID_ANY, '&Cancel')
        staline = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, (-1, 2), \
            wx.LI_HORIZONTAL)
        
        b = 5
        hsizer1 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer1.Add(b1, 0)
        hsizer1.Add(b2, 0, wx.LEFT, b)
        
        vsizer1 = wx.BoxSizer(wx.VERTICAL)
        vsizer1.Add(wred, 1, wx.EXPAND | wx.ALL, b)
        vsizer1.Add(staline, 0, wx.GROW | wx.ALL, b)
        vsizer1.Add(hsizer1, 0, wx.ALIGN_RIGHT | wx.ALL, b)
        self.SetSizer(vsizer1)

#-------------------------------------------------------------------

# 7 items, 2 ColWins and 5 Buttons.
# ColWin's: one is sizable, the other not.
# Buttons at the right of the frame.
# Something like a toolbar at the right.

class MyPanel9(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        wred = ColWin(self, wx.ID_ANY, wx.RED)
        wwhite = ColWin(self, wx.ID_ANY, wx.WHITE)

        b1 = wx.Button(self, wx.ID_ANY, '1')
        b2 = wx.Button(self, wx.ID_ANY, '2')
        b3 = wx.Button(self, wx.ID_ANY, '3')
        b4 = wx.Button(self, wx.ID_ANY, '4')
        b5 = wx.Button(self, wx.ID_ANY, '5')

        vsizer1 = wx.BoxSizer(wx.VERTICAL)
        b = 3
        vsizer1.Add(wred, 1, wx.EXPAND | wx.BOTTOM, b)
        vsizer1.Add(wwhite, 0, wx.EXPAND, b)

        vsizer2 = wx.BoxSizer(wx.VERTICAL)
        b = 5
        vsizer2.Add(b1, 0, wx.BOTTOM, b)
        vsizer2.Add(b2, 0, wx.BOTTOM, b)
        vsizer2.Add(b3, 0, wx.BOTTOM, b)
        vsizer2.Add(b4, 0, wx.BOTTOM, b)
        vsizer2.Add(b5, 0, wx.BOTTOM, b)

        hsizer1 = wx.BoxSizer(wx.HORIZONTAL)
        b = 10
        hsizer1.Add(vsizer1, 1, wx.EXPAND | wx.LEFT | wx.TOP | wx.BOTTOM, b)
        hsizer1.Add(vsizer2, 0, wx.EXPAND| wx.ALL, b)
#        hsizer1.SetSizeHints(self)

        self.SetSizer(hsizer1)

#-------------------------------------------------------------------

# 7 items, 2 ColWins and 5 Buttons.
# The ColWin's are sizable.
# The Buttons 1..4 have a fixed hight and a default width.
# The Button 5 is disabled and has an expandable size.
# Something like a toolbar at the top.
# Toolbar look.

class MyPanel10(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        wred = ColWin(self, wx.ID_ANY, wx.RED)
        wwhite = ColWin(self, wx.ID_ANY, wx.WHITE)

        h = 40
        b1 = wx.Button(self, wx.ID_ANY, '1', (-1, h))
        b2 = wx.Button(self, wx.ID_ANY, '2', wx.DefaultPosition, (-1, h))
        b3 = wx.Button(self, wx.ID_ANY, '3', wx.DefaultPosition, (-1, h))
        b4 = wx.Button(self, wx.ID_ANY, '4', wx.DefaultPosition, (-1, h))
        b5 = wx.Button(self, wx.ID_ANY, '', wx.DefaultPosition, (-1, h))
        b5.Enable(False)
        
        hsizer1 = wx.BoxSizer(wx.HORIZONTAL)
        b = 0
        f = wx.ALL
        hsizer1.Add(b1, 0, f, border=b)
        hsizer1.Add(b2, 0, f, border=b)
        hsizer1.Add(b3, 0, f, border=b)
        hsizer1.Add(b4, 0, f, border=b)
        hsizer1.Add(b5, 1, f | wx.EXPAND, b)

        b = 2
        hsizer2 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer2.Add(wred, 1, wx.EXPAND | wx.RIGHT, b)
        hsizer2.Add(wwhite, 1, wx.EXPAND | wx.LEFT, b)

        b = 5
        vsizer1 = wx.BoxSizer(wx.VERTICAL)
        vsizer1.Add(hsizer1, 0, wx.EXPAND, b)
        vsizer1.Add(hsizer2, 1, wx.ALL | wx.EXPAND, b)

        self.SetSizer(vsizer1)

#-------------------------------------------------------------------

# 3 ColWins, horizontally, 2 spacers with a fixed height.

class MyPanel11(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        
        wred = ColWin(self, wx.ID_ANY, wx.RED)
        wblue = ColWin(self, wx.ID_ANY, wx.BLUE)
        wgreen = ColWin(self, wx.ID_ANY, wx.GREEN)
        
        b = 0
        h = 20
        hsizer1 = wx.BoxSizer(wx.VERTICAL)
        hsizer1.Add(wred, 1, wx.EXPAND | wx.ALL, b)
# a fixed width of 20 pixels between the two items.        
        hsizer1.Add((-1, h))
        hsizer1.Add(wblue, 1, wx.EXPAND | wx.ALL, b)
        hsizer1.Add((-1, h))
        hsizer1.Add(wgreen, 1, wx.EXPAND | wx.ALL, b)
        self.SetSizer(hsizer1)

#-------------------------------------------------------------------

# 4 items, 1 ColWin, 3 Buttons.
# The buttons 1 and 3 are left/right aligned, the Button 2 is centered.
# Use of spacers to set a gap between the Buttons.
# Better way?

class MyPanel12(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        wgreen = ColWin(self, wx.ID_ANY, wx.NamedColour('green'))
        b1 = wx.Button(self, wx.ID_ANY, 'button1')
        b2 = wx.Button(self, wx.ID_ANY, 'button2')
        b3 = wx.Button(self, wx.ID_ANY, 'button3')
        
        b = 0
        hsizer1 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer1.Add(b1, 0, wx.ALL, b)
        hsizer1.AddStretchSpacer()
        hsizer1.Add(b2, 0, wx.ALL, b)
        hsizer1.AddStretchSpacer()
        hsizer1.Add(b3, 0, wx.ALL, b)

##        tip: this does not work
#        b = 100
#        hsizer1 = wx.BoxSizer(wx.HORIZONTAL)
#        hsizer1.Add(b1, 0, wx.ALIGN_LEFT, b)
#        hsizer1.Add(b2, 0, wx.ALIGN_CENTER, b)
#        hsizer1.Add(b3, 0, wx.ALIGN_RIGHT, b)

        b = 5
        vsizer2 = wx.BoxSizer(wx.VERTICAL)
        vsizer2.Add(wgreen, 1, wx.EXPAND | wx.ALL, b)
        vsizer2.Add(hsizer1, 0, wx.EXPAND | wx.ALL, b)
#        vsizer2.SetSizeHints(self)
        self.SetSizer(vsizer2)

#-------------------------------------------------------------------

# 4 items, 1 ColWin, 3 Buttons.
# The Buttons 1 and 3 are top/bottom aligned, the Button 2 is centered.
# Use of spacers to set a gap between the Buttons.
# Better way?

class MyPanel13(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        wgreen = ColWin(self, wx.ID_ANY, wx.NamedColour('green'))
        b1 = wx.Button(self, wx.ID_ANY, 'button1')
        b2 = wx.Button(self, wx.ID_ANY, 'button2')
        b3 = wx.Button(self, wx.ID_ANY, 'button3')
        
        b = 0
        vsizer1 = wx.BoxSizer(wx.VERTICAL)
        vsizer1.Add(b1, 0, wx.ALL, b)
        vsizer1.AddStretchSpacer()
        vsizer1.Add(b2, 0, wx.ALL, b)
        vsizer1.AddStretchSpacer()
        vsizer1.Add(b3, 0, wx.ALL, b)

        b = 5
        hsizer2 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer2.Add(vsizer1, 0, wx.EXPAND | wx.ALL, b)
        hsizer2.Add(wgreen, 1, wx.EXPAND | wx.ALL, b)
        self.SetSizer(hsizer2)

#-------------------------------------------------------------------

# An input box.

class MyPanel14(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.parent = parent
        
        s = 'abc' + os.linesep + 'def' + os.linesep + 'ghi'
        statxt = wx.StaticText(self, wx.ID_ANY, s)
        txt = wx.TextCtrl(self, wx.ID_ANY, 'input')
        staline = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, (-1, 2), wx.LI_HORIZONTAL)

        b1 = wx.Button(self, wx.ID_ANY, "&OK")
        b2 = wx.Button(self, wx.ID_ANY, "&Cancel")
        
        b = 10
        hsizer1 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer1.Add(b1, 0)
        hsizer1.Add(b2, 0, wx.LEFT, b)

        b = 5
        vsizer1 = wx.BoxSizer(wx.VERTICAL)
        vsizer1.Add(statxt, 0, wx.GROW | wx.ALL, b)
        vsizer1.Add(txt, 0, wx.GROW | wx.ALL, b)
        vsizer1.Add(staline, 0, wx.GROW | wx.ALL, b)
        vsizer1.Add(hsizer1, 0, wx.ALIGN_RIGHT | wx.ALL, b)
        vsizer1.SetMinSize((300, -1))
        
        self.SetSizerAndFit(vsizer1)
        self.parent.SetClientSize(vsizer1.GetSize())
        self.parent.CenterOnScreen()

#-------------------------------------------------------------------

# A message box.

class MyPanel15(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.parent = parent
        
        s = 'This is a rather long message with'
        s += (os.linesep + 'a lot of lines...')*20
        
        statxt = wx.StaticText(self, wx.ID_ANY, s)
        statxt.SetBackgroundColour(wx.WHITE)
        staline = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, (-1, 2), wx.LI_HORIZONTAL)
        b1 = wx.Button(self, wx.ID_ANY, "&OK")
        
        b = 5
        vsizer1 = wx.BoxSizer(wx.VERTICAL)
        vsizer1.Add(statxt, 1, wx.EXPAND | wx.ALL, b)
        vsizer1.Add(staline, 0, wx.GROW | wx.ALL, b)
        vsizer1.Add(b1, 0, wx.ALIGN_CENTER | wx.ALL, b)
        vsizer1.SetMinSize((200, -1))
        self.SetSizerAndFit(vsizer1)
        
        self.parent.SetClientSize(vsizer1.GetSize())
        self.parent.CenterOnScreen()

#-------------------------------------------------------------------

# A serie of couples, StaticTexts-TextCtrls.
# Buttons ok and cancel.
# This is not elegant. A better way: FlexGridSizer.

class MyPanel16(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.parent = parent

        self.SetFont(wx.Font(10, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False))

        lab1 = wx.StaticText(self, wx.ID_ANY, 'hydrogen :', style=wx.ALIGN_RIGHT)
        lab2 = wx.StaticText(self, wx.ID_ANY, 'tin :', style=wx.ALIGN_RIGHT)
        lab3 = wx.StaticText(self, wx.ID_ANY, 'mendelevium :', style=wx.ALIGN_RIGHT)
        lab4 = wx.StaticText(self, wx.ID_ANY, 'carbon :', style=wx.ALIGN_RIGHT)
        txt1 = wx.TextCtrl(self, wx.ID_ANY, '')
        txt2 = wx.TextCtrl(self, wx.ID_ANY, '')
        txt3 = wx.TextCtrl(self, wx.ID_ANY, '')
        txt4 = wx.TextCtrl(self, wx.ID_ANY, '')
        b1 = wx.Button(self, wx.ID_ANY, '&OK')
        b2 = wx.Button(self, wx.ID_ANY, '&Cancel')
        staline = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, (-1, 2), wx.LI_HORIZONTAL)
        
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
        
        self.SetSizerAndFit(vsizer1)
        self.parent.SetClientSize(vsizer1.GetSize())
        
#-------------------------------------------------------------------

# 1 Colwin.
# 4 buttons in a "toolbar". Button 2 and 3 are centered.

class MyPanel17(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        wgreen = ColWin(self, wx.ID_ANY, wx.NamedColour('green'))
        b1 = wx.Button(self, wx.ID_ANY, 'button1')
        b2 = wx.Button(self, wx.ID_ANY, 'button2')
        b3 = wx.Button(self, wx.ID_ANY, 'button3')
        b4 = wx.Button(self, wx.ID_ANY, 'button4')
        
        b = 0
        hsizer1a = wx.BoxSizer(wx.HORIZONTAL)
        hsizer1a.Add(b2, 0, wx.ALL, b)
        hsizer1a.Add(b3, 0, wx.ALL, b)
        
        b = 0
        hsizer1 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer1.Add(b1, 0, wx.ALL, b)
        hsizer1.AddStretchSpacer()
        hsizer1.Add(hsizer1a, 0, wx.ALL, b)
        hsizer1.AddStretchSpacer()
        hsizer1.Add(b4, 0, wx.ALL, b)

        b = 0
        hsizer1b = wx.BoxSizer(wx.HORIZONTAL)
        hsizer1b.AddStretchSpacer()
        hsizer1b.Add(wgreen, 1, wx.EXPAND | wx.ALL, b)
        hsizer1b.AddStretchSpacer()

        b = 5
        vsizer2 = wx.BoxSizer(wx.VERTICAL)
        vsizer2.Add(hsizer1, 0, wx.EXPAND | wx.ALL, b)
        vsizer2.Add(hsizer1b, 1, wx.EXPAND | wx.ALL, b)
        
        self.SetSizer(vsizer2)

#-------------------------------------------------------------------

# Five buttons in a vertical box sizer.
# Show the usage of wx.GROW instead of wx.EXPAND. The buttons grow
# only in the horizontal direction.

class MyPanel18(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.parent = parent
        
        b1 = wx.Button(self, wx.ID_ANY, 'a')
        b2 = wx.Button(self, wx.ID_ANY, 'text')
        b3 = wx.Button(self, wx.ID_ANY, 'long text')
        b4 = wx.Button(self, wx.ID_ANY, 'abc def ghi jkl mno pqr stu vwx yz')
        b5 = wx.Button(self, wx.ID_ANY, 'zz')

        b = 10
        vsizer1 = wx.BoxSizer(wx.VERTICAL)
        vsizer1.Add(b1, 0, wx.GROW | wx.ALL, b)
        vsizer1.Add(b2, 0, wx.GROW | wx.LEFT | wx.RIGHT | wx.BOTTOM, b)
        vsizer1.Add(b3, 0, wx.GROW | wx.LEFT | wx.RIGHT | wx.BOTTOM, b)
        vsizer1.Add(b4, 0, wx.GROW | wx.LEFT | wx.RIGHT | wx.BOTTOM, b)
        vsizer1.Add(b5, 0, wx.GROW | wx.LEFT | wx.RIGHT | wx.BOTTOM, b)

        #set the sizer
        self.SetSizerAndFit(vsizer1)
        #set the client size of the main frame
        #This sets the size of the window client area in pixels.
        #Using this function to size a window tends to be more device-independent
        #than wx.Window.SetSize
        self.parent.SetClientSize(vsizer1.GetSize())
        #get the size of the main frame
        r = self.parent.GetSize()
        #set the minimal size of the main frame
        self.parent.SetMinSize(r)
        #centering
        self.parent.CentreOnScreen()

#-------------------------------------------------------------------

# Three ColWins in a horizontal box sizer.
# Show the usage of wx.GROW instead of wx.EXPAND. The ColWins grow
# only in the vertical direction.

class MyPanel19(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.parent = parent

        wred = ColWin(self, wx.ID_ANY, wx.RED)
        wblue = ColWin(self, wx.ID_ANY, wx.BLUE)
        wgreen = ColWin(self, wx.ID_ANY, wx.GREEN)

        b = 10
        hsizer1 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer1.Add(wred, 0, wx.GROW | wx.ALL, b)
        hsizer1.Add(wblue, 0, wx.GROW | wx.TOP | wx.RIGHT | wx.BOTTOM, b)
        hsizer1.Add(wgreen, 0, wx.GROW | wx.TOP | wx.RIGHT | wx.BOTTOM, b)

        #force some widths of the coloured windows
        hsizer1.SetItemMinSize(wred, (100, -1))
        hsizer1.SetItemMinSize(wblue, (100, -1))
        hsizer1.SetItemMinSize(wgreen, (100, -1))

        #set a height, all ColWin have the same height.
        hsizer1.SetMinSize((-1, 300))

        #set the sizer
        self.SetSizerAndFit(hsizer1)
        #set the client size of the main frame
        self.parent.SetClientSize(hsizer1.GetSize())
        #get the size of the main frame
        r = self.parent.GetSize()
        #set the minimal size of the main frame
        self.parent.SetMinSize(r)
        #centering
        self.parent.CentreOnScreen()

#-------------------------------------------------------------------

# An input box with size constraints.
# Variant of MyPanel14.

class MyPanel20(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.parent = parent
        
        s = 'abc' + os.linesep + 'def' + os.linesep + 'ghi'
        statxt = wx.StaticText(self, wx.ID_ANY, s)
        txt = wx.TextCtrl(self, wx.ID_ANY, 'input')
        staline = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, (-1, 2), wx.LI_HORIZONTAL)

        b1 = wx.Button(self, wx.ID_ANY, "&OK")
        b2 = wx.Button(self, wx.ID_ANY, "&Cancel")
        
        b = 10
        hsizer1 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer1.Add(b1, 0)
        hsizer1.Add(b2, 0, wx.LEFT, b)

        b = 5
        vsizer1 = wx.BoxSizer(wx.VERTICAL)
        vsizer1.Add(statxt, 0, wx.GROW | wx.ALL, b)
        vsizer1.Add(txt, 0, wx.GROW | wx.ALL, b)
        vsizer1.Add(staline, 0, wx.GROW | wx.ALL, b)
        vsizer1.Add(hsizer1, 0, wx.ALIGN_RIGHT | wx.ALL, b)
        vsizer1.SetMinSize((300, -1))
        
        #set the sizer
        self.SetSizerAndFit(vsizer1)
        #get the size of the fit sizer
        r = vsizer1.GetSize()
        #set the client size of the parent frame
        self.parent.SetClientSize(r)
        #get the size of the parent frame
        r = self.parent.GetSize()
        #lock the vertical size and set a minimal horizontal size (200)
        self.parent.SetMinSize((200, r[1]))
        self.parent.SetMaxSize((-1, r[1]))
        #centre the parent frame
        self.parent.CenterOnScreen()

#-------------------------------------------------------------------

if __name__ == "__main__":

    import baseframe
    
    app = wx.PySimpleApp()
    frame = baseframe.MyFrame(None, panel=MyPanel)
    frame.Show()
    app.MainLoop()

#eof-----------------------------------------------------------------

