#Boa:MDIParent:wxMDIParentFrame1

import wx
from wx.lib.anchors import LayoutAnchors

import wxMDIChildFrame1

def create(parent):
    return wxMDIParentFrame1(parent)

[wxID_WXMDIPARENTFRAME1, wxID_WXMDIPARENTFRAME1SASHLAYOUTWINDOW1, 
 wxID_WXMDIPARENTFRAME1TREECTRL1, 
] = [wx.NewId() for _init_ctrls in range(3)]

[wxID_WXMDIPARENTFRAME1MENU1ITEMS0] = [wx.NewId() for _init_coll_menu1_Items in range(1)]

class wxMDIParentFrame1(wx.MDIParentFrame):
    def _init_coll_menuBar1_Menus(self, parent):
        # generated method, don't edit

        parent.Append(menu=self.menu1, title='&File')

    def _init_coll_menu1_Items(self, parent):
        # generated method, don't edit

        parent.Append(help='Items0', id=wxID_WXMDIPARENTFRAME1MENU1ITEMS0,
              kind=wx.ITEM_NORMAL, text='New child window')
        self.Bind(wx.EVT_MENU, self.OnMenu1items0Menu,
              id=wxID_WXMDIPARENTFRAME1MENU1ITEMS0)

    def _init_utils(self):
        # generated method, don't edit
        self.menuBar1 = wx.MenuBar()

        self.menu1 = wx.Menu(title='')

        self._init_coll_menuBar1_Menus(self.menuBar1)
        self._init_coll_menu1_Items(self.menu1)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.MDIParentFrame.__init__(self, id=wxID_WXMDIPARENTFRAME1, name='',
              parent=prnt, pos=wx.Point(129, 88), size=wx.Size(544, 318),
              style=wx.DEFAULT_FRAME_STYLE | wx.VSCROLL | wx.HSCROLL,
              title='wxMDIParentFrame1')
        self._init_utils()
        self.SetMenuBar(self.menuBar1)
        self.SetAutoLayout(True)
        self.SetClientSize(wx.Size(536, 291))
        self.Bind(wx.EVT_SIZE, self.OnWxmdiparentframe1Size)

        self.sashLayoutWindow1 = wx.SashLayoutWindow(id=wxID_WXMDIPARENTFRAME1SASHLAYOUTWINDOW1,
              name='sashLayoutWindow1', parent=self, pos=wx.Point(0, 0),
              size=wx.Size(137, 272), style=wx.CLIP_CHILDREN | wx.SW_3D)
        self.sashLayoutWindow1.SetOrientation(wx.LAYOUT_VERTICAL)
        self.sashLayoutWindow1.SetAlignment(wx.LAYOUT_LEFT)
        self.sashLayoutWindow1.SetSashVisible(wx.SASH_RIGHT, True)
        self.sashLayoutWindow1.SetDefaultSize(wx.Size(137, 272))
        self.sashLayoutWindow1.Bind(wx.EVT_SASH_DRAGGED,
              self.OnSashlayoutwindow1SashDragged,
              id=wxID_WXMDIPARENTFRAME1SASHLAYOUTWINDOW1)

        self.treeCtrl1 = wx.TreeCtrl(id=wxID_WXMDIPARENTFRAME1TREECTRL1,
              name='treeCtrl1', parent=self.sashLayoutWindow1, pos=wx.Point(0,
              0), size=wx.Size(134, 272), style=wx.TR_HAS_BUTTONS)

    def __init__(self, parent):
        self._init_ctrls(parent)

        child1 = wxMDIChildFrame1.create(self)
        child1.Show(True)

    def OnMenu1items0Menu(self, event):
        wxMDIChildFrame1.create(self).Show(True)

    def OnWxmdiparentframe1Size(self, event):
        wx.LayoutAlgorithm().LayoutMDIFrame(self)

    def OnSashlayoutwindow1SashDragged(self, event):
        if event.GetDragStatus() == wx.SASH_STATUS_OUT_OF_RANGE:
            return

        eID = event.GetId()
        if eID == wxID_WXMDIPARENTFRAME1SASHLAYOUTWINDOW1:
            self.sashLayoutWindow1.SetDefaultSize(wx.Size(event.GetDragRect().width, 0))

        wx.LayoutAlgorithm().LayoutMDIFrame(self)
        self.GetClientWindow().Refresh()
