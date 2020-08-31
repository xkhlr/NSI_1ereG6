from time import sleep
cont,z,hour,minute,second,s="o","\a",4,60,60,1
minute=second=0
while cont=="o":
    for i in range(hour):
        minute=60
        print(z)
        for ii in range(minute):
            second=60
            print(z)
            for iii in range(second):
                print("Il reste {} heure(s) {} minute, {} secondes".format(hour,minute,second))
                sleep(s)
                second-=1
            minute-=1
        hour-=1

    print(z)
    sleep(0.5)
    print(z)
    sleep(0.5)
    print(z)
    sleep(0.5)
    print(z)
    sleep(0.5)
    print(z)
    sleep(0.5)
    print(z)
    sleep(0.5)
    print(z)
    sleep(0.5)
    print(z)
    sleep(0.5)
    print(z)
    sleep(0.5)
    cont=input("\a Recmmencer le décompt? [(o)ui/(n)on]:")
    if cont=="n" or cont=="N":
        print("Au revoir, créé par Henry letellier")
    elif cont=="o" or cont=="O" or cont==0 or cont=="0":
        cont="o"
        print("et c'est reparti pour un tour")
    else:
        print("assurez-vous d'avoir entré soit 'o' pour oui ou 'n' pour non\n Vous avez entré {}".format(cont))
        cont="o"
