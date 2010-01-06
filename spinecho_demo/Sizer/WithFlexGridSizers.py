# -*- coding: iso-8859-1 -*-
#--------------------------------------------------------------------
# Name:      WithFlexGridSizers.py
# Purpose:   An application to learn sizers
# Author:    Jean-Michel Fauth, Switzerland
# Copyright: (c) 2007-2008 Jean-Michel Fauth
# Licence:   None
# os dev:    winXP sp2
# py dev:    Python 2.5.4
# wx dev:    wxPython 2.8.9.1-ansi
# Revision:  28 December 2008
#--------------------------------------------------------------------

# Mainly FlexGridSizers

#--------------------------------------------------------------------

import wx
from colourwindow import ColWin

#--------------------------------------------------------------------

# A FlexGridSizer.
# 4 ColWins as cells, all sizeable.

class MyPanel1(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        wred = ColWin(self, wx.ID_ANY, wx.RED)
        wblue = ColWin(self, wx.ID_ANY, wx.BLUE)
        wwhite = ColWin(self, wx.ID_ANY, wx.WHITE)
        wcyan = ColWin(self, wx.ID_ANY, wx.CYAN)

        hgap, vgap = 0, 0
        nrows, ncols = 2, 2
        fgs = wx.FlexGridSizer(nrows, ncols, hgap, vgap)
        
        b = 5
        fgs.AddMany([(wred, 1, wx.EXPAND | wx.ALL, b),
                     (wblue, 1, wx.EXPAND | wx.ALL, b),
                     (wwhite, 1, wx.EXPAND | wx.ALL, b),
                     (wcyan, 1, wx.EXPAND | wx.ALL, b),
                    ])

        # or
        #~ fgs.Add(wred, 1, wx.EXPAND | wx.ALL, b)
        #~ fgs.Add(wblue, 1, wx.EXPAND | wx.ALL, b)
        #~ fgs.Add(wwhite, 1, wx.EXPAND | wx.ALL, b)
        #~ fgs.Add(wcyan, 1, wx.EXPAND | wx.ALL, b)
        
        #set all rows and cols sizable, try to comment / uncomment
        fgs.AddGrowableRow(0)
        fgs.AddGrowableRow(1)
        fgs.AddGrowableCol(0)
        fgs.AddGrowableCol(1)
        
        self.SetSizer(fgs)
        
#-------------------------------------------------------------------

# A FlexgridSizer with 4 cells.
# The cell (0, 0) is a column of 3 Buttons.
# The cell (1, 1) is a row of 3 Buttons.
# The cell (1, 0) is empty.
# The cell (0, 1) is a ColWin.

class MyPanel2(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        wwhite = ColWin(self, wx.ID_ANY, wx.WHITE)
        b1 = wx.Button(self, wx.ID_ANY, 'button1')
        b2 = wx.Button(self, wx.ID_ANY, 'button2')
        b3 = wx.Button(self, wx.ID_ANY, 'button3')
        b4 = wx.Button(self, wx.ID_ANY, 'button4')
        b5 = wx.Button(self, wx.ID_ANY, 'button5')
        b6 = wx.Button(self, wx.ID_ANY, 'button6')
        
        b = 0
        hsizer1 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer1.Add(b1, 0, wx.ALL, b)
        hsizer1.Add((-1, -1), 1)
        hsizer1.Add(b2, 0, wx.ALL, b)
        hsizer1.Add((-1, -1), 1)
        hsizer1.Add(b3, 0, wx.ALL, b)

        b = 0
        vsizer1 = wx.BoxSizer(wx.VERTICAL)
        vsizer1.Add(b4, 0, wx.ALL, b)
        vsizer1.Add((-1, -1), 1)
        vsizer1.Add(b5, 0, wx.ALL, b)
        vsizer1.Add((-1, -1), 1)
        vsizer1.Add(b6, 0, wx.ALL, b)

        hgap, vgap = 0, 0
        nrows, ncols = 2, 2
        fgs = wx.FlexGridSizer(nrows, ncols, hgap, vgap)
        
        b = 5
        fgs.AddMany([(vsizer1, 1, wx.EXPAND | wx.ALL, b),
                     (wwhite, 1, wx.EXPAND | wx.ALL, b),
                     ((-1, -1), 1, wx.EXPAND | wx.ALL, b),
                     (hsizer1, 1, wx.EXPAND | wx.ALL, b),
                    ])

        #really tricky ;-)
        fgs.AddGrowableRow(0)
        fgs.AddGrowableCol(1)
        
        self.SetSizer(fgs)

#-------------------------------------------------------------------

# A FlexGridSizer of 9 cells (3x3) with 5 ColWins in cells and 4 empty cells.

class MyPanel3(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        wwhite = ColWin(self, wx.ID_ANY, wx.WHITE)
        wblue = ColWin(self, wx.ID_ANY, wx.BLUE)
        wgreen = ColWin(self, wx.ID_ANY, wx.GREEN)
        wcyan = ColWin(self, wx.ID_ANY, wx.CYAN)
        wred = ColWin(self, wx.ID_ANY, wx.RED)

        hgap, vgap = 0, 0
        nrows, ncols = 3, 3
        fgs = wx.FlexGridSizer(nrows, ncols, hgap, vgap)
        
        b = 5
        fgs.AddMany([(wwhite, 1, wx.EXPAND | wx.ALL, b),
                     ((-1, -1), 1, wx.EXPAND | wx.ALL, b),
                     (wblue, 1, wx.EXPAND | wx.ALL, b),
                     
                     ((-1, -1), 1, wx.EXPAND | wx.ALL, b),
                     (wgreen, 1, wx.EXPAND | wx.ALL, b),
                     ((-1, -1), 1, wx.EXPAND | wx.ALL, b),
                     
                     (wred, 1, wx.EXPAND | wx.ALL, b),
                     ((-1, -1), 1, wx.EXPAND | wx.ALL, b),
                     (wcyan, 1, wx.EXPAND | wx.ALL, b),
                    ])

        fgs.AddGrowableRow(0)
        fgs.AddGrowableRow(1)
        fgs.AddGrowableRow(2)
        
        fgs.AddGrowableCol(0)
        fgs.AddGrowableCol(1)
        fgs.AddGrowableCol(2)
        
        self.SetSizer(fgs)

#-------------------------------------------------------------------

# A FlexGridSizer of 9 cells (3x3) with 4 ColWins in cells and 5 empty cells.
# The rows 1 and 3 have a fixed size.

class MyPanel4(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)

        h = 40
        wwhite = ColWin(self, wx.ID_ANY, wx.WHITE)
        wblue = ColWin(self, wx.ID_ANY, wx.BLUE)
        wgreen = ColWin(self, wx.ID_ANY, wx.GREEN)
        wred = ColWin(self, wx.ID_ANY, wx.RED)

        hgap, vgap = 0, 0
        nrows, ncols = 3, 3
        fgs = wx.FlexGridSizer(nrows, ncols, hgap, vgap)
        
        b = 5
        fgs.AddMany([((-1, -1), 1, wx.EXPAND | wx.ALL, b),
                     (wwhite, 1, wx.EXPAND | wx.ALL, b),
                     ((-1, -1), 1, wx.EXPAND | wx.ALL, b),
                     
                     (wblue, 1, wx.EXPAND | wx.ALL, b),
                     ((-1, -1), 1, wx.EXPAND | wx.ALL, b),
                     (wgreen, 1, wx.EXPAND | wx.ALL, b),
                     
                     ((-1, -1), 1, wx.EXPAND | wx.ALL, b),
                     (wred, 1, wx.EXPAND | wx.ALL, b),
                     ((-1, -1), 1, wx.EXPAND | wx.ALL, b),
                    ])

        fgs.AddGrowableRow(1)
        
        fgs.AddGrowableCol(0)
        fgs.AddGrowableCol(1)
        fgs.AddGrowableCol(2)
        
        self.SetSizer(fgs)

#-------------------------------------------------------------------

class MyPanel5(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.parent = parent

        #~ self.SetFont(wx.Font(14, wx.DEFAULT, wx.NORMAL, wx.NORMAL, False))

        b1 = wx.Button(self, wx.ID_ANY, 'button1')
        b2 = wx.Button(self, wx.ID_ANY, 'aa bb cc')
        b3 = wx.Button(self, wx.ID_ANY, 'h')
        b4 = wx.Button(self, wx.ID_ANY, 'bibliothèque')
        b5 = wx.Button(self, wx.ID_ANY, 'xx F5')
        b6 = wx.Button(self, wx.ID_ANY, 'bu     tto      n5')
        b7 = wx.Button(self, wx.ID_ANY, 'but to       n5')
        b8 = wx.Button(self, wx.ID_ANY, 'bu tt         on5')
        b9 = wx.Button(self, wx.ID_ANY, 'bu      tto     n5')
        b10= wx.Button(self, wx.ID_ANY, 'button5')
        
        hgap, vgap = 0, 0
        nrows, ncols = 5, 2
        fgs = wx.FlexGridSizer(nrows, ncols, hgap, vgap)
        
        b = 0
        fgs.AddMany([(b1, 0, wx.EXPAND | wx.ALL, b),
                     (b2, 0, wx.EXPAND | wx.ALL, b),
                     (b3, 0, wx.EXPAND | wx.ALL, b),
                     (b4, 0, wx.EXPAND | wx.ALL, b),
                     (b5, 0, wx.EXPAND | wx.ALL, b),
                     (b6, 0, wx.EXPAND | wx.ALL, b),
                     (b7, 0, wx.EXPAND | wx.ALL, b),
                     (b8, 0, wx.EXPAND | wx.ALL, b),
                     (b9, 0, wx.EXPAND | wx.ALL, b),
                     (b10, 0, wx.EXPAND | wx.ALL, b),
                    ])

        self.SetSizerAndFit(fgs)
        
        #the items are not sizable, once set, pass the fitted size to the parent
        self.parent.SetClientSize(fgs.GetSize())
        self.parent.CenterOnScreen()

#-----------------------------------------------------------------

# 8 StaticTexts, 8 TextCtrls, 6 Buttons.
# To be used in a dialog window.

class MyPanel6(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.parent = parent

        lab1 = wx.StaticText(self, wx.ID_ANY, 'hydrogen:', style=wx.ALIGN_RIGHT)
        lab2 = wx.StaticText(self, wx.ID_ANY, 'tin :', style=wx.ALIGN_RIGHT)
        lab3 = wx.StaticText(self, wx.ID_ANY, 'mendelevium :', style=wx.ALIGN_RIGHT)
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
        b1 = wx.Button(self, wx.ID_ANY, '&Use')
        b2 = wx.Button(self, wx.ID_ANY, '&the')
        b3 = wx.Button(self, wx.ID_ANY, '&wonderful')
        b4 = wx.Button(self, wx.ID_ANY, '&sizer')
        b5 = wx.Button(self, wx.ID_ANY, '&world')
        b6 = wx.Button(self, wx.ID_ANY, '&Ok')
        staline = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, (-1, 2), wx.LI_HORIZONTAL)

        b = 10
        sizer1 = wx.FlexGridSizer(4, 4, b, b)
        sizer1.AddMany([ 
            (lab1, 1, wx.EXPAND | wx.ALL),
            (txt1, 1, wx.EXPAND | wx.ALL),
            (lab2, 1, wx.EXPAND | wx.ALL),
            (txt2, 1, wx.EXPAND | wx.ALL),
            
            (lab3, 1, wx.EXPAND | wx.ALL),
            (txt3, 1, wx.EXPAND | wx.ALL),
            (lab4, 1, wx.EXPAND | wx.ALL),
            (txt4, 1, wx.EXPAND | wx.ALL),
    
            (lab5, 1, wx.EXPAND | wx.ALL),
            (txt5, 1, wx.EXPAND | wx.ALL),
            (lab6, 1, wx.EXPAND | wx.ALL),
            (txt6, 1, wx.EXPAND | wx.ALL),
    
            (lab7, 1, wx.EXPAND | wx.ALL),
            (txt7, 1, wx.EXPAND | wx.ALL),
            (lab8, 1, wx.EXPAND | wx.ALL),
            (txt8, 1, wx.EXPAND | wx.ALL),
            ])

        #~ sizer1.AddGrowableCol(0)
        sizer1.AddGrowableCol(1)
        #~ sizer1.AddGrowableCol(2)
        sizer1.AddGrowableCol(3)

        sizer2 = wx.BoxSizer(wx.HORIZONTAL)
        b = 5
        sizer2.Add(b1, 0, border=b)
        sizer2.Add(b2, 0, wx.LEFT, b)
        sizer2.Add(b3, 0, wx.LEFT, b)
        sizer2.Add(b4, 0, wx.LEFT, b)
        sizer2.Add(b5, 0, wx.LEFT, b)
        sizer2.Add(b6, 0, wx.LEFT, b)

        sizer3 = wx.BoxSizer(wx.VERTICAL)
        b = 10
        sizer3.Add(staline, 0, wx.EXPAND, b)
        sizer3.Add(sizer1, 1, wx.GROW | wx.ALL, b)
        sizer3.Add(sizer2, 0, wx.ALIGN_CENTER | wx.ALL, b)

        # From the wxPython users list
        #~ So just call SetSizer, and then use sizer->GetMinSize() and 
        #~ frame->GetClientSize() and decide if to call frame->SetClientSize or not.

        self.SetSizer(sizer3)
        r1 = sizer3.GetMinSize()
        self.parent.SetClientSize(r1)
        
        #for tests
        #~ print r1
        #~ r2 = self.parent.GetClientSize()
        #~ print r2
        #~ self.parent.SetMinSize((-1, r1[1]))
        #~ r3 = self.parent.GetBestSize()
        #~ print r3
        #~ self.parent.SetMinSize(r2)
        
        #~ print sizer1.GetSize()
        #~ print sizer2.GetSize()
        #~ print sizer3.GetSize()
        
        #~ self.Layout()
        #~ print self.GetBestSize()
        #~ r = self.GetBestSize()
        #~ self.parent.SetClientSize(r)
        #~ self.parent.SetMinSize((-1, r[1]))
        #~ self.Fit()
        #~ self.SetSizerAndFit(sizer3)
        #~ self.parent.SetMinSize((-1, self.GetBestSize()[1]))

        #~ print sizer1.GetSize()
        #~ print sizer2.GetSize()
        #~ print sizer3.GetSize()

        #~ self.CentreOnParent()

#-----------------------------------------------------------------

# 16 Colwins as items.
# Toying with MinSize, SizeHints.

class MyPanel7(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.parent = parent

        wwhite1 = ColWin(self, wx.ID_ANY, wx.WHITE)
        wblue1 = ColWin(self, wx.ID_ANY, wx.BLUE)
        wgreen1 = ColWin(self, wx.ID_ANY, wx.GREEN)
        wcyan1 = ColWin(self, wx.ID_ANY, wx.CYAN)

        wwhite2 = ColWin(self, wx.ID_ANY, wx.WHITE)
        wblue2 = ColWin(self, wx.ID_ANY, wx.BLUE)
        wgreen2 = ColWin(self, wx.ID_ANY, wx.GREEN)
        wcyan2 = ColWin(self, wx.ID_ANY, wx.CYAN)
        
        wwhite3 = ColWin(self, wx.ID_ANY, wx.WHITE)
        wblue3 = ColWin(self, wx.ID_ANY, wx.BLUE)
        wgreen3 = ColWin(self, wx.ID_ANY, wx.GREEN)
        wcyan3 = ColWin(self, wx.ID_ANY, wx.CYAN)
        
        wwhite4 = ColWin(self, wx.ID_ANY, wx.WHITE)
        wblue4 = ColWin(self, wx.ID_ANY, wx.BLUE)
        wgreen4 = ColWin(self, wx.ID_ANY, wx.GREEN)
        wcyan4 = ColWin(self, wx.ID_ANY, wx.CYAN)

        hgap, vgap = 0, 0
        nrows, ncols = 4, 4
        fgs = wx.FlexGridSizer(nrows, ncols, hgap, vgap)
        
        b = 5
        fgs.AddMany([(wwhite1, 1, wx.EXPAND | wx.ALL, b),
                     (wblue1, 1, wx.EXPAND | wx.ALL, b),
                     (wgreen1, 1, wx.EXPAND | wx.ALL, b),
                     (wcyan1, 1, wx.EXPAND | wx.ALL, b),
                     
                     (wwhite2, 1, wx.EXPAND | wx.ALL, b),
                     (wblue2, 1, wx.EXPAND | wx.ALL, b),
                     (wgreen2, 1, wx.EXPAND | wx.ALL, b),
                     (wcyan2, 1, wx.EXPAND | wx.ALL, b),
                     
                     (wwhite3, 1, wx.EXPAND | wx.ALL, b),
                     (wblue3, 1, wx.EXPAND | wx.ALL, b),
                     (wgreen3, 1, wx.EXPAND | wx.ALL, b),
                     (wcyan3, 1, wx.EXPAND | wx.ALL, b),

                     (wwhite4, 1, wx.EXPAND | wx.ALL, b),
                     (wblue4, 1, wx.EXPAND | wx.ALL, b),
                     (wgreen4, 1, wx.EXPAND | wx.ALL, b),
                     (wcyan4, 1, wx.EXPAND | wx.ALL, b),
                    ])

        #~ fgs.AddGrowableRow(0)
        #~ fgs.AddGrowableRow(1)
        #~ fgs.AddGrowableRow(2)
        #~ fgs.AddGrowableRow(3)
        
        fgs.AddGrowableCol(0)
        fgs.AddGrowableCol(1)
        fgs.AddGrowableCol(2)
        fgs.AddGrowableCol(3)
        
        self.SetSizer(fgs)
        fgs.SetMinSize((400, -1))
        r = fgs.GetMinSize()
        self.parent.SetClientSize(r)

#-----------------------------------------------------------------

# A 3 x 3 flexgrid sizer.
# The item [1, 1] has a fixed sized. The others have a flexible size.

class MyPanel8(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.parent = parent

        ItemSize = (200, 100)
        
        wblue2 = ColWin(self, wx.ID_ANY, wx.BLUE)
        wblue2.SetSize(ItemSize)
        
        hgap, vgap = 0, 0
        nrows, ncols = 3, 3
        fgs = wx.FlexGridSizer(nrows, ncols, hgap, vgap)
        b = 0
        fgs.AddMany([(-1, -1),
                     (-1, -1),
                     (-1, -1), 
                     
                     (-1, -1),
                     (wblue2, 0, wx.ALL, b),
                     (-1, -1),
                     
                     (-1, -1),
                     (-1, -1),
                     (-1, -1),
                    ])

        fgs.AddGrowableRow(0)
        fgs.AddGrowableRow(2)
        fgs.AddGrowableCol(0)
        fgs.AddGrowableCol(2)
        
        self.SetSizer(fgs)
        
        self.parent.SetSize((500, 400))
        self.parent.CentreOnScreen()

#-----------------------------------------------------------------

# A 3 x 5 flexgrid sizer.
# The items [1, 1] and [1, 3] have a fixed sized. The others have a flexible size.

class MyPanel9(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.parent = parent

        ItemSize = (100, 100)
        
        wred = ColWin(self, wx.ID_ANY, wx.RED)
        wred.SetSize(ItemSize)
        wblue = ColWin(self, wx.ID_ANY, wx.BLUE)
        wblue.SetSize(ItemSize)
        
        hgap, vgap = 0, 0
        nrows, ncols = 3, 5
        fgs = wx.FlexGridSizer(nrows, ncols, hgap, vgap)
        b = 0
        fgs.AddMany([(-1, -1),
                     (-1, -1),
                     (-1, -1), 
                     (-1, -1), 
                     (-1, -1), 
                     
                     (-1, -1),
                     (wblue, 0, wx.ALL, b),
                     (-1, -1),
                     (wred, 0, wx.ALL, b),
                     (-1, -1),
                     
                     (-1, -1),
                     (-1, -1),
                     (-1, -1),
                     (-1, -1),
                     (-1, -1),
                    ])

        fgs.AddGrowableRow(0)
        fgs.AddGrowableRow(2)
        fgs.AddGrowableCol(0)
        fgs.AddGrowableCol(2)
        fgs.AddGrowableCol(4)
        
        self.SetSizer(fgs)
        
        self.parent.SetSize((500, 300))
        self.parent.CentreOnScreen()

#-----------------------------------------------------------------

# StaticText / TextCtrl pairs packed in a FlexGridSizer, fgs1
# fgs1 in centered
# fgs1 in sandwich between two ColWin's

class MyPanel10(wx.Panel):

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

        wblue = ColWin(self, wx.ID_ANY, wx.BLUE)
        wyellow = ColWin(self, wx.ID_ANY, '#ffff00')
        h = 50
        wblue.SetSize((-1, h))
        wyellow.SetSize((-1, h))
        
        hgap, vgap = 10, 6
        nrows, ncols = 8, 2
        fgs1 = wx.FlexGridSizer(nrows, ncols, hgap, vgap)
        fgs1.AddMany([ 
            (lab1, 1, wx.EXPAND | wx.ALL),
            (txt1, 1, wx.EXPAND | wx.ALL),
            
            (lab2, 1, wx.EXPAND | wx.ALL),
            (txt2, 1, wx.EXPAND | wx.ALL),
            
            (lab3, 1, wx.EXPAND | wx.ALL),
            (txt3, 1, wx.EXPAND | wx.ALL),
            
            (lab4, 1, wx.EXPAND | wx.ALL),
            (txt4, 1, wx.EXPAND | wx.ALL),
    
            (lab5, 1, wx.EXPAND | wx.ALL),
            (txt5, 1, wx.EXPAND | wx.ALL),
            
            (lab6, 1, wx.EXPAND | wx.ALL),
            (txt6, 1, wx.EXPAND | wx.ALL),
    
            (lab7, 1, wx.EXPAND | wx.ALL),
            (txt7, 1, wx.EXPAND | wx.ALL),
            
            (lab8, 1, wx.EXPAND | wx.ALL),
            (txt8, 1, wx.EXPAND | wx.ALL),
            ])

        b = 10
        hsizer1 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer1.AddStretchSpacer()
        hsizer1.Add(fgs1, 0, wx.TOP | wx.BOTTOM, b)
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
    frame = baseframe.MyFrame(None, panel=MyPanel1)
    frame.Show()
    app.MainLoop()

#eof-----------------------------------------------------------------



