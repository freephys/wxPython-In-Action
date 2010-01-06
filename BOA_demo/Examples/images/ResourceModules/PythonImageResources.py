#Boa:Frame:ResourceModuleFrm

import wx

import Boa_img

BoaSectionIcons = ('Palette', 'Editor', 'Designer', 'Inspector', 'Debugger',
                   'Collection Editor', 'Class Browser', 'Output & Errors',
                   'Help', 'Shell', 'Explorer', 'Zope')

def create(parent):
    return ResourceModuleFrm(parent)

[wxID_RESOURCEMODULEFRM, wxID_RESOURCEMODULEFRMBITMAPBUTTON, 
 wxID_RESOURCEMODULEFRMLISTVIEW, 
] = [wx.NewId() for _init_ctrls in range(3)]

[wxID_RESOURCEMODULEFRMTOOLBAR1TOOLS0, wxID_RESOURCEMODULEFRMTOOLBAR1TOOLS1,
 wxID_RESOURCEMODULEFRMTOOLBAR1TOOLS2, wxID_RESOURCEMODULEFRMTOOLBAR1TOOLS3,
 wxID_RESOURCEMODULEFRMTOOLBAR1TOOLS4, wxID_RESOURCEMODULEFRMTOOLBAR1TOOLS5,
 wxID_RESOURCEMODULEFRMTOOLBAR1TOOLS6,
] = [wx.NewId() for _init_coll_toolBar_Tools in range(7)]

class ResourceModuleFrm(wx.Frame):
    def _init_coll_images_Images(self, parent):
        # generated method, don't edit

        parent.Add(bitmap=Boa_img.getPaletteBitmap(), mask=wx.NullBitmap)
        parent.Add(bitmap=Boa_img.getEditorBitmap(), mask=wx.NullBitmap)
        parent.Add(bitmap=Boa_img.getDesignerBitmap(), mask=wx.NullBitmap)
        parent.Add(bitmap=Boa_img.getInspectorBitmap(), mask=wx.NullBitmap)
        parent.Add(bitmap=Boa_img.getDebuggerBitmap(), mask=wx.NullBitmap)
        parent.Add(bitmap=Boa_img.getCollectionEditorBitmap(),
              mask=wx.NullBitmap)
        parent.Add(bitmap=Boa_img.getClassBrowserBitmap(), mask=wx.NullBitmap)
        parent.Add(bitmap=Boa_img.getOutputErrorBitmap(), mask=wx.NullBitmap)
        parent.Add(bitmap=Boa_img.getHelpBitmap(), mask=wx.NullBitmap)
        parent.Add(bitmap=Boa_img.getShellBitmap(), mask=wx.NullBitmap)
        parent.Add(bitmap=Boa_img.getExplorerBitmap(), mask=wx.NullBitmap)
        parent.Add(bitmap=Boa_img.getZopeBitmap(), mask=wx.NullBitmap)

    def _init_utils(self):
        # generated method, don't edit
        self.images = wx.ImageList(height=16, width=16)
        self._init_coll_images_Images(self.images)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_RESOURCEMODULEFRM,
              name='ResourceModuleFrm', parent=prnt, pos=wx.Point(604, 403),
              size=wx.Size(419, 260), style=wx.DEFAULT_FRAME_STYLE,
              title='Images using a Resource Module built with img2py')
        self._init_utils()
        self.SetClientSize(wx.Size(411, 233))
        self.SetBackgroundColour(wx.Colour(0, 128, 255))
        self.SetSizeHints(419, 260, 419, 260)
        self.Center(wx.BOTH)

        self.bitmapButton = wx.BitmapButton(bitmap=Boa_img.getBoaButtonBitmap(),
              id=wxID_RESOURCEMODULEFRMBITMAPBUTTON, name='bitmapButton',
              parent=self, pos=wx.Point(16, 67), size=wx.Size(112, 88),
              style=wx.BU_AUTODRAW)
        self.bitmapButton.Bind(wx.EVT_BUTTON, self.OnBitmapbuttonButton,
              id=wxID_RESOURCEMODULEFRMBITMAPBUTTON)

        self.listView = wx.ListView(id=wxID_RESOURCEMODULEFRMLISTVIEW,
              name='listView', parent=self, pos=wx.Point(148, 27),
              size=wx.Size(247, 176), style=wx.LC_SINGLE_SEL|wx.LC_ICON)
        self.listView.SetImageList(self.images, wx.IMAGE_LIST_NORMAL)
        self.listView.SetBackgroundColour(wx.Colour(255, 255, 242))
        self.listView.Bind(wx.EVT_LIST_ITEM_ACTIVATED,
              self.OnListviewListItemActivated,
              id=wxID_RESOURCEMODULEFRMLISTVIEW)

    def __init__(self, parent):
        self._init_ctrls(parent)
        for i, name in zip(range(len(BoaSectionIcons)), BoaSectionIcons):
            self.listView.InsertImageStringItem(i, name, i)

    def OnBitmapbuttonButton(self, event):
        self.Close()

    def OnListviewListItemActivated(self, event):
        event.Skip()


if __name__ == '__main__':
    app = wx.PySimpleApp()
    wx.InitAllImageHandlers()
    frame = create(None)
    frame.Show()

    app.MainLoop()
