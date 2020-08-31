from time import sleep
import os
i=0
print(os.getcwd())
while i<11:
    z=0
    d=0
    while d<51:
        print("Cela fait {} heure(s) et {} minutes que le programme tourne.".format(i,d))
        sleep(60)
        d+=1
    i+=1
    print("\a")
    os.system("temps.bat")
    os.system("Timee.vbs")
    os.system("Timee.vbs")
    os.system("Timee.vbs")
    os.system("Timee.vbs")
    os.system("Timee.vbs")
    os.system("Timee.vbs")
    os.system("Timee.vbs")
    os.system("Timee.vbs")
    os.system("Timee.vbs")
    while z<601:
        #os.system("tempsecoule.vbs")
        os.system("temp.vbs")
        sleep(0.5)
        print("Number of pop-ups open: {} pop_ups".format(z))
        z+=1
        print("Created By Henry Letellier.")
