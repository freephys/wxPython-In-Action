#!/usr/bin/env python

#
# Demo Infrastructure
#

import wx
import WithBoxSizers
import WithBoxSizersTwo

class Demo:
    def __init__(self, title, plotFunction):
        self.title = title
        self.plotFunction = plotFunction

    def run(self):
        import baseframe
        frame = baseframe.MyFrame(None,title=self.title, panel=self.plotFunction)
        frame.Show()
#        panel = wx.Panel.__init__(self,-1,self.title)
#        self.plotFunction
#        panel.show()

    def makeButton(self, parent):
        btn = wx.Button(parent, -1, self.title)
        wx.EVT_BUTTON(btn, btn.GetId(), self.OnButton)
        return btn

    def OnButton(self, evt):
        self.run()


DEMONSTRATIONS = [
    Demo('1 ColWin', WithBoxSizers.MyPanel1),
    Demo('2 ColWins, vertically', WithBoxSizers.MyPanel2),
    Demo('3 ColWins, horizontally', WithBoxSizers.MyPanel3),
    Demo('3 ColWins, horizontally, height ratio 1:2:3', WithBoxSizers.MyPanel4),
    Demo('2 ColWins, vertically, a fixed width of 50 pixels between the two items', WithBoxSizers.MyPanel5),
    Demo('Two items, 1 ColWin and 1 Button, verically', WithBoxSizers.MyPanel6),
    Demo('3 items, 1 ColWin and 2 Buttons',WithBoxSizers.MyPanel7),
    Demo('4 items, 1 ColWin, 2 Buttons, 1 StaticLine', WithBoxSizers.MyPanel8),
    Demo('7 items, 2 ColWins and 5 Buttons', WithBoxSizers.MyPanel9),
    Demo('7 items, 2 ColWins and 5 Buttons', WithBoxSizers.MyPanel10),
    Demo('3 ColWins, horizontally, 2 spacers with a fixed height', WithBoxSizers.MyPanel11),
    Demo('4 items, 1 ColWin, 3 Buttons, with 2 AddStretchSpacer', WithBoxSizers.MyPanel12),
    Demo('4 items, 1 ColWin, 3 Buttons',WithBoxSizers.MyPanel13),
    Demo('An input box',WithBoxSizers.MyPanel14),
    Demo('An input box with size constraints,lock the vertical size and set a minimal horizontal size (200)',WithBoxSizers.MyPanel20),
    Demo('A message box',WithBoxSizers.MyPanel15),
    Demo('StaticTexts-TextCtrls-Buttons ok and cancel, A better way: FlexGridSizer ',WithBoxSizers.MyPanel16),
    Demo('1 Colwin.4 buttons in a "toolbar". Button 2 and 3 are centered',WithBoxSizers.MyPanel17),
    Demo('5 buttons,Show usage of wx.GROW instead of wx.EXPAND; self.parent.SetMinSize',WithBoxSizers.MyPanel18)
    ]

DEMONSTRATIONS_TWO = [
    Demo('Three ColWins. The B width is fixed. A and C are expanded', WithBoxSizersTwo.MyPanel1),
    Demo('A item (ColWin) with a fixed size, centered in the panel',WithBoxSizersTwo.MyPanel3),
    Demo('Two separated items (ColWin) with fixed sized centered in the panel',WithBoxSizersTwo.MyPanel5),
    Demo('Pairs of "labels" - "text entries" widgets with different styles',WithBoxSizersTwo.MyPanel6),
    ]
class TestFrame(wx.Frame):
    def __init__(self, parent, id, title, **kwds):
        wx.Frame.__init__(self, parent, id, title, **kwds)

        buttons = [demo.makeButton(self) for demo in DEMONSTRATIONS]
        
        buttons2 = [demo.makeButton(self) for demo in DEMONSTRATIONS_TWO]

        sizer = wx.BoxSizer(wx.VERTICAL)
        for btn in buttons:
            sizer.Add(btn, 0, wx.EXPAND)
        
        staline = wx.StaticLine(self, wx.ID_ANY, wx.DefaultPosition, (-1, 15), \
            wx.LI_HORIZONTAL)
        sizer.Add(staline,1,wx.GROW | wx.ALL)
        
        for btn in buttons2:
            sizer.Add(btn,0,wx.EXPAND)

        self.SetSizer(sizer)
        self.Fit()
        

        wx.EVT_WINDOW_DESTROY(self, self.OnWindowDestroy)

    def OnWindowDestroy(self, evt):
        wx.GetApp().ExitMainLoop()


def main():
    app = wx.PySimpleApp()
    frame = TestFrame(None, -1, 'BoxSizer Demos')
    frame.Show(True)
    app.MainLoop()
    

if __name__ == '__main__':
    main() 