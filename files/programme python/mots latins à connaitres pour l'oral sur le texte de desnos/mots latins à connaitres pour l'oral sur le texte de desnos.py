print("hi")
from time import sleep
from random import randint
from tkinter import*
#from tkinter.messagebox import*
import turtle as tur
print("hi")

#éléments pour faire une intro
fenetre = Tk()
label = Label(fenetre, text="Les cinques éléments à suivre pour fair une bonne intro:")
label.pack()
value = StringVar() 
bouton1 = Checkbutton(fenetre, text="Qui parle?")
bouton2 = Checkbutton(fenetre, text="A qui?")
bouton3 = Checkbutton(fenetre, text="De quoi?")
bouton4 = Checkbutton(fenetre, text="où?")
bouton5 = Checkbutton(fenetre, text="Comment?")
bouton6 = Checkbutton(fenetre, text="Quand?")
bouton7 = Checkbutton(fenetre, text="Pourquoi?")
bouton8 = Checkbutton(fenetre, text="Dans quel but?")
bouton9 = Checkbutton(fenetre, text="Pour aboutir à quoi?")
bouton10 = Checkbutton(fenetre, text="Qu'en tirer?")
place=[TOP,LEFT,RIGHT]
bouton1.pack(side=place[randint(0,2)])
bouton2.pack(side=place[randint(0,2)])
bouton3.pack(side=place[randint(0,2)])
bouton4.pack(side=place[randint(0,2)])
bouton5.pack(side=place[randint(0,2)])
bouton6.pack(side=place[randint(0,2)])
bouton7.pack(side=place[randint(0,2)])
bouton8.pack(side=place[randint(0,2)])
bouton9.pack(side=place[randint(0,2)])
bouton10.pack(side=place[randint(0,2)])
label1= Label(fenetre, text="                                ")
label1.pack()
bouton=Button(fenetre, text="Valider", command=fenetre.destroy)
bouton.pack()
fenetre.mainloop()

#FATUM
fenetre = Tk()
label = Label(fenetre, text="FATUM")
label.pack()
value = StringVar() 
value.set("Traduction de FATUM:")
entree = Entry(fenetre, textvariable=string, width=30)
bouton=Button(fenetre, text="Valider", command=fenetre.destroy)
entree.pack()
bouton.pack()
fenetre.mainloop()

#CATHARSIS
fenetre = Tk()
label = Label(fenetre, text="FATUM")
label.pack()
value = StringVar() 
value.set("Traduction de FATUM:")
entree = Entry(fenetre, textvariable=string, width=30)
bouton=Button(fenetre, text="Valider", command=fenetre.destroy)
entree.pack()
bouton.pack()
fenetre.mainloop()

#CRISTALISATION
fenetre = Tk()
label = Label(fenetre, text="FATUM")
label.pack()
value = StringVar() 
value.set("Traduction de FATUM:")
entree = Entry(fenetre, textvariable=string, width=30)
bouton=Button(fenetre, text="Valider", command=fenetre.destroy)
entree.pack()
bouton.pack()
fenetre.mainloop()

#Connaitre l'élégance du poème (chant de devil)
fenetre = Tk()
label = Label(fenetre, text="FATUM")
label.pack()
value = StringVar() 
value.set("Traduction de FATUM:")
entree = Entry(fenetre, textvariable=string, width=30)
bouton=Button(fenetre, text="Valider", command=fenetre.destroy)
entree.pack()
bouton.pack()
fenetre.mainloop()
#Les cinques éléments à suivre pour fair une bonne intro:
#    schéma communicatif:
#        Qui parle?
#        A qui?
#    De quoi?
#    où?
#    Comment?
#    Quand?
#
#FATUM=Le destin
#turtle.goto(0,100)
#turtle.circle(200)
#turtle.goto(0,0)
#turtle.
a=100
def circle(a):
    tur.title("CADRAN SOLAIREE OMNES HORARE FUGIUNT ULTIMA NECAT. Toutes les heures fuient la dernière tue")
    tur.penup()
    tur.goto(0,a)
    tur.pendown()
    tur.circle(200)
    tur.penup()
    tur.goto(0,0)
    tur.pendown()
    tur.write("CADRAN SOLAIREE\nOMNES HORARE FUGIUNT\nULTIMA NECAT\nToutes les heures fuient\nla dernière tue")
    tur.forward(2)
    return a
#circle(-100)
e=input("Appuyez sur une touche pour continuer...")
