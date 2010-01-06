#Boa:FramePanel:Panel1

import wx

[wxID_PANEL1] = [wx.NewId() for _init_ctrls in range(1)]

class TabPanel(wx.Panel):
    def _init_ctrls(self, prnt):
        wx.Panel.__init__(self, style=wx.TAB_TRAVERSAL, name='', parent=prnt, pos=wx.DefaultPosition, id=wxID_PANEL1, size=wx.Size(200, 100))

    def __init__(self, parent, id, pos, size, style, name):
        self._init_ctrls(parent)
