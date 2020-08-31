i=0
while i==0:
    annee=int(input("entrez une année:"))
    annneebis4=annee/4
    anneebis100=annee/100
    print("annee={}, annneebis4={}, anneebis100={}".format(annee,annneebis4,anneebis100))
    annneebis4=annneebis4.is_integer()
#print("annneebis4={}, anneebis100={}".format(annneebis4,anneebis100))
#anneebis100=anneebis100.is_integer()
    if annneebis4==True: #and anneebis100==True:
        print("L'année {} est bissextile".format(annee))
    else:
        print("L'année {} n'est pas bissextile".format(annee))

    Pause=input("appuyez sur entrer pour continuer")
