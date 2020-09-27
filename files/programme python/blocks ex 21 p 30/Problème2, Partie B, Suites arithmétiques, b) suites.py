import datetime
date=datetime.datetime.now()
DATE="{}_{}_{}".format(date.day,date.month,date.year)
def write(a):
    f=open("Problème2_Partie_B_Suites_arithmétiques_b)_suites_data_{}.txt".format(DATE),"a")
    f.write(a)
    f.close()
def Sn(s,r,i,e):
  while s<=e:
   s+=r
   print("U{}={}+{}={}".format(i,s-r,r,s))
   write("U{}={}+{}={}\n".format(i,s-r,r,s))
   i+=1
Sn(1800,2790,0,590490)
s=int(input("Entrez U0:"))
write("U0={}\n".format(s))
r=int(input("entrez la raison r:"))
write("r={}\n".format(r))
i=0
write("i={}\n".format(i))
e=int(input("Entrez la valeur à atteindre:"))
write("Valeur à atteindre = {}".format(e))
Sn(s,r,i,e)
print("créé par Henry letellier")
Pause=input("Appuyez sur entré pour continuer")
Pause=input("Appuyez sur entré pour continuer")
Pause=input("Appuyez sur entré pour continuer")
Pause=input("Appuyez sur entré pour continuer")
Pause=input("Appuyez sur entré pour continuer")
exit()
