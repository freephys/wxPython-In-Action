#Boa:Frame:Frame2

""" Mixing Custom Classes and Special Attributes to make the type of
    a control dynamically setable at run-time """

import wx

class RedDynCtrl(wx.Window):
    def __init__(self, *_args, **_kwargs):
        wx.Window.__init__(self, *_args, **_kwargs)
        self.SetBackgroundColour(wx.RED)

class BlueDynCtrl(wx.Window):
    def __init__(self, *_args, **_kwargs):
        wx.Window.__init__(self, *_args, **_kwargs)
        self.SetBackgroundColour(wx.BLUE)
    


def create(parent, DynCtrl):
    return Frame2(parent, DynCtrl)

[wxID_FRAME2, wxID_FRAME2WINDOW1, 
] = [wx.NewId() for _init_ctrls in range(2)]

   

class Frame2(wx.Frame):
    _custom_classes = {'wx.Window': ['self.DynamicControl']}
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME2, name='', parent=prnt,
              pos=wx.Point(303, 211), size=wx.Size(322, 182),
              style=wx.DEFAULT_FRAME_STYLE, title='Frame2')
        self.SetClientSize(wx.Size(314, 155))

        self.window1 = self.DynamicControl(id=wxID_FRAME2WINDOW1,
              name='window1', parent=self, pos=wx.Point(0, 0), size=wx.Size(314,
              155), style=0)

    # Control class is passed in as parameter and set to a special frame attribute
    # After dropping the custom classes base class on the frame, manually change
    # the class of the control to your special frame attribute name
    def __init__(self, parent, DynCtrl):
        self.DynamicControl = wx.Window
        self.DynamicControl = DynCtrl
        
        self._init_ctrls(parent)
        
        self.SetPosition(wx.DefaultPosition)


if __name__ == '__main__':
    app = wx.PySimpleApp()
    wx.InitAllImageHandlers()
    redFrame = create(None, RedDynCtrl)
    blueFrame = create(None, BlueDynCtrl)

    redFrame.Show()
    blueFrame.Show()

    app.MainLoop()
