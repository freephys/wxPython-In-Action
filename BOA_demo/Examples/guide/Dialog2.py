# -*- coding: iso-8859-1 -*-#
#-----------------------------------------------------------------------------
# Name:        Dialog2.py
# Purpose:     Lets do the About dialog with sizers
#
# Author:      Werner F. Bruhin
#
# Created:     2005/17/03
# RCS-ID:      $Id: Dialog2.py,v 1.4 2007/07/03 06:26:16 wbruhin Exp $
# Copyright:   (c) 2003 - 2005
# Licence:     Shareware, see license.txt for details
#-----------------------------------------------------------------------------
#Boa:Dialog:Dialog2

import wx

def create(parent):
    return Dialog2(parent)

[wxID_DIALOG2, wxID_DIALOG2BUTTON1, wxID_DIALOG2STATICBITMAP1, 
 wxID_DIALOG2STATICBITMAP2, wxID_DIALOG2STATICBITMAP3, 
 wxID_DIALOG2STATICTEXT1, wxID_DIALOG2STATICTEXT2, 
] = [wx.NewId() for _init_ctrls in range(7)]

class Dialog2(wx.Dialog):
    def _init_coll_fgsButton_Items(self, parent):
        # generated method, don't edit

        parent.AddWindow(self.button1, 1, border=2, flag=wx.ALL)

    def _init_coll_bsDialog_Items(self, parent):
        # generated method, don't edit

        parent.AddSizer(self.fsTextctrls, 0, border=2, flag=wx.ALL)
        parent.AddSizer(self.fgsImages, 2, border=2,
              flag=wx.ALIGN_CENTER_HORIZONTAL | wx.ALL)
        parent.AddSizer(self.fgsButton, 0, border=2,
              flag=wx.ALIGN_CENTER_HORIZONTAL | wx.ALL)

    def _init_coll_fgsImages_Items(self, parent):
        # generated method, don't edit

        parent.AddWindow(self.staticBitmap2, 1, border=2,
              flag=wx.ALIGN_CENTER | wx.ALL)
        parent.AddWindow(self.staticBitmap1, 1, border=2, flag=wx.ALL)
        parent.AddWindow(self.staticBitmap3, 1, border=2,
              flag=wx.ALIGN_CENTER | wx.ALL)

    def _init_coll_fsTextctrls_Items(self, parent):
        # generated method, don't edit

        parent.AddWindow(self.staticText1, 1, border=2,
              flag=wx.ALIGN_CENTER_HORIZONTAL | wx.ALL)
        parent.AddWindow(self.staticText2, 1, border=2,
              flag=wx.ALIGN_CENTER_HORIZONTAL | wx.ALL)

    def _init_sizers(self):
        # generated method, don't edit
        self.bsDialog = wx.BoxSizer(orient=wx.VERTICAL)

        self.fsTextctrls = wx.FlexGridSizer(cols=1, hgap=0, rows=0, vgap=0)

        self.fgsImages = wx.FlexGridSizer(cols=3, hgap=0, rows=0, vgap=0)

        self.fgsButton = wx.FlexGridSizer(cols=1, hgap=0, rows=0, vgap=0)

        self._init_coll_bsDialog_Items(self.bsDialog)
        self._init_coll_fsTextctrls_Items(self.fsTextctrls)
        self._init_coll_fgsImages_Items(self.fgsImages)
        self._init_coll_fgsButton_Items(self.fgsButton)

        self.SetSizer(self.bsDialog)

    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Dialog.__init__(self, id=wxID_DIALOG2, name='', parent=prnt,
              pos=wx.Point(302, 249), size=wx.Size(597, 281),
              style=wx.DEFAULT_DIALOG_STYLE, title='About Notebook')
        self.SetClientSize(wx.Size(581, 245))

        self.staticText1 = wx.StaticText(id=wxID_DIALOG2STATICTEXT1,
              label='Notebook - Simple text editor.', name='staticText1',
              parent=self, pos=wx.Point(4, 4), size=wx.Size(681, 24),
              style=wx.ALIGN_CENTRE)
        self.staticText1.SetFont(wx.Font(14, wx.SWISS, wx.NORMAL, wx.NORMAL,
              False, 'Microsoft Sans Serif'))

        self.staticText2 = wx.StaticText(id=wxID_DIALOG2STATICTEXT2,
              label='This is my first Boa Contstructor application',
              name='staticText2', parent=self, pos=wx.Point(244, 32),
              size=wx.Size(201, 13), style=0)
        self.staticText2.SetBackgroundColour(wx.Colour(255, 255, 0))

        self.staticBitmap1 = wx.StaticBitmap(bitmap=wx.Bitmap('Boa.jpg',
              wx.BITMAP_TYPE_JPEG), id=wxID_DIALOG2STATICBITMAP1,
              name='staticBitmap1', parent=self, pos=wx.Point(173, 53),
              size=wx.Size(236, 157), style=0)

        self.staticBitmap2 = wx.StaticBitmap(bitmap=wx.Bitmap('Debian.png',
              wx.BITMAP_TYPE_PNG), id=wxID_DIALOG2STATICBITMAP2,
              name='staticBitmap2', parent=self, pos=wx.Point(52, 116),
              size=wx.Size(117, 31), style=0)

        self.staticBitmap3 = wx.StaticBitmap(bitmap=wx.Bitmap('wxWidgetsButton.png',
              wx.BITMAP_TYPE_PNG), id=wxID_DIALOG2STATICBITMAP3,
              name='staticBitmap3', parent=self, pos=wx.Point(413, 107),
              size=wx.Size(116, 49), style=0)

        self.button1 = wx.Button(id=wxID_DIALOG2BUTTON1, label='Close',
              name='button1', parent=self, pos=wx.Point(253, 218),
              size=wx.Size(75, 23), style=0)
        self.button1.Bind(wx.EVT_BUTTON, self.OnButton1Button,
              id=wxID_DIALOG2BUTTON1)

        self._init_sizers()

    def __init__(self, parent):
        self._init_ctrls(parent)

    def OnButton1Button(self, event):
        self.Close()
