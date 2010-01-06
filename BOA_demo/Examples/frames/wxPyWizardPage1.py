#Boa:PyWizardPage:wxPyWizardPage1

import wx
import wx.wizard 

[wxID_WXPYWIZARDPAGE1, wxID_WXPYWIZARDPAGE1BUTTON1, 
 wxID_WXPYWIZARDPAGE1BUTTON2, wxID_WXPYWIZARDPAGE1STATICTEXT1, 
] = [wx.NewId() for _init_ctrls in range(4)]

class wxPyWizardPage1(wx.wizard.PyWizardPage):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.wizard.PyWizardPage.__init__(self, bitmap=wx.NullBitmap, parent=prnt,
              resource='')

        self.staticText1 = wx.StaticText(id=wxID_WXPYWIZARDPAGE1STATICTEXT1,
              label='PyWizardPage1', name='staticText1', parent=self,
              pos=wx.Point(8, 8), size=wx.Size(76, 13), style=0)

        self.button1 = wx.Button(id=wxID_WXPYWIZARDPAGE1BUTTON1,
              label='button1', name='button1', parent=self, pos=wx.Point(8, 32),
              size=wx.Size(75, 23), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_WXPYWIZARDPAGE1BUTTON1)

        self.button2 = wx.Button(id=wxID_WXPYWIZARDPAGE1BUTTON2,
              label='button2', name='button2', parent=self, pos=wx.Point(400,
              88), size=wx.Size(75, 23), style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)

    _next = None
    def GetNext(self):
        return self._next
    def SetNext(self, value):
        self._next = value
    Next = property(GetNext, SetNext)

    _prev = None
    def GetPrev(self):
        return self._prev
    def SetPrev(self, value):
        self._prev = value
    Prev = property(GetPrev, SetPrev)

    def OnButton1Button(self, event):
        self.staticText1.SetLabel(`self.GetSize()`)
