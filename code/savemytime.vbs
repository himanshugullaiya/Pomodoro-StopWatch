Set oShell = CreateObject ("Wscript.Shell")
Dim strArgs
strArgs = "cmd /c python stopwatch.py"
oShell.Run strArgs,0,false