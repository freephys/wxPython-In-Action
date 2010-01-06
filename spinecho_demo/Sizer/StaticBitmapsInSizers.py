# -*- coding: iso-8859-1 -*-
#--------------------------------------------------------------------
# Name:      StaticBitmapsInSizers.py
# Purpose:   An application to learn sizers
# Author:    Jean-Michel Fauth, Switzerland
# Copyright: (c) 2007-2008 Jean-Michel Fauth
# Licence:   None
# os dev:    winXP sp2
# py dev:    Python 2.5.4
# wx dev:    wxPython 2.8.9.1-ansi
# Revision:  28 December 2008
#--------------------------------------------------------------------

# StaticBitmaps in Sizers.
# A StaticBitmaps can not be expanded. It receives the size of
# the contained image.

#--------------------------------------------------------------------

import wx

#--------------------------------------------------------------------

# A panel containing two images in StaticBitmaps in a horizontal sizer.

class MyPanel1(wx.Panel):
    
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.parent = parent

        bmp1 = wx.Bitmap('pomme1.jpg', wx.BITMAP_TYPE_JPEG)
        bmp2 = wx.Bitmap('pomme2.jpg', wx.BITMAP_TYPE_JPEG)
        
        stabmp1 = wx.StaticBitmap(self, wx.NewId(), wx.EmptyBitmap(10, 10), \
                wx.DefaultPosition, wx.DefaultSize, style=wx.SUNKEN_BORDER)
        stabmp1.SetBitmap(bmp1)
        stabmp2 = wx.StaticBitmap(self, wx.NewId(), wx.EmptyBitmap(10, 10), \
                wx.DefaultPosition, wx.DefaultSize, style=wx.SUNKEN_BORDER)
        stabmp2.SetBitmap(bmp2)

        b = 10
        hsizer1 = wx.BoxSizer(wx.HORIZONTAL)
        hsizer1.Add(stabmp1, 0, wx.ALIGN_CENTRE_VERTICAL | wx.ALL, b)
        hsizer1.Add(stabmp2, 0, wx.ALIGN_CENTRE_VERTICAL | wx.ALL, b)
        
        self.SetSizerAndFit(hsizer1)
        self.parent.SetClientSize(hsizer1.GetSize())
        self.parent.CentreOnScreen()

#-------------------------------------------------------------------

# A panel containing two images in StaticBitmaps in a vertical sizer.

class MyPanel2(wx.Panel):
    
    def __init__(self, parent):
        wx.Panel.__init__(self, parent)
        self.parent = parent

        bmp1 = wx.Bitmap('pomme1.jpg', wx.BITMAP_TYPE_JPEG)
        bmp2 = wx.Bitmap('pomme2.jpg', wx.BITMAP_TYPE_JPEG)
        
        stabmp1 = wx.StaticBitmap(self, wx.NewId(), wx.EmptyBitmap(10, 10), \
                wx.DefaultPosition, wx.DefaultSize, style=wx.SUNKEN_BORDER)
        stabmp1.SetBitmap(bmp1)
        stabmp2 = wx.StaticBitmap(self, wx.NewId(), wx.EmptyBitmap(10, 10), \
                wx.DefaultPosition, wx.DefaultSize, style=wx.SUNKEN_BORDER)
        stabmp2.SetBitmap(bmp2)

        b = 10
        vsizer1 = wx.BoxSizer(wx.VERTICAL)
        vsizer1.Add(stabmp1, 0, wx.ALIGN_CENTRE_VERTICAL | wx.ALL, b)
        vsizer1.Add(stabmp2, 0, wx.ALIGN_CENTRE_HORIZONTAL | wx.ALL, b)
        
        self.SetSizerAndFit(vsizer1)
        self.parent.SetClientSize(vsizer1.GetSize())
        self.parent.CentreOnScreen()

#-------------------------------------------------------------------

if __name__ == "__main__":

    import baseframe
    
    app = wx.PySimpleApp()
    frame = baseframe.MyFrame(None, panel=MyPanel1)
    frame.Show()
    app.MainLoop()

#eof----------------------------------------------------------------
