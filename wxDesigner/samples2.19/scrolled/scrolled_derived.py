#!/bin/env python
#----------------------------------------------------------------------------
# Name:         scrolled_derived.py
# Author:       XXXX
# Created:      XX/XX/XX
# Copyright:    
#----------------------------------------------------------------------------

import wx

# WDR: classes

class MyScrolledWindow(wx.ScrolledWindow):
    def __init__(self, parent, id,
        pos = wx.DefaultPosition, size = wx.DefaultSize,
        style = wx.HSCROLL|wx.VSCROLL ):
        wx.ScrolledWindow.__init__(self, parent, id, pos, size, style)
        
        # WDR: handler declarations for MyScrolledWindow
        wx.EVT_LEFT_DOWN(self, self.OnLeftDown)
        wx.EVT_PAINT(self, self.OnPaint)

    # WDR: methods for MyScrolledWindow

    # WDR: handler implementations for MyScrolledWindow

    def OnLeftDown(self, event):
        dialog = wx.MessageDialog( self, "Left click.", "Test", wx.OK|wx.ICON_INFORMATION )
        dialog.ShowModal()
        dialog.Destroy()

    def OnPaint(self, event):
        dc = wx.PaintDC( self )
        self.PrepareDC( dc )
        dc.DrawLine( 0,0,300,300 )


