#!/usr/bin/env python
#Boa:App:BoaApp

import wx

import wxFrame1

modules ={'wxFrame1': [1, 'Main frame of Application', 'wxFrame1.py'],
 'wxFrame2': [0,
              'Example of frame as an attribute of another frame',
              'wxFrame2.py'],
 'wxFrame3': [0, 'Example of a dynamic frame', 'wxFrame3.py'],
 'wxPyWizardPage1': [0, '', 'wxPyWizardPage1.py'],
 'wxPyWizardPage2': [0, '', 'wxPyWizardPage2.py'],
 'wxWizard1': [0, '', 'wxWizard1.py'],
 'wxWizardPageSimple1': [0, '', 'wxWizardPageSimple1.py'],
 'wxWizardPageSimple2': [0, '', 'wxWizardPageSimple2.py']}

class BoaApp(wx.App):
    def OnInit(self):
        wx.InitAllImageHandlers()
        self.main = wxFrame1.create(None)
        self.main.Show(True)
        self.SetTopWindow(self.main)
        return True

def main():
    application = BoaApp(0)
    application.MainLoop()

if __name__ == '__main__':
    main()
