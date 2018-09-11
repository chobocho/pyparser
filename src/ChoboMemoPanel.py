import wx
import os
import choboutil

class ChoboMemoPanel(wx.Panel):
    def __init__(self, parent, *args, **kw):
        super(ChoboMemoPanel, self).__init__(*args, **kw)
        self.memoText = wx.TextCtrl(self, style = wx.TE_MULTILINE, size=(800,300))
        self.drawUI()
        self.parent = parent

    def onClear(self):
        print ("onclear")
        self.memoText.SetValue("")

    def setFocus(self):
        self.memoText.SetFocus()

    def onRun(self, evt):
        data = self.onRunCmd()
        self.parent.setResult(data)

    def onSetData(self, data):
        self.memoText.SetValue(data)

    def onClearMemo(self, evt):
        self.onClear()

    def onRunCmd(self):
        print ("onRunCmd")
        return choboutil.findemail(self.memoText.GetValue())

    def drawUI(self):
        print ("ChoboMemoPanel::drawUI")
        sizer = wx.BoxSizer(wx.VERTICAL)

        memoMngBox = wx.BoxSizer(wx.HORIZONTAL)

        self.memoText.SetValue("")
        memoMngBox.Add(self.memoText, 1, wx.EXPAND)
        sizer.Add(memoMngBox, 1, wx.EXPAND)

        ##
        memoMngBtnBox = wx.BoxSizer(wx.HORIZONTAL)

        self.runBtn = wx.Button(self, 10, "Run (Ctrl+R)", size=(30,30))
        self.runBtn.Bind(wx.EVT_BUTTON, self.onRun)
        memoMngBtnBox.Add(self.runBtn, 1, wx.EXPAND)

        self.memoClearBtn = wx.Button(self, 10, "Clear (Ctrl+D)", size=(30,30))
        self.memoClearBtn.Bind(wx.EVT_BUTTON, self.onClearMemo)
        memoMngBtnBox.Add(self.memoClearBtn, 1, wx.EXPAND)

        sizer.Add(memoMngBtnBox, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)
        
        ##
        self.SetSizer(sizer)
        self.SetAutoLayout(True)
