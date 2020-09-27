from time import sleep
import datetime
date=datetime.datetime.now()
DATE="{}_{}_{}".format(date.day,date.month,date.year)
def write(a):
    f=open("Blocks_data_{}.txt".format(DATE),"a")
    f.write(a)
    f.close()
blockmax=int(input("Entrez le nombre de bloc disponible:"))
block=1
level=1
while block<blockmax:
    print("niveau {} : nombre de block {}".format(level,block))
    write("niveau {} : nombre de block {}\n".format(level,block))
    block+=3
    level+=1
sleep(2)
print("créé par Henry Letellier")
sleep(5)
