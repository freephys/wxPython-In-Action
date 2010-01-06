#Boa:Frame:Frame1

import wx
from wx.lib.anchors import LayoutAnchors

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BUTTON1, wxID_FRAME1BUTTON2, wxID_FRAME1STATICTEXT1, 
 wxID_FRAME1TEXTCTRL1, 
] = [wx.NewId() for _init_ctrls in range(5)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='Frame1', parent=prnt,
              pos=wx.Point(173, 135), size=wx.Size(417, 149),
              style=wx.DEFAULT_FRAME_STYLE, title='wxFrame1')
        self.SetAutoLayout(True)
        self.SetClientSize(wx.Size(409, 122))

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label='staticText1', name='staticText1', parent=self,
              pos=wx.Point(23, 25), size=wx.Size(52, 13), style=0)

        self.textCtrl1 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL1, name='textCtrl1',
              parent=self, pos=wx.Point(96, 25), size=wx.Size(288, 23), style=0,
              value='textCtrl1')
        self.textCtrl1.SetConstraints(LayoutAnchors(self.textCtrl1, True, True,
              True, True))

        self.button1 = wx.Button(id=wxID_FRAME1BUTTON1, label='button1',
              name='button1', parent=self, pos=wx.Point(216, 72),
              size=wx.Size(72, 24), style=0)
        self.button1.SetConstraints(LayoutAnchors(self.button1, False, False,
              True, True))

        self.button2 = wx.Button(id=wxID_FRAME1BUTTON2, label='button2',
              name='button2', parent=self, pos=wx.Point(312, 72),
              size=wx.Size(72, 24), style=0)
        self.button2.SetConstraints(LayoutAnchors(self.button2, False, False,
              True, True))

    def __init__(self, parent):
        self._init_ctrls(parent)


if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = create(None)
    frame.Show(True)
    app.MainLoop()
