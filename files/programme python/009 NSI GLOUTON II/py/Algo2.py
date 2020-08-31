# ALGORITHME GLOUTON
# Probleme sac à dos
#
# Algo 2: classement suivant les masses
# liste_objet est une liste composée de triplets (numero, masse, valeur)
# liste_objet=[(1, masse, valeur),(2, masse, valeur), ...]
# par exemple [(1, 4kg, 8€), 2, 5kg, 10€), (3,8kg, 15€) ...etc]
#
liste_objet=[(1,4,8), (2,5,10), (3,8,15),(4,3,4)]
masse_max=11

# objet[0]=numero, objet[1]=masse, objet[2]=valeur:

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

print("Masse totale: ",masse_totale, "kg")
print("Valeur totale: ",valeur_totale, "€")
print("liste des objets pris: ",objet_pris)
