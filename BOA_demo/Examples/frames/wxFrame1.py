#Boa:Frame:wxFrame1

import wx

def create(parent):
    return wxFrame1(parent)

[wxID_WXFRAME1, wxID_WXFRAME1BUTTON1, wxID_WXFRAME1BUTTON2, 
 wxID_WXFRAME1BUTTON3, 
] = [wx.NewId() for _init_ctrls in range(4)]

class wxFrame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_WXFRAME1, name='', parent=prnt,
              pos=wx.Point(299, 227), size=wx.Size(370, 146),
              style=wx.DEFAULT_FRAME_STYLE, title='wxFrame1')
        self.SetClientSize(wx.Size(362, 119))

        self.button1 = wx.Button(id=wxID_WXFRAME1BUTTON1, label='Show Frame 2',
              name='button1', parent=self, pos=wx.Point(112, 16),
              size=wx.Size(152, 23), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_WXFRAME1BUTTON1)

        self.button2 = wx.Button(id=wxID_WXFRAME1BUTTON2, label='Show Frame 3',
              name='button2', parent=self, pos=wx.Point(112, 48),
              size=wx.Size(152, 23), style=0)
        self.button2.Bind(wx.EVT_BUTTON, self.OnButton2Button,
              id=wxID_WXFRAME1BUTTON2)

        self.button3 = wx.Button(id=wxID_WXFRAME1BUTTON3, label='Show Wizard',
              name='button3', parent=self, pos=wx.Point(112, 80),
              size=wx.Size(152, 23), style=0)
        self.button3.Bind(wx.EVT_BUTTON, self.OnButton3Button,
              id=wxID_WXFRAME1BUTTON3)

    def __init__(self, parent):
        self._init_ctrls(parent)

        import wxFrame2
        self.frame2 = wxFrame2.create(self)

    def OnButton1Button(self, event):
        """ Example of a frame kept as a reference

        Note it was created in __init__
        """
        self.frame2.Show(True)

    def OnButton2Button(self, event):
        """ Example of a dynamic unreferenced frame """
        import wxFrame3
        wxFrame3.create(self).Show(True)

    def OnButton3Button(self, event):
        """ Example of calling a wxWizard """
        import wxWizard1

        if wxWizard1.run(self):
            wx.MessageBox('Wizard completed')
        else:
            wx.MessageBox('Wizard cancelled')




if __name__ == '__main__':
    app = wx.PySimpleApp()
    wx.InitAllImageHandlers()
    frame = create(None)
    # needed when running from Boa under Windows 9X
    frame.Show();frame.Hide();frame.Show()

    app.MainLoop()
