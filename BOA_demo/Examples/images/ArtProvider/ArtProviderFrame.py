#Boa:Frame:Frame1

# To use an artprovider for bitmap properties, click the edit button of the
# property editor to open the file dialog. On the file dialog, change the
# image type to ArtProvider and click Open.

import wx

import ArtProviderExample

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BITMAPBUTTON1, wxID_FRAME1BITMAPBUTTON2, 
 wxID_FRAME1PANEL1, wxID_FRAME1STATICTEXT1, wxID_FRAME1STATICTEXT2, 
] = [wx.NewId() for _init_ctrls in range(6)]

class Frame1(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(141, 122), size=wx.Size(270, 155),
              style=wx.DEFAULT_FRAME_STYLE, title='ArtProvider Demo')
        self.SetClientSize(wx.Size(262, 121))

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1', parent=self,
              pos=wx.Point(0, 0), size=wx.Size(262, 121),
              style=wx.TAB_TRAVERSAL)

        self.bitmapButton1 = wx.BitmapButton(bitmap=wx.ArtProvider.GetBitmap('wxART_BOA_ICON',
              wx.ART_TOOLBAR, wx.DefaultSize), id=wxID_FRAME1BITMAPBUTTON1,
              name='bitmapButton1', parent=self.panel1, pos=wx.Point(168, 56),
              size=wx.Size(32, 32), style=wx.BU_AUTODRAW)

        self.bitmapButton2 = wx.BitmapButton(bitmap=wx.ArtProvider.GetBitmap('wxART_TIP',
              wx.ART_TOOLBAR, wx.DefaultSize), id=wxID_FRAME1BITMAPBUTTON2,
              name='bitmapButton2', parent=self.panel1, pos=wx.Point(56, 40),
              size=wx.Size(56, 56), style=wx.BU_AUTODRAW)

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label='Standard ArtId', name='staticText1', parent=self.panel1,
              pos=wx.Point(48, 16), size=wx.Size(73, 13), style=0)

        self.staticText2 = wx.StaticText(id=wxID_FRAME1STATICTEXT2,
              label='Custom ArtId', name='staticText2', parent=self.panel1,
              pos=wx.Point(152, 16), size=wx.Size(65, 13), style=0)

    def __init__(self, parent):
        self._init_ctrls(parent)


if __name__ == '__main__':
    app = wx.PySimpleApp()
    
    # Install the art provider in your application
    wx.ArtProvider.PushProvider(ArtProviderExample.ArtProviderExample())
    
    frame = create(None)
    frame.Show()

    app.MainLoop()
