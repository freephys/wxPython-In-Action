#Boa:Frame:wxFrame2

import wx

def create(parent):
    return wxFrame2(parent)

[wxID_WXFRAME2] = [wx.NewId() for _init_ctrls in range(1)]

class wxFrame2(wx.Frame):
    """ A reference to this frame is kept in frame1 therefor we have to
        stop the frame from being destroyed when it is closed. This is done
        by connecting to the close event and hiding the form """
    def _init_utils(self):
        # generated method, don't edit
        pass

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_WXFRAME2, name='', parent=prnt,
              pos= wx.Point(198, 198), size= wx.Size(342, 146),
              style=wx.DEFAULT_FRAME_STYLE, title='wxFrame2')
        self._init_utils()
        self.SetClientSize(wx.Size(334, 119))
        self.Bind(wx.EVT_CLOSE, self.OnWxframe2Close)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnWxframe2Close(self, event):
        self.Show(False)
