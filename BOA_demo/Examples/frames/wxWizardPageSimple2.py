#Boa:WizardPageSimple:wxWizardPageSimple2

import wx
import wx.wizard

[wxID_WXWIZARDPAGESIMPLE2, wxID_WXWIZARDPAGESIMPLE2BUTTON1, 
] = [wx.NewId() for _init_ctrls in range(2)]

class wxWizardPageSimple2(wx.wizard.WizardPageSimple):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.wizard.WizardPageSimple.__init__(self, next=None, parent=prnt,
              prev=None)
        self.SetAutoLayout(True)

        self.button1 = wx.Button(id=wxID_WXWIZARDPAGESIMPLE2BUTTON1,
              label='Simple Page 2', name='button1', parent=self,
              pos=wx.Point(8, 8), size=wx.Size(200, 32), style=0)
        self.button1.SetAutoLayout(True)

    def __init__(self, parent):
        self._init_ctrls(parent)
