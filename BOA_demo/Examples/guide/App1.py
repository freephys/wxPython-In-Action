#!/usr/bin/env python
#Boa:App:BoaApp

import wx

import Frame1

modules ={'Dialog1': [0, '', 'Dialog1.py'],
 'Dialog2': [0, '', 'Dialog2.py'],
 'Frame1': [1, 'Main frame of Application', 'Frame1.py']}

class BoaApp(wx.App):
    def OnInit(self):
        wx.InitAllImageHandlers()
        self.main = Frame1.create(None)
        self.main.Show()
        self.SetTopWindow(self.main)
        return True

def main():
    application = BoaApp(0)
    application.MainLoop()

if __name__ == '__main__':
    main()
