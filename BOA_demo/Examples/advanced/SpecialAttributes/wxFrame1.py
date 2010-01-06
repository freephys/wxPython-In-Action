#Boa:Frame:wxFrame1

import wx

def create(parent, title):
    return wxFrame1(parent, title)

[wxID_WXFRAME1, wxID_WXFRAME1BUTTON1, wxID_WXFRAME1SPLITTERWINDOW1, 
 wxID_WXFRAME1TEXTCTRL1, wxID_WXFRAME1TEXTCTRL2, wxID_WXFRAME1TEXTCTRL3, 
] = [wx.NewId() for _init_ctrls in range(6)]

class wxFrame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_WXFRAME1, name='', parent=prnt,
              pos=wx.Point(286, 235), size=wx.Size(307, 300),
              style=wx.DEFAULT_FRAME_STYLE, title=self.frameTitle)
        self.SetClientSize(wx.Size(299, 273))

        self.button1 = wx.Button(id=wxID_WXFRAME1BUTTON1,
              label=self.buttonLabel, name='button1', parent=self,
              pos=wx.Point(96, 104), size=wx.Size(104, 24), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_WXFRAME1BUTTON1)

        self.textCtrl1 = wx.TextCtrl(id=wxID_WXFRAME1TEXTCTRL1,
              name='textCtrl1', parent=self, pos=wx.Point(8, 8),
              size=wx.Size(280, 72), style=0, value='textCtrl1')

        self.splitterWindow1 = wx.SplitterWindow(id=wxID_WXFRAME1SPLITTERWINDOW1,
              name='splitterWindow1', parent=self, point=wx.Point(8, 144),
              size=wx.Size(280, 120), style=wx.SP_3D)

        self.textCtrl2 = wx.TextCtrl(id=wxID_WXFRAME1TEXTCTRL2,
              name='textCtrl2', parent=self.splitterWindow1, pos=wx.Point(2, 2),
              size=wx.Size(138, 116), style=0, value='textCtrl2')

        self.textCtrl3 = wx.TextCtrl(id=wxID_WXFRAME1TEXTCTRL3,
              name='textCtrl3', parent=self.splitterWindow1, pos=wx.Point(147,
              2), size=wx.Size(131, 116), style=0, value='textCtrl3')
        self.splitterWindow1.SplitVertically(self.textCtrl2, self.textCtrl3,
              self.splitSize)

    def __init__(self, parent, frameTitle):
        self.frameTitle = 'Frame Caption'
        self.frameTitle = frameTitle
        self.buttonLabel = 'Press Me!'
        self.splitSize = 150
        self._init_ctrls(parent)

    def OnButton1Button(self, event):
        self.Close()


if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = create(None, 'Hello World')
    frame.Show(True)
    app.MainLoop()
