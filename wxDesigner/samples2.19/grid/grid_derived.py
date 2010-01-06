#!/bin/env python
#----------------------------------------------------------------------------
# Name:         grid_derived.py
# Author:       XXXX
# Created:      XX/XX/XX
# Copyright:    
#----------------------------------------------------------------------------

import wx
import wx.grid

# WDR: classes

class MyGrid(wx.grid.Grid):
    def __init__(self, parent, id, pos, size, style):
        wx.grid.Grid.__init__(self, parent, id, pos, size, style)
        
        # WDR: handler declarations for MyGrid
        wx.grid.EVT_GRID_CELL_RIGHT_CLICK(self, self.OnRightClick)

    # WDR: methods for MyGrid

    # WDR: handler implementations for MyGrid

    def OnRightClick(self, event):
        dialog = wx.MessageDialog( self, "You right-clicked on a cell!", "MyGrid", wx.ICON_INFORMATION );
        dialog.CentreOnParent()
        dialog.ShowModal()
        dialog.Destroy()

