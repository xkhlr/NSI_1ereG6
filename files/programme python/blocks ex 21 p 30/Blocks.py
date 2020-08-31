from time import sleep
blockmax=int(input("Entrez le nombre de bloc disponible:"))
block=1
level=1
while block<blockmax:
    print("niveau {} : nombre de block {}".format(level,block))
    block+=3
    level+=1
sleep(2)
print("créé par Henry Letellier")
sleep(5)
