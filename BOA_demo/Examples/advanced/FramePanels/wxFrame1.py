#Boa:Frame:wxFrame1

import wx

from wxPanel1 import wxPanel1
from wxPanel2 import wxPanel2
from wxPanel3 import wxPanel3

def create(parent):
    return wxFrame1(parent)

[wxID_WXFRAME1, wxID_WXFRAME1NOTEBOOK1, wxID_WXFRAME1PANEL1, 
 wxID_WXFRAME1PANEL2, wxID_WXFRAME1PANEL3, wxID_WXFRAME1PANEL4, 
 wxID_WXFRAME1PANEL5, wxID_WXFRAME1PANEL6, wxID_WXFRAME1PANEL7, 
] = [wx.NewId() for _init_ctrls in range(9)]

class wxFrame1(wx.Frame):
    _custom_classes = {'wx.Panel': ['wxPanel1', 'wxPanel2', 'wxPanel3']}
    def _init_coll_notebook1_Pages(self, parent):
        # generated method, don't edit

        parent.AddPage(imageId=-1, page=self.panel1, select=False,
              text='Pages0')
        parent.AddPage(imageId=-1, page=self.panel2, select=False,
              text='Pages1')
        parent.AddPage(imageId=-1, page=self.panel3, select=True, text='Pages2')

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_WXFRAME1, name='', parent=prnt,
              pos=wx.Point(306, 164), size=wx.Size(491, 364),
              style=wx.DEFAULT_FRAME_STYLE, title='wxFrame1')
        self.SetClientSize(wx.Size(483, 337))

        self.notebook1 = wx.Notebook(id=wxID_WXFRAME1NOTEBOOK1, name='notebook1',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(483, 337), style=0)

        self.panel1 = wxPanel1(id=wxID_WXFRAME1PANEL1, name='panel1',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(475, 311),
              style=wx.TAB_TRAVERSAL)

        self.panel2 = wxPanel2(id=wxID_WXFRAME1PANEL2, name='panel2',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(475, 311),
              style=wx.TAB_TRAVERSAL)

        self.panel3 = wx.Panel(id=wxID_WXFRAME1PANEL3, name='panel3',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(475, 311),
              style=wx.TAB_TRAVERSAL)

        self.panel4 = wxPanel3(id=wxID_WXFRAME1PANEL4, name='panel4',
              parent=self.panel3, pos=wx.Point(16, 16), size=wx.Size(200, 100),
              style=wx.RAISED_BORDER|wx.TAB_TRAVERSAL)

        self.panel5 = wxPanel3(id=wxID_WXFRAME1PANEL5, name='panel5',
              parent=self.panel3, pos=wx.Point(16, 136), size=wx.Size(200, 100),
              style=wx.STATIC_BORDER|wx.TAB_TRAVERSAL)

        self.panel6 = wxPanel3(id=wxID_WXFRAME1PANEL6, name='panel6',
              parent=self.panel3, pos=wx.Point(232, 16), size=wx.Size(200, 100),
              style=wx.SUNKEN_BORDER|wx.TAB_TRAVERSAL)

        self.panel7 = wxPanel3(id=wxID_WXFRAME1PANEL7, name='panel7',
              parent=self.panel3, pos=wx.Point(232, 136), size=wx.Size(200,
              100), style=wx.SIMPLE_BORDER|wx.TAB_TRAVERSAL)

        self._init_coll_notebook1_Pages(self.notebook1)

    def __init__(self, parent):
        self._init_ctrls(parent)
