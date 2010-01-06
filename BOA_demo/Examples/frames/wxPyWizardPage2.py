#Boa:PyWizardPage:wxPyWizardPage2

import wx
import wx.wizard

[wxID_WXPYWIZARDPAGE2, wxID_WXPYWIZARDPAGE2BUTTON1, 
 wxID_WXPYWIZARDPAGE2BUTTON2, 
] = [wx.NewId() for _init_ctrls in range(3)]

class wxPyWizardPage2(wx.wizard.PyWizardPage):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.wizard.PyWizardPage.__init__(self, bitmap=wx.NullBitmap, parent=prnt,
              resource='')
        self.SetName('wxPyWizardPage2')
        self.SetBackgroundColour(wx.Colour(128, 128, 255))

        self.button1 = wx.Button(id=wxID_WXPYWIZARDPAGE2BUTTON1,
              label='button1', name='button1', parent=self, pos=wx.Point(8, 8),
              size=wx.Size(75, 23), style=0)

        self.button2 = wx.Button(id=wxID_WXPYWIZARDPAGE2BUTTON2,
              label='button2', name='button2', parent=self, pos=wx.Point(184,
              224), size=wx.Size(75, 23), style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)

    _next = None
    def GetNext(self):
        return self._next

    _prev = None
    def GetPrev(self):
        return self._prev
