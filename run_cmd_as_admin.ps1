$cmd = 'title Kurs & mode con: cols=120 lines=10 & color F0 & cd /d "C:\Users\Patryk\PycharmProjects\RaPSteam_docx\files\beginner\module_1\lesson_2\code\" & python arguments.py & pause'
Start-Process -FilePath "cmd.exe" -ArgumentList "/k $cmd" -Verb RunAs
