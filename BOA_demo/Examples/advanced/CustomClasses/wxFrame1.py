#Boa:Frame:wxFrame1

import wx

def create(parent):
    return wxFrame1(parent)

[wxID_WXFRAME1, wxID_WXFRAME1TREECTRL1, 
] = [wx.NewId() for _init_ctrls in range(2)]

class wxFrame1(wx.Frame):
    _custom_classes = {'wx.TreeCtrl': ['MyTreeCtrl']}
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_WXFRAME1, name='', parent=prnt,
              pos=wx.Point(154, 154), size=wx.Size(488, 258),
              style=wx.DEFAULT_FRAME_STYLE, title='wxFrame1')
        self.SetClientSize(wx.Size(480, 231))

        self.treeCtrl1 = MyTreeCtrl(id=wxID_WXFRAME1TREECTRL1, name='treeCtrl1',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(480, 231),
              style=wx.TR_HAS_BUTTONS)

    def __init__(self, parent):
        self._init_ctrls(parent)


class MyTreeCtrl(wx.TreeCtrl):
    pass


if __name__ == '__main__':
    app = wx.PySimpleApp()
    wx.InitAllImageHandlers()
    frame = create(None)
    frame.Show()

    app.MainLoop()
