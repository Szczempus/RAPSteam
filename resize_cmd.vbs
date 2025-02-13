Set objShell = CreateObject("WScript.Shell")
objShell.AppActivate "Command Prompt"
WScript.Sleep 500
objShell.SendKeys "% "
WScript.Sleep 500
objShell.SendKeys "x"
WScript.Sleep 500
objShell.SendKeys "s"
WScript.Sleep 500
objShell.SendKeys "{RIGHT}{RIGHT}{RIGHT}{RIGHT}{RIGHT}{RIGHT}{DOWN}{DOWN}{DOWN}{DOWN}{ENTER}"

