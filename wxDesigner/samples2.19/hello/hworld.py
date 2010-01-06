#!/bin/env python
#----------------------------------------------------------------------------
# Name:         hworld.py
# Author:       XXXX
# Created:      XX/XX/XX
# Copyright:    
#----------------------------------------------------------------------------

import wx
from hworld_wdr import *

#----------------------------------------------------------------------------

class MyApp(wx.App):
    
    def OnInit(self):
        dialog = wx.Dialog(None, -1, "Hello World")
        MyDialogFunc(dialog, True)
        dialog.CentreOnScreen()
        dialog.ShowModal()
        return True

#----------------------------------------------------------------------------

app = MyApp(True)
app.MainLoop()

