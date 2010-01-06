#Boa:Frame:FrameI18N

import os

import wx

# define _ or add _ to builtins in your app file
_ = wx.GetTranslation

def create(parent):
    return FrameI18N(parent)

[wxID_FRAMEI18N, wxID_FRAMEI18NSTATICTEXT1, 
] = [wx.NewId() for _init_ctrls in range(2)]

class FrameI18N(wx.Frame):
    def _init_ctrls(self, prnt):
        # generated method, don't edit
        wx.Frame.__init__(self, id=wxID_FRAMEI18N, name='FrameI18N',
              parent=prnt, pos=wx.Point(448, 205), size=wx.Size(308, 70),
              style=wx.DEFAULT_FRAME_STYLE, title=_('I18N Example'))
        self.SetClientSize(wx.Size(300, 43))

        self.staticText1 = wx.StaticText(id=wxID_FRAMEI18NSTATICTEXT1,
              label=_('the quick brown fox jumps over the lazy dog'),
              name='staticText1', parent=self, pos=wx.Point(0, 0),
              size=wx.Size(300, 43), style=0)
        self.staticText1.SetToolTipString(_('I18N Example'))

    def __init__(self, parent):
        self._init_ctrls(parent)
        
        # example of built-in wxPython translated text, note the title of the msg dlg
        wx.LogMessage(_('I18N Example'))
        
class BoaApp(wx.App):
    def OnInit(self):
        # choose language
        self.locale = wx.Locale(wx.LANGUAGE_AFRIKAANS)
    
        # setup catalog
        wx.Locale.AddCatalogLookupPathPrefix('locale')
        self.locale.AddCatalog('i18n_example') 
    
        # show main frame
        self.main = create(None)
        self.main.Show()
        self.SetTopWindow(self.main)

        return True

def main():
    application = BoaApp(0)
    application.MainLoop()        
    
if __name__ == '__main__':
    main()

