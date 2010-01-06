#!/usr/bin/env python
#Boa:App:BoaApp

import wx

import wxMDIParentFrame1

modules ={'wxMDIChildFrame1': [0, '', 'wxMDIChildFrame1.py'],
 'wxMDIParentFrame1': [1, '', 'wxMDIParentFrame1.py']}

class BoaApp(wx.App):
    def OnInit(self):
        self.main = wxMDIParentFrame1.create(None)
        self.main.Show(True)
        self.SetTopWindow(self.main)
        return True

def main():
    application = BoaApp(0)
    application.MainLoop()

if __name__ == '__main__':
    main()
