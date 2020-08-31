# def return_main(mazes):
#   os.system("cd ..\..")
#   os.system("color 0A")
#   print(OS)
#   f=open("maze_symbole_legend.txt","w")
#   f.write(mazes)
#   f.close()
#   f=open("maze_symbole_legend.txt","r")
#   print("f={}".format(f))
#   f.read()
#   print("f={}".format(f.read()))
#   f.close()

import pygame, os
from pygame.locals import *

pygame.init()

#définition de la fenêtre
#fenetre = pygame.display.set_mode((640, 480))
fenetre = pygame.display.set_mode((640,480), RESIZABLE)

#définition d'ou se trouve l'image
fond = pygame.image.load("background.jpg").convert()
fenetre.blit(fond, (0,0))

#insertion d'un personnage
perso=pygame.image.load("perso.png").convert_alpha()
fenetre.blit(perso,(200,300))


#afficher l'image dans la fenêtre
pygame.display.flip()


continuer=1
while continuer:
    continuer=int(input())

#continuer = "o"
#i=0

#Boucle infinie
#while continuer=="o":
#    print("worked")
#    if i==1000:
#        continuer="n"
#        break
#    else:i+=1
#    print("i={}".format(i))
#    continue
