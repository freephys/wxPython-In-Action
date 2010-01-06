#Boa:FramePanel:wxPanel1

import wx

def create(parent):
    return wxPanel1(parent)

[wxID_WXPANEL1, wxID_WXPANEL1STATICTEXT1, wxID_WXPANEL1TEXTCTRL1, 
] = [wx.NewId() for _init_ctrls in range(3)]

class wxPanel1(wx.Panel):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Panel.__init__(self, id=wxID_WXPANEL1, name='', parent=prnt,
              pos=wx.Point(352, 271), size=wx.Size(293, 224),
              style=wx.TAB_TRAVERSAL)
        self.SetClientSize(wx.Size(285, 197))

        self.staticText1 = wx.StaticText(id=wxID_WXPANEL1STATICTEXT1,
              label='wxPanel1', name='staticText1', parent=self, pos=wx.Point(8,
              16), size=wx.Size(46, 13), style=0)

        self.textCtrl1 = wx.TextCtrl(id=wxID_WXPANEL1TEXTCTRL1, name='textCtrl1',
              parent=self, pos=wx.Point(8, 40), size=wx.Size(100, 21), style=0,
              value='textCtrl1')

    def __init__(self, parent, id, pos, size, style, name):
        self._init_ctrls(parent)
