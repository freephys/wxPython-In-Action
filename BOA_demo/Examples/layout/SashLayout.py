#Boa:Frame:Frame1

import wx

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1PANEL1, wxID_FRAME1SASHLAYOUTWINDOW1, 
 wxID_FRAME1SASHLAYOUTWINDOW2, wxID_FRAME1SASHLAYOUTWINDOW3, 
 wxID_FRAME1SASHLAYOUTWINDOW4, wxID_FRAME1STATICTEXT1, wxID_FRAME1TEXTCTRL1, 
 wxID_FRAME1TEXTCTRL2, 
] = [wx.NewId() for _init_ctrls in range(9)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='Frame1', parent=prnt,
              pos=wx.Point(327, 136), size=wx.Size(518, 376),
              style=wx.DEFAULT_FRAME_STYLE, title='Sash layout')
        self.SetClientSize(wx.Size(510, 349))
        self.Bind(wx.EVT_SIZE, self.OnWxframe1Size)

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(248, 50), size=wx.Size(262, 234),
              style=wx.TAB_TRAVERSAL)

        self.sashLayoutWindow1 = wx.SashLayoutWindow(id=wxID_FRAME1SASHLAYOUTWINDOW1,
              name='sashLayoutWindow1', parent=self, pos=wx.Point(0, 0),
              size=wx.Size(510, 50), style=wx.CLIP_CHILDREN | wx.SW_3D)
        self.sashLayoutWindow1.SetBackgroundColour(wx.Colour(255, 0, 0))
        self.sashLayoutWindow1.SetOrientation(wx.LAYOUT_HORIZONTAL)
        self.sashLayoutWindow1.SetAlignment(wx.LAYOUT_TOP)
        self.sashLayoutWindow1.SetSashVisible(wx.SASH_BOTTOM, True)
        self.sashLayoutWindow1.SetDefaultSize(wx.Size(510, 50))
        self.sashLayoutWindow1.Bind(wx.EVT_SASH_DRAGGED,
              self.OnSashlayoutwindow1SashDragged,
              id=wxID_FRAME1SASHLAYOUTWINDOW1)

        self.sashLayoutWindow4 = wx.SashLayoutWindow(id=wxID_FRAME1SASHLAYOUTWINDOW4,
              name='sashLayoutWindow4', parent=self, pos=wx.Point(0, 284),
              size=wx.Size(510, 65), style=wx.CLIP_CHILDREN | wx.SW_3D)
        self.sashLayoutWindow4.SetBackgroundColour(wx.Colour(0, 0, 255))
        self.sashLayoutWindow4.SetAlignment(wx.LAYOUT_BOTTOM)
        self.sashLayoutWindow4.SetSashVisible(wx.SASH_TOP, True)
        self.sashLayoutWindow4.SetOrientation(wx.LAYOUT_HORIZONTAL)
        self.sashLayoutWindow4.SetDefaultSize(wx.Size(308, 65))
        self.sashLayoutWindow4.SetExtraBorderSize(10)
        self.sashLayoutWindow4.Bind(wx.EVT_SASH_DRAGGED,
              self.OnSashlayoutwindow4SashDragged,
              id=wxID_FRAME1SASHLAYOUTWINDOW4)

        self.sashLayoutWindow2 = wx.SashLayoutWindow(id=wxID_FRAME1SASHLAYOUTWINDOW2,
              name='sashLayoutWindow2', parent=self, pos=wx.Point(0, 50),
              size=wx.Size(112, 234), style=wx.CLIP_CHILDREN | wx.SW_3D)
        self.sashLayoutWindow2.SetBackgroundColour(wx.Colour(128, 255, 0))
        self.sashLayoutWindow2.SetExtraBorderSize(20)
        self.sashLayoutWindow2.SetAlignment(wx.LAYOUT_LEFT)
        self.sashLayoutWindow2.SetOrientation(wx.LAYOUT_VERTICAL)
        self.sashLayoutWindow2.SetSashVisible(wx.SASH_RIGHT, True)
        self.sashLayoutWindow2.SetDefaultSize(wx.Size(112, 113))
        self.sashLayoutWindow2.Bind(wx.EVT_SASH_DRAGGED,
              self.OnSashlayoutwindow2SashDragged,
              id=wxID_FRAME1SASHLAYOUTWINDOW2)

        self.sashLayoutWindow3 = wx.SashLayoutWindow(id=wxID_FRAME1SASHLAYOUTWINDOW3,
              name='sashLayoutWindow3', parent=self, pos=wx.Point(112, 50),
              size=wx.Size(136, 234), style=wx.CLIP_CHILDREN | wx.SW_3D)
        self.sashLayoutWindow3.SetBackgroundColour(wx.Colour(0, 255, 255))
        self.sashLayoutWindow3.SetAlignment(wx.LAYOUT_LEFT)
        self.sashLayoutWindow3.SetOrientation(wx.LAYOUT_VERTICAL)
        self.sashLayoutWindow3.SetSashVisible(wx.SASH_RIGHT, True)
        self.sashLayoutWindow3.SetDefaultSize(wx.Size(136, 234))
        self.sashLayoutWindow3.Bind(wx.EVT_SASH_DRAGGED,
              self.OnSashlayoutwindow3SashDragged,
              id=wxID_FRAME1SASHLAYOUTWINDOW3)

        self.textCtrl1 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL1, name='textCtrl1',
              parent=self.sashLayoutWindow2, pos=wx.Point(20, 20),
              size=wx.Size(69, 194), style=0, value='textCtrl1')

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label='staticText1', name='staticText1', parent=self.panel1,
              pos=wx.Point(16, 16), size=wx.Size(52, 13), style=0)

        self.textCtrl2 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL2, name='textCtrl2',
              parent=self.sashLayoutWindow4, pos=wx.Point(10, 13),
              size=wx.Size(490, 42), style=0, value='textCtrl2')

    def __init__(self, parent):
        self._init_ctrls(parent)

    def checkStatusRange(self, event):
        return event.GetDragStatus() != wx.SASH_STATUS_OUT_OF_RANGE

    def doLayout(self):
        wx.LayoutAlgorithm().LayoutWindow(self, self.panel1)
        self.panel1.Refresh()

    def OnWxframe1Size(self, event):
        self.doLayout()

    def OnSashlayoutwindow1SashDragged(self, event):
        if self.checkStatusRange(event):
            self.sashLayoutWindow1.SetDefaultSize(wx.Size(1000, event.GetDragRect().height))
            self.doLayout()

    def OnSashlayoutwindow2SashDragged(self, event):
        if self.checkStatusRange(event):
            self.sashLayoutWindow2.SetDefaultSize(wx.Size(event.GetDragRect().width, 1000))
            self.doLayout()

    def OnSashlayoutwindow3SashDragged(self, event):
        if self.checkStatusRange(event):
            self.sashLayoutWindow3.SetDefaultSize(wx.Size(event.GetDragRect().width, 1000))
            self.doLayout()

    def OnSashlayoutwindow4SashDragged(self, event):
        if self.checkStatusRange(event):
            self.sashLayoutWindow4.SetDefaultSize(wx.Size(1000, event.GetDragRect().height))
            self.doLayout()


if __name__ == '__main__':
    app = wx.PySimpleApp()
    wx.InitAllImageHandlers()
    frame = create(None)
    frame.Show()
    app.MainLoop()
