#Boa:Frame:Frame1

import wx
import Dialog2

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1STATUSBAR1, wxID_FRAME1TEXTEDITOR, 
] = [wx.NewId() for _init_ctrls in range(3)]

[wxID_FRAME1MENUFILECLOSE, wxID_FRAME1MENUFILEEXIT, wxID_FRAME1MENUFILEOPEN, 
 wxID_FRAME1MENUFILESAVE, wxID_FRAME1MENUFILESAVEAS, 
] = [wx.NewId() for _init_coll_menuFile_Items in range(5)]

[wxID_FRAME1MENUHELPABOUT] = [wx.NewId() for _init_coll_menuHelp_Items in range(1)]

class Frame1(wx.Frame):
    def _init_coll_menuBar1_Menus(self, parent):
        # generated method, don't edit

        parent.Append(menu=self.menuFile, title='File')
        parent.Append(menu=self.menuHelp, title='Help')

    def _init_coll_menuHelp_Items(self, parent):
        # generated method, don't edit

        parent.Append(help='Display general information about Notebook',
              id=wxID_FRAME1MENUHELPABOUT, kind=wx.ITEM_NORMAL, text='About')
        self.Bind(wx.EVT_MENU, self.OnMenuHelpAboutMenu,
              id=wxID_FRAME1MENUHELPABOUT)

    def _init_coll_menuFile_Items(self, parent):
        # generated method, don't edit

        parent.Append(help='Open a file', id=wxID_FRAME1MENUFILEOPEN,
              kind=wx.ITEM_NORMAL, text='Open')
        parent.Append(help='Save file', id=wxID_FRAME1MENUFILESAVE,
              kind=wx.ITEM_NORMAL, text='Save')
        parent.Append(help='Save file as', id=wxID_FRAME1MENUFILESAVEAS,
              kind=wx.ITEM_NORMAL, text='Save as')
        parent.Append(help='Close file', id=wxID_FRAME1MENUFILECLOSE,
              kind=wx.ITEM_NORMAL, text='Close')
        parent.Append(help='Close program', id=wxID_FRAME1MENUFILEEXIT,
              kind=wx.ITEM_NORMAL, text='Exit')
        self.Bind(wx.EVT_MENU, self.OnMenuFileOpenMenu,
              id=wxID_FRAME1MENUFILEOPEN)
        self.Bind(wx.EVT_MENU, self.OnMenuFileSaveMenu,
              id=wxID_FRAME1MENUFILESAVE)
        self.Bind(wx.EVT_MENU, self.OnMenuFileSaveasMenu,
              id=wxID_FRAME1MENUFILESAVEAS)
        self.Bind(wx.EVT_MENU, self.OnMenuFileExitMenu,
              id=wxID_FRAME1MENUFILEEXIT)
        self.Bind(wx.EVT_MENU, self.OnMenuFileCloseMenu,
              id=wxID_FRAME1MENUFILECLOSE)

    def _init_coll_statusBar1_Fields(self, parent):
        # generated method, don't edit
        parent.SetFieldsCount(1)

        parent.SetStatusText(number=0, text='status')

        parent.SetStatusWidths([-1])

    def _init_utils(self):
        # generated method, don't edit
        self.menuFile = wx.Menu(title='')

        self.menuHelp = wx.Menu(title='')

        self.menuBar1 = wx.MenuBar()

        self._init_coll_menuFile_Items(self.menuFile)
        self._init_coll_menuHelp_Items(self.menuHelp)
        self._init_coll_menuBar1_Menus(self.menuBar1)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(361, 246), size=wx.Size(613, 436),
              style=wx.DEFAULT_FRAME_STYLE, title='Notebook')
        self._init_utils()
        self.SetClientSize(wx.Size(605, 402))
        self.SetMenuBar(self.menuBar1)

        self.statusBar1 = wx.StatusBar(id=wxID_FRAME1STATUSBAR1,
              name='statusBar1', parent=self, style=0)
        self._init_coll_statusBar1_Fields(self.statusBar1)
        self.SetStatusBar(self.statusBar1)

        self.textEditor = wx.TextCtrl(id=wxID_FRAME1TEXTEDITOR,
              name='textEditor', parent=self, pos=wx.Point(0, 0),
              size=wx.Size(605, 359), style=wx.TE_MULTILINE, value='')

    def __init__(self, parent):
        self._init_ctrls(parent)
        self.FileName=None

    def OnMenuFileOpenMenu(self, event):
        dlg = wx.FileDialog(self, "Choose a file", ".", "", "*.*", wx.OPEN)
        try:
            if dlg.ShowModal() == wx.ID_OK:
                filename = dlg.GetPath()
                # Your code
                self.textEditor.LoadFile(filename) 
                self.FileName=filename
                self.SetTitle(('Notebook - %s') % filename)
        finally:
            dlg.Destroy()

    def OnMenuFileSaveMenu(self, event):
        if self.FileName == None:
            return self.OnFileSaveasMenu(event)
        else:
            self.textEditor.SaveFile(self.FileName)

    def OnMenuFileSaveasMenu(self, event):
        dlg = wx.FileDialog(self, "Save file as", ".", "", "*.*", wx.SAVE)
        try:
            if dlg.ShowModal() == wx.ID_OK:
                filename = dlg.GetPath()
                # Your code
                self.textEditor.SaveFile(filename) 
                self.FileName=filename
                self.SetTitle(('Notebook - %s') % filename)
        finally:
            dlg.Destroy()

    def OnMenuFileExitMenu(self, event):
        self.Close()

    def OnMenuFileCloseMenu(self, event):
        self.FileName = None
        self.txtEditor.Clear()
        self.SetTitle('Notebook')

    def OnMenuHelpAboutMenu(self, event):
        dlg = Dialog2.Dialog2(self)
        try:
            dlg.ShowModal()
        finally:
            dlg.Destroy()  


