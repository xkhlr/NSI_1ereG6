import math
from time import sleep
print("Question 1)a)")
i=0
UN=0
n=int(input("Entrez le nombre de fois que l'on calculera Un:"))
while i<n+1:
    UN=math.sqrt(3*UN+4)
    print("U{}={}".format(i,UN))
    sleep(1)
    i+=1

print("Question 1)b)")
i=0
UN=0
S=[]
n=int(input("Entrez le nombre de fois que l'on calculera Un:"))
while i<n+1:
    UN=math.sqrt(3*UN+4)
    print("U{}={}".format(i,UN))
    S.append(UN)
    sleep(1)
    i+=1
