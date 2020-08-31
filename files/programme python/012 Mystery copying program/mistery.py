import shutil, os
print("Créé par Henry Letellier")
print(os.getcwd())
try:
    f=open("coucou.txt","r")
    print(f.read())
    f.close()
except:
    f=open("coucou.txt","a")
    f.write("coucou\nCréé par Henry Letellier")
    f.close()
i=0
inc=0
while i==0:
    shutil.copy("coucou.txt","coucou{}.txt".format(inc))
    inc+=1
