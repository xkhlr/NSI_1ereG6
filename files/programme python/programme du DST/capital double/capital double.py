from time import sleep 
def capital(capital, interet):
    montant=capital
    n=0
    while montant<=2*capital:
        montant=montant+interet
        n+=1
    return n
print("capital(2,3)={}".format(capital(2,3)))
sleep(5)
