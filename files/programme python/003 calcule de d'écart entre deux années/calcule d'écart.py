#Exercice 1: Combien d'années révolues y a-t-il entre deux évènements définits?
import datetime
from time import sleep
date=datetime.datetime.now()
lot,cont=0,"o"
f=open("Data_ex1_logique_evenements.txt","a")
f.write("#================================================================================Data=========================================================\nDate:{}/{}/{}\n".format(date.day,date.month,date.year))
while cont=="o" or cont==0 or cont=="O":
    ev1=input("Entrez la date du premier évènement (en année):")
    ev2=input("Entrez la date du deuxième évenement (en année, doit être plus grand que le précédent):")
    check1=str.isnumeric(ev1)
    check2=str.isnumeric(ev2)
    print("check1:{}, check2:{}".format(check1,check2))
    if check1==True:
        if check2==True:
            ev1,ev2=int(ev1),int(ev2)
            temp=ev2-ev1
            if temp>1:an="s."
            elif temp<2 and temp>-2:an="."
            elif temp<-1:an="s."
            print("Le temps écoulé entre le premier évènement et le second évènement est de {} an{}\ncréé par Henry Letellier \u2122, \xae, \xa9".format(temp,an))
            f.write("\n----------------------------------------------------------------Calcule du lot n°{}----------------------------------------------------------------\nLe temps écoulé entre le premier évènement ({}) et le second évènement ({}) est de {} an{}".format(lot,ev1,ev2,temp,an))
        else:print("Merci de rentrer uniquement le chiffre de l'année de votre second évènement.\nVous avez rentré(e): '{}'".format(ev2))
    else:print("Merci de rentrer uniquement le chiffre de l'année de votre premier évènement.\nVous avez rentré(e): '{}'".format(ev1))
    sleep(5)
    contt=input("Voulez-vous calculer un nouvel évènement? [(o)ui/(n)on]:")
    if contt=="o" or contt=="O" or contt==0:cont,lot="o",lot+1
    elif contt=="N" or contt=="n":cont="n"
    else:
        print("Assurez-vous d'avoir entré la lettre 'n' pour non ou la lettre 'o' pour oui.\nVous avez entré: {}".format(contt))
        continue
f.write("\ncréé par Henry Letellier \u2122, \xae, \xa9\n#==============================================================================fin Data=======================================================\n")
print("Au revoir")
print("Vous avez utilisé(e) {} fois l'application.".format(lot))
sleep(4)
