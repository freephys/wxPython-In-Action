#Boa:FramePanel:wxPanel2

import wx

def create(parent):
    return wxPanel2(parent)

[wxID_WXPANEL2, wxID_WXPANEL2CHECKBOX1, wxID_WXPANEL2STATICTEXT1, 
] = [wx.NewId() for _init_ctrls in range(3)]

class wxPanel2(wx.Panel):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Panel.__init__(self, id=wxID_WXPANEL2, name='', parent=prnt,
              pos=wx.Point(356, 242), size=wx.Size(331, 263),
              style=wx.TAB_TRAVERSAL)
        self.SetClientSize(wx.Size(323, 236))

        self.staticText1 = wx.StaticText(id=wxID_WXPANEL2STATICTEXT1,
              label='wxPanel2', name='staticText1', parent=self,
              pos=wx.Point(16, 16), size=wx.Size(46, 13), style=0)

        self.checkBox1 = wx.CheckBox(id=wxID_WXPANEL2CHECKBOX1, label='checkBox1',
              name='checkBox1', parent=self, pos=wx.Point(16, 40),
              size=wx.Size(73, 13), style=0)

    def __init__(self, parent, id, pos, size, style, name):
        self._init_ctrls(parent)
