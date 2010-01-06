# -*- coding: iso-8859-1 -*-
#--------------------------------------------------------------------
# Name:      StaticTextsInSizers.py
# Purpose:   An application to learn sizers
# Author:    Jean-Michel Fauth, Switzerland
# Copyright: (c) 2007-2008 Jean-Michel Fauth
# Licence:   None
# os dev:    winXP sp2
# py dev:    Python 2.5.4
# wx dev:    wxPython 2.8.9.1-ansi
# Revision:  28 December 2008
#--------------------------------------------------------------------

# Mainly StaticTexts in various sizers.
# StaticTexts are quite tricky => special module.

#--------------------------------------------------------------------

import os
import wx
from colourwindow import ColWin

#-------------------------------------------------------------------

# StaticTexts in a FlexGridSizer.
# StaticTexts with a single line.
# Texts in StaticTexts are defined before laying out.
# StaticTexts with default style.

class MyPanel1(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.parent = parent

        #by default, wx.ALIGN_LEFT and autoresize
        lab1 = wx.StaticText(self, wx.ID_ANY, 'hydrogen')
        lab2 = wx.StaticText(self, wx.ID_ANY, 'tin')
        lab3 = wx.StaticText(self, wx.ID_ANY, 'mendelevium')
        lab4 = wx.StaticText(self, wx.ID_ANY, 'carbon')
        lab5 = wx.StaticText(self, wx.ID_ANY, 'nitrogen')
        lab6 = wx.StaticText(self, wx.ID_ANY, 'argon')
        lab7 = wx.StaticText(self, wx.ID_ANY, 'iron')
        lab8 = wx.StaticText(self, wx.ID_ANY, 'platin')
        lab9 = wx.StaticText(self, wx.ID_ANY, 'cobalt')
        
        all = [lab1, lab2, lab3, lab4, lab5, lab6, lab7, lab8, lab9]
        for e in all:
            e.SetBackgroundColour((255, 255, 200))
            
        staline = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, (-1, 2), wx.LI_HORIZONTAL)
        b1 = wx.Button(self, wx.ID_ANY, 'button1')

        hgap, vgap = 10, 10
        nrows, ncols = 3, 3
        fgs = wx.FlexGridSizer(nrows, ncols, hgap, vgap)
        
        b = 0
        
        #statictexts fit the size of the texts, statictextzs are left aligned
        #~ f = wx.ALL
        #statictexts fit the size of the sizer, texts in statictexts are left aligned
        f = wx.ALL | wx.EXPAND
        #statictexts fit the size of the texts, statictexts are centered
        #~ f = wx.ALL | wx.ALIGN_CENTRE
        #statictexts fit the size of the sizer, texts in statictexts are left aligned
        #~ f = wx.ALL | wx.ALIGN_CENTRE | wx.EXPAND
        #statictexts fit the size of the texts, statictexts are right aligned
        #~ f = wx.ALL | wx.ALIGN_RIGHT
        #statictexts fit the size of the sizer, texts in statictexts are left aligned
        #~ f = wx.ALL | wx.ALIGN_RIGHT | wx.EXPAND

        fgs.AddMany([(lab1, 0, f, b),
                     (lab2, 0, f, b),
                     (lab3, 0, f, b),
                     
                     (lab4, 0, f, b),
                     (lab5, 0, f, b),
                     (lab6, 0, f, b),
                     
                     (lab7, 0, f, b),
                     (lab8, 0, f, b),
                     (lab9, 0, f, b),
                    ])

        #~ fgs.AddGrowableRow(0)
        #~ fgs.AddGrowableRow(1)
        #~ fgs.AddGrowableRow(2)
        fgs.AddGrowableCol(0)
        fgs.AddGrowableCol(1)
        fgs.AddGrowableCol(2)

        b = 10
        vsizer1 = wx.BoxSizer(wx.VERTICAL)
        vsizer1.Add(fgs, 0, wx.ALL | wx.EXPAND, border=b)
        vsizer1.Add(staline, 0, wx.EXPAND)
        vsizer1.Add(b1, 0, wx.ALL | wx.ALIGN_RIGHT, border=b)
        
        self.SetSizer(vsizer1)
        r = vsizer1.GetMinSize()
        self.parent.SetClientSize(r)
        self.parent.CentreOnScreen()

#-----------------------------------------------------------------

# StaticTexts in a FlexGridSizer.
# StaticTexts with a single line.
# Texts in StaticTexts are defined before laying out.
# StaticTexts with a defined style.

class MyPanel2(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.parent = parent

        #by default, wx.ALIGN_LEFT and autoresize
        #~ sty = wx.ALIGN_CENTRE | wx.ST_NO_AUTORESIZE 
        sty = wx.ALIGN_RIGHT | wx.ST_NO_AUTORESIZE 

        lab1 = wx.StaticText(self, wx.ID_ANY, 'hydrogen', style=sty)
        lab2 = wx.StaticText(self, wx.ID_ANY, 'tin', style=sty)
        lab3 = wx.StaticText(self, wx.ID_ANY, 'mendelevium', style=sty)
        lab4 = wx.StaticText(self, wx.ID_ANY, 'carbon', style=sty)
        lab5 = wx.StaticText(self, wx.ID_ANY, 'nitrogen', style=sty)
        lab6 = wx.StaticText(self, wx.ID_ANY, 'argon', style=sty)
        lab7 = wx.StaticText(self, wx.ID_ANY, 'iron', style=sty)
        lab8 = wx.StaticText(self, wx.ID_ANY, 'platin', style=sty)
        lab9 = wx.StaticText(self, wx.ID_ANY, 'cobalt', style=sty)
        
        all = [lab1, lab2, lab3, lab4, lab5, lab6, lab7, lab8, lab9]
        for e in all:
            e.SetBackgroundColour((255, 255, 200))
            
        staline = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, (-1, 2), wx.LI_HORIZONTAL)
        b1 = wx.Button(self, wx.ID_ANY, 'button1')

        hgap, vgap = 10, 10
        nrows, ncols = 3, 3
        fgs = wx.FlexGridSizer(nrows, ncols, hgap, vgap)
        
        b = 0
        
        #*** with statictexts sty = wx.ALIGN_CENTRE | wx.ST_NO_AUTORESIZE 
        #statictexts fit the size of the texts, statictextzs are left aligned
        #~ f = wx.ALL
        #statictexts fit the size of the sizer, texts in statictexts are centered
        #~ f = wx.ALL | wx.EXPAND
        #statictexts fit the size of the texts, statictexts are centered
        #~ f = wx.ALL | wx.ALIGN_CENTRE
        #statictexts fit the size of the sizer, texts in statictexts are centered
        #~ f = wx.ALL | wx.ALIGN_CENTRE | wx.EXPAND
        #statictexts fit the size of the texts, statictexts are right aligned
        #~ f = wx.ALL | wx.ALIGN_RIGHT
        #statictexts fit the size of the sizer, texts in statictexts are centered
        #~ f = wx.ALL | wx.ALIGN_RIGHT | wx.EXPAND

        #*** with statictexts sty = wx.ALIGN_RIGHT | wx.ST_NO_AUTORESIZE 
        #statictexts fit the size of the texts, statictextzs look left aligned
        #~ f = wx.ALL
        #statictexts fit the size of the sizer, texts in statictexts are right aligned
        #~ f = wx.ALL | wx.EXPAND
        #statictexts fit the size of the texts, statictexts are centered
        #~ f = wx.ALL | wx.ALIGN_CENTRE
        #statictexts fit the size of the sizer, texts in statictexts are right aligned
        #~ f = wx.ALL | wx.ALIGN_CENTER | wx.EXPAND
        #statictexts fit the size of the texts, statictexts are right aligned
        #~ f = wx.ALL | wx.ALIGN_RIGHT
        #statictexts fit the size of the sizer, texts in statictexts are right aligned
        f = wx.ALL | wx.ALIGN_RIGHT | wx.EXPAND

        fgs.AddMany([(lab1, 0, f, b),
                     (lab2, 0, f, b),
                     (lab3, 0, f, b),
                     
                     (lab4, 0, f, b),
                     (lab5, 0, f, b),
                     (lab6, 0, f, b),
                     
                     (lab7, 0, f, b),
                     (lab8, 0, f, b),
                     (lab9, 0, f, b),
                    ])

        #~ fgs.AddGrowableRow(0)
        #~ fgs.AddGrowableRow(1)
        #~ fgs.AddGrowableRow(2)
        fgs.AddGrowableCol(0)
        fgs.AddGrowableCol(1)
        fgs.AddGrowableCol(2)

        b = 10
        vsizer1 = wx.BoxSizer(wx.VERTICAL)
        vsizer1.Add(fgs, 0, wx.ALL | wx.EXPAND, border=b)
        vsizer1.Add(staline, 0, wx.EXPAND)
        vsizer1.Add(b1, 0, wx.ALL | wx.ALIGN_RIGHT, border=b)
        
        self.SetSizer(vsizer1)
        r = vsizer1.GetMinSize()
        self.parent.SetClientSize(r)
        self.parent.CentreOnScreen()

#-----------------------------------------------------------------

# StaticTexts in a FlexGridSizer.
# StaticTexts with one or more lines.
# Texts in StaticTexts are defined before laying out.
# Textx in StaticTexts are "pushed" to the center of the sizer.

class MyPanel3(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.parent = parent

        #by default, wx.ALIGN_LEFT and autoresize
        sty1 = wx.ALIGN_RIGHT | wx.ST_NO_AUTORESIZE
        sty2 = wx.ALIGN_CENTRE | wx.ST_NO_AUTORESIZE 
        sty3 = wx.ALIGN_LEFT | wx.ST_NO_AUTORESIZE 

        lab1 = wx.StaticText(self, wx.ID_ANY, 'hydrogen', style=sty1)
        lab2 = wx.StaticText(self, wx.ID_ANY, 'tin', style=sty2)
        lab3 = wx.StaticText(self, wx.ID_ANY, 'mendelevium', style=sty3)
        lab4 = wx.StaticText(self, wx.ID_ANY, 'carbon', style=sty1)
        lab5 = wx.StaticText(self, wx.ID_ANY, 'nitrogen', style=sty2)
        lab6 = wx.StaticText(self, wx.ID_ANY, 'argon', style=sty3)
        lab7 = wx.StaticText(self, wx.ID_ANY, 'iron', style=sty1)
        lab8 = wx.StaticText(self, wx.ID_ANY, 'platin', style=sty2)
        lab9 = wx.StaticText(self, wx.ID_ANY, 'cobalt', style=sty3)
        
        txt1 = 'one two three' + os.linesep + 'four five six' + os.linesep + 'seven eight nine'
        txt2 = 'one two three four five six seven eight nine' * 3
        all = [lab1, lab2, lab3, lab4, lab5, lab6, lab7, lab8, lab9]
        for e in all:
            e.SetBackgroundColour((255, 255, 200))
            e.SetLabel(txt1)
            #changing font size: ok
            e.SetFont(wx.Font(10, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL))
        #variation
        #~ lab5.SetLabel(txt1 + os.linesep + txt2)
        #~ lab2.SetLabel('ten')
        
        staline = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, (-1, 2), wx.LI_HORIZONTAL)
        b1 = wx.Button(self, wx.ID_ANY, 'button1')

        hgap, vgap = 10, 10
        nrows, ncols = 3, 3
        fgs = wx.FlexGridSizer(nrows, ncols, hgap, vgap)
        
        b = 0
        
        f1 = wx.ALL | wx.ALIGN_RIGHT | wx.EXPAND
        f2 = wx.ALL | wx.ALIGN_CENTER | wx.EXPAND
        f3 = wx.ALL | wx.EXPAND | wx.ALIGN_LEFT
        f = wx.ALL

        fgs.AddMany([(lab1, 0, f1, b),
                     (lab2, 0, f2, b),
                     (lab3, 0, f3, b),
                     
                     (lab4, 0, f1, b),
                     (lab5, 0, f2, b),
                     (lab6, 0, f3, b),
                     
                     (lab7, 0, f1, b),
                     (lab8, 0, f2, b),
                     (lab9, 0, f3, b),
                    ])

        #~ fgs.AddGrowableRow(0)
        #~ fgs.AddGrowableRow(1)
        #~ fgs.AddGrowableRow(2)
        fgs.AddGrowableCol(0)
        fgs.AddGrowableCol(1)
        fgs.AddGrowableCol(2)

        b = 10
        vsizer1 = wx.BoxSizer(wx.VERTICAL)
        vsizer1.Add(fgs, 0, wx.ALL | wx.EXPAND, border=b)
        vsizer1.Add(staline, 0, wx.EXPAND)
        vsizer1.Add(b1, 0, wx.ALL | wx.ALIGN_RIGHT, border=b)
        
        self.SetSizer(vsizer1)
        r = vsizer1.GetMinSize()
        self.parent.SetClientSize(r)
        self.parent.CentreOnScreen()

#-----------------------------------------------------------------

# 9 StaticTexts in BoxSizers, 3 horizontal sizers in one vertical sizer.
# StaticTexts with one or more lines.
# Texts in StaticTexts are defined before laying out.

class MyPanel4(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.parent = parent

        lab1 = wx.StaticText(self, wx.ID_ANY, 'hydrogen')
        lab2 = wx.StaticText(self, wx.ID_ANY, 'tin')
        lab3 = wx.StaticText(self, wx.ID_ANY, 'mendelevium')
        lab4 = wx.StaticText(self, wx.ID_ANY, 'carbon')
        lab5 = wx.StaticText(self, wx.ID_ANY, 'nitrogen')
        lab6 = wx.StaticText(self, wx.ID_ANY, 'argon')
        lab7 = wx.StaticText(self, wx.ID_ANY, 'iron')
        lab8 = wx.StaticText(self, wx.ID_ANY, 'platin')
        lab9 = wx.StaticText(self, wx.ID_ANY, 'cobalt')
        
        txt1 = 'one two three' + os.linesep + 'four five six' + os.linesep + 'seven eight nine'
        all = [lab1, lab2, lab3, lab4, lab5, lab6, lab7, lab8, lab9]
        for e in all:
            e.SetBackgroundColour((255, 255, 200))
            #~ e.SetLabel(txt1)

        b = 5
        f = wx.ALL
        hsizer1 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer1.Add(lab1, 1, f, b)
        hsizer1.Add(lab2, 2, f, b)
        hsizer1.Add(lab3, 3, f, b)

        f = wx.ALL
        hsizer2 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer2.Add(lab4, 2, f, b)
        hsizer2.Add(lab5, 3, f, b)
        hsizer2.Add(lab6, 1, f, b)

        f = wx.ALL
        hsizer3 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer3.Add(lab7, 3, f, b)
        hsizer3.Add(lab8, 1, f, b)
        hsizer3.Add(lab9, 2, f, b)

        b = 0
        f = wx.ALL | wx.EXPAND
        vsizer1 = wx.BoxSizer(wx.VERTICAL)
        vsizer1.Add(hsizer1, 1, f, b)
        vsizer1.Add(hsizer2, 1, f, b)
        vsizer1.Add(hsizer3, 1, f, b)
        
        self.SetSizerAndFit(vsizer1)
        r = vsizer1.GetMinSize()
        self.parent.SetClientSize(r)
        self.parent.CenterOnScreen()

#-----------------------------------------------------------------

# 9 StaticTexts in BoxSizers, 3 vertical sizers in one horizontal sizer.
# StaticTexts with one or more lines.
# Texts in StaticTexts are defined before laying out.

class MyPanel5(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.parent = parent

        lab1 = wx.StaticText(self, wx.ID_ANY, 'hydrogen')
        lab2 = wx.StaticText(self, wx.ID_ANY, 'tin')
        lab3 = wx.StaticText(self, wx.ID_ANY, 'mendelevium')
        lab4 = wx.StaticText(self, wx.ID_ANY, 'carbon')
        lab5 = wx.StaticText(self, wx.ID_ANY, 'nitrogen')
        lab6 = wx.StaticText(self, wx.ID_ANY, 'argon')
        lab7 = wx.StaticText(self, wx.ID_ANY, 'iron')
        lab8 = wx.StaticText(self, wx.ID_ANY, 'platin')
        lab9 = wx.StaticText(self, wx.ID_ANY, 'cobalt')
        
        txt1 = 'one two three' + os.linesep + 'four five six' + os.linesep + 'seven eight nine'
        all = [lab1, lab2, lab3, lab4, lab5, lab6, lab7, lab8, lab9]
        for e in all:
            e.SetBackgroundColour((255, 255, 200))
            e.SetLabel(txt1)

        b = 5
        f = wx.ALL | wx.EXPAND
        vsizer1 = wx.BoxSizer(wx.VERTICAL)
        vsizer1.Add(lab1, 0, f, b)
        vsizer1.Add(lab2, 0, f, b)
        vsizer1.Add(lab3, 0, f, b)

        f = wx.ALL | wx.EXPAND
        vsizer2 = wx.BoxSizer(wx.VERTICAL)
        vsizer2.Add(lab4, 0, f, b)
        vsizer2.Add(lab5, 0, f, b)
        vsizer2.Add(lab6, 0, f, b)

        f = wx.ALL | wx.EXPAND
        vsizer3 = wx.BoxSizer(wx.VERTICAL)
        vsizer3.Add(lab7, 0, f, b)
        vsizer3.Add(lab8, 0, f, b)
        vsizer3.Add(lab9, 0, f, b)

        b = 0
        f = wx.ALL | wx.GROW #|wx.EXPAND
        hsizer1 = wx.BoxSizer(wx.HORIZONTAL)
        #each vertical sizers and statictexts have the same width
        #and statictext do not expand
        #~ p = 0 #each vertical sizers and statictexts have the same width
        #all vertical sizers and statictexts have the same width
        #and statictexts expand
        p = 1 #all vertical sizers and statictexts have the same width
        #~ hsizer1.Add(vsizer1, p, f, b)
        #~ hsizer1.Add(vsizer2, p, f, b)
        #~ hsizer1.Add(vsizer3, p, f, b)
        
        #only the two last "columns" expand
        hsizer1.Add(vsizer1, 0, f, b)
        hsizer1.Add(vsizer2, p, f, b)
        hsizer1.Add(vsizer3, p, f, b)
        hsizer1.SetItemMinSize(vsizer1, (200, -1))

        self.SetSizerAndFit(hsizer1)
        r = hsizer1.GetMinSize()
        self.parent.SetClientSize(r)
        self.parent.CenterOnScreen()

#-----------------------------------------------------------------

# StaticTexts in a GridBagSizer.
# StaticTexts with a single line.
# Texts in StaticTexts are defined before laying out.
# StaticTexts with a defined style.

# Why does an GridBagSizer expand differently compare to FlexGrid sizer?
# Partial answer, GridBagSizer does not like small items. That's the case
# with one line StaticTexts. See WithGridBagSizers.panel_406

class MyPanel6(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.parent = parent

        #by default, wx.ALIGN_LEFT and autoresize
        sty = wx.ALIGN_LEFT
        #~ sty = wx.ALIGN_CENTRE | wx.ST_NO_AUTORESIZE 
        #~ sty = wx.ALIGN_RIGHT | wx.ST_NO_AUTORESIZE 

        lab1 = wx.StaticText(self, wx.ID_ANY, 'hydrogen', style=sty)
        lab2 = wx.StaticText(self, wx.ID_ANY, 'tin', style=sty)
        lab3 = wx.StaticText(self, wx.ID_ANY, 'mendelevium', style=sty)
        lab4 = wx.StaticText(self, wx.ID_ANY, 'carbon', style=sty)
        lab5 = wx.StaticText(self, wx.ID_ANY, 'nitrogen', style=sty)
        lab6 = wx.StaticText(self, wx.ID_ANY, 'argon', style=sty)
        lab7 = wx.StaticText(self, wx.ID_ANY, 'iron', style=sty)
        lab8 = wx.StaticText(self, wx.ID_ANY, 'platin', style=sty)
        lab9 = wx.StaticText(self, wx.ID_ANY, 'cobalt', style=sty)
        
        all = [lab1, lab2, lab3, lab4, lab5, lab6, lab7, lab8, lab9]
        for e in all:
            e.SetBackgroundColour((255, 255, 200))
            
        staline = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, (-1, 2), wx.LI_HORIZONTAL)
        b1 = wx.Button(self, wx.ID_ANY, 'button1')

        vgap, hgap = 50, 20
        gbs = wx.GridBagSizer(vgap, hgap)
        
        b = 0
        f = wx.ALL | wx.EXPAND
        #~ f = wx.ALL
        gbs.Add(lab1, (0, 0), (1, 1), f, b)
        gbs.Add(lab2, (0, 1), (1, 1), f, b)
        gbs.Add(lab3, (0, 2), (1, 1), f, b)
        
        gbs.Add(lab4, (1, 0), (1, 1), f, b)
        gbs.Add(lab5, (1, 1), (1, 1), f, b)
        gbs.Add(lab6, (1, 2), (1, 1), f, b)
        
        gbs.Add(lab7, (2, 0), (1, 1), f, b)
        gbs.Add(lab8, (2, 1), (1, 1), f, b)
        gbs.Add(lab9, (2, 2), (1, 1), f, b)


        #~ gbs.AddGrowableRow(0)
        #~ gbs.AddGrowableRow(1)
        #~ gbs.AddGrowableRow(2)
        gbs.AddGrowableCol(0)
        gbs.AddGrowableCol(1)
        gbs.AddGrowableCol(2)

        b = 10
        vsizer1 = wx.BoxSizer(wx.VERTICAL)
        vsizer1.Add(gbs, 0, wx.ALL | wx.EXPAND, border=b)
        vsizer1.Add(staline, 0, wx.EXPAND)
        vsizer1.Add(b1, 0, wx.ALL | wx.ALIGN_RIGHT, border=b)
        
        self.SetSizer(vsizer1)
        r = vsizer1.GetMinSize()
        self.parent.SetClientSize(r)
        self.parent.CentreOnScreen()


#-----------------------------------------------------------------

# FlexGridSizer with fixed sized StaticTexts and a ColWin
# Here, the item have a fixed sized, they are packed with
# a FlexGridSizer and the main frame size is set accordingly


class MyPanel7(wx.Panel):

    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.parent = parent

        #do not do this
        #~ self.parent.SetClientSize((800, 400))
        
        wgreen = ColWin(self, wx.ID_ANY, wx.GREEN)
        
        s = 'abc'
        s = ''
        si = (150, -1)
        lab1 = wx.StaticText(self, wx.ID_ANY, s, size=si)
        lab2 = wx.StaticText(self, wx.ID_ANY, s, size=si)
        lab3 = wx.StaticText(self, wx.ID_ANY, s, size=si)
        lab4 = wx.StaticText(self, wx.ID_ANY, s, size=si)
        lab5 = wx.StaticText(self, wx.ID_ANY, s, size=si)
        lab6 = wx.StaticText(self, wx.ID_ANY, s, size=si)
        
        all = [lab1, lab2, lab3, lab4, lab5, lab6]
        for e in all:
            e.SetBackgroundColour((255, 255, 200))

        hgap, vgap = 5, 5
        nrows, ncols = 3, 2
        fgs = wx.FlexGridSizer(nrows, ncols, hgap, vgap)
        f = wx.ALL #| wx.EXPAND
        b = 0
        fgs.AddMany([(lab1, 0, f, b),
                     (lab2, 0, f, b),
                     
                     (lab3, 0, f, b),
                     (lab4, 0, f, b),
                     
                     (lab5, 0, f, b),
                     (lab6, 0, f, b),
                    ])
        #~ fgs.AddGrowableCol(0)
        #~ fgs.AddGrowableCol(1)
        
        b = 5
        vsizer1 = wx.BoxSizer(wx.VERTICAL)
        #~ vsizer1.Add((-1, 100))
        vsizer1.Add(wgreen, 0, wx.ALL | wx.ALIGN_CENTER, b)
        vsizer1.Add(fgs, 0, wx.ALL | wx.ALIGN_CENTER, b)
        
        vsizer1.SetItemMinSize(wgreen, (380, 130))
        self.SetSizer(vsizer1)
        self.parent.SetClientSize(vsizer1.GetMinSize())
        self.parent.CentreOnScreen()

        sty = wx.SYSTEM_MENU | wx.CAPTION | wx.MINIMIZE_BOX | wx.CLOSE_BOX
        #~ self.parent.SetStyle(sty)
        self.parent.SetWindowStyle(sty)

#-----------------------------------------------------------------

if __name__ == "__main__":

    import baseframe
    
    app = wx.PySimpleApp()
    frame = baseframe.MyFrame(None, panel=MyPanel1)
    frame.Show()
    app.MainLoop()

#eof-----------------------------------------------------------------
