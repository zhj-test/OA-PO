;ControlFocus("title","text",ClassnameNN )
;�������뽹�㵽ָ�����ڵ�ĳ���ؼ���
Sleep(1000)
ControlFocus("��", "","Edit1")
; Wait 10 seconds for the Upload window to appear
WinWait("[CLASS:#32770]","",10)
; Set the File name text on the Edit field
;�޸�ָ���ؼ����ı�.?
Sleep(1000)
ControlSetText("��", "", "Edit1", "C:\Users\Public\Pictures\Sample Pictures\����.jpg")
Sleep(1000)
; Click on the Open button
ControlClick("��", "","Button1");