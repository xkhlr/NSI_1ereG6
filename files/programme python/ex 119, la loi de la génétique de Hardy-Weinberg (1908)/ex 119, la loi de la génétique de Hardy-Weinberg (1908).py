from time import sleep
import os, datetime
date=datetime.datetime.now()
DATE="{}/{}/{}".format(date.day,date.month,date.year)
try:
    fi=open("ex_119,_la_loi_de_la_génétique_de_Hardy-Weinberg_(1908).txt","r")
    s=fi.read()
    print(chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E)+"      Affichage du cache     "+chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C))
    print(s)
    print(chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E)+" Fin de l'affichage du cache "+chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C))
    fi.close()
    print(os.getcwd())
except:
    print("Fichier non existant")
nbtours=0
P0=1/4
Q0=1/2
R0=1/4
P=1/2
Q=1/2
R=1/4
print("Créé par Henry Letellier {} {} {}".format(chr(169),chr(0xA9),chr(0xAE)))
P=1/2
Q=1/2
R=1/4
G=0
print(chr(0xBB), chr(0xBB), chr(0xBB), chr(0xBB), chr(0xBB), chr(0xBB), chr(0xBB), chr(0xBB), chr(0xBB), chr(0xBB), chr(0xBB), chr(0xBB), chr(0xBB), chr(0xBB), chr(0xBB), chr(0xBB), chr(0xBB), chr(0xBB), chr(0xBB), chr(0xBB), chr(0xBB), chr(0xBB))
print(chr(0xAB), chr(0xAB), chr(0xAB), chr(0xAB), chr(0xAB), chr(0xAB), chr(0xAB), chr(0xAB), chr(0xAB), chr(0xAB), chr(0xAB), chr(0xAB), chr(0xAB), chr(0xAB), chr(0xAB), chr(0xAB), chr(0xAB), chr(0xAB), chr(0xAB), chr(0xAB), chr(0xAB), chr(0xAB))
print(chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E))
print(chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C))
file=open("ex_119,_la_loi_de_la_génétique_de_Hardy-Weinberg_(1908).txt", "a")
file.write("########### Début du log du {} ######################\n{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{} Chemin d'accès:{} {}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}\n".format(DATE,chr(0xBB),chr(0xBB),chr(0xBB),chr(0xBB),chr(0xBB),chr(0xBB),chr(0xBB),chr(0xBB),chr(0xBB),chr(0xBB),chr(0xBB),chr(0xBB),chr(0xBB),chr(0xBB),chr(0xBB),chr(0xBB),chr(0xBB),chr(0xBB),chr(0xBB),chr(0xBB),chr(0xBB),chr(0xBB),os.getcwd(),chr(0xAB),chr(0xAB),chr(0xAB),chr(0xAB),chr(0xAB),chr(0xAB),chr(0xAB),chr(0xAB),chr(0xAB),chr(0xAB),chr(0xAB),chr(0xAB),chr(0xAB),chr(0xAB),chr(0xAB),chr(0xAB),chr(0xAB),chr(0xAB),chr(0xAB),chr(0xAB),chr(0xAB),chr(0xAB)))
file.write("{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{} donées de départ {}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}\n".format(chr(0x3E), chr(0x3E), chr(0x3E),chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E),chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C)))
file.write("nbtours={}\nP0={}\nQ0={}\nR0={}\n".format(nbtours,P0,Q0,R0))
file.write("P={}\nQ={}\nR={}\nG={}\n".format(P,Q,R,G))
file.write("{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{} fin des donées de départ {}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}\n".format(chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E), chr(0x3E),chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C), chr(0x3C)))
file.close()
CG=input("Entrez le nombre de générations à calculer: [de 0 à n]")
print ("1/2={} ,   1/3={},   1/4={},   1/5={},   1/6={},   1/7={}, 1/8={}, 1/9={}, 1/10={}".format(1/2,1/3,1/4,1/5,1/6,1/7,1/8,1/9,1/10))
float(G)
P=input("Entrez P0: [de 0 à n, il n'est pas possible de mettre des fractions, valeur par défaut 1/4 (laisser cette question vide pour la prendre)]")
Q=input("Entrez Q0: [de 0 à n, il n'est pas possible de mettre des fractions, valeur par défaut 1/2 (laisser cette question vide pour la prendre)]")
R=input("Entrez R0: [de 0 à n, il n'est pas possible de mettre des fractions, valeur par défaut 1/4 (laisser cette question vide pour la prendre)]")
file=open("ex_119,_la_loi_de_la_génétique_de_Hardy-Weinberg_(1908).txt", "a")
file.write("=========== Donées saisies par l'utilisateur ======================\n")
file.write("CG={}\nP={}\nQ={}\nR={}\n".format(CG,P,Q,R))
file.write("=========== Fin des donées saisies par l'utilisateur ======================\n")
file.close()
if CG=="n" or CG=="N" or CG=="" or CG==" ":
   CG=-1
else:
    try:
        int(R)
    except:
        if R=="":
            R=1/4
        float(R)
        print(False)
    try:
        int(Q)
    except:
        if Q=="":
            Q=1/2
        float(Q)
        print(False)
    try:
        int(P)
    except:
        if P=="":
            P=1/4
        float(P)
        print(False)
    float(CG)
    file=open("ex_119,_la_loi_de_la_génétique_de_Hardy-Weinberg_(1908).txt", "a")
    file.write("=========== Donées finale, après avoir été traité par le programme de vérification ======================\n")
    file.write("CG={}\nP={}\nQ={}\nR={}\n".format(CG,P,Q,R))
    file.write("=========== Fin donées finale, après avoir été traité par le programme de vérification ======================\n")
    file.close()
    while float(G)<float(CG):
        file=open("ex_119,_la_loi_de_la_génétique_de_Hardy-Weinberg_(1908).txt", "a")
        file.write("=========== Données du tour n°{} ======================\n".format(nbtours+1))
        file.write("P{}={}\nQ{}={}\nR{}={}\n".format(G,P,G,Q,G,R))
        file.close()
        print("P{}={}\nQ{}={}\nR{}={}\n".format(G,P,G,Q,G,R))
        G+=1
        P1=(float(P)+(float(Q)/2))**2
        R1=(float(R)+(float(Q)/2))**2
        Q1=1-(float(P1)+float(R1))
        print("P{}=({}+({}/2))**2={}\nR{}=({}+({}/2))**2={}\nQ{}=1-({}+{})={}\n".format(G,P,Q,P1,G,R,Q,R1,G,P1,R1,Q1))
        file=open("ex_119,_la_loi_de_la_génétique_de_Hardy-Weinberg_(1908).txt", "a")
        file.write("P{}=({}+({}/2))**2={}\nR{}=({}+({}/2))**2={}\nQ{}=1-({}+{})={}\n".format(G,P,Q,P1,G,R,Q,R1,G,P1,R1,Q1))
        P,Q,R=P1,Q1,R1
        file.write("P{}={}\nR{}={}\nQ{}={}\n".format(G,P,G,R,G,Q))
        file.write("=========== Fin donées du tour n°{} ======================\n".format(nbtours+1))
        print("P{}={}\nR{}={}\nQ{}={}\n".format(G,P,G,R,G,Q))
        file.write("Créé par Henry Letellier {} {} {}\n".format(chr(169),chr(0xA9),chr(0xAE)))
        file.close()
        nbtours+=1
        sleep(1)
if CG==-1:
    try:
        int(R)
    except:
        if R=="":
            R=1/4
        float(R)
        print(False)
    try:
        int(Q)
    except:
        if Q=="":
            Q=1/2
        float(Q)
        print(False)
    try:
        int(P)
    except:
        if P=="":
            P=1/4
        float(P)
        print(False)
    float(CG)
    file=open("ex_119,_la_loi_de_la_génétique_de_Hardy-Weinberg_(1908).txt", "a")
    file.write("=========== Donées finale, après avoir été traité par le programme de vérification ======================\n")
    file.write("nbtours={}\nCG={}\nP={}\nQ={}\nR={}\n".format(nbtours,CG,P,Q,R))
    file.write("=========== Fin donées finale, après avoir été traité par le programme de vérification ======================\n")
    file.close()
    while CG==-1:
        file=open("ex_119,_la_loi_de_la_génétique_de_Hardy-Weinberg_(1908).txt", "a")
        file.write("=========== Données du tour n°{} ======================\n".format(nbtours))
        file.write("nbtours={}\nCG={}\nP{}={}\nQ{}={}\nR{}={}\n".format(nbtours,CG,nbtours,P,nbtours,Q,nbtours,R))
        file.close()
        print("P{}={}\nQ{}={}\nR{}={}\n".format(nbtours,P,nbtours,Q,nbtours,R))
        print("P{}=({}+({}/2))**2=\nR{}=({}+({}/2))**2=\nQ{}=1-({}+{})={}\n".format(nbtours,P,Q,(P+(Q/2))**2,nbtours,R,Q,(R+(Q/2))**2,nbtours,P,R,1-(((P+(Q/2))**2)+((R+(Q/2))**2))))
        P1=(float(P)+(float(Q)/2))**2
        R1=(float(R)+(float(Q)/2))**2
        Q1=1-(float(P1)+float(R1))
        print("P{}={}\nQ{}={}\nR{}={}\n".format(nbtours,P,nbtours,Q,nbtours,R))
        file=open("ex_119,_la_loi_de_la_génétique_de_Hardy-Weinberg_(1908).txt", "a")
        file.write("P{}=({}+({}/2))**2=\nR{}=({}+({}/2))**2=\nQ{}=1-({}+{})={}\n".format(nbtours,P,Q,P1,nbtours,R,Q,R1,nbtours,P,R,Q1))
        file.write("P{}={}\nQ{}={}\nR{}={}\n".format(nbtours,P,nbtours,Q,nbtours,R))
        file.write("=========== Fin donées du tour n°{} ======================\n".format(nbtours))
        P,R,Q=P1,R1,Q1
        file.write("Créé par Henry Letellier{} {} {}\n".format(chr(169),chr(0xA9),chr(0xAE)))
        file.close()
        nbtours+=1
        sleep(1)
file=open("ex_119,_la_loi_de_la_génétique_de_Hardy-Weinberg_(1908).txt", "a")
file.write("\n{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{} Chemin d'accès: {} {}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}\n########### Fin du log du {} ######################".format(chr(0xBB),chr(0xBB),chr(0xBB),chr(0xBB),chr(0xBB),chr(0xBB),chr(0xBB),chr(0xBB),chr(0xBB),chr(0xBB),chr(0xBB),chr(0xBB),chr(0xBB),chr(0xBB),chr(0xBB),chr(0xBB),chr(0xBB),chr(0xBB),chr(0xBB),chr(0xBB),chr(0xBB),chr(0xBB),os.getcwd(),chr(0xAB),chr(0xAB),chr(0xAB),chr(0xAB),chr(0xAB),chr(0xAB),chr(0xAB),chr(0xAB),chr(0xAB),chr(0xAB),chr(0xAB),chr(0xAB),chr(0xAB),chr(0xAB),chr(0xAB),chr(0xAB),chr(0xAB),chr(0xAB),chr(0xAB),chr(0xAB),chr(0xAB),chr(0xAB),DATE))
file.close()
#Q=1-(P+R)
#P=(P+Q/2)**2
#R=(R+Q/2)**2
