#Boa:Frame:FrameI18N

import os

# Import gettext and define _ or add _ to builtins in your app file
import gettext
_ = gettext.gettext

import wx

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


if __name__ == '__main__':
    app = wx.PySimpleApp()

    # choose language
    os.environ['LANGUAGE'] = 'af'

    # setup gettext
    gettext.bindtextdomain('i18n_example', 'locale') 
    gettext.textdomain('i18n_example') 
    
    frame = create(None)
    frame.Show()

    app.MainLoop()
