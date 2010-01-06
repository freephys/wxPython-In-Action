# -*- coding: iso-8859-1 -*-
#--------------------------------------------------------------------
# Name:      WithFlexGridSizers_two.py
# Purpose:   An application to learn sizers
# Author:    Jean-Michel Fauth, Switzerland
# Copyright: (c) 2007-2008 Jean-Michel Fauth
# Licence:   None
# os dev:    winXP sp2
# py dev:    Python 2.5.4
# wx dev:    wxPython 2.8.9.1-ansi
# Revision:  27 December 2008
#--------------------------------------------------------------------

# Mainly FlexGridSizers, part two

#--------------------------------------------------------------------

import wx
from colourwindow import ColWin

#--------------------------------------------------------------------

# A FlexGridSizer.
# Each row contains a ColWin, a StaticText and a TextCtrl.
# The FlexGridSizer is packed between a title and buttons.

class MyPanel1(wx.Panel):
    
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, wx.ID_ANY)
        self.parent = parent

        #the widgets

        wsize = (16, 16)
        wgreen = ColWin(self, wx.ID_ANY, wx.GREEN)
        wgreen.SetSize(wsize)
        wred = ColWin(self, wx.ID_ANY, wx.RED)
        wred.SetSize(wsize)
        wblue = ColWin(self, wx.ID_ANY, wx.BLUE)
        wblue.SetSize(wsize)
        wblack = ColWin(self, wx.ID_ANY, wx.BLACK)
        wblack.SetSize(wsize)
        wyellow = ColWin(self, wx.ID_ANY, (255, 255, 0))
        wyellow.SetSize(wsize)
        
        title = wx.StaticText(self, wx.ID_ANY, 'HALOGENE (atomic mass)')

        label1 = wx.StaticText(self, wx.ID_ANY, 'Flurorine')
        txt1 = wx.TextCtrl(self, wx.ID_ANY,'18.9984 g/mol')
 
        label2 = wx.StaticText(self, wx.ID_ANY, 'Chlorine')
        txt2 = wx.TextCtrl(self, wx.ID_ANY,'more than fluorine')
 
        label3 = wx.StaticText(self, wx.ID_ANY, 'Bromine')
        txt3 = wx.TextCtrl(self, wx.ID_ANY, 'more than chlorine')
 
        label4 = wx.StaticText(self, wx.ID_ANY, 'Iodine')
        txt4 = wx.TextCtrl(self, wx.ID_ANY, 'more than bromine')

        label5 = wx.StaticText(self, wx.ID_ANY, 'Astatine')
        txt5 = wx.TextCtrl(self, wx.ID_ANY, 'less than radon !')

        but1 = wx.Button(self, wx.ID_ANY, 'OK')
        but2 = wx.Button(self, wx.ID_ANY, 'Cancel')

        staline1 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, (-1, 2), \
                        wx.LI_HORIZONTAL)
        staline2 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, (-1, 2), \
                        wx.LI_HORIZONTAL)

        #the sizers

        hsizer1 = wx.BoxSizer(wx.HORIZONTAL)
        b = 5
        hsizer1.Add(title, 0)
        
        hsizer2 = wx.BoxSizer(wx.HORIZONTAL)
        b = 5
        hsizer2.Add(but1, 0, wx.RIGHT, b)
        hsizer2.Add(but2, 0)
        
        fgs = wx.FlexGridSizer(rows=5, cols=3, hgap=5, vgap=5)
        f1 = wx.ALL | wx.ALIGN_CENTRE_VERTICAL
        f2 = wx.ALL | wx.ALIGN_RIGHT | wx.ALIGN_CENTRE_VERTICAL
        f3 = wx.ALL | wx.EXPAND
        b = 0
        fgs.AddMany([(wgreen, 0, f1, b),
                     (label1, 0, f2, b),
                     (txt1, 0, f3, b),
                     
                     (wred, 0, f1, b),
                     (label2, 0, f2, b),
                     (txt2, 0, f3, b),
                     
                     (wblue, 0, f1, b),
                     (label3, 0, f2, b),
                     (txt3, 0, f3, b),

                     (wblack, 0, f1, b),
                     (label4, 0, f2, b),
                     (txt4, 0, f3, b),
                     
                     (wyellow, 0, f1, b),
                     (label5, 0, f2, b),
                     (txt5, 0, f3, b),
                    ])
        fgs.AddGrowableCol(2)

        vsizer1 = wx.BoxSizer(wx.VERTICAL)
        b = 10
        vsizer1.Add(hsizer1, 0, wx.TOP | wx.CENTER, b)
        vsizer1.Add(staline1, 0, wx.ALL | wx.EXPAND, b)
        vsizer1.Add(fgs, 0, wx.LEFT | wx.RIGHT | wx.CENTRE | wx.EXPAND, b*4)
        vsizer1.Add(staline2, 0, wx.ALL | wx.EXPAND, b)
        vsizer1.Add(hsizer2, 0, wx.BOTTOM | wx.CENTER, b)
         
        #set the size and lock the frame size
        
        self.SetSizerAndFit(vsizer1)
        self.parent.SetClientSize(vsizer1.GetSize())
        r = self.parent.GetSize()
        self.parent.SetMaxSize((-1, r[1]))
        self.parent.SetMinSize((r[0], r[1]))

#-----------------------------------------------------------------

# A FlexGridSizer.
# Each row contains a ColWin, a StaticText and a TextCtrl.
# The FlexGridSizer is packed between a title and buttons.
# For each row, the ColWin and the StaticText are packed together in a sizer.

class MyPanel2(wx.Panel):
    
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, wx.ID_ANY)
        self.parent = parent

        #the widgets

        wsize = (16, 16)
        wgreen = ColWin(self, wx.ID_ANY, wx.GREEN)
        wgreen.SetSize(wsize)
        wred = ColWin(self, wx.ID_ANY, wx.RED)
        wred.SetSize(wsize)
        wblue = ColWin(self, wx.ID_ANY, wx.BLUE)
        wblue.SetSize(wsize)
        wblack = ColWin(self, wx.ID_ANY, wx.BLACK)
        wblack.SetSize(wsize)
        wyellow = ColWin(self, wx.ID_ANY, (255, 255, 0))
        wyellow.SetSize(wsize)
        
        title = wx.StaticText(self, wx.ID_ANY, 'HALOGENE (atomic mass)')

        label1 = wx.StaticText(self, wx.ID_ANY, 'Flurorine')
        txt1 = wx.TextCtrl(self, wx.ID_ANY,'18.9984 g/mol')
 
        label2 = wx.StaticText(self, wx.ID_ANY, 'Chlorine')
        txt2 = wx.TextCtrl(self, wx.ID_ANY,'more than fluorine')
 
        label3 = wx.StaticText(self, wx.ID_ANY, 'Bromine')
        txt3 = wx.TextCtrl(self, wx.ID_ANY, 'more than chlorine')
 
        label4 = wx.StaticText(self, wx.ID_ANY, 'Iodine')
        txt4 = wx.TextCtrl(self, wx.ID_ANY, 'more than bromine')

        label5 = wx.StaticText(self, wx.ID_ANY, 'Astatine')
        txt5 = wx.TextCtrl(self, wx.ID_ANY, 'less than radon !')

        but1 = wx.Button(self, wx.ID_ANY, 'OK')
        but2 = wx.Button(self, wx.ID_ANY, 'Cancel')

        staline1 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, (-1, 2), \
                        wx.LI_HORIZONTAL)
        staline2 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, (-1, 2), \
                        wx.LI_HORIZONTAL)

        #the sizers

        hsizer1 = wx.BoxSizer(wx.HORIZONTAL)
        b = 5
        hsizer1.Add(title, 0)
        
        hsizer2 = wx.BoxSizer(wx.HORIZONTAL)
        b = 5
        hsizer2.Add(but1, 0, wx.RIGHT, b)
        hsizer2.Add(but2, 0)
        
        #labels and coloured windows are grouped before packed in fgs
        
        hsizerA = wx.BoxSizer(wx.HORIZONTAL)
        b = 5
        hsizerA.Add(wgreen, 0, wx.RIGHT, b)
        hsizerA.Add(label1, 0)

        hsizerB = wx.BoxSizer(wx.HORIZONTAL)
        b = 5
        hsizerB.Add(wred, 0, wx.RIGHT, b)
        hsizerB.Add(label2, 0)

        hsizerC = wx.BoxSizer(wx.HORIZONTAL)
        b = 5
        hsizerC.Add(wblue, 0, wx.RIGHT, b)
        hsizerC.Add(label3, 0)

        hsizerD = wx.BoxSizer(wx.HORIZONTAL)
        b = 5
        hsizerD.Add(wblack, 0, wx.RIGHT, b)
        hsizerD.Add(label4, 0)
        
        hsizerE = wx.BoxSizer(wx.HORIZONTAL)
        b = 5
        hsizerE.Add(wyellow, 0, wx.RIGHT, b)
        hsizerE.Add(label5, 0)
        
        #number of cols!
        fgs = wx.FlexGridSizer(rows=5, cols=2, hgap=5, vgap=5)
        f1 = wx.ALL
        f2 = wx.ALL | wx.ALIGN_RIGHT
        f3 = wx.ALL | wx.EXPAND
        b = 0
        fgs.AddMany([(hsizerA, 0, f2, b),
                     (txt1, 0, f3, b),
                     
                     (hsizerB, 0, f2, b),
                     (txt2, 0, f3, b),
                     
                     (hsizerC, 0, f2, b),
                     (txt3, 0, f3, b),

                     (hsizerD, 0, f2, b),
                     (txt4, 0, f3, b),
                     
                     (hsizerE, 0, f2, b),
                     (txt5, 0, f3, b),
                    ])
        #growable col!
        fgs.AddGrowableCol(1)

        vsizer1 = wx.BoxSizer(wx.VERTICAL)
        b = 10
        vsizer1.Add(hsizer1, 0, wx.TOP | wx.CENTER, b)
        vsizer1.Add(staline1, 0, wx.ALL | wx.EXPAND, b)
        vsizer1.Add(fgs, 0, wx.LEFT | wx.RIGHT | wx.CENTRE | wx.EXPAND, b*4)
        vsizer1.Add(staline2, 0, wx.ALL | wx.EXPAND, b)
        vsizer1.Add(hsizer2, 0, wx.BOTTOM | wx.CENTER, b)
         
        #set the size and lock the frame size
        
        self.SetSizerAndFit(vsizer1)
        self.parent.SetClientSize(vsizer1.GetSize())
        r = self.parent.GetSize()
        self.parent.SetMaxSize((-1, r[1]))
        self.parent.SetMinSize((r[0], r[1]))


#-----------------------------------------------------------------

# A FlexGridSizer.
# Each row contains a ColWin, a StaticText and a TextCtrl.
# The FlexGridSizer is packed between a title and buttons.

class MyPanel3(wx.Panel):
    
    def __init__(self, parent):
        wx.Panel.__init__(self, parent, wx.ID_ANY)
        self.parent = parent

        #the widgets

        wxgreen1 = ColWin(self, wx.ID_ANY, wx.GREEN)
        wxgreen2 = ColWin(self, wx.ID_ANY, wx.GREEN)
        wxgreen3 = ColWin(self, wx.ID_ANY, wx.GREEN)
        wred1 = ColWin(self, wx.ID_ANY, wx.RED)
        wred2 = ColWin(self, wx.ID_ANY, wx.RED)
        wred3 = ColWin(self, wx.ID_ANY, wx.RED)
        wblue1 = ColWin(self, wx.ID_ANY, wx.BLUE)
        wblue2 = ColWin(self, wx.ID_ANY, wx.BLUE)
        wblue3 = ColWin(self, wx.ID_ANY, wx.BLUE)
        wblack1 = ColWin(self, wx.ID_ANY, wx.BLACK)
        wblack2 = ColWin(self, wx.ID_ANY, wx.BLACK)
        wblack3 = ColWin(self, wx.ID_ANY, wx.BLACK)
        wyellow1 = ColWin(self, wx.ID_ANY, (255, 255, 0))
        wyellow2 = ColWin(self, wx.ID_ANY, (255, 255, 0))
        wyellow3 = ColWin(self, wx.ID_ANY, (255, 255, 0))
        
        title = wx.StaticText(self, wx.ID_ANY, 'HALOGENE (atomic mass)')

        label1 = wx.StaticText(self, wx.ID_ANY, 'Flurorine')
        txt1 = wx.TextCtrl(self, wx.ID_ANY,'18.9984 g/mol')
 
        label2 = wx.StaticText(self, wx.ID_ANY, 'Chlorine')
        txt2 = wx.TextCtrl(self, wx.ID_ANY,'more than fluorine')
 
        label3 = wx.StaticText(self, wx.ID_ANY, 'Bromine')
        txt3 = wx.TextCtrl(self, wx.ID_ANY, 'more than chlorine')
 
        label4 = wx.StaticText(self, wx.ID_ANY, 'Iodine')
        txt4 = wx.TextCtrl(self, wx.ID_ANY, 'more than bromine')

        label5 = wx.StaticText(self, wx.ID_ANY, 'Astatine')
        txt5 = wx.TextCtrl(self, wx.ID_ANY, 'less than radon !')

        but1 = wx.Button(self, wx.ID_ANY, 'OK')
        but2 = wx.Button(self, wx.ID_ANY, 'Cancel')

        staline1 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, (-1, 2), \
                        wx.LI_HORIZONTAL)
        staline2 = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, (-1, 2), \
                        wx.LI_HORIZONTAL)

        labels = [label1, label2, label3, label4, label5]
        txts = [txt1, txt2, txt3, txt4, txt5]
        wins = [wxgreen1, wred1, wblue1, wblack1, wyellow1, \
                wxgreen2, wred2, wblue2, wblack2, wyellow2, \
                wxgreen3, wred3, wblue3, wblack3, wyellow3]
        
        fo1 = wx.Font(-1, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, \
                      wx.FONTWEIGHT_NORMAL, False)
        fo2 = wx.Font(-1, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, \
                      wx.FONTWEIGHT_NORMAL, False)
        
        for e in labels:
            e.SetFont(fo1)
        for e in txts:
            e.SetFont(fo2)
        for e in wins:
            e.SetSize((20, 6))
        
        #the sizers

        hsizer1 = wx.BoxSizer(wx.HORIZONTAL)
        b = 5
        hsizer1.Add(title, 0)
        
        hsizer2 = wx.BoxSizer(wx.HORIZONTAL)
        b = 5
        hsizer2.Add(but1, 0, wx.RIGHT, b)
        hsizer2.Add(but2, 0)
        
        fgs = wx.FlexGridSizer(rows=5, cols=5, hgap=5, vgap=5)
        f1 = wx.ALL | wx.ALIGN_CENTRE_VERTICAL
        f3 = wx.ALL | wx.EXPAND
        f2 = wx.ALL | wx.ALIGN_RIGHT | wx.ALIGN_CENTRE_VERTICAL
        f4 = wx.ALL | wx.ALIGN_TOP
        f5 = wx.ALL | wx.ALIGN_BOTTOM
        
        b = 0
        fgs.AddMany([(wxgreen1, 0, f1, b),
                     (wxgreen2, 0, f4, b),
                     (wxgreen3, 0, f5, b),
                     (label1, 0, f2, b),
                     (txt1, 0, f3, b),
                     
                     (wred1, 0, f1, b),
                     (wred2, 0, f4, b),
                     (wred3, 0, f5, b),
                     (label2, 0, f2, b),
                     (txt2, 0, f3, b),
                     
                     (wblue1, 0, f1, b),
                     (wblue2, 0, f4, b),
                     (wblue3, 0, f1, b),
                     (label3, 0, f5, b),
                     (txt3, 0, f3, b),

                     (wblack1, 0, f1, b),
                     (wblack2, 0, f4, b),
                     (wblack3, 0, f5, b),
                     (label4, 0, f2, b),
                     (txt4, 0, f3, b),
                     
                     (wyellow1, 0, f1, b),
                     (wyellow2, 0, f4, b),
                     (wyellow3, 0, f5, b),
                     (label5, 0, f2, b),
                     (txt5, 0, f3, b),
                    ])
        fgs.AddGrowableCol(4)

        vsizer1 = wx.BoxSizer(wx.VERTICAL)
        b = 10
        vsizer1.Add(hsizer1, 0, wx.TOP | wx.CENTER, b)
        vsizer1.Add(staline1, 0, wx.ALL | wx.EXPAND, b)
        vsizer1.Add(fgs, 0, wx.LEFT | wx.RIGHT | wx.CENTRE | wx.EXPAND, b*4)
        vsizer1.Add(staline2, 0, wx.ALL | wx.EXPAND, b)
        vsizer1.Add(hsizer2, 0, wx.BOTTOM | wx.CENTER, b)
         
        #set the size and lock the frame size
        
        self.SetSizerAndFit(vsizer1)
        self.parent.SetClientSize(vsizer1.GetSize())
        r = self.parent.GetSize()
        self.parent.SetMaxSize((-1, r[1]))
        self.parent.SetMinSize((r[0], r[1]))

#-----------------------------------------------------------------

if __name__ == "__main__":

    import baseframe
    
    app = wx.PySimpleApp()
    frame = baseframe.MyFrame(None, panel=MyPanel1)
    frame.Show()
    app.MainLoop()

#eof-----------------------------------------------------------------



