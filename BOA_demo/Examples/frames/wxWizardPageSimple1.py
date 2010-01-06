#Boa:WizardPageSimple:wxWizardPageSimple1

import wx
import wx.wizard 

[wxID_WXWIZARDPAGESIMPLE1, wxID_WXWIZARDPAGESIMPLE1BUTTON1, 
] = [wx.NewId() for _init_ctrls in range(2)]

class wxWizardPageSimple1(wx.wizard.WizardPageSimple):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.wizard.WizardPageSimple.__init__(self, next=None, parent=prnt,
              prev=None)
        self.SetAutoLayout(True)

        self.button1 = wx.Button(id=wxID_WXWIZARDPAGESIMPLE1BUTTON1,
              label='Simple Page 1', name='button1', parent=self,
              pos=wx.Point(8, 8), size=wx.Size(200, 32), style=0)
        self.button1.SetAutoLayout(True)

    def __init__(self, parent):
        self._init_ctrls(parent)
