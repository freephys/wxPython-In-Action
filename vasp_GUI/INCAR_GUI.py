#!/usr/bin/env python

import re
import  os
#import string
import wx
import wx.lib.agw.foldpanelbar as fpb
from INCAR_data import *

#---------------------------------------------------------------------------

# This is how you pre-establish a file filter so that the dialog
# only shows the extension(s) you want it to.
wildcard = "Vasp Files (INCAR)|INCAR|"     \
           "All files (*.*)|*.*"

#---------------------------------------------------------------------------

class IncarFrame(wx.Frame):    
    def __init__(self):

        wx.Frame.__init__(self,None,id=wx.ID_ANY, title="INCAR GUI", pos=wx.DefaultPosition,
                 size=(650,650), style=wx.DEFAULT_FRAME_STYLE)
        
        self.statusbar = self.CreateStatusBar(2, wx.ST_SIZEGRIP)
        self.statusbar.SetStatusWidths([-4, -3])
        self.statusbar.SetStatusText("Leo Shen", 0)
        self.statusbar.SetStatusText("Welcome to Vasp GUI!", 1)
        
        self._leftWindow1 = wx.SashLayoutWindow(self, -1, wx.DefaultPosition,
                                                wx.Size(200, 1000), wx.NO_BORDER |
                                                wx.SW_3D | wx.CLIP_CHILDREN)

        self._leftWindow1.SetDefaultSize(wx.Size(320, 1000))
        self._leftWindow1.SetOrientation(wx.LAYOUT_VERTICAL)
        self._leftWindow1.SetAlignment(wx.LAYOUT_LEFT)
        self._leftWindow1.SetSashVisible(wx.SASH_RIGHT, True)
        self._leftWindow1.SetExtraBorderSize(10)
        
        #self._rightWindow1 = wx.SashLayoutWindow(self, -1, wx.DefaultPosition,
        #                                        wx.Size(200, 1000), wx.NO_BORDER |
        #                                        wx.SW_3D | wx.CLIP_CHILDREN)
        #
        #self._rightWindow1.SetDefaultSize(wx.Size(220, 1000))
        #self._rightWindow1.SetOrientation(wx.LAYOUT_VERTICAL)
        #self._rightWindow1.SetAlignment(wx.LAYOUT_LEFT)
        #self._rightWindow1.SetSashVisible(wx.SASH_LEFT, True)
        #self._rightWindow1.SetExtraBorderSize(10)
        
        self.remainingSpace = wx.Panel(self, -1, style=wx.SUNKEN_BORDER)
        #self.txtCtrl = wx.TextCtrl(self.remainingSpace, -1,size=(450, 450), style=wx.TE_MULTILINE|wx.TE_PROCESS_ENTER|wx.ALL)
        #self.ImportIncarButton = wx.Button(self.remainingSpace, -1,"Import",(20, 20))
        
        self.Bind(wx.EVT_SIZE, self.OnSize)
#        self.txtCtrl.Bind(wx.EVT_TEXT,self.OnTxtChange)
        
        self.CreateIncarLeftFoldPanel(0)
        self.CreateIncarRightFoldPanel()
        
    def OnSize(self, event):

        wx.LayoutAlgorithm().LayoutWindow(self, self.remainingSpace)
        event.Skip()

    def CreateIncarRightFoldPanel(self):
        
        self.remainingSpace.DestroyChildren()
        
        self._vsizer = wx.BoxSizer(wx.VERTICAL)
        self._hsizer = wx.BoxSizer(wx.HORIZONTAL)
        self.txtCtrl = wx.TextCtrl(self.remainingSpace, -1,size=(450, 450), style=wx.TE_MULTILINE|wx.TE_PROCESS_ENTER|wx.ALL)
        self.ImportIncarButton = wx.Button(self.remainingSpace, -1,"Import INCAR",(20, 20),name="BUTTON_IMPORT_INCAR")
        self.ExportIncarButton = wx.Button(self.remainingSpace, -1,"Export INCAR",(20, 20),name="BUTTON_EXPORT_INCAR")
        self._hsizer.Add(self.ImportIncarButton,0,wx.ALIGN_CENTER,5)
        self._hsizer.Add(self.ExportIncarButton,0,wx.ALIGN_CENTER,5)        

        self._vsizer.Add(self.txtCtrl,1,wx.ALIGN_CENTER|wx.GROW, 5)
        self._vsizer.Add(self._hsizer)
        self.remainingSpace.SetSizer(self._vsizer)
        
        self.ImportIncarButton.Bind(wx.EVT_BUTTON, self.OnButtonImport)
        self.ExportIncarButton.Bind(wx.EVT_BUTTON, self.OnButtonExport)
        
    def CreateIncarLeftFoldPanel(self, fpb_flags):

        # delete earlier panel
        self._leftWindow1.DestroyChildren()

        # recreate the foldpanelbar

        self._pnl = fpb.FoldPanelBar(self._leftWindow1, -1, wx.DefaultPosition,
                                     wx.Size(-1,-1), fpb.FPB_DEFAULT_STYLE, fpb_flags)
        #Create fold panel of Output Writing
        outputTagFoldPanel = self._pnl.AddFoldPanel("Tags of Output Writing", collapsed=False)
        
        #add LCHARG
        # step 1 : create static text 
        self._pnl.AddFoldPanelWindow(outputTagFoldPanel, wx.StaticText(outputTagFoldPanel, -1, "LCHARG:Write Charge density"),
                                     fpb.FPB_ALIGN_WIDTH, 5, 20)
        #step 2 : create choice
        self._lchargChoice = wx.Choice(outputTagFoldPanel, -1, (10, 10), choices = LCHARG_LIST,name="LCHARG")
        self._lchargChoice.SetSelection(0)
        #step 3 : add choice to Fold Panel
        self._pnl.AddFoldPanelWindow(outputTagFoldPanel, self._lchargChoice, fpb.FPB_ALIGN_WIDTH, 2, 20) 
        
        # add ELF
        self._pnl.AddFoldPanelWindow(outputTagFoldPanel, wx.StaticText(outputTagFoldPanel, -1, "LELF:Write Electron Localization Function"),
                                     fpb.FPB_ALIGN_WIDTH, 5, 20)
        self._lelfChoice = wx.Choice(outputTagFoldPanel, -1, (10, 10), choices = LELF_LIST,name="LELF")
        self._lelfChoice.SetSelection(1)
        self._pnl.AddFoldPanelWindow(outputTagFoldPanel, self._lelfChoice, fpb.FPB_ALIGN_WIDTH, 2, 20) 
        
        #add LVTOT
        self._pnl.AddFoldPanelWindow(outputTagFoldPanel, wx.StaticText(outputTagFoldPanel, -1, "LVTOT:Write Electric Potential "),
                                     fpb.FPB_ALIGN_WIDTH, 5, 20)
        self._lvtotChoice = wx.Choice(outputTagFoldPanel, -1, (10, 10), choices = LVTOT_LIST,name="LVTOT")
        self._lvtotChoice.SetSelection(1)
        self._pnl.AddFoldPanelWindow(outputTagFoldPanel, self._lvtotChoice, fpb.FPB_ALIGN_WIDTH, 2, 20)
        
        # add LWAVE
        self._pnl.AddFoldPanelWindow(outputTagFoldPanel,wx.StaticText(outputTagFoldPanel,-1,"LWAVE:Write WAVECAR"),
                                     fpb.FPB_ALIGN_WIDTH,5,20)
        self._lwaveChoice = wx.Choice(outputTagFoldPanel,-1,(10,10),choices = LWAVE_LIST,name="LWAVE")
        self._lwaveChoice.SetSelection(0)
        self._pnl.AddFoldPanelWindow(outputTagFoldPanel,self._lwaveChoice,fpb.FPB_ALIGN_WIDTH, 2, 20)
        
        #add NWRITE RadioBox 
        self._nwriteRadioBox = wx.RadioBox(outputTagFoldPanel,-1,"NWRITE:OUTCAR verbosity flag",wx.DefaultPosition,wx.DefaultSize,
                                           NWRITE_LIST,4,wx.RA_SPECIFY_COLS,name="NWRITE")
        self._nwriteRadioBox.SetItemToolTip(0,Tag_Tips["NWRITE"][0])
        self._nwriteRadioBox.SetItemToolTip(1,Tag_Tips["NWRITE"][1])
        self._nwriteRadioBox.SetItemToolTip(2,Tag_Tips["NWRITE"][2])
        self._nwriteRadioBox.SetItemToolTip(3,Tag_Tips["NWRITE"][3])
        self._nwriteRadioBox.SetSelection(2)
        self._pnl.AddFoldPanelWindow(outputTagFoldPanel,self._nwriteRadioBox,fpb.FPB_ALIGN_WIDTH,2,20)
        
        #add LORBIT RadioBox and bind it with EVT_RADIOBOX 
        self._lorbitRadioBox = wx.RadioBox(outputTagFoldPanel,-1,"LORBIT:Projected DOSCAR&PROOUT", wx.DefaultPosition, wx.DefaultSize,
                LORBIT_LIST, 4, wx.RA_SPECIFY_COLS,name="LORBIT"
                )        
        self._lorbitRadioBox.SetItemToolTip(0,Tag_Tips["LORBIT"][0])
        self._lorbitRadioBox.SetItemToolTip(1,Tag_Tips["LORBIT"][1])
        self._lorbitRadioBox.SetItemToolTip(2,Tag_Tips["LORBIT"][2])
        self._lorbitRadioBox.SetItemToolTip(3,Tag_Tips["LORBIT"][3])
        self._lorbitRadioBox.SetItemToolTip(4,Tag_Tips["LORBIT"][4])
        self._lorbitRadioBox.SetSelection(0)
        self._pnl.AddFoldPanelWindow(outputTagFoldPanel, self._lorbitRadioBox, fpb.FPB_ALIGN_WIDTH, 2, 20)
        
        #add event listener
        self._lchargChoice.Bind(wx.EVT_CHOICE,self.EvtChoice)
        self._lelfChoice.Bind(wx.EVT_CHOICE,self.EvtChoice)
        self._lvtotChoice.Bind(wx.EVT_CHOICE,self.EvtChoice)
        self._lwaveChoice.Bind(wx.EVT_CHOICE,self.EvtChoice)
        self._lorbitRadioBox.Bind(wx.EVT_RADIOBOX,self.EvtRadioBox)
        self._nwriteRadioBox.Bind(wx.EVT_RADIOBOX,self.EvtRadioBox)
        #Create fold panel related to Ion movement
        IonMoveTagFoldPanel = self._pnl.AddFoldPanel("Tags of Ion Movement", collapsed=True)
        
        #add IBRION RadioBox
        self._ibrionRadioBox = wx.RadioBox(IonMoveTagFoldPanel,-1,"IBRION:how ions are moved", wx.DefaultPosition, wx.DefaultSize,
                IBRION_LIST, 5, wx.RA_SPECIFY_COLS,name="IBRION"
                )        
        self._ibrionRadioBox.SetItemToolTip(0,Tag_Tips["IBRION"][0])
        self._ibrionRadioBox.SetItemToolTip(1,Tag_Tips["IBRION"][1])
        self._ibrionRadioBox.SetItemToolTip(2,Tag_Tips["IBRION"][2])
        self._ibrionRadioBox.SetItemToolTip(3,Tag_Tips["IBRION"][3])
        self._ibrionRadioBox.SetItemToolTip(4,Tag_Tips["IBRION"][4])
        self._lorbitRadioBox.SetSelection(0)
        self._pnl.AddFoldPanelWindow(IonMoveTagFoldPanel, self._ibrionRadioBox, fpb.FPB_ALIGN_WIDTH, 2, 20)
        
        #add event listener for IonMoveTagFoldPanel
        self._ibrionRadioBox.Bind(wx.EVT_RADIOBOX,self.EvtRadioBox)
    def EvtChoice(self,event):
        choice = self.FindWindowById(event.GetId())
        choiceName = choice.Name
        choiceContent = INCAR_Tags[choiceName][choice.GetCurrentSelection()]
        curChoice = " = ".join([choiceName, choiceContent])
        textOfCtrl = self.txtCtrl.GetValue() 
        if(textOfCtrl.find(choiceName) == -1):
           self.txtCtrl.WriteText("%s\n" %(curChoice))
        else:
            pattern = re.compile("%s\s*.*" %(choiceName)) # variable substitution
            replacedText = re.sub(pattern,curChoice,textOfCtrl)
            self.txtCtrl.SetValue(replacedText)
    def EvtRadioBox(self,event):
        radioBox = self.FindWindowById(event.GetId())
        radioName = radioBox.Name
        radioContent = INCAR_Tags[radioName][radioBox.GetSelection()] #event.GetInt() also works
        curChoice = " = ".join([radioName, radioContent])
        textOfCtrl = self.txtCtrl.GetValue() 
        if(textOfCtrl.find(radioName) == -1):
           self.txtCtrl.WriteText("%s\n" %(curChoice))
        else:
            pattern = re.compile("%s\s*.*" %(radioName)) # variable substitution
            replacedText = re.sub(pattern,curChoice,textOfCtrl)
            self.txtCtrl.SetValue(replacedText)
    def OnButtonImport(self,event):
        buttonSelected = self.FindWindowById(event.GetId())
        buttonName = buttonSelected.Name
        if(buttonName == "BUTTON_IMPORT_INCAR"):
            dlg = wx.FileDialog(
            self, message="Choose a file",
            defaultDir=os.getcwd(), 
            defaultFile="INCAR",
            wildcard=wildcard,
            style=wx.OPEN | wx.MULTIPLE | wx.CHANGE_DIR # can select more than one file
            )
            if dlg.ShowModal() == wx.ID_OK:
            # This returns a file that were selected.
                path = dlg.GetPath() 
        dlg.Destroy()            
    def OnButtonExport(self,event):
        buttonSelected = self.FindWindowById(event.GetId())
        buttonName = buttonSelected.Name
        if(buttonName == "BUTTON_EXPORT_INCAR"):
            dlg = wx.FileDialog(
            self, message="Save file as ...", defaultDir=os.getcwd(), 
            defaultFile="", wildcard=wildcard, style=wx.SAVE|wx.OVERWRITE_PROMPT
            )
        dlg.SetFilterIndex(2)
        if dlg.ShowModal() == wx.ID_OK:
            path = dlg.GetPath()
            f = open('INCAR','w')
            textOfCtrl = self.txtCtrl.GetValue()
            f.write(textOfCtrl)
            f.close()
        dlg.Destroy()
        
if __name__ == '__main__':
        app = wx.PySimpleApp()
        frame = IncarFrame()
        frame.Show()
        app.MainLoop()