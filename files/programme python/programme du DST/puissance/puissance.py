from time import sleep
def puissance(x,y):
    p=x
    for i in range(y-1):
        p*=x
    return p
sleep(5)
print("puissance(2,0)={}".format(puissance(2,0)))
sleep(2)
print("puissance(2,0)={}".format(puissance(2,0)))
sleep(2)
print("puissance(2,2)={}".format(puissance(2,2)))
sleep(2)
print("puissance(2,10)={}".format(puissance(2,10)))
sleep(2)
