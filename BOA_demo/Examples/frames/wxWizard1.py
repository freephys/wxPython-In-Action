#Boa:Wizard:wxWizard1

import wx
import wx.wizard

def create(parent):
    return wxWizard1(parent)

def run(parent):
    wizard = create(parent)

    import wxPyWizardPage1, wxPyWizardPage2
    import wxWizardPageSimple1, wxWizardPageSimple2

    pwpage1 = wxPyWizardPage1.wxPyWizardPage1(wizard)
    pwpage2 = wxPyWizardPage2.wxPyWizardPage2(wizard)
    wspage1 = wxWizardPageSimple1.wxWizardPageSimple1(wizard)
    wspage2 = wxWizardPageSimple2.wxWizardPageSimple2(wizard)

    pwpage1.SetNext(pwpage2)
    pwpage2._next = wspage1
    pwpage2._prev = pwpage1
    wspage1.SetPrev(pwpage2)
    wx.wizard.WizardPageSimple.Chain(wspage1, wspage2)

    return wizard.RunWizard(pwpage1)


[wxID_WXWIZARD1, wxID_WXWIZARD1BUTTON1, wxID_WXWIZARD1STATICTEXT1, 
] = [wx.NewId() for _init_ctrls in range(3)]

class wxWizard1(wx.wizard.Wizard):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.wizard.Wizard.__init__(self, bitmap=wx.Bitmap('WizImage.png',
              wx.BITMAP_TYPE_PNG), id=wxID_WXWIZARD1, parent=prnt,
              pos=wx.Point(333, 205), title='wxWizard Example')
        self.Bind(wx.wizard.EVT_WIZARD_PAGE_CHANGING,
              self.OnWxwizard1WizardPageChanging, id=wxID_WXWIZARD1)
        self.Bind(wx.wizard.EVT_WIZARD_PAGE_CHANGED,
              self.OnWxwizard1WizardPageChanged, id=wxID_WXWIZARD1)

        self.button1 = wx.Button(id=wxID_WXWIZARD1BUTTON1, label='debug',
              name='button1', parent=self, pos=wx.Point(8, 312),
              size=wx.Size(40, 23), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_WXWIZARD1BUTTON1)

        self.staticText1 = wx.StaticText(id=wxID_WXWIZARD1STATICTEXT1,
              label='(status)', name='staticText1', parent=self, pos=wx.Point(8,
              293), size=wx.Size(34, 13), style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnButton1Button(self, event):
        wx.LogMessage(`self.GetChildren()`) #GetSizer().

    def OnWxwizard1WizardPageChanging(self, event):
        self.staticText1.SetLabel('Changing...')

    def OnWxwizard1WizardPageChanged(self, event):
        self.staticText1.SetLabel('Changed to %s'%event.GetPage().GetName())
