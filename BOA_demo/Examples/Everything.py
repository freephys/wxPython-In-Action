#Boa:Frame:Frame1

""" Frame containing all controls available on the Palette. """

import wxversion
wxversion.select('2.5')

import wx
from wx.lib.anchors import LayoutAnchors
import wx.grid
import wx.lib.buttons
import wx.html
import wx.gizmos

import Everything_img

def create(parent):
    return Frame1(parent)

[wxID_FRAME1, wxID_FRAME1BITMAPBUTTON1, wxID_FRAME1BUTTON1, 
 wxID_FRAME1CHECKBOX1, wxID_FRAME1CHECKLISTBOX1, wxID_FRAME1CHOICE1, 
 wxID_FRAME1COMBOBOX1, wxID_FRAME1CONTEXTHELPBUTTON1, 
 wxID_FRAME1DYNAMICSASHWINDOW1, wxID_FRAME1EDITABLELISTBOX1, 
 wxID_FRAME1GAUGE1, wxID_FRAME1GENBITMAPBUTTON1, 
 wxID_FRAME1GENBITMAPTEXTTOGGLEBUTTON1, wxID_FRAME1GENBITMAPTOGGLEBUTTON1, 
 wxID_FRAME1GENBUTTON1, wxID_FRAME1GENTOGGLEBUTTON1, wxID_FRAME1GRID1, 
 wxID_FRAME1HTMLWINDOW1, wxID_FRAME1LEDNUMBERCTRL1, wxID_FRAME1LISTBOX1, 
 wxID_FRAME1LISTCTRL1, wxID_FRAME1NOTEBOOK1, wxID_FRAME1PANEL1, 
 wxID_FRAME1PANEL2, wxID_FRAME1PANEL3, wxID_FRAME1PANEL4, wxID_FRAME1PANEL5, 
 wxID_FRAME1PANEL6, wxID_FRAME1RADIOBOX1, wxID_FRAME1RADIOBUTTON1, 
 wxID_FRAME1SASHLAYOUTWINDOW1, wxID_FRAME1SASHWINDOW1, wxID_FRAME1SCROLLBAR1, 
 wxID_FRAME1SCROLLEDWINDOW1, wxID_FRAME1SLIDER1, wxID_FRAME1SPINBUTTON1, 
 wxID_FRAME1SPLITTERWINDOW1, wxID_FRAME1STATICBITMAP1, wxID_FRAME1STATICBOX1, 
 wxID_FRAME1STATICLINE1, wxID_FRAME1STATICTEXT1, wxID_FRAME1STATUSBAR1, 
 wxID_FRAME1TEXTCTRL1, wxID_FRAME1TOGGLEBUTTON1, wxID_FRAME1TOOLBAR1, 
 wxID_FRAME1TREECTRL1, wxID_FRAME1WINDOW1, wxID_FRAME1WINDOW10, 
 wxID_FRAME1WINDOW2, wxID_FRAME1WINDOW3, wxID_FRAME1WINDOW4, 
 wxID_FRAME1WINDOW5, wxID_FRAME1WINDOW6, wxID_FRAME1WINDOW7, 
 wxID_FRAME1WINDOW8, wxID_FRAME1WINDOW9, 
] = [wx.NewId() for _init_ctrls in range(56)]

[wxID_FRAME1TOOLBAR1TOOLS0] = [wx.NewId() for _init_coll_toolBar1_Tools in range(1)]

[wxID_FRAME1MENU1ITEMS0] = [wx.NewId() for _init_coll_menu1_Items in range(1)]

[wxID_FRAME1TIMER1] = [wx.NewId() for _init_utils in range(1)]

class Frame1(wx.Frame):
    def _init_coll_menuBar1_Menus(self, parent):
        # generated method, don't edit

        parent.Append(menu=self.menu1, title='Menus0')

    def _init_coll_menu1_Items(self, parent):
        # generated method, don't edit

        parent.Append(help='', id=wxID_FRAME1MENU1ITEMS0, text='Items0')
        self.Bind(wx.EVT_MENU, self.OnMenu1items0Menu,
              id=wxID_FRAME1MENU1ITEMS0)

    def _init_coll_toolBar1_Tools(self, parent):
        # generated method, don't edit

        parent.AddTool(bitmap=Everything_img.getBoaBitmap(),
              id=wxID_FRAME1TOOLBAR1TOOLS0, isToggle=False, longHelpString='',
              pushedBitmap=wx.NullBitmap, shortHelpString='Tools0')
        self.Bind(wx.EVT_TOOL, self.OnToolbar1tools0Tool,
              id=wxID_FRAME1TOOLBAR1TOOLS0)

        parent.Realize()

    def _init_coll_notebook1_Pages(self, parent):
        # generated method, don't edit

        parent.AddPage(imageId=-1, page=self.panel1, select=False,
              text='Containers/Layout')
        parent.AddPage(imageId=-1, page=self.panel2, select=False,
              text='Basic Controls')
        parent.AddPage(imageId=-1, page=self.panel3, select=False,
              text='Buttons')
        parent.AddPage(imageId=-1, page=self.panel4, select=True,
              text='List Controls')
        parent.AddPage(imageId=-1, page=self.panel5, select=False,
              text='Anchors')
        parent.AddPage(imageId=-1, page=self.panel6, select=False, text='Misc')

    def _init_coll_statusBar1_Fields(self, parent):
        # generated method, don't edit
        parent.SetFieldsCount(2)

        parent.SetStatusText(number=0, text='Fields0')
        parent.SetStatusText(number=1, text='Fields1')

        parent.SetStatusWidths([-1, -1])

    def _init_utils(self):
        # generated method, don't edit
        self.menuBar1 = wx.MenuBar()

        self.menu1 = wx.Menu(title='')

        self.imageList1 = wx.ImageList(height=16, width=16)

        self.stockCursor1 = wx.StockCursor(id=wx.CURSOR_PENCIL)

        self.timer1 = wx.Timer(id=wxID_FRAME1TIMER1, owner=self)
        self.Bind(wx.EVT_TIMER, self.OnTimer1Timer, id=wxID_FRAME1TIMER1)

        self._init_coll_menuBar1_Menus(self.menuBar1)
        self._init_coll_menu1_Items(self.menu1)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAME1, name='', parent=prnt,
              pos=wx.Point(556, 295), size=wx.Size(516, 476),
              style=wx.DEFAULT_FRAME_STYLE, title='Everything')
        self._init_utils()
        self.SetClientSize(wx.Size(508, 449))
        self.SetMenuBar(self.menuBar1)
        self.Center(wx.BOTH)

        self.toolBar1 = wx.ToolBar(id=wxID_FRAME1TOOLBAR1, name='toolBar1',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(508, 27),
              style=wx.TB_HORIZONTAL | wx.NO_BORDER)
        self.SetToolBar(self.toolBar1)

        self.statusBar1 = wx.StatusBar(id=wxID_FRAME1STATUSBAR1,
              name='statusBar1', parent=self, style=0)
        self.statusBar1.SetPosition(wx.Point(0, 308))
        self.statusBar1.SetSize(wx.Size(422, 20))
        self._init_coll_statusBar1_Fields(self.statusBar1)
        self.SetStatusBar(self.statusBar1)

        self.notebook1 = wx.Notebook(id=wxID_FRAME1NOTEBOOK1, name='notebook1',
              parent=self, pos=wx.Point(0, 27), size=wx.Size(508, 383),
              style=0)

        self.panel1 = wx.Panel(id=wxID_FRAME1PANEL1, name='panel1',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(500, 357),
              style=wx.TAB_TRAVERSAL)

        self.splitterWindow1 = wx.SplitterWindow(id=wxID_FRAME1SPLITTERWINDOW1,
              name='splitterWindow1', parent=self.panel1, point=wx.Point(8, 8),
              size=wx.Size(200, 100), style=wx.SP_3D)

        self.scrolledWindow1 = wx.ScrolledWindow(id=wxID_FRAME1SCROLLEDWINDOW1,
              name='scrolledWindow1', parent=self.splitterWindow1,
              pos=wx.Point(2, 2), size=wx.Size(98, 96),
              style=wx.SUNKEN_BORDER | wx.TAB_TRAVERSAL)
        self.scrolledWindow1.SetToolTipString('wxScrolledWindow')

        self.sashWindow1 = wx.SashWindow(id=wxID_FRAME1SASHWINDOW1,
              name='sashWindow1', parent=self.splitterWindow1, pos=wx.Point(107,
              2), size=wx.Size(91, 96), style=wx.CLIP_CHILDREN | wx.SW_3D)
        self.splitterWindow1.SplitVertically(self.scrolledWindow1,
              self.sashWindow1, 100)

        self.sashLayoutWindow1 = wx.SashLayoutWindow(id=wxID_FRAME1SASHLAYOUTWINDOW1,
              name='sashLayoutWindow1', parent=self.panel1, pos=wx.Point(8,
              120), size=wx.Size(200, 80), style=wx.CLIP_CHILDREN | wx.SW_3D)

        self.window1 = wx.Window(id=wxID_FRAME1WINDOW1, name='window1',
              parent=self.panel1, pos=wx.Point(216, 120), size=wx.Size(96, 80),
              style=wx.SIMPLE_BORDER)
        self.window1.SetCursor(self.stockCursor1)

        self.dynamicSashWindow1 = wx.gizmos.DynamicSashWindow(id=wxID_FRAME1DYNAMICSASHWINDOW1,
              name='dynamicSashWindow1', parent=self.panel1, pos=wx.Point(216,
              8), size=wx.Size(100, 100), style=wx.CLIP_CHILDREN)

        self.panel2 = wx.Panel(id=wxID_FRAME1PANEL2, name='panel2',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(500, 357),
              style=wx.TAB_TRAVERSAL)

        self.staticText1 = wx.StaticText(id=wxID_FRAME1STATICTEXT1,
              label='staticText1', name='staticText1', parent=self.panel2,
              pos=wx.Point(16, 16), size=wx.Size(52, 13), style=0)

        self.textCtrl1 = wx.TextCtrl(id=wxID_FRAME1TEXTCTRL1, name='textCtrl1',
              parent=self.panel2, pos=wx.Point(16, 40), size=wx.Size(100, 21),
              style=0, value='textCtrl1')

        self.comboBox1 = wx.ComboBox(choices=[], id=wxID_FRAME1COMBOBOX1,
              name='comboBox1', parent=self.panel2, pos=wx.Point(16, 72),
              size=wx.Size(125, 21), style=0, validator=wx.DefaultValidator,
              value='comboBox1')

        self.choice1 = wx.Choice(choices=[], id=wxID_FRAME1CHOICE1,
              name='choice1', parent=self.panel2, pos=wx.Point(16, 104),
              size=wx.Size(125, 21), style=0, validator=wx.DefaultValidator)

        self.checkBox1 = wx.CheckBox(id=wxID_FRAME1CHECKBOX1, label='checkBox1',
              name='checkBox1', parent=self.panel2, pos=wx.Point(16, 136),
              size=wx.Size(73, 13), style=0)

        self.radioButton1 = wx.RadioButton(id=wxID_FRAME1RADIOBUTTON1,
              label='radioButton1', name='radioButton1', parent=self.panel2,
              pos=wx.Point(16, 160), size=wx.Size(80, 20), style=0)

        self.slider1 = wx.Slider(id=wxID_FRAME1SLIDER1, maxValue=100,
              minValue=0, name='slider1', parent=self.panel2,
              point=wx.Point(152, 16), size=wx.Size(136, 20),
              style=wx.SL_HORIZONTAL, validator=wx.DefaultValidator, value=0)
        self.slider1.Bind(wx.EVT_SCROLL, self.OnSlider1Slider)

        self.scrollBar1 = wx.ScrollBar(id=wxID_FRAME1SCROLLBAR1,
              name='scrollBar1', parent=self.panel2, pos=wx.Point(16, 192),
              size=wx.Size(120, 14), style=wx.SB_HORIZONTAL)
        self.scrollBar1.SetThumbPosition(0)

        self.staticBitmap1 = wx.StaticBitmap(bitmap=Everything_img.getBoaBitmap(),
              id=wxID_FRAME1STATICBITMAP1, name='staticBitmap1',
              parent=self.panel2, pos=wx.Point(160, 136), size=wx.Size(16, 16),
              style=0)

        self.staticLine1 = wx.StaticLine(id=wxID_FRAME1STATICLINE1,
              name='staticLine1', parent=self.panel2, pos=wx.Point(15, 216),
              size=wx.Size(121, 2), style=0)

        self.staticBox1 = wx.StaticBox(id=wxID_FRAME1STATICBOX1,
              label='staticBox1', name='staticBox1', parent=self.panel2,
              pos=wx.Point(152, 120), size=wx.Size(144, 40), style=0)

        self.htmlWindow1 = wx.html.HtmlWindow(id=wxID_FRAME1HTMLWINDOW1,
              name='htmlWindow1', parent=self.panel2, pos=wx.Point(152, 168),
              size=wx.Size(144, 80), style=wx.html.HW_SCROLLBAR_AUTO)

        self.lEDNumberCtrl1 = wx.gizmos.LEDNumberCtrl(id=wxID_FRAME1LEDNUMBERCTRL1,
              parent=self.panel2, pos=wx.Point(152, 40), size=wx.Size(136, 40),
              style=wx.gizmos.LED_ALIGN_CENTER)
        self.lEDNumberCtrl1.SetValue('123')

        self.panel3 = wx.Panel(id=wxID_FRAME1PANEL3, name='panel3',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(500, 357),
              style=wx.TAB_TRAVERSAL)

        self.button1 = wx.Button(id=wxID_FRAME1BUTTON1, label='button1',
              name='button1', parent=self.panel3, pos=wx.Point(16, 16),
              size=wx.Size(75, 23), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_FRAME1BUTTON1)
        self.button1.Bind(wx.EVT_LEFT_UP, self.OnButton1LeftUp)

        self.bitmapButton1 = wx.BitmapButton(bitmap=Everything_img.getBoaBitmap(),
              id=wxID_FRAME1BITMAPBUTTON1, name='bitmapButton1',
              parent=self.panel3, pos=wx.Point(16, 56), size=wx.Size(72, 24),
              style=wx.BU_AUTODRAW, validator=wx.DefaultValidator)
        self.bitmapButton1.Bind(wx.EVT_BUTTON, self.OnBitmapbutton1Button,
              id=wxID_FRAME1BITMAPBUTTON1)

        self.spinButton1 = wx.SpinButton(id=wxID_FRAME1SPINBUTTON1,
              name='spinButton1', parent=self.panel3, pos=wx.Point(136, 96),
              size=wx.Size(32, 16), style=wx.SP_HORIZONTAL)
        self.spinButton1.Bind(wx.EVT_COMMAND_SCROLL,
              self.OnSpinbutton1CommandScroll, id=wxID_FRAME1SPINBUTTON1)

        self.toggleButton1 = wx.ToggleButton(id=wxID_FRAME1TOGGLEBUTTON1,
              label='toggleButton1', name='toggleButton1', parent=self.panel3,
              pos=wx.Point(104, 16), size=wx.Size(81, 23), style=0)
        self.toggleButton1.Bind(wx.EVT_BUTTON, self.OnTogglebutton1Button,
              id=wxID_FRAME1TOGGLEBUTTON1)

        self.genButton1 = wx.lib.buttons.GenButton(ID=wxID_FRAME1GENBUTTON1,
              label='genButton1', name='genButton1', parent=self.panel3,
              pos=wx.Point(16, 160), size=wx.Size(88, 37), style=0)

        self.genBitmapButton1 = wx.lib.buttons.GenBitmapButton(ID=wxID_FRAME1GENBITMAPBUTTON1,
              bitmap=Everything_img.getBoaBitmap(), name='genBitmapButton1',
              parent=self.panel3, pos=wx.Point(16, 192), size=wx.Size(59, 58),
              style=0)

        self.genToggleButton1 = wx.lib.buttons.GenToggleButton(ID=wxID_FRAME1GENTOGGLEBUTTON1,
              label='genToggleButton1', name='genToggleButton1',
              parent=self.panel3, pos=wx.Point(104, 160), size=wx.Size(113, 37),
              style=0)

        self.genBitmapToggleButton1 = wx.lib.buttons.GenBitmapToggleButton(ID=wxID_FRAME1GENBITMAPTOGGLEBUTTON1,
              bitmap=Everything_img.getBoaBitmap(),
              name='genBitmapToggleButton1', parent=self.panel3,
              pos=wx.Point(72, 192), size=wx.Size(59, 58), style=0)

        self.genBitmapTextToggleButton1 = wx.lib.buttons.GenBitmapTextToggleButton(ID=wxID_FRAME1GENBITMAPTEXTTOGGLEBUTTON1,
              bitmap=Everything_img.getBoaBitmap(),
              label='genBitmapTextToggleButton1',
              name='genBitmapTextToggleButton1', parent=self.panel3,
              pos=wx.Point(128, 192), size=wx.Size(88, 58), style=0)

        self.contextHelpButton1 = wx.ContextHelpButton(parent=self.panel3,
              pos=wx.Point(136, 64), size=wx.Size(20, 19),
              style=wx.BU_AUTODRAW)

        self.panel4 = wx.Panel(id=wxID_FRAME1PANEL4, name='panel4',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(500, 357),
              style=wx.TAB_TRAVERSAL)

        self.radioBox1 = wx.RadioBox(choices=['asd'], id=wxID_FRAME1RADIOBOX1,
              label='radioBox1', majorDimension=1, name='radioBox1',
              parent=self.panel4, point=wx.Point(16, 16), size=wx.DefaultSize,
              style=wx.RA_SPECIFY_COLS, validator=wx.DefaultValidator)

        self.listBox1 = wx.ListBox(choices=[], id=wxID_FRAME1LISTBOX1,
              name='listBox1', parent=self.panel4, pos=wx.Point(16, 64),
              size=wx.Size(115, 63), style=0, validator=wx.DefaultValidator)

        self.checkListBox1 = wx.CheckListBox(choices=[],
              id=wxID_FRAME1CHECKLISTBOX1, name='checkListBox1',
              parent=self.panel4, pos=wx.Point(16, 136), size=wx.Size(115, 63),
              style=0, validator=wx.DefaultValidator)

        self.grid1 = wx.grid.Grid(id=wxID_FRAME1GRID1, name='grid1',
              parent=self.panel4, pos=wx.Point(144, 16), size=wx.Size(128, 112),
              style=0)

        self.listCtrl1 = wx.ListCtrl(id=wxID_FRAME1LISTCTRL1, name='listCtrl1',
              parent=self.panel4, pos=wx.Point(280, 16), size=wx.Size(100, 30),
              style=wx.LC_ICON, validator=wx.DefaultValidator)

        self.treeCtrl1 = wx.TreeCtrl(id=wxID_FRAME1TREECTRL1, name='treeCtrl1',
              parent=self.panel4, pos=wx.Point(280, 56), size=wx.Size(100, 80),
              style=wx.TR_HAS_BUTTONS, validator=wx.DefaultValidator)

        self.editableListBox1 = wx.gizmos.EditableListBox(id=wxID_FRAME1EDITABLELISTBOX1,
              label='editableListBox1', name='editableListBox1',
              parent=self.panel4, pos=wx.Point(152, 152), size=wx.Size(200,
              100))

        self.panel5 = wx.Panel(id=wxID_FRAME1PANEL5, name='panel5',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(500, 357),
              style=wx.TAB_TRAVERSAL)
        self.panel5.SetAutoLayout(True)

        self.window2 = wx.Window(id=wxID_FRAME1WINDOW2, name='window2',
              parent=self.panel5, pos=wx.Point(446, 16), size=wx.Size(40, 40),
              style=0)
        self.window2.SetBackgroundColour(wx.Colour(128, 255, 0))
        self.window2.SetConstraints(LayoutAnchors(self.window2, False, True,
              True, False))

        self.window3 = wx.Window(id=wxID_FRAME1WINDOW3, name='window3',
              parent=self.panel5, pos=wx.Point(16, 299), size=wx.Size(40, 40),
              style=0)
        self.window3.SetBackgroundColour(wx.Colour(128, 255, 0))
        self.window3.SetConstraints(LayoutAnchors(self.window3, True, False,
              False, True))

        self.window4 = wx.Window(id=wxID_FRAME1WINDOW4, name='window4',
              parent=self.panel5, pos=wx.Point(446, 299), size=wx.Size(40, 40),
              style=0)
        self.window4.SetBackgroundColour(wx.Colour(128, 255, 0))
        self.window4.SetConstraints(LayoutAnchors(self.window4, False, False,
              True, True))

        self.window5 = wx.Window(id=wxID_FRAME1WINDOW5, name='window5',
              parent=self.panel5, pos=wx.Point(16, 16), size=wx.Size(40, 40),
              style=0)
        self.window5.SetBackgroundColour(wx.Colour(128, 255, 0))
        self.window5.SetConstraints(LayoutAnchors(self.window5, True, True,
              False, False))

        self.window6 = wx.Window(id=wxID_FRAME1WINDOW6, name='window6',
              parent=self.panel5, pos=wx.Point(192, 16), size=wx.Size(126, 40),
              style=0)
        self.window6.SetBackgroundColour(wx.Colour(128, 255, 0))
        self.window6.SetConstraints(LayoutAnchors(self.window6, True, True,
              True, False))

        self.window7 = wx.Window(id=wxID_FRAME1WINDOW7, name='window7',
              parent=self.panel5, pos=wx.Point(446, 120), size=wx.Size(40, 115),
              style=0)
        self.window7.SetBackgroundColour(wx.Colour(128, 255, 0))
        self.window7.SetConstraints(LayoutAnchors(self.window7, False, True,
              True, True))

        self.window8 = wx.Window(id=wxID_FRAME1WINDOW8, name='window8',
              parent=self.panel5, pos=wx.Point(192, 299), size=wx.Size(126, 40),
              style=0)
        self.window8.SetBackgroundColour(wx.Colour(128, 255, 0))
        self.window8.SetConstraints(LayoutAnchors(self.window8, True, False,
              True, True))

        self.window9 = wx.Window(id=wxID_FRAME1WINDOW9, name='window9',
              parent=self.panel5, pos=wx.Point(16, 120), size=wx.Size(40, 115),
              style=0)
        self.window9.SetBackgroundColour(wx.Colour(128, 255, 0))
        self.window9.SetConstraints(LayoutAnchors(self.window9, True, True,
              False, True))

        self.window10 = wx.Window(id=wxID_FRAME1WINDOW10, name='window10',
              parent=self.panel5, pos=wx.Point(225, 147), size=wx.Size(40, 40),
              style=0)
        self.window10.SetBackgroundColour(wx.Colour(128, 255, 0))
        self.window10.SetConstraints(LayoutAnchors(self.window10, False, False,
              False, False))

        self.panel6 = wx.Panel(id=wxID_FRAME1PANEL6, name='panel6',
              parent=self.notebook1, pos=wx.Point(0, 0), size=wx.Size(500, 357),
              style=wx.TAB_TRAVERSAL)

        self.gauge1 = wx.Gauge(id=wxID_FRAME1GAUGE1, name='gauge1',
              parent=self.panel2, pos=wx.Point(152, 88), range=100,
              size=wx.Size(136, 16), style=wx.GA_SMOOTH | wx.GA_HORIZONTAL,
              validator=wx.DefaultValidator)
        self.gauge1.SetValue(50)

        self._init_coll_toolBar1_Tools(self.toolBar1)
        self._init_coll_notebook1_Pages(self.notebook1)

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnMenu1items0Menu(self, event):
        print 'Menu0'

    def OnToolbar1tools0Tool(self, event):
        raise 'Tool0'

    def OnButton1Button(self, event):
        self.timer1.Start(1000, False)

    def OnBitmapbutton1Button(self, event):
        event.Skip()

    def OnSpinbutton1CommandScroll(self, event):
        event.Skip()

    def OnTogglebutton1Button(self, event):
        event.Skip()

    def OnButton1Help(self, event):
        event.Skip()

    def OnButton1LeftUp(self, event):
        event.Skip()

    def OnTimer1Timer(self, event):
        import time
        self.staticText1.SetLabel(time.asctime())

    def OnSlider1Slider(self, event):
        self.lEDNumberCtrl1.SetValue(`event.GetPosition()`)
        self.gauge1.SetValue(event.GetPosition())

if __name__ == '__main__':
    app = wx.PySimpleApp()
    wx.InitAllImageHandlers()
    frame = create(None)
    frame.Show(True)
    app.MainLoop()

