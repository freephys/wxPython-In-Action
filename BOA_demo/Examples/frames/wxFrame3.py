#Boa:Frame:wxFrame3

import wx

def create(parent):
    return wxFrame3(parent)

[wxID_WXFRAME3] = [wx.NewId() for _init_ctrls in range(1)]

class wxFrame3(wx.Frame):
    def _init_utils(self):
        # generated method, don't edit
        pass

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_WXFRAME3, name='', parent=prnt,
              pos= wx.Point(176, 176), size= wx.Size(960, 692),
              style=wx.DEFAULT_FRAME_STYLE, title='wxFrame3')
        self._init_utils()
        self.SetClientSize(wx.Size(952, 665))

    def __init__(self, parent):
        self._init_ctrls(parent)
