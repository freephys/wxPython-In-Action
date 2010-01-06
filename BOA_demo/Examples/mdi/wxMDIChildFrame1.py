#Boa:MDIChild:wxMDIChildFrame1

import wx

def create(parent):
    return wxMDIChildFrame1(parent)

[wxID_WXMDICHILDFRAME1, wxID_WXMDICHILDFRAME1BUTTON1, 
 wxID_WXMDICHILDFRAME1RADIOBUTTON1, 
] = [wx.NewId() for _init_ctrls in range(3)]

class wxMDIChildFrame1(wx.MDIChildFrame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.MDIChildFrame.__init__(self, id=wxID_WXMDICHILDFRAME1, name='',
              parent=prnt, pos=wx.Point(38, 49), size=wx.Size(326, 158),
              style=wx.DEFAULT_FRAME_STYLE, title='wxMDIChildFrame1')
        self.SetClientSize(wx.Size(318, 131))

        self.button1 = wx.Button(id=wxID_WXMDICHILDFRAME1BUTTON1,
              label='button1', name='button1', parent=self, pos=wx.Point(8, 8),
              size=wx.Size(75, 23), style=0)

        self.radioButton1 = wx.RadioButton(id=wxID_WXMDICHILDFRAME1RADIOBUTTON1,
              label='radioButton1', name='radioButton1', parent=self,
              pos=wx.Point(8, 40), size=wx.Size(80, 20), style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)
