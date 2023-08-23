#cs ----------------------------------------------------------------------------

 AutoIt Version: 3.3.16.1
 Author:         myName

 Script Function:
	Template AutoIt script.

#ce ----------------------------------------------------------------------------

; Script Start - Add your code below here

WinWaitActive("#32770", "File Upload", 10)
ControlSetText("File Upload", " ", "Edit1", "D:\SpeechAce\SSW-Automation\ssw-automation\source\speechace_logo.png")
ControlClick("File Upload", " ", "Button1")