;ControlFocus("title","text",ClassnameNN )
;设置输入焦点到指定窗口的某个控件上
Sleep(1000)
ControlFocus("打开", "","Edit1")
; Wait 10 seconds for the Upload window to appear
WinWait("[CLASS:#32770]","",10)
; Set the File name text on the Edit field
;修改指定控件的文本.?
Sleep(1000)
ControlSetText("打开", "", "Edit1", "C:\Users\Public\Pictures\Sample Pictures\灯塔.jpg")
Sleep(1000)
; Click on the Open button
ControlClick("打开", "","Button1");