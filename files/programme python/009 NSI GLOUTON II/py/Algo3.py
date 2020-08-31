# ALGORITHME GLOUTON
# Probleme sac à dos
#
# Algo 3: classement du plus fort au plus faible
# liste_objet est une liste composée de triplets (numero, masse, valeur)
# liste_objet=[(1, masse, valeur),(2, masse, valeur), ...]
# par exemple [(1, 4kg, 8€), 2, 5kg, 10€), (3,8kg, 15€) ...etc]
#
liste_objet=[(1,4,8), (2,5,10), (3,8,15),(4,3,4)]
masse_max=11

liste_triee=sorted(liste_objet, key=lambda objet: objet[2], reverse=True) #tri suivant valeur
print("liste triée:",liste_triee)

masse_totale=0
objet_pris=[] #liste des numéros des objets pris
valeur_totale=0

# on parcours la liste triée et on additionne les masses
# si masse totale <= masse_max

for objet in liste_triee:
    if (masse_totale+objet[1])<=masse_max:
        masse_totale=masse_totale+objet[1]
        objet_pris=objet_pris+[objet[0]]
        valeur_totale=valeur_totale+objet[2]
# objet[0]=numero, objet[1]=masse, objet[2]=valeur, objet[3]=valeur/masse:
# On veut créer (en faisant une boucle for) une liste2 qui intègre le rapport valeur/masse:
# de la forme [(1, masse, valeur, valeur/masse), (2,masse,valeur,valeur/masse),...]
# compléter le code ci-dessous et intégrer le fand votre programme au bon endroit:
liste2=[]
for objet in liste_objet:
    liste2=liste2+[(objet[0],objet[1],objet[2],objet[2]/objet[1])]
liste_triee=sorted(liste2, key=lambda objet: objet[3], reverse=True) #tri suivant valeur/masse

print("Masse totale: ",masse_totale, "kg")
print("Valeur totale: ",valeur_totale, "€")
print("liste des objets pris: ",objet_pris)
print("liste triee: ",liste_triee)
print("liste2 :", liste2)
