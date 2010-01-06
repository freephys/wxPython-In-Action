#Boa:Frame:AttrMixinFrame

""" Example module which demonstrates the use of Attribute Mixin classes.

Attribute Mixin classes can be used to centralise attribute declarations
that can be shared between frames.

The mixin class name must end with the postfix _AttrMixin.

"""

import wx

# Note: The AttrMixin class must be imported in this form and it's module must
#       be in the same directory as the frame module
from AttrMixins import Test_AttrMixin

def create(parent):
    return AttrMixinFrame(parent)

[wxID_ATTRMIXINFRAME, wxID_ATTRMIXINFRAMEBUTTON1, 
] = [wx.NewId() for _init_ctrls in range(2)]

# Note: Inherits from the AttrMixin class after wxFrame
class AttrMixinFrame(wx.Frame, Test_AttrMixin):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_ATTRMIXINFRAME, name='AttrMixinFrame',
              parent=prnt, pos=wx.Point(352, 222), size=wx.Size(201, 104),
              style=wx.DEFAULT_FRAME_STYLE, title=self.frameTitle)
        self.SetClientSize(wx.Size(193, 77))

        self.button1 = wx.Button(id=wxID_ATTRMIXINFRAMEBUTTON1,
              label=self.buttonLabel, name='button1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(193, 77), style=0)

    def __init__(self, parent):
        # Note: Call inherited mixin constructor before _init_ctrls
        Test_AttrMixin.__init__(self)

        self._init_ctrls(parent)


if __name__ == '__main__':
    app = wx.PySimpleApp()
    wx.InitAllImageHandlers()
    frame = create(None)
    frame.Show()
    app.MainLoop()
