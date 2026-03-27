import wx

class ModernApp(wx.Frame):
    def __init__(self):
        super().__init__(None, title="App", size=(600, 500))
        panel = wx.Panel(self)
        sizer = wx.BoxSizer(wx.VERTICAL)
        
        # Заголовок
        title = wx.StaticText(panel, label="💓 Modern wxPython")
        title_font = wx.Font(28, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL,
                           wx.FONTWEIGHT_BOLD, False, "Segoe UI")
        title.SetFont(title_font)
        sizer.Add(title, 0, wx.ALL | wx.CENTER, 30)
        
        
        self.slider = wx.Slider(panel, value=50, minValue=0, maxValue=100,
                               style=wx.SL_HORIZONTAL | wx.SL_LABELS)
        self.slider.SetMinSize((350, -1))  # Ширина 350px!
        sizer.Add(self.slider, 0, wx.ALL | wx.EXPAND, 20)
        
        # Значение
        self.value = wx.StaticText(panel, label="50")
        value_font = wx.Font(20, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL,
                           wx.FONTWEIGHT_BOLD, False, "Segoe UI")
        self.value.SetFont(value_font)
        sizer.Add(self.value, 0, wx.ALL | wx.CENTER, 20)
        
        
        self.btn = wx.Button(panel, label="OK!")
        self.btn.SetMinSize((150, 60))       
        self.btn.SetFont(wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL,
                               wx.FONTWEIGHT_BOLD, False, "Segoe UI"))
        self.btn.SetBackgroundColour(wx.Colour(0, 120, 215))  
        self.btn.SetForegroundColour(wx.WHITE)
        self.btn.Bind(wx.EVT_BUTTON, self.on_click)
        sizer.Add(self.btn, 0, wx.ALL | wx.CENTER, 30)
        
        
        btn2 = wx.Button(panel, label="Сброс")
        btn2.SetMinSize((150, 50))
        sizer.Add(btn2, 0, wx.ALL | wx.CENTER, 10)
        
        panel.SetSizer(sizer)
        self.Centre()
        self.Show()

    def on_click(self, event):
        value = self.slider.GetValue()
        self.value.SetLabelText(str(value))
        wx.MessageBox(f"Значение: {value}", "Результат", 
                     wx.OK | wx.ICON_INFORMATION)

if __name__ == "__main__":
    app = wx.App()
    ModernApp()
    app.MainLoop()
