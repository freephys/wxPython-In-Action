#Boa:Frame:wxFrame1

""" This example demonstrates how to load .xrc files created e.g. by XRCed.

Support only allows creating/linking the components. The contents of the
xcr file is not displayed at design-time and can certainly not be managed in
the Designer.

Note that the XRCSupport plug-in must be installed. """

import wx
import wx.xrc

def create(parent):
    return wxFrame1(parent)

[wxID_WXFRAME1, wxID_WXFRAME1BOAXRCPANEL, wxID_WXFRAME1BUTTON1, 
 wxID_WXFRAME1PANEL1, 
] = [wx.NewId() for _init_ctrls in range(4)]

class wxFrame1(wx.Frame):
    def _init_utils(self):
        # generated method, don't edit
        self.xmlResource1 = wx.xrc.XmlResource(filemask='Input.xrc')

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_WXFRAME1, name='', parent=prnt,
              pos=wx.Point(250, 248), size=wx.Size(240, 165),
              style=wx.DEFAULT_FRAME_STYLE, title='wxFrame1')
        self._init_utils()
        self.SetClientSize(wx.Size(232, 138))

        self.panel1 = wx.Panel(id=wxID_WXFRAME1PANEL1, name='panel1',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(232, 138),
              style=wx.TAB_TRAVERSAL)

        self.boaXrcPanel = self.xmlResource1.LoadPanel(name='boaXrcPanel',
              parent=self.panel1)
        self.boaXrcPanel.SetSize(wx.Size(216, 88))
        self.boaXrcPanel.SetPosition(wx.Point(8, 8))

        self.button1 = wx.Button(id=wxID_WXFRAME1BUTTON1, label='OK',
              name='button1', parent=self.panel1, pos=wx.Point(144, 104),
              size=wx.Size(75, 23), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_WXFRAME1BUTTON1)

    def __init__(self, parent):
        self._init_ctrls(parent)

        # to reference an xrc control
        self.xrcLabel = wx.xrc.XRCCTRL(self, 'inputLbl')
        self.xrcTextCtrl = wx.xrc.XRCCTRL(self, 'inputCtrl')
        self.xrcCheck = wx.xrc.XRCCTRL(self, 'inputCheck')
        # to bind an event to an xrc control
        self.Bind(wx.EVT_CHECKBOX, self.OnCheckbox, id=self.xrcCheck.GetId())

    def OnButton1Button(self, event):
        print 'Entered %s'%self.xrcTextCtrl.GetValue()
        self.Close()

    def OnCheckbox(self, event):
        print 'Checkbox clicked'


if __name__ == '__main__':
    app = wx.PySimpleApp()
    wx.InitAllImageHandlers()
    frame = create(None)
    frame.Show()
    app.MainLoop()
