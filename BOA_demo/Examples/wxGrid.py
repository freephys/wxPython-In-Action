#Boa:Frame:wxFrame1

import wx
import wx.grid

def create(parent):
    return wxFrame1(parent)

[wxID_WXFRAME1, wxID_WXFRAME1GRID1, 
] = [wx.NewId() for _init_ctrls in range(2)]

class wxFrame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_WXFRAME1, name='', parent=prnt,
              pos=wx.Point(318, 214), size=wx.Size(432, 242),
              style=wx.DEFAULT_FRAME_STYLE, title='wxFrame1')
        self.SetClientSize(wx.Size(424, 215))

        self.grid1 = wx.grid.Grid(id=wxID_WXFRAME1GRID1, name='grid1',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(424, 215), style=0)
        self.grid1.EnableGridLines(True)

    def __init__(self, parent):
        self._init_ctrls(parent)

        # Either CreateGrid or SetTable must be manually added in your code
        # before you populate the grid
        self.grid1.CreateGrid(3, 3)


if __name__ == '__main__':
    app = wx.PySimpleApp()
    wx.InitAllImageHandlers()
    frame = create(None)
    frame.Show()
    app.MainLoop()
