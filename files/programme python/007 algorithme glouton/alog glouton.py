someineur=int(input("Quel est le montant à rendre (en €): "))
someincent=int(input("Quel est le montant à rendre (en centimes): ")) #en html à limiter à 100
monnaiecent=[1,2,5,10,20,50]
monnaieeur=[1,2,5,10,20,100,200,500]
rendu50c=rendu20c=rendu10c=rendu5c=rendu1c=rendu500=rendu200=rendu100=rendu50=rendu20=rendu10=rendu5=rendu2=rendu=0
#888
while someincent>0:
    if someincent>1:
        if someincent>2:
            if someincent>5:
                if someincent>10:
                    if someincent>20:
                        if someincent>50:
                           someincent-=50
                           rendu50c+=1
                    else:
                        someincent-=20
                        rendu20c+=1
                else:
                    someincent-=10
                    rendu10c+=1
            else:
                someincent-=5
                rendu5c+=1
        else:
            someincent-=2
            rendu2c+=1
    else:
        someincent-=1
        rendu1c+=1
                            
else:
    if rendu50c==2:
        rendu50c=0
        rendu+=1
        print("Le calcule des centimes est terminé.")
        someincent=0
    elif someincent==0:
        print("Le calcule des centimes est terminé.")
        print(someincent)
    else:
        print(someincent)


while someineur>0:
    if someineur>1:
        if someineur>2:
            if someineur>5:
                if someineur>10:
                    if someineur>20:
                        if someineur>50:
                            if someineur>100:
                                if someineur>200:
                                    if someineur>500:
                                        someineur-=500
                                        rendu500+=1
                                    else:
                                        someineur-=200
                                        rendu200+=1
                                else:
                                    someineur-100
                                    rendu100+=1
                            else:
                                someineur-=50
                                rendu50+=1
                        else:
                            someineur-=20
                            rendu20+=1
                    else:
                        someineur-=10
                        rendu10+=1
                else:
                    someineur-=5
                    rendu5+=1
            else:
                someineur-=2
                rendu2+=1
        else:
            someineur-=1
            rendu+=1
    elif someineur==0:
        print("calcule des euros terminé")
    else:
        print(someineur)

print("Le Programme vous rendra:")
print("   - {} pièce(s) de 1 euro".format(rendu1))
print("   - {} pièce(s) de 2 euros".format(rendu2))
print("   - {} pièce(s) de 5 euros".format(rendu5))
print("   - {} pièce(s) de 10 euros".format(rendu10))
print("   - {} pièce(s) de 20 euros".format(rendu20))
print("   - {} pièce(s) de 50 euros".format(rendu50))
print("   - {} pièce(s) de 100 euros".format(rendu100))
print("   - {} pièce(s) de 200 euros".format(rendu200))
print("   - {} pièce(s) de 500 euros".format(rendu500))
print(",")
print("   - {} pièce(s) de 1 centime".format(rendu1c))
print("   - {} pièce(s) de 2 centimes".format(rendu2c))
print("   - {} pièce(s) de 5 centimes".format(rendu5c))
print("   - {} pièce(s) de 10 centimes".format(rendu10c))
print("   - {} pièce(s) de 20 centimes".format(rendu20c))
print("   - {} pièce(s) de 50 centimes".format(rendu50c))


