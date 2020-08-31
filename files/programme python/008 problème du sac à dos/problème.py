import random
mAx=9999999999999
To1=1000000000000
Go1=1000000000
Mo1=1000000
Ko1=1000
o1=1
listIn=[]
listOut=[]
nb_fichier=[]
nb_fichier_mis=0
nb_fichier_not_mis=0
fichiers_mis="\n"
fichiers_not_mis="\n"
space_max=0
pris=0
print("""1 Tera octet = 1 000 000 000 000 octets
1 Giga octet = 1 000 000 000 octets
1 Méga octet = 1 000 000 octets
1 Kilo octet = 1 000 octets """)
Taille_libre_cle=input("Quelle est l'espace libre dans votre clé: ")
Choix_taille_nombre=input("Choix entre [(T)aile/(N)ombre] de vidéo: ")
nb_fichier_a_trier=int(input("Combien de fichiers avez-vous? "))
if Taille_libre_cle=="max" or Taille_libre_cle=="Max" or Taille_libre_cle=="MAx" or Taille_libre_cle=="MAX" or Taille_libre_cle=="mAX" or Taille_libre_cle=="mAx" or Taille_libre_cle=="maX":
  Taille_libre_cle=int(mAx)
  Taille_libre_cle=int(Taille_libre_cle)
else:Taille_libre_cle=int(Taille_libre_cle)
nb_g=nb_fichier_a_trier
for i in range(nb_fichier_a_trier):
    c=dict()
    a=input("Quel est le nom de votre fichier n°{}:".format(i+1))
    b=input("Quel est la taille de votre fichier n°{}:".format(i+1))
    if b=="" or b==" ":
      b=random.randint(1,9999999999999)
    c['nom']='{}'.format(a)
    c['taille']='{}'.format(b)
    c['pris']=0
    nb_fichier.append(c)
i=0
print(nb_fichier)
print("Choix_taille_nombre={}, nb_fichier_a_trier={}, Taille_libre_cle={}, i={}".format(Choix_taille_nombre,nb_fichier_a_trier,Taille_libre_cle,i))
if Choix_taille_nombre=="T" or Choix_taille_nombre=="t":
    while nb_fichier_a_trier>0:
        if int(nb_fichier[i]['taille']) < Taille_libre_cle:
            pris+=1
            w=nb_fichier[i]['taille']
            Taille_libre_cle=Taille_libre_cle-int(w)
            nb_fichier[i]['pris']=1
            iin=nb_fichier[i]['nom']
            listIn.append(iin)
            print("<")
            print(w, Taille_libre_cle)
        elif int(nb_fichier[i]['taille']) == Taille_libre_cle:
            w=nb_fichier[i]['taille']
            Taille_libre_cle=Taille_libre_cle-int(w)
            nb_fichier[i]['pris']=1
            iin=nb_fichier[i]['nom']
            listIn.append(iin)
            print("==")
            print(w, Taille_libre_cle)
        elif int(nb_fichier[i]['taille']) > Taille_libre_cle:
            nb_fichier[i]['pris']=-1
            out=nb_fichier[i]['nom']
            listOut.append(out)
            nb_fichier_not_mis+=1
            print(">")
        print("i={}, nb_fichier_a_trier={}, Taille_libre_cle={}".format(i, nb_fichier_a_trier,Taille_libre_cle))
        nb_fichier_a_trier-=1
        i+=1
        print("i={}, nb_fichier_a_trier={}, Taille_libre_cle={}".format(i, nb_fichier_a_trier,Taille_libre_cle))
elif Choix_taille_nombre=="N" or Choix_taille_nombre=="n":
    while nb_fichier_a_trier>0:
        if int(nb_fichier[i]['taille']) < Taille_libre_cle:
            w=nb_fichier[i]['taille']
            Taille_libre_cle=Taille_libre_cle-int(w)
            nb_fichier[i]['pris']=1
            iin=nb_fichier[i]['nom']
            listIn.append(iin)
            print("<")
            print(w, Taille_libre_cle)
        elif int(nb_fichier[i]['taille']) == Taille_libre_cle:
            nb_fichier[i]['pris']=-1
            out=nb_fichier[i]['nom']
            listOut.append(out)
            print("==")
            nb_fichier_not_mis+=1
        elif int(nb_fichier[i]['taille']) > Taille_libre_cle:
            nb_fichier[i]['pris']=-1
            out=nb_fichier[i]['nom']
            listOut.append(out)
            nb_fichier_not_mis+=1
            print(">")
        print("i={}, nb_fichier_a_trier={}, Taille_libre_cle={}".format(i, nb_fichier_a_trier,Taille_libre_cle))
        nb_fichier_a_trier-=1
        i+=1
        print("i={}, nb_fichier_a_trier={}, Taille_libre_cle={}".format(i, nb_fichier_a_trier,Taille_libre_cle))
print("listInt={}, listOut={}".format(listIn,listOut))
print(nb_fichier)
pris=0
for i in range(nb_g):
    if nb_fichier[i]['pris']==1:
        z=nb_fichier[i]['nom']
        fichiers_mis+=z
        fichiers_mis+="\n"
        pris+=1
    if nb_fichier[i]['pris']==-1:
        z=nb_fichier[i]['nom']
        fichiers_not_mis+=z
        fichiers_not_mis+="\n"

print("Le nombre total de fichiers qui on pu être pris mis dans la clé sont : {}".format(pris))
iiin=len(listIn)
oout=len(listOut)
print("Les fichiers mis sont: ")
for letter in range(iiin):
  print("- {}".format(listIn[letter]))
print("Le nombre total de fichiers qui n'ont pas pu être pris mis dans la clé sont : {}".format(nb_fichier_not_mis))
print("Les fichiers mis sont: ")
for i in range(oout):
  print("- {}".format(listOut[i]))
print("Créé par Henry Letllier")
