#Boa:Frame:Frame1

import wx

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BUTTON1, wxID_FRAME1BUTTON10, wxID_FRAME1BUTTON11, 
 wxID_FRAME1BUTTON12, wxID_FRAME1BUTTON13, wxID_FRAME1BUTTON14, 
 wxID_FRAME1BUTTON15, wxID_FRAME1BUTTON16, wxID_FRAME1BUTTON17, 
 wxID_FRAME1BUTTON18, wxID_FRAME1BUTTON19, wxID_FRAME1BUTTON2, 
 wxID_FRAME1BUTTON20, wxID_FRAME1BUTTON21, wxID_FRAME1BUTTON3, 
 wxID_FRAME1BUTTON4, wxID_FRAME1BUTTON5, wxID_FRAME1BUTTON6, 
 wxID_FRAME1BUTTON7, wxID_FRAME1BUTTON8, wxID_FRAME1BUTTON9, 
 wxID_FRAME1NOTEBOOK1, wxID_FRAME1PANEL1, wxID_FRAME1PANEL2, 
 wxID_FRAME1PANEL3, wxID_FRAME1PANEL4, wxID_FRAME1STATICBOX1, 
] = [wx.NewId() for _init_ctrls in range(28)]

class Frame1(wx.Frame):
    def _init_coll_staticBoxSizer1_Items(self, parent):
        # generated method, don't edit

        parent.AddSpacer(wx.Size(8,8), border=0, flag=wx.ALIGN_CENTER)
        parent.AddWindow(self.button16, 0, border=0, flag=wx.ALIGN_CENTER)
        parent.AddWindow(self.button17, 1, border=0, flag=wx.ALIGN_CENTER)
        parent.AddWindow(self.button18, 0, border=0, flag=wx.ALIGN_CENTER)
        parent.AddSpacer(wx.Size(8,8), border=0, flag=wx.ALIGN_CENTER)

    def _init_coll_flexGridSizer1_Items(self, parent):
        # generated method, don't edit

        parent.AddWindow(self.button10, 0, border=10, flag=wx.GROW | wx.ALL)
        parent.AddWindow(self.button11, 0, border=10, flag=wx.ALL)
        parent.AddWindow(self.button12, 0, border=10, flag=wx.ALL)
        parent.AddWindow(self.button13, 0, border=10,
              flag=wx.ALIGN_CENTER | wx.ALL)
        parent.AddWindow(self.button14, 0, border=10, flag=wx.ALL)
        parent.AddWindow(self.button15, 0, border=10, flag=wx.ALL)

    def _init_coll_flexGridSizer1_Growables(self, parent):
        # generated method, don't edit

        parent.AddGrowableRow(0)
        parent.AddGrowableCol(0)

    def _init_coll_gridSizer1_Items(self, parent):
        # generated method, don't edit

        parent.AddWindow(self.button4, 0, border=0, flag=0)
        parent.AddWindow(self.button5, 0, border=0, flag=0)
        parent.AddWindow(self.button6, 0, border=0, flag=0)
        parent.AddWindow(self.button7, 0, border=0, flag=0)
        parent.AddWindow(self.button8, 0, border=0, flag=0)
        parent.AddWindow(self.button9, 0, border=0, flag=0)

    def _init_coll_boxSizer1_Items(self, parent):
        # generated method, don't edit

        parent.AddWindow(self.button1, 0, border=0, flag=wx.ALIGN_LEFT)
        parent.AddSizer(self.boxSizer2, 0, border=0, flag=wx.ALIGN_CENTER)
        parent.AddWindow(self.button3, 0, border=0, flag=wx.ALIGN_RIGHT)
        parent.AddWindow(self.button2, 1, border=0, flag=wx.ALIGN_CENTER)

    def _init_coll_boxSizer2_Items(self, parent):
        # generated method, don't edit

        parent.AddWindow(self.button19, 0, border=8,
              flag=wx.ALL | wx.ALIGN_CENTER)
        parent.AddSpacer(wx.Size(16,16), border=0, flag=0)
        parent.AddWindow(self.button20, 0, border=0, flag=wx.ALIGN_CENTER)
        parent.AddSpacer(wx.Size(16,16), border=0, flag=0)
        parent.AddWindow(self.button21, 0, border=8,
              flag=wx.ALL | wx.ALIGN_CENTER)

    def _init_coll_notebook1_Pages(self, parent):
        # generated method, don't edit

        parent.AddPage(imageId=-1, page=self.panel1, select=True,
              text='Box Sizer')
        parent.AddPage(imageId=-1, page=self.panel2, select=False,
              text='Grid Sizer')
        parent.AddPage(imageId=-1, page=self.panel3, select=False,
              text='Flex Grid Sizer')
        parent.AddPage(imageId=-1, page=self.panel4, select=False,
              text='StaticBox Sizer')

    def _init_sizers(self):
        # generated method, don't edit
        self.notebookSizer1 = wx.NotebookSizer(nb=self.notebook1)

        self.boxSizer1 = wx.BoxSizer(orient=wx.VERTICAL)

        self.gridSizer1 = wx.GridSizer(cols=2, hgap=0, rows=3, vgap=0)

        self.flexGridSizer1 = wx.FlexGridSizer(cols=3, hgap=0, rows=3, vgap=0)

        self.staticBoxSizer1 = wx.StaticBoxSizer(box=self.staticBox1,
              orient=wx.VERTICAL)

        self.boxSizer2 = wx.BoxSizer(orient=wx.HORIZONTAL)

        self._init_coll_boxSizer1_Items(self.boxSizer1)
        self._init_coll_gridSizer1_Items(self.gridSizer1)
        self._init_coll_flexGridSizer1_Growables(self.flexGridSizer1)
        self._init_coll_flexGridSizer1_Items(self.flexGridSizer1)
        self._init_coll_staticBoxSizer1_Items(self.staticBoxSizer1)
        self._init_coll_boxSizer2_Items(self.boxSizer2)

        self.panel1.SetSizer(self.boxSizer1)
        self.panel2.SetSizer(self.gridSizer1)
        self.panel3.SetSizer(self.flexGridSizer1)
        self.panel4.SetSizer(self.staticBoxSizer1)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='Frame1', parent=prnt,
              pos=wx.Point(585, 379), size=wx.Size(458, 307),
              style=wx.DEFAULT_FRAME_STYLE, title='Sizer demo')
        self.SetClientSize(wx.Size(450, 280))
        self.Center(wx.BOTH)

        self.notebook1 = wx.Notebook(id=wxID_FRAME1NOTEBOOK1, name='notebook1',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(450, 280), style=0)

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(442, 254),
              style=wx.TAB_TRAVERSAL)

        self.button1 = wx.Button(id=wxID_FRAME1BUTTON1, label='button1',
              name='button1', parent=self.panel1, pos=wx.Point(0, 0),
              size=wx.Size(75, 23), style=0)

        self.button2 = wx.Button(id=wxID_FRAME1BUTTON2, label='button2',
              name='button2', parent=self.panel1, pos=wx.Point(183, 103),
              size=wx.Size(75, 151), style=0)

        self.button3 = wx.Button(id=wxID_FRAME1BUTTON3, label='button3',
              name='button3', parent=self.panel1, pos=wx.Point(367, 80),
              size=wx.Size(75, 23), style=0)

        self.panel2 = wx.Panel(id=wxID_FRAME1PANEL2, name='panel2',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(442, 254),
              style=wx.TAB_TRAVERSAL)

        self.button4 = wx.Button(id=wxID_FRAME1BUTTON4, label='button4',
              name='button4', parent=self.panel2, pos=wx.Point(0, 0),
              size=wx.Size(75, 23), style=0)

        self.button5 = wx.Button(id=wxID_FRAME1BUTTON5, label='button5',
              name='button5', parent=self.panel2, pos=wx.Point(221, 0),
              size=wx.Size(75, 23), style=0)

        self.button6 = wx.Button(id=wxID_FRAME1BUTTON6, label='button6',
              name='button6', parent=self.panel2, pos=wx.Point(0, 84),
              size=wx.Size(75, 23), style=0)

        self.button7 = wx.Button(id=wxID_FRAME1BUTTON7, label='button7',
              name='button7', parent=self.panel2, pos=wx.Point(221, 84),
              size=wx.Size(75, 23), style=0)

        self.button8 = wx.Button(id=wxID_FRAME1BUTTON8, label='button8',
              name='button8', parent=self.panel2, pos=wx.Point(0, 168),
              size=wx.Size(75, 23), style=0)

        self.button9 = wx.Button(id=wxID_FRAME1BUTTON9, label='button9',
              name='button9', parent=self.panel2, pos=wx.Point(221, 168),
              size=wx.Size(75, 23), style=0)

        self.panel3 = wx.Panel(id=wxID_FRAME1PANEL3, name='panel3',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(442, 254),
              style=wx.TAB_TRAVERSAL)

        self.panel4 = wx.Panel(id=wxID_FRAME1PANEL4, name='panel4',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(442, 254),
              style=wx.TAB_TRAVERSAL)

        self.staticBox1 = wx.StaticBox(id=wxID_FRAME1STATICBOX1,
              label='staticBox1', name='staticBox1', parent=self.panel4,
              pos=wx.Point(0, 0), size=wx.Size(442, 254), style=0)

        self.button10 = wx.Button(id=wxID_FRAME1BUTTON10, label='button10',
              name='button10', parent=self.panel3, pos=wx.Point(10, 10),
              size=wx.Size(232, 191), style=0)

        self.button11 = wx.Button(id=wxID_FRAME1BUTTON11, label='button11',
              name='button11', parent=self.panel3, pos=wx.Point(262, 10),
              size=wx.Size(75, 23), style=0)

        self.button12 = wx.Button(id=wxID_FRAME1BUTTON12, label='button12',
              name='button12', parent=self.panel3, pos=wx.Point(357, 10),
              size=wx.Size(75, 23), style=0)

        self.button13 = wx.Button(id=wxID_FRAME1BUTTON13, label='button13',
              name='button13', parent=self.panel3, pos=wx.Point(88, 221),
              size=wx.Size(75, 23), style=0)

        self.button14 = wx.Button(id=wxID_FRAME1BUTTON14, label='button14',
              name='button14', parent=self.panel3, pos=wx.Point(262, 221),
              size=wx.Size(75, 23), style=0)

        self.button15 = wx.Button(id=wxID_FRAME1BUTTON15, label='button15',
              name='button15', parent=self.panel3, pos=wx.Point(357, 221),
              size=wx.Size(75, 23), style=0)

        self.button16 = wx.Button(id=wxID_FRAME1BUTTON16, label='button16',
              name='button16', parent=self.panel4, pos=wx.Point(183, 25),
              size=wx.Size(75, 23), style=0)

        self.button17 = wx.Button(id=wxID_FRAME1BUTTON17, label='button17',
              name='button17', parent=self.panel4, pos=wx.Point(161, 48),
              size=wx.Size(120, 170), style=0)

        self.button18 = wx.Button(id=wxID_FRAME1BUTTON18, label='button18',
              name='button18', parent=self.panel4, pos=wx.Point(128, 218),
              size=wx.Size(185, 23), style=0)

        self.button19 = wx.Button(id=wxID_FRAME1BUTTON19, label='button19',
              name='button19', parent=self.panel1, pos=wx.Point(70, 40),
              size=wx.Size(75, 23), style=0)

        self.button20 = wx.Button(id=wxID_FRAME1BUTTON20, label='button20',
              name='button20', parent=self.panel1, pos=wx.Point(169, 23),
              size=wx.Size(104, 57), style=0)

        self.button21 = wx.Button(id=wxID_FRAME1BUTTON21, label='button21',
              name='button21', parent=self.panel1, pos=wx.Point(297, 40),
              size=wx.Size(75, 23), style=0)

        self._init_coll_notebook1_Pages(self.notebook1)

        self._init_sizers()

    def __init__(self, parent):
        self._init_ctrls(parent)


if __name__ == '__main__':
    app = wx.PySimpleApp()
    wx.InitAllImageHandlers()
    frame = create(None)
    frame.Show()

    app.MainLoop()
