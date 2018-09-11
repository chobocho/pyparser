import wx
import wx.lib.mixins.listctrl as listmix
import os
import ChoboMemoPanel
import ChoboResultPanel
'''
Start  : 2018.09.12
Update : 2018.09.12a
'''

SW_TITLE = "PyParser V0627.0601a"

class PyParserFrame(wx.Frame):
    def __init__(self, *args, **kw):
        super(PyParserFrame, self).__init__(*args, **kw)

        ctrl_C_Id = wx.NewId()
        self.Bind(wx.EVT_MENU, self.onCopyResult, id=ctrl_C_Id)
        ctrl_L_Id = wx.NewId()
        self.Bind(wx.EVT_MENU, self.onFocusOnSource, id=ctrl_L_Id)
        ctrl_R_Id = wx.NewId()
        self.Bind(wx.EVT_MENU, self.onRun, id=ctrl_R_Id)
        ctrl_Q_Id = wx.NewId()
        self.Bind(wx.EVT_MENU, self.onClose, id=ctrl_Q_Id)
        ctrl_D_Id = wx.NewId()
        self.Bind(wx.EVT_MENU, self.onClear, id=ctrl_D_Id)

        accel_tbl = wx.AcceleratorTable([(wx.ACCEL_CTRL,  ord('C'), ctrl_C_Id),
                                         (wx.ACCEL_CTRL,  ord('L'), ctrl_L_Id),
                                         (wx.ACCEL_CTRL,  ord('Q'), ctrl_Q_Id),
                                         (wx.ACCEL_CTRL,  ord('R'), ctrl_R_Id),
                                         (wx.ACCEL_CTRL,  ord('D'), ctrl_D_Id)])
        self.SetAcceleratorTable(accel_tbl)

        self.splitter = wx.SplitterWindow(self, -1, wx.Point(0, 0), wx.Size(800, 600), wx.SP_3D | wx.SP_BORDER)
        self.sourcePanel = ChoboMemoPanel.ChoboMemoPanel(self, self.splitter)
        self.resultPanel = ChoboResultPanel.ChoboResultPanel(self, self.splitter)
        self.splitter.SplitHorizontally(self.sourcePanel, self.resultPanel)
        self.splitter.SetMinimumPaneSize(20)

        sizer = wx.BoxSizer(wx.VERTICAL)
        sizer.Add(self.splitter, 1, wx.EXPAND)
        self.SetSizer(sizer)

    def onCopyResult(self, event):
        print ("onCopyResult")
        self.resultPanel.onCopyCmd()

    def onFocusOnSource(self, event):
        print ("onFocusOnSource")
        self.sourcePanel.setFocus()

    def onRun(self, event):
        print("onRun")
        result = self.sourcePanel.onRunCmd()
        self.setResult(result)

    def setResult(self, data):
        if len(data) > 0:
            self.resultPanel.onSetData(data)
        else:
            self.resultPanel.onSetData("None")

    def onClear(self, event):
        self.sourcePanel.onClear()
        print("onClear")

    def onClose(self, event):
        self.Close()

def main(): 
    app = wx.App()
    frm = PyParserFrame(None, title=SW_TITLE, size=(800,600))
    frm.Show()
    app.MainLoop()

if __name__ == '__main__':
    main()