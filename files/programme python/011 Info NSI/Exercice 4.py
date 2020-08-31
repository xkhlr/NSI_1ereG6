from random import randint
n=int(input("Entrer la valeur maximales à calculer:"))
A=int(input("Entrez A (un nombre inferieur à 20):"))
if A>20:
    A=randint(1,20)
    print("Comme la valeur de A était supérieur à 20 nous lui avons affecté une nouvelle valeur aléatoirement choisie en 1 et 20")
    print("A vaut maintenant {}".format(A))
N=1
S=[]
Sup=[]
inf=[]
while N<n+1:
    U=(1)/(N)
    S.append(int(U))
    print("∑={}, n={}".format(U,N))
    if U>A:
        Sup.append(U)
    else:
        inf.append(U)
    N+=1

#for letter in S:
#    if S[letter]>A:
#        Sup.append(S[letter])
#    else:
#        inf.append(S[letter])

print("Les nombres suppérieur à A ({}) sont:".format(A))
print(Sup)
print("Les nombres inférieurs à A ({}) sont:".format(A))
print(inf)
Pause=input("appuyez sur entré pour continuer")
