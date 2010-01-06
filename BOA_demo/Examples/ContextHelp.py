#Boa:Frame:wxFrame2

import wx

def create(parent):
    return wxFrame2(parent)

[wxID_WXFRAME2, wxID_WXFRAME2CONTEXTHELPBUTTON1, wxID_WXFRAME2PANEL1, 
 wxID_WXFRAME2TEXTCTRL1, 
] = [wx.NewId() for _init_ctrls in range(4)]

class wxFrame2(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_WXFRAME2, name='', parent=prnt,
              pos=wx.Point(176, 176), size=wx.Size(266, 64),
              style=wx.DEFAULT_FRAME_STYLE,
              title='Minimal context help example')
        self.SetClientSize(wx.Size(258, 37))

        self.panel1 = wx.Panel(id=wxID_WXFRAME2PANEL1, name='panel1',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(258, 37),
              style=wx.TAB_TRAVERSAL)

        self.textCtrl1 = wx.TextCtrl(id=wxID_WXFRAME2TEXTCTRL1,
              name='textCtrl1', parent=self.panel1, pos=wx.Point(8, 8),
              size=wx.Size(192, 21), style=0, value='textCtrl1')
        self.textCtrl1.SetHelpText('Here be expansive')
        self.textCtrl1.SetToolTipString('Here be spartan')

        self.contextHelpButton1 = wx.ContextHelpButton(parent=self.panel1,
              pos=wx.Point(224, 8), size=wx.Size(20, 19), style=wx.BU_AUTODRAW)

    def __init__(self, parent):
        self._init_ctrls(parent)


if __name__ == '__main__':
    app = wx.PySimpleApp()
    # Note this help provider is needed and was added by hand
    provider = wx.SimpleHelpProvider()
    wx.HelpProvider.Set(provider)

    wx.ToolTip.Enable(True)
    frame = create(None)
    frame.Show(True)

    app.MainLoop()
