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
position_perso = perso.get_rect()
perso_x=0
perso_y=0
fenetre.blit(perso, (perso_x, perso_y))


#afficher l'image dans la fenêtre
pygame.display.flip()

#rendre le déplacement fluide
pygame.key.set_repeat(400, 30)


continuer=1
while continuer:
    for event in pygame.event.get():   #On parcours la liste de tous les événements reçus
        if event.type == QUIT:     #Si un de ces événements est de type QUIT
            continuer = 0      #On arrête la boucle
        if event.type == MOUSEBUTTONDOWN:
            if event.button == 1:	#Si clic gauche
                #On change les coordonnées du perso
                perso_x = event.pos[0]
                perso_y = event.pos[1]
        if event.type == KEYDOWN:
            if event.key == K_LEFT:
                print("GAUCHE")
                position_perso = position_perso.move(-3,0)
            if event.key == K_UP:
                print("HAUT")
                position_perso = position_perso.move(0,-3)
            if event.key == K_DOWN:
                print("EN BAS")
                position_perso = position_perso.move(0,3)
            if event.key == K_RIGHT:
                print("DROITE")
                position_perso = position_perso.move(3,0)
            if event.key == K_SPACE:
                print("Espace")
            if event.key == K_RETURN:
                print("Entrée")
    #Re-collage
    fenetre.blit(fond, (0,0))	
    fenetre.blit(perso, position_perso)
    #Rafraichissement
    pygame.display.flip()    



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

#https://openclassrooms.com/fr/courses/1399541-interface-graphique-pygame-pour-python/1399995-gestion-des-evenements-1#/id/r-1400798
