repertoire = [ {'nom':'Dupont', 'tel':'5234'}, {'nom':'Tournesol', 'tel':'5248'},{'nom':'Dupond', 'tel':'3452'}]
for i in range(len(repertoire)):
    if repertoire[i] == 'Dupond' :
        print(repertoire[i]['tel'])


for i in range(len(repertoire)):
    if repertoire[i]['nom'] == 'Dupond' :
        print(repertoire[i]['tel'])


a = 10
if a < 5:
    a = 20
elif a < 100:
    a = 500
elif a < 1000:
    a = 1
else:
    a = 0
print(a)

def f(a,b):
    assert b!=0,'le deuxième argument est nul'
    result = a/b

#r=f(4,0)
#print(r)

def f(t):
    n = len(t)
    for k in range(1,n):
        t[k] = t[k] + t[k-1]
#L = [1, 3, 4, 5, 2]
#print(f(L))

def trouverLettre(phrase,lettre):
    indexResultat = 0
    for i in range(len(phrase)):
        if phrase[i]== lettre:
            indexResultat=i
        return indexResultat
c=trouverLettre("Vive l’informatique","e")
print("tourver lettre = {}".format(trouverLettre("Vive l’informatique","e")))
print("c={}".format(c))

def mystere(T):
    k = len(T)
    val = T[k-1]
    if k == 1:
        return T[k-1]
    else:
        while k >= 0:
            if val < T[k-2]:
                val = T[k-2]
                k = k-1
                return val
#def mystere(T):
# k = len(T)
# val = T[k-1]
# if k == 1:
#  print(T[k-1])
# else:
#  while k >= 0:
#   if val < T[k-2]:
#    val = T[k-2]
#    k = k-1
#    print(val)
def mystere(T):
 k = len(T)
 val = T[k-1]
 if k == 1:
  return T[k-1]
 else:
  while k >= 0:
   if val < T[k-2]:
    val = T[k-2]
    k = k-1
    return val

k = len(T)
val = T[k-1]
if k == 1:
 print(T[k-1])
else:
 while k >= 0:
  if val < T[k-2]:
   val = T[k-2]
   k = k-1
   print(val)

#print("mystere(ee)={}".format(mystere(ee)))
#print("mystere(1)={}".format(mystere(1)))
#print("mystere(2)={}".format(mystere(2)))
#print("mystere(3)={}".format(mystere(3)))
#print("mystere(4)={}".format(mystere(4)))
#print("mystere(5)={}".format(mystere(5)))
#print("mystere(6)={}".format(mystere(6)))
#print("mystere(7)={}".format(mystere(7)))
#print("mystere(8)={}".format(mystere(8)))
#print("mystere(9)={}".format(mystere(9)))
#print("mystere(10)={}".format(mystere(10)))
#print("mystere(11)={}".format(mystere(11)))
#print("mystere(12)={}".format(mystere(12)))
#print("mystere(13)={}".format(mystere(13)))
#print("mystere(14)={}".format(mystere(14)))
#print("mystere(15)={}".format(mystere(15)))
#print("mystere(16)={}".format(mystere(16)))
#print("mystere(17)={}".format(mystere(17)))
#print("mystere(18)={}".format(mystere(18)))
#print("mystere(19)={}".format(mystere(19)))
#print("mystere(20)={}".format(mystere(20)))
