def factorielle(n):
    i=0
    fact=1
    while i<n:
        i=i+1
        fact=fact*i
    print(fact)

print("Factorielle(4)")
factorielle(4)
print("Factorielle(24)")
factorielle(24)

def f(L,m):
    R = []
    for i in range(len(L)):
        if L[i] > m:
            R.append(L[i])
    return R
L = [1, 7, 3, 4, 8, 2, 0, 3, 5]
print("f(L,4)")
print(f(L,4))

def minimum(L):
    mini = 0
    for e in L:
        if e < mini:
            mini = e
    return mini
print("[-1,-8,12,2,23]")
print(minimum([-1,-8,12,2,23]))
print("[0,18,12,2,3]")
print(minimum([0,18,12,2,3]))
print("[-1,-1,12,12,23]")
print(minimum([-1,-1,12,12,23]))
print("[1,8,12,2,23]")
print(minimum([1,8,12,2,23]))

print("if i > iMax:")
liste = [5,12,15,3,15,17,29,1]
iMax = 0
for i in range(1,len(liste)):
    if i > iMax:
        iMax = i

print (liste[iMax])

print("if liste[i] > liste[iMax]:")
liste = [5,12,15,3,15,17,29,1]
iMax = 0
for i in range(1,len(liste)):
    if liste[i] > liste[iMax]:
        iMax = i

print (liste[iMax])

print("if liste[i] > iMax:")

liste = [5,12,15,3,15,17,29,1]
iMax = 0
for i in range(1,len(liste)):
    if liste[i] > iMax:
        iMax = i

print (liste[iMax])

print("if i > liste[iMax]:")
liste = [5,12,15,3,15,17,29,1]
iMax = 0
for i in range(1,len(liste)):
    if i > liste[iMax]:
        iMax = i

print (liste[iMax])


L = [1,2,3,4,1,2,3,4,0,2]

element = L[0]
for k in L:
    if k > element:
        element = k
    print(element)
