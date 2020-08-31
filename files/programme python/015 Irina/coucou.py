import os
def G(f):
    os.system("cd {}".format(f))
def pause():
    os.system("pause")
def osget():
    print("current directory: {}".format(os.getcwd()))
osget()
G("..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..\..")
pause()
osget()
try:
    print("hi")
    osget()
    G("..")
    pause()
    osget()
    #goto("C:\Users\..\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup")
    G("Users")
    osget()
    pause()
    G("..\..\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup")
    osget()
    pause()
    print("succes")
except:
    print("fail")
pause()
