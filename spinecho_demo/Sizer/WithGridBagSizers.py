# -*- coding: iso-8859-1 -*-
#--------------------------------------------------------------------
# Name:      WithGridBagSizers.py
# Purpose:   An application to learn sizers
# Author:    Jean-Michel Fauth, Switzerland
# Copyright: (c) 2007-2008 Jean-Michel Fauth
# Licence:   None
# os dev:    winXP sp2
# py dev:    Python 2.5.4
# wx dev:    wxPython 2.8.9.1-ansi
# Revision:  27 December 2008
#--------------------------------------------------------------------

# Mainly GridBagSizers

#--------------------------------------------------------------------

import wx
from colourwindow import ColWin

#--------------------------------------------------------------------

# A GridBagSizer of 4 cells (2x2).
# Note: cell spanning is always specified.
# gbs.Add.__doc__ : Add(self, item, GBPosition pos, GBSpan span=DefaultSpan,
#                     int flag=0, int border=0, userData=None) -> wx.GBSizerItem.

class MyPanel1(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        wwhite = ColWin(self, wx.ID_ANY, wx.WHITE)
        wblue = ColWin(self, wx.ID_ANY, wx.BLUE)
        wgreen = ColWin(self, wx.ID_ANY, wx.GREEN)
        wred = ColWin(self, wx.ID_ANY, wx.RED)

        vgap, hgap = 10, 20
        gbs = wx.GridBagSizer(vgap, hgap)

        b = 0
        gbs.Add(wwhite, (0, 0), (1, 1), wx.EXPAND | wx.ALL, b)
        gbs.Add(wblue, (0, 1), (1, 1), wx.EXPAND | wx.ALL, b)
        gbs.Add(wgreen, (1, 0), (1, 1), wx.EXPAND | wx.ALL, b)
        gbs.Add(wred, (1, 1), (1, 1), wx.EXPAND | wx.ALL, b)

        gbs.AddGrowableRow(0)
        gbs.AddGrowableRow(1)
        gbs.AddGrowableCol(0)
        gbs.AddGrowableCol(1)
        
        self.SetSizer(gbs)

#-------------------------------------------------------------------

# A GridBagSizer of 9 cells (3x3).
# Note: cell spanning is always specified.
# vgap and hgap define the space between the cells and not between the
# cells and the border of the panel/frame. This example creates a constant
# spacing for all cells.

class MyPanel2(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        wwhite = ColWin(self, wx.ID_ANY, wx.WHITE)
        wblue = ColWin(self, wx.ID_ANY, wx.BLUE)
        wgreen = ColWin(self, wx.ID_ANY, wx.GREEN)
        wred = ColWin(self, wx.ID_ANY, wx.RED)
        wblack = ColWin(self, wx.ID_ANY, wx.BLACK)
        wpink = ColWin(self, wx.ID_ANY, wx.NamedColour('pink'))
        wyellow = ColWin(self, wx.ID_ANY, wx.NamedColour('yellow'))
        wcyan = ColWin(self, wx.ID_ANY, wx.NamedColour('cyan'))
        worange = ColWin(self, wx.ID_ANY, wx.NamedColour('orange'))

        vgap = hgap = 10
        gbs = wx.GridBagSizer(vgap, hgap)

        b = vgap
        gbs.Add(wwhite, (0, 0), (1, 1), wx.EXPAND | wx.LEFT | wx.TOP, b)
        gbs.Add(wblue, (0, 1), (1, 1), wx.EXPAND | wx.TOP, b)
        gbs.Add(wgreen, (0, 2), (1, 1), wx.EXPAND | wx.RIGHT | wx.TOP, b)
        
        gbs.Add(wred, (1, 0), (1, 1), wx.EXPAND | wx.LEFT, b)
        gbs.Add(wblack, (1, 1), (1, 1), wx.EXPAND)
        gbs.Add(wpink, (1, 2), (1, 1), wx.EXPAND | wx.RIGHT, b)

        gbs.Add(wyellow, (2, 0), (1, 1), wx.EXPAND | wx.LEFT | wx.BOTTOM, b)
        gbs.Add(wcyan, (2, 1), (1, 1), wx.EXPAND | wx.BOTTOM, b)
        gbs.Add(worange, (2, 2), (1, 1), wx.EXPAND | wx.RIGHT | wx.BOTTOM, b)

        gbs.AddGrowableRow(0)
        gbs.AddGrowableRow(1)
        gbs.AddGrowableRow(2)
        gbs.AddGrowableCol(0)
        gbs.AddGrowableCol(1)
        gbs.AddGrowableCol(2)
        
        self.SetSizer(gbs)

#--------------------------------------------------------------------

# Tip: do not use StaticLine in "grid sizers".
# Correction: Staticline now ok, from wxPython ?

class MyPanel3(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        wwhite = ColWin(self, wx.ID_ANY, wx.WHITE)
        wblue = ColWin(self, wx.ID_ANY, wx.BLUE)
        wgreen = ColWin(self, wx.ID_ANY, wx.GREEN)
        wred = ColWin(self, wx.ID_ANY, wx.RED)
        wblack = ColWin(self, wx.ID_ANY, wx.BLACK)
        wpink = ColWin(self, wx.ID_ANY, wx.NamedColour('pink'))
        wyellow = ColWin(self, wx.ID_ANY, wx.NamedColour('yellow'))
        wcyan = ColWin(self, wx.ID_ANY, wx.NamedColour('cyan'))
        worange = ColWin(self, wx.ID_ANY, wx.NamedColour('orange'))

        staline = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, (-1, 2), wx.LI_HORIZONTAL)

        vgap = hgap = 5
        gbs = wx.GridBagSizer(vgap, hgap)

        b = 10
        gbs.Add(wwhite, (0, 0), (1, 1), wx.EXPAND | wx.LEFT | wx.TOP, b)
        gbs.Add(wblue, (0, 1), (1, 1), wx.EXPAND | wx.TOP, b)
        gbs.Add(wgreen, (0, 2), (1, 1), wx.EXPAND | wx.RIGHT | wx.TOP, b)
        
        gbs.Add(wred, (1, 0), (1, 1), wx.EXPAND | wx.LEFT, b)
        gbs.Add(wblack, (1, 1), (1, 1), wx.EXPAND)
        gbs.Add(wpink, (1, 2), (1, 1), wx.EXPAND | wx.RIGHT, b)
        
        gbs.Add(staline, (2, 0), (1, 3), wx.EXPAND | wx.LEFT | wx.RIGHT, b)

        gbs.Add(wyellow, (3, 0), (1, 1), wx.EXPAND | wx.LEFT | wx.BOTTOM, b)
        gbs.Add(wcyan, (3, 1), (1, 1), wx.EXPAND | wx.BOTTOM, b)
        gbs.Add(worange, (3, 2), (1, 1), wx.EXPAND | wx.RIGHT | wx.BOTTOM, b)

        gbs.AddGrowableRow(0)
        gbs.AddGrowableRow(1)
        #gbs.AddGrowableRow(2) Staticline 
        gbs.AddGrowableRow(3)
        gbs.AddGrowableCol(0)
        gbs.AddGrowableCol(1)
        gbs.AddGrowableCol(2)
        
        self.SetSizer(gbs)
        
#-------------------------------------------------------------------

# - A GridBagSizer of 9 cells (3x3).

class MyPanel4(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        wwhite = ColWin(self, wx.ID_ANY, wx.WHITE)
        wblue = ColWin(self, wx.ID_ANY, wx.BLUE)
        wgreen = ColWin(self, wx.ID_ANY, wx.GREEN)
        wred = ColWin(self, wx.ID_ANY, wx.RED)
        wblack = ColWin(self, wx.ID_ANY, wx.BLACK)
        wpink = ColWin(self, wx.ID_ANY, wx.NamedColour('pink'))
        wyellow = ColWin(self, wx.ID_ANY, wx.NamedColour('yellow'))
        wcyan = ColWin(self, wx.ID_ANY, wx.NamedColour('cyan'))
        worange = ColWin(self, wx.ID_ANY, wx.NamedColour('orange'))

        vgap = hgap = 10
        gbs = wx.GridBagSizer(vgap, hgap)

        b = 0
        gbs.Add(wwhite, (0, 0), (1, 1), wx.EXPAND, b)
        gbs.Add(wblue, (0, 1), (1, 1), wx.EXPAND, b)
        gbs.Add(wgreen, (0, 2), (1, 1), wx.EXPAND, b)
        
        gbs.Add(wred, (1, 0), (1, 1), wx.EXPAND, b)
        gbs.Add(wblack, (1, 1), (1, 1), wx.EXPAND)
        gbs.Add(wpink, (1, 2), (1, 1), wx.EXPAND, b)

        gbs.Add(wyellow, (2, 0), (1, 1), wx.EXPAND, b)
        gbs.Add(wcyan, (2, 1), (1, 1), wx.EXPAND, b)
        gbs.Add(worange, (2, 2), (1, 1), wx.EXPAND, b)

        gbs.AddGrowableRow(0)
        gbs.AddGrowableRow(1)
        gbs.AddGrowableRow(2)
        gbs.AddGrowableCol(0)
        gbs.AddGrowableCol(1)
        gbs.AddGrowableCol(2)
        
        b = vgap
        vsizer1 = wx.BoxSizer(wx.VERTICAL)
        vsizer1.Add(gbs, 1, wx.EXPAND | wx.ALL, b)
        self.SetSizer(vsizer1)

#-------------------------------------------------------------------

# A GridBagSizer of 25 cells (5x5).
# Spanning.
# Cell (1, 1) is empty.
# Comment / uncomment code lines to test, adapt span argument.

class MyPanel5(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        wwhite = ColWin(self, wx.ID_ANY, wx.WHITE)
        # wblue = ColWin(self, wx.ID_ANY, wx.BLUE)
        # wgreen = ColWin(self, wx.ID_ANY, wx.GREEN)
        wred = ColWin(self, wx.ID_ANY, wx.RED)
        wblack = ColWin(self, wx.ID_ANY, wx.BLACK)
        
        wpink = ColWin(self, wx.ID_ANY, wx.NamedColour('pink'))
        # wyellow = ColWin(self, wx.ID_ANY, wx.NamedColour('yellow'))
        wcyan = ColWin(self, wx.ID_ANY, wx.NamedColour('cyan'))
        worange = ColWin(self, wx.ID_ANY, wx.NamedColour('orange'))
        wgold = ColWin(self, wx.ID_ANY, wx.NamedColour('gold'))

        wtan = ColWin(self, wx.ID_ANY, wx.NamedColour('tan'))
        wcoral = ColWin(self, wx.ID_ANY, wx.NamedColour('coral'))
        # wplum = ColWin(self, wx.ID_ANY, wx.NamedColour('plum'))
        wspringgreen = ColWin(self, wx.ID_ANY, wx.NamedColour('spring green'))
        # wbrown = ColWin(self, wx.ID_ANY, wx.NamedColour('brown'))

        wwheat = ColWin(self, wx.ID_ANY, wx.NamedColour('wheat'))
        # wvioletred = ColWin(self, wx.ID_ANY, wx.NamedColour('violet red'))
        # wgoldenrod = ColWin(self, wx.ID_ANY, wx.NamedColour('goldenrod'))
        wpalegreen = ColWin(self, wx.ID_ANY, wx.NamedColour('pale green'))
        # wyellowgreen = ColWin(self, wx.ID_ANY, wx.NamedColour('yellow green'))

        wnavy = ColWin(self, wx.ID_ANY, wx.NamedColour('navy'))
        wskyblue = ColWin(self, wx.ID_ANY, wx.NamedColour('sky blue'))
        wmagenta = ColWin(self, wx.ID_ANY, wx.NamedColour('magenta'))
        wkhaki = ColWin(self, wx.ID_ANY, wx.NamedColour('khaki'))
        # wslateblue = ColWin(self, wx.ID_ANY, wx.NamedColour('slate blue'))

        vgap = hgap = 10
        gbs = wx.GridBagSizer(vgap, hgap)

        b = 0
        gbs.Add(wwhite, (0, 0), (1, 3), wx.EXPAND | wx.ALL, b)
        # gbs.Add(wblue, (0, 1), (1, 1), wx.EXPAND | wx.ALL, b)
        # gbs.Add(wgreen, (0, 2), (1, 1), wx.EXPAND | wx.ALL, b)
        gbs.Add(wred, (0, 3), (1, 1), wx.EXPAND | wx.ALL, b)
        gbs.Add(wblack, (0, 4), (1, 1), wx.EXPAND | wx.ALL, b)

        gbs.Add(wpink, (1, 0), (1, 1), wx.EXPAND | wx.ALL, b)
        # gbs.Add(wyellow, (1, 1), (1, 1), wx.EXPAND | wx.ALL, b)
        gbs.Add(wcyan, (1, 2), (1, 1), wx.EXPAND | wx.ALL, b)
        gbs.Add(worange, (1, 3), (1, 1), wx.EXPAND | wx.ALL, b)
        gbs.Add(wgold, (1, 4), (4, 1), wx.EXPAND | wx.ALL, b)

        gbs.Add(wtan, (2, 0), (1, 1), wx.EXPAND | wx.ALL, b)
        gbs.Add(wcoral, (2, 1), (2, 2), wx.EXPAND | wx.ALL, b)
        # gbs.Add(wplum, (2, 2), (1, 1), wx.EXPAND | wx.ALL, b)
        gbs.Add(wspringgreen, (2, 3), (1, 1), wx.EXPAND | wx.ALL, b)
        # gbs.Add(wbrown, (2, 4), (1, 1), wx.EXPAND | wx.ALL, b)

        gbs.Add(wwheat, (3, 0), (1, 1), wx.EXPAND | wx.ALL, b)
        # gbs.Add(wvioletred, (3, 1), (1, 1), wx.EXPAND | wx.ALL, b)
        # gbs.Add(wgoldenrod, (3, 2), (1, 1), wx.EXPAND | wx.ALL, b)
        gbs.Add(wpalegreen, (3, 3), (1, 1), wx.EXPAND | wx.ALL, b)
        # gbs.Add(wyellowgreen, (3, 4), (1, 1), wx.EXPAND | wx.ALL, b)

        gbs.Add(wnavy, (4, 0), (1, 1), wx.EXPAND | wx.ALL, b)
        gbs.Add(wskyblue, (4, 1), (1, 1), wx.EXPAND | wx.ALL, b)
        gbs.Add(wmagenta, (4, 2), (1, 1), wx.EXPAND | wx.ALL, b)
        gbs.Add(wkhaki, (4, 3), (1, 1), wx.EXPAND | wx.ALL, b)
        # gbs.Add(wslateblue, (4, 4), (1, 1), wx.EXPAND | wx.ALL, b)

        gbs.AddGrowableRow(0)
        gbs.AddGrowableRow(1)
        gbs.AddGrowableRow(2)
        gbs.AddGrowableRow(3)
        gbs.AddGrowableRow(4)
        gbs.AddGrowableCol(0)
        gbs.AddGrowableCol(1)
        gbs.AddGrowableCol(2)
        gbs.AddGrowableCol(3)
        gbs.AddGrowableCol(4)
        
        self.SetSizer(gbs)

#-------------------------------------------------------------------

# A GridBagSizer of 16 cells (4x4).
# The third (index = 2) row and colom have a fixed size.

class MyPanel6(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        
        wwhite = ColWin(self, wx.ID_ANY, wx.WHITE)
        wblue = ColWin(self, wx.ID_ANY, wx.BLUE)
        wgreen = ColWin(self, wx.ID_ANY, wx.GREEN)
        wred = ColWin(self, wx.ID_ANY, wx.RED)
        
        wpink = ColWin(self, wx.ID_ANY, wx.NamedColour('pink'))
        wyellow = ColWin(self, wx.ID_ANY, wx.NamedColour('yellow'))
        wcyan = ColWin(self, wx.ID_ANY, wx.NamedColour('cyan'))
        worange = ColWin(self, wx.ID_ANY, wx.NamedColour('orange'))

        wtan = ColWin(self, wx.ID_ANY, wx.NamedColour('tan'))
        wcoral = ColWin(self, wx.ID_ANY, wx.NamedColour('coral'))
        wplum = ColWin(self, wx.ID_ANY, wx.NamedColour('plum'))
        wspringgreen = ColWin(self, wx.ID_ANY, wx.NamedColour('spring green'))

        wwheat = ColWin(self, wx.ID_ANY, wx.NamedColour('wheat'))
        wvioletred = ColWin(self, wx.ID_ANY, wx.NamedColour('violet red'))
        wgoldenrod = ColWin(self, wx.ID_ANY, wx.NamedColour('goldenrod'))
        wpalegreen = ColWin(self, wx.ID_ANY, wx.NamedColour('pale green'))

        vgap = hgap = 10
        gbs = wx.GridBagSizer(vgap, hgap)

        b = 0
        gbs.Add(wwhite, (0, 0), (1, 1), wx.EXPAND | wx.ALL, b)
        gbs.Add(wblue, (0, 1), (1, 1), wx.EXPAND | wx.ALL, b)
        gbs.Add(wgreen, (0, 2), (1, 1), wx.EXPAND | wx.ALL, b)
        gbs.Add(wred, (0, 3), (1, 1), wx.EXPAND | wx.ALL, b)

        gbs.Add(wpink, (1, 0), (1, 1), wx.EXPAND | wx.ALL, b)
        gbs.Add(wyellow, (1, 1), (1, 1), wx.EXPAND | wx.ALL, b)
        gbs.Add(wcyan, (1, 2), (1, 1), wx.EXPAND | wx.ALL, b)
        gbs.Add(worange, (1, 3), (1, 1), wx.EXPAND | wx.ALL, b)

        gbs.Add(wtan, (2, 0), (1, 1), wx.EXPAND | wx.ALL, b)
        gbs.Add(wcoral, (2, 1), (1, 1), wx.EXPAND | wx.ALL, b)
        gbs.Add(wplum, (2, 2), (1, 1), wx.EXPAND | wx.ALL, b)
        gbs.Add(wspringgreen, (2, 3), (1, 1), wx.EXPAND | wx.ALL, b)

        gbs.Add(wwheat, (3, 0), (1, 1), wx.EXPAND | wx.ALL, b)
        gbs.Add(wvioletred, (3, 1), (1, 1), wx.EXPAND | wx.ALL, b)
        gbs.Add(wgoldenrod, (3, 2), (1, 1), wx.EXPAND | wx.ALL, b)
        gbs.Add(wpalegreen, (3, 3), (1, 1), wx.EXPAND | wx.ALL, b)

        gbs.AddGrowableRow(0)
        gbs.AddGrowableRow(1)
        #~ gbs.AddGrowableRow(2)
        gbs.AddGrowableRow(3)
        gbs.AddGrowableCol(0)
        gbs.AddGrowableCol(1)
        #~ gbs.AddGrowableCol(2)
        gbs.AddGrowableCol(3)
        
        self.SetSizer(gbs)

#-----------------------------------------------------------------

# Test with small sized items.
# GrisBagSizer used for packing.
# Comparaison with a FlexGridSizer.
# -> If the items are too small, eg (10, 10), packing is ok, but sizer is smaller
# than the allowed minimal frame size, especially the width.

class MyPanel7(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.parent = parent

        wwhite = ColWin(self, wx.ID_ANY, wx.WHITE)
        wblue = ColWin(self, wx.ID_ANY, wx.BLUE)
        wgreen = ColWin(self, wx.ID_ANY, wx.GREEN)
        wred = ColWin(self, wx.ID_ANY, wx.RED)
        
        wpink = ColWin(self, wx.ID_ANY, wx.NamedColour('pink'))
        wyellow = ColWin(self, wx.ID_ANY, wx.NamedColour('yellow'))
        wcyan = ColWin(self, wx.ID_ANY, wx.NamedColour('cyan'))
        worange = ColWin(self, wx.ID_ANY, wx.NamedColour('orange'))

        wtan = ColWin(self, wx.ID_ANY, wx.NamedColour('tan'))
        wcoral = ColWin(self, wx.ID_ANY, wx.NamedColour('coral'))
        wplum = ColWin(self, wx.ID_ANY, wx.NamedColour('plum'))
        wspringgreen = ColWin(self, wx.ID_ANY, wx.NamedColour('spring green'))

        wwheat = ColWin(self, wx.ID_ANY, wx.NamedColour('wheat'))
        wvioletred = ColWin(self, wx.ID_ANY, wx.NamedColour('violet red'))
        wgoldenrod = ColWin(self, wx.ID_ANY, wx.NamedColour('goldenrod'))
        wpalegreen = ColWin(self, wx.ID_ANY, wx.NamedColour('pale green'))

        all = [wwhite, wblue, wgreen, wred, wpink, wyellow, wcyan, worange, \
               wtan, wcoral, wplum, wspringgreen, wwheat, wvioletred, \
               wgoldenrod, wpalegreen]
        for e in all:
            e.SetSize((10, 10))
        
        UseGridBagSizer = False
        UseGridBagSizer = True
        
        if UseGridBagSizer:
            print 'UseGridBagSizer'
            
            vgap, hgap = 0, 0
            b = 5
            f = wx.ALL
            
            gbs = wx.GridBagSizer(vgap, hgap)

            gbs.Add(wwhite, (0, 0), (1, 1), f, b)
            gbs.Add(wblue, (0, 1), (1, 1), f, b)
            gbs.Add(wgreen, (0, 2), (1, 1), f, b)
            gbs.Add(wred, (0, 3), (1, 1), f, b)

            gbs.Add(wpink, (1, 0), (1, 1), f, b)
            gbs.Add(wyellow, (1, 1), (1, 1), f, b)
            gbs.Add(wcyan, (1, 2), (1, 1), f, b)
            gbs.Add(worange, (1, 3), (1, 1), f, b)

            gbs.Add(wtan, (2, 0), (1, 1), f, b)
            gbs.Add(wcoral, (2, 1), (1, 1), f, b)
            gbs.Add(wplum, (2, 2), (1, 1), f, b)
            gbs.Add(wspringgreen, (2, 3), (1, 1), f, b)

            gbs.Add(wwheat, (3, 0), (1, 1), f, b)
            gbs.Add(wvioletred, (3, 1), (1, 1), f, b)
            gbs.Add(wgoldenrod, (3, 2), (1, 1), f, b)
            gbs.Add(wpalegreen, (3, 3), (1, 1), f, b)

            #self.SetSizer(gbs)
            self.parent.SetMinSize((0, 0))
            self.SetSizerAndFit(gbs)
            r = gbs.GetSize()
            self.parent.SetClientSize(r)
            self.parent.CentreOnScreen()
            
        if not UseGridBagSizer: #FlexGridSizer
            
            nrows, ncols = 4, 4
            vgap, hgap = 0, 0
            b = 5
            f = wx.ALL
            
            fgs = wx.FlexGridSizer(nrows, ncols, hgap, vgap)
        
            fgs.AddMany([
                        (wwhite, 0, f, b),
                        (wblue, 0, f, b),
                        (wgreen, 0, f, b),
                        (wred, 0, f, b),
                        
                        (wpink, 0, f, b),
                        (wyellow, 0, f, b),
                        (wcyan, 0, f, b),
                        (worange, 0, f, b),

                        (wtan, 0, f, b),
                        (wcoral, 0, f, b),
                        (wplum, 0, f, b),
                        (wspringgreen, 0, f, b),

                        (wwheat, 0, f, b),
                        (wvioletred, 0, f, b),
                        (wgoldenrod, 0, f, b),
                        (wpalegreen, 0, f, b),
                        ])

            self.SetSizerAndFit(fgs)
            r = fgs.GetSize()
            self.parent.SetClientSize(r)
            self.parent.CentreOnScreen()

#-----------------------------------------------------------------

# StaticText / TextCtrl pairs packed in a GridBagSizer, gbs1
# gbs1 in centered
# gbs1 in sandwich between two ColWin's
# Similar to WithFlexGridSizers.MyPanel10 (?)

class MyPanel8(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.parent = parent
        
        #widgets
        lab1 = wx.StaticText(self, wx.ID_ANY, 'hydrogen :', style=wx.ALIGN_RIGHT)
        lab2 = wx.StaticText(self, wx.ID_ANY, 'tin :', style=wx.ALIGN_RIGHT)
        s = ('mendelevium -- ' * 3).rstrip('- ') + ' :'
        lab3 = wx.StaticText(self, wx.ID_ANY, s, style=wx.ALIGN_RIGHT)
        lab4 = wx.StaticText(self, wx.ID_ANY, 'carbon :', style=wx.ALIGN_RIGHT)
        lab5 = wx.StaticText(self, wx.ID_ANY, 'nitrogen :', style=wx.ALIGN_RIGHT)
        lab6 = wx.StaticText(self, wx.ID_ANY, 'argon :', style=wx.ALIGN_RIGHT)
        lab7 = wx.StaticText(self, wx.ID_ANY, 'iron :', style=wx.ALIGN_RIGHT)
        lab8 = wx.StaticText(self, wx.ID_ANY, 'gold :', style=wx.ALIGN_RIGHT)
        txt1 = wx.TextCtrl(self, wx.ID_ANY, '')
        txt2 = wx.TextCtrl(self, wx.ID_ANY, '')
        txt3 = wx.TextCtrl(self, wx.ID_ANY, '')
        txt4 = wx.TextCtrl(self, wx.ID_ANY, '')
        txt5 = wx.TextCtrl(self, wx.ID_ANY, '')
        txt6 = wx.TextCtrl(self, wx.ID_ANY, '')
        txt7 = wx.TextCtrl(self, wx.ID_ANY, '')
        txt8 = wx.TextCtrl(self, wx.ID_ANY, '')

        lab0 = wx.StaticText(self, wx.ID_ANY, 'A few chemical elements', style=wx.ALIGN_CENTER)
        lab0.SetBackgroundColour('#f0f0f0')
        lab0.SetForegroundColour(wx.RED)
        tmpfo = lab0.GetFont()
        tmpfo.SetPointSize(int(tmpfo.GetPointSize() * 1.5))
        lab0.SetFont(tmpfo)

        wblue = ColWin(self, wx.ID_ANY, wx.BLUE)
        wyellow = ColWin(self, wx.ID_ANY, '#ffff00')
        h = 50
        wblue.SetSize((-1, h))
        wyellow.SetSize((-1, h))

        vgap, hgap = 4, 10
        gbs1 = wx.GridBagSizer(vgap, hgap)

        b = 0
        gbs1.Add(lab0, (0, 0), (1, 2), wx.EXPAND, b),
        
        gbs1.Add(lab1, (1, 0), (1, 1), wx.EXPAND | wx.ALL, b)
        gbs1.Add(txt1, (1, 1), (1, 1), wx.EXPAND | wx.ALL, b)

        gbs1.Add(lab2, (2, 0), (1, 1), wx.EXPAND | wx.ALL, b)
        gbs1.Add(txt2, (2, 1), (1, 1), wx.EXPAND | wx.ALL, b)
        
        gbs1.Add(lab3, (3, 0), (1, 1), wx.EXPAND | wx.ALL, b)
        gbs1.Add(txt3, (3, 1), (1, 1), wx.EXPAND | wx.ALL, b)

        gbs1.Add(lab4, (4, 0), (1, 1), wx.EXPAND | wx.ALL, b)
        gbs1.Add(txt4, (4, 1), (1, 1), wx.EXPAND | wx.ALL, b)

        gbs1.Add(lab5, (5, 0), (1, 1), wx.EXPAND | wx.ALL, b)
        gbs1.Add(txt5, (5, 1), (1, 1), wx.EXPAND | wx.ALL, b)

        gbs1.Add(lab6, (6, 0), (1, 1), wx.EXPAND | wx.ALL, b)
        gbs1.Add(txt6, (6, 1), (1, 1), wx.EXPAND | wx.ALL, b)

        gbs1.Add(lab7, (7, 0), (1, 1), wx.EXPAND | wx.ALL, b)
        gbs1.Add(txt7, (7, 1), (1, 1), wx.EXPAND | wx.ALL, b)

        gbs1.Add(lab8, (8, 0), (1, 1), wx.EXPAND | wx.ALL, b)
        gbs1.Add(txt8, (8, 1), (1, 1), wx.EXPAND | wx.ALL, b)

        b = 10
        hsizer1 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer1.AddStretchSpacer()
        hsizer1.Add(gbs1, 0, wx.TOP | wx.BOTTOM, b)
        hsizer1.AddStretchSpacer()

        b = 0
        vsizer1 = wx.BoxSizer(wx.VERTICAL)
        vsizer1.Add(wblue, 0, wx.GROW | wx.ALL, b)
        vsizer1.SetItemMinSize(wblue, (600, -1))
        vsizer1.Add(hsizer1, 0, wx.EXPAND | wx.ALL, b)
        vsizer1.Add(wyellow, 0, wx.GROW | wx.ALL, b)

        self.SetSizerAndFit(vsizer1)
        self.parent.SetClientSize(vsizer1.GetSize())


#-----------------------------------------------------------------

if __name__ == "__main__":

    import baseframe
    
    app = wx.PySimpleApp()
    frame = baseframe.MyFrame(None, panel=MyPanel8)
    frame.Show()
    app.MainLoop()

#eof----------------------------------------------------------------
