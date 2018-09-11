import wx
import os
import choboutil

class ChoboResultPanel(wx.Panel):
    def __init__(self, parent, *args, **kw):
        super(ChoboResultPanel, self).__init__(*args, **kw)
        self.memoText = wx.TextCtrl(self, style = wx.TE_MULTILINE, size=(800,300))
        self.drawUI()
        self.parent = parent

    def onClear(self):
        print ("onclear")
        self.memoText.SetValue("")

    def setFocus(self):
        self.memoText.SetFocus()

    def onCopy(self, evt):
        self.onCopyCmd()

    def onSetData(self, data):
        self.memoText.SetValue(data)

    def onClearMemo(self, evt):
        self.onClear()

    def onCopyCmd(self):
        print ("onCopyCmd")

        if wx.TheClipboard.Open():
            wx.TheClipboard.SetData(wx.TextDataObject(self.memoText.GetValue()))
            wx.TheClipboard.Close()

    def drawUI(self):
        print ("ChoboMemoPanel::drawUI")
        sizer = wx.BoxSizer(wx.VERTICAL)

        memoMngBox = wx.BoxSizer(wx.HORIZONTAL)

        self.memoText.SetValue("")
        memoMngBox.Add(self.memoText, 1, wx.EXPAND)
        sizer.Add(memoMngBox, 1, wx.EXPAND)

        ##
        memoMngBtnBox = wx.BoxSizer(wx.HORIZONTAL)

        self.copyBtn = wx.Button(self, 10, "Copy (Ctrl+C)", size=(30,30))
        self.copyBtn.Bind(wx.EVT_BUTTON, self.onCopy)
        memoMngBtnBox.Add(self.copyBtn, 1, wx.EXPAND)

        self.memoClearBtn = wx.Button(self, 10, "Clear", size=(30,30))
        self.memoClearBtn.Bind(wx.EVT_BUTTON, self.onClearMemo)
        memoMngBtnBox.Add(self.memoClearBtn, 1, wx.EXPAND)

        sizer.Add(memoMngBtnBox, 0, wx.GROW|wx.ALIGN_CENTER_VERTICAL|wx.ALL, 5)
        
        ##
        self.SetSizer(sizer)
        self.SetAutoLayout(True)
