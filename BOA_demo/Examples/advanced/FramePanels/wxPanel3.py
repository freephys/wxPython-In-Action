#Boa:FramePanel:wxPanel3

import wx

def create(parent):
    return wxPanel3(parent)

[wxID_WXPANEL3, wxID_WXPANEL3BUTTON1, wxID_WXPANEL3STATICTEXT1, 
] = [wx.NewId() for _init_ctrls in range(3)]

class wxPanel3(wx.Panel):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Panel.__init__(self, id=wxID_WXPANEL3, name='', parent=prnt,
              pos=wx.Point(198, 198), size=wx.Size(200, 100), style=self.style)
        self.SetClientSize(wx.Size(192, 73))

        self.staticText1 = wx.StaticText(id=wxID_WXPANEL3STATICTEXT1,
              label='wxPanel3', name='staticText1', parent=self, pos=wx.Point(8,
              8), size=wx.Size(46, 13), style=0)

        self.button1 = wx.Button(id=wxID_WXPANEL3BUTTON1, label='button1',
              name='button1', parent=self, pos=wx.Point(8, 32), size=wx.Size(75,
              23), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_WXPANEL3BUTTON1)

    def __init__(self, parent, id, pos, size, style, name):
        # style is added as a 'frame attribute' because many styles cannot be
        # changed after creation.
        self.style = wx.TAB_TRAVERSAL
        self.style = style

        self._init_ctrls(parent)

        # This code must be added manually to override the design-time values
        # This is only needed for those FramePanels that are not directly
        # contained (when it's parent sizes it)
        self.SetPosition(pos)
        self.SetSize(size)

    def OnButton1Button(self, event):
        self.staticText1.SetLabel('Click!')
