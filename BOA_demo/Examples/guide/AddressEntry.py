#Boa:Frame:AddressEntry

import wx

def create(parent):
    return AddressEntry(parent)

[wxID_ADDRESSENTRY, wxID_ADDRESSENTRYADD, wxID_ADDRESSENTRYADDRESS, 
 wxID_ADDRESSENTRYCITY, wxID_ADDRESSENTRYCLOSE, wxID_ADDRESSENTRYCOUNTRY, 
 wxID_ADDRESSENTRYDELETE, wxID_ADDRESSENTRYFIRSTNAME, 
 wxID_ADDRESSENTRYLASTNAME, wxID_ADDRESSENTRYLISTCTRL1, 
 wxID_ADDRESSENTRYPANEL1, wxID_ADDRESSENTRYPOSTAL, wxID_ADDRESSENTRYSAVE, 
 wxID_ADDRESSENTRYSTADDRESS, wxID_ADDRESSENTRYSTCITY, 
 wxID_ADDRESSENTRYSTCOUNTRY, wxID_ADDRESSENTRYSTFIRSTNAME, 
 wxID_ADDRESSENTRYSTLASTNAME, wxID_ADDRESSENTRYSTPOSTAL, 
] = [wx.NewId() for _init_ctrls in range(19)]

class AddressEntry(wx.Frame):
    def _init_coll_fgsFields_Items(self, parent):
        # generated method, don't edit

        parent.AddWindow(self.stFirstName, 0, border=2,
              flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL)
        parent.AddWindow(self.firstName, 0, border=2, flag=wx.ALL | wx.EXPAND)
        parent.AddWindow(self.stLastName, 0, border=2,
              flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL)
        parent.AddWindow(self.lastName, 0, border=2, flag=wx.ALL | wx.EXPAND)
        parent.AddWindow(self.stAddress, 0, border=2,
              flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL)
        parent.AddWindow(self.address, 0, border=2, flag=wx.ALL | wx.EXPAND)
        parent.AddWindow(self.stPostal, 0, border=2,
              flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL)
        parent.AddWindow(self.postal, 0, border=2, flag=wx.ALL | wx.EXPAND)
        parent.AddWindow(self.stCity, 0, border=2,
              flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL)
        parent.AddWindow(self.City, 0, border=2, flag=wx.ALL | wx.EXPAND)
        parent.AddWindow(self.stCountry, 0, border=2,
              flag=wx.ALL | wx.ALIGN_CENTER_VERTICAL)
        parent.AddWindow(self.Country, 0, border=2, flag=wx.ALL | wx.EXPAND)

    def _init_coll_fgsButtons_Items(self, parent):
        # generated method, don't edit

        parent.AddWindow(self.add, 0, border=2, flag=wx.ALL)
        parent.AddWindow(self.delete, 0, border=2, flag=wx.ALL)
        parent.AddWindow(self.save, 0, border=2, flag=wx.ALL)
        parent.AddWindow(self.close, 0, border=2, flag=wx.ALL)

    def _init_coll_bsMain_Items(self, parent):
        # generated method, don't edit

        parent.AddWindow(self.listCtrl1, 1, border=2, flag=wx.ALL | wx.EXPAND)
        parent.AddSizer(self.fgsFields, 0, border=0, flag=wx.EXPAND)
        parent.AddSizer(self.fgsButtons, 0, border=0, flag=0)

    def _init_coll_fgsFields_Growables(self, parent):
        # generated method, don't edit

        parent.AddGrowableCol(1)

    def _init_coll_listCtrl1_Columns(self, parent):
        # generated method, don't edit

        parent.InsertColumn(col=0, format=wx.LIST_FORMAT_LEFT,
              heading='First name', width=-1)
        parent.InsertColumn(col=1, format=wx.LIST_FORMAT_LEFT,
              heading='Last name', width=-1)
        parent.InsertColumn(col=2, format=wx.LIST_FORMAT_LEFT, heading='City',
              width=-1)
        parent.InsertColumn(col=3, format=wx.LIST_FORMAT_LEFT,
              heading='Country', width=-1)

    def _init_sizers(self):
        # generated method, don't edit
        self.bsMain = wx.BoxSizer(orient=wx.VERTICAL)

        self.fgsFields = wx.FlexGridSizer(cols=2, hgap=0, rows=0, vgap=0)

        self.fgsButtons = wx.FlexGridSizer(cols=0, hgap=0, rows=1, vgap=0)

        self._init_coll_bsMain_Items(self.bsMain)
        self._init_coll_fgsFields_Items(self.fgsFields)
        self._init_coll_fgsFields_Growables(self.fgsFields)
        self._init_coll_fgsButtons_Items(self.fgsButtons)

        self.panel1.SetSizer(self.bsMain)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_ADDRESSENTRY, name='AddressEntry',
              parent=prnt, pos=wx.Point(816, 236), size=wx.Size(445, 355),
              style=wx.DEFAULT_FRAME_STYLE, title='Address entry form')
        self.SetClientSize(wx.Size(429, 319))

        self.panel1 = wx.Panel(id=wxID_ADDRESSENTRYPANEL1, name='panel1',
              parent=self, pos=wx.Point(0, 0), size=wx.Size(429, 319),
              style=wx.TAB_TRAVERSAL)

        self.listCtrl1 = wx.ListCtrl(id=wxID_ADDRESSENTRYLISTCTRL1,
              name='listCtrl1', parent=self.panel1, pos=wx.Point(2, 2),
              size=wx.Size(425, 87), style=wx.LC_REPORT)
        self._init_coll_listCtrl1_Columns(self.listCtrl1)

        self.stFirstName = wx.StaticText(id=wxID_ADDRESSENTRYSTFIRSTNAME,
              label='First name', name='stFirstName', parent=self.panel1,
              pos=wx.Point(2, 97), size=wx.Size(51, 13), style=0)

        self.firstName = wx.TextCtrl(id=wxID_ADDRESSENTRYFIRSTNAME,
              name='firstName', parent=self.panel1, pos=wx.Point(61, 93),
              size=wx.Size(366, 21), style=0, value='')

        self.stLastName = wx.StaticText(id=wxID_ADDRESSENTRYSTLASTNAME,
              label='Last name', name='stLastName', parent=self.panel1,
              pos=wx.Point(2, 122), size=wx.Size(55, 13), style=0)

        self.lastName = wx.TextCtrl(id=wxID_ADDRESSENTRYLASTNAME,
              name='lastName', parent=self.panel1, pos=wx.Point(61, 118),
              size=wx.Size(366, 21), style=0, value='')

        self.stAddress = wx.StaticText(id=wxID_ADDRESSENTRYSTADDRESS,
              label='Address', name='stAddress', parent=self.panel1,
              pos=wx.Point(2, 172), size=wx.Size(55, 13), style=0)

        self.address = wx.TextCtrl(id=wxID_ADDRESSENTRYADDRESS, name='address',
              parent=self.panel1, pos=wx.Point(61, 143), size=wx.Size(366, 72),
              style=wx.TE_MULTILINE, value='')

        self.stPostal = wx.StaticText(id=wxID_ADDRESSENTRYSTPOSTAL,
              label='Postal', name='stPostal', parent=self.panel1,
              pos=wx.Point(2, 223), size=wx.Size(55, 13), style=0)

        self.postal = wx.TextCtrl(id=wxID_ADDRESSENTRYPOSTAL, name='postal',
              parent=self.panel1, pos=wx.Point(61, 219), size=wx.Size(366, 21),
              style=0, value='')

        self.stCity = wx.StaticText(id=wxID_ADDRESSENTRYSTCITY, label='City',
              name='stCity', parent=self.panel1, pos=wx.Point(2, 248),
              size=wx.Size(55, 13), style=0)

        self.City = wx.TextCtrl(id=wxID_ADDRESSENTRYCITY, name='city',
              parent=self.panel1, pos=wx.Point(61, 244), size=wx.Size(366, 21),
              style=0, value='')

        self.stCountry = wx.StaticText(id=wxID_ADDRESSENTRYSTCOUNTRY,
              label='Country', name='stCountry', parent=self.panel1,
              pos=wx.Point(2, 273), size=wx.Size(55, 13), style=0)

        self.Country = wx.TextCtrl(id=wxID_ADDRESSENTRYCOUNTRY, name='country',
              parent=self.panel1, pos=wx.Point(61, 269), size=wx.Size(366, 21),
              style=0, value='')

        self.add = wx.Button(id=wx.ID_ADD, label='', name='add',
              parent=self.panel1, pos=wx.Point(2, 294), size=wx.Size(75, 23),
              style=0)
        self.add.Bind(wx.EVT_BUTTON, self.OnAddButton, id=wxID_ADDRESSENTRYADD)

        self.delete = wx.Button(id=wx.ID_DELETE, label='', name='delete',
              parent=self.panel1, pos=wx.Point(81, 294), size=wx.Size(75, 23),
              style=0)

        self.save = wx.Button(id=wx.ID_SAVE, label='', name='save',
              parent=self.panel1, pos=wx.Point(160, 294), size=wx.Size(75, 23),
              style=0)

        self.close = wx.Button(id=wx.ID_CLOSE, label='', name='close',
              parent=self.panel1, pos=wx.Point(239, 294), size=wx.Size(75, 23),
              style=0)

        self._init_sizers()

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnAddButton(self, event):
        event.Skip()


if __name__ == '__main__':
    app = wx.PySimpleApp()
    frame = create(None)
    frame.Show()

    app.MainLoop()
