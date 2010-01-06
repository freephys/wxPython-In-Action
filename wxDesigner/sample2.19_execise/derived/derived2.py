#!/bin/env python
#----------------------------------------------------------------------------
# Name:         derived2.py
# Author:       XXXX
# Created:      XX/XX/XX
# Copyright:    
#----------------------------------------------------------------------------

import wx

# WDR: classes

class Derived_ctrl(wx.TextCtrl):
    def __init__(self, parent, id, value, pos, size, style):
        wx.TextCtrl.__init__(self, parent, id, value, pos, size, style)
        
        # WDR: handler declarations for MyTextCtrl
        wx.EVT_CHAR(self, self.OnChar)

    # WDR: methods for MyTextCtrl

    # WDR: handler implementations for MyTextCtrl

    def OnChar(self, event):
        # do something special here
        wx.Bell()
        event.Skip(True)

