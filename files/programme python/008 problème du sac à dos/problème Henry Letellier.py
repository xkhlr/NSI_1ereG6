To1=1000000000000
Go1=1000000000
Mo1=1000000
Ko1=1000
o1=1
nb_fichier=[]
nb_fichier_mis=0
nb_fichier_not_mis=0
fichiers_mis="\n"
fichiers_not_mis="\n"
space_max=0
pris=0
def pause():
    pause=input("Apuyez sur entrer pour continuer...")
print("""1 Tera octet = 1 000 000 000 000 octets
1 Giga octet = 1 000 000 000 octets
1 Méga octet = 1 000 000 octets
1 Kilo octet = 1 000 octets """)
Taille_libre_cle=input("Quelle est l'espace libre dans votre clé: ")
Choix_taille_nombre=input("Choix entre [(T)aile/(N)ombre] de vidéo: ")
nb_g=nb_fichier_a_trier=int(input("Combien de fichiers avez-vous? "))
for i in range(nb_fichier_a_trier):
    c=dict()
    a=input("Quel est le nom de votre fichier n°{}:".format(i+1))
    b=input("Quel est la taille de votre fichier n°{}:".format(i+1))
    c['nom']='{}'.format(a)
    c['taille']='{}'.format(b)
    c['pris']=0
    nb_fichier.append(c)
print(nb_fichier)
if Choix_taille_nombre=="T" or Choix_taille_nombre=="t":
    while nb_fichier_a_trier>0:
        if nb_fichier[i]['taille'] > Taille_libre_cle:
            nb_fichier[i]['pris']=-1
            #nb_fichier_not_mis+=1
        elif nb_fichier[i]['taille'] == Taille_libre_cle:
            w=nb_fichier[i]['taille']
            Taille_libre_cle-=w
            nb_fichier[i]['pris']=1
        elif nb_fichier[i]['taille'] < Taille_libre_cle:
            pris+=1
            w=nb_fichier[i]['taille']
            Taille_libre_cle-=w
            nb_fichier[i]['pris']=1
        nb_fichier_a_trier-=1
elif Choix_taille_nombre=="N" or Choix_taille_nombre=="n":
    while nb_fichier_a_trier>0:
        if nb_fichier[i]['taille'] > Taille_libre_cle:
            nb_fichier[i]['pris']=-1
            #nb_fichier_not_mis+=1
        elif nb_fichier[i]['taille'] == Taille_libre_cle:
            nb_fichier[i]['pris']=-1
            #nb_fichier_not_mis+=1
        elif nb_fichier[i]['taille'] < Taille_libre_cle:
            w=nb_fichier[i]['taille']
            Taille_libre_cle-=w
            nb_fichier[i]['pris']=1
        nb_fichier_a_trier-=1
print(nb_fichier)
pris=0
for i in range(nb_g):
    if nb_fichier[i]['pris']==1 or nb_fichier[i]['pris']==0:
        z=nb_fichier[i]['nom']
        fichiers_mis.append(z)
        fichiers_mis.append("\n")
        pris+=1
    if nb_fichier[i]['pris']==-1:
        z=nb_fichier[i]['nom']
        fichiers_not_mis+=z
        fichiers_not_mis+="\n"

print("Le nombre total de fichiers qui on pu être pris mis dans la clé sont : {}".format(pris))
print("Les fichiers mis sont: ".format(fichiers_mis))
print("Le nombre total de fichiers qui n'ont pas pu être pris mis dans la clé sont : {}".format(nb_fichier_not_mis))
print("Les fichiers mis sont: ".format(fichiers_not_mis))
pause()
pause()
