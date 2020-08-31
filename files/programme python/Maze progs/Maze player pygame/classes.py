"""Classes du jeu de Labyrinthe Donkey Kong"""

import pygame
from pygame.locals import * 
from constantes import *

class Niveau:
	"""Classe permettant de créer un niveau"""
	def __init__(self, fichier):
		self.fichier = fichier
		self.structure = 0
	
	
	def generer(self):
		"""Méthode permettant de générer le niveau en fonction du fichier.
		On crée une liste générale, contenant une liste par ligne à afficher"""	
		#On ouvre le fichier
		with open(self.fichier, "r") as fichier:
			structure_niveau = []
			#On parcourt les lignes du fichier
			for ligne in fichier:
				ligne_niveau = []
				#On parcourt les sprites (lettres) contenus dans le fichier
				for sprite in ligne:
					#On ignore les "\n" de fin de ligne
					if sprite != '\n':
						#On ajoute le sprite à la liste de la ligne
						ligne_niveau.append(sprite)
				#On ajoute la ligne à la liste du niveau
				structure_niveau.append(ligne_niveau)
			#On sauvegarde cette structure
			self.structure = structure_niveau
	
	
	def afficher(self, fenetre):
		print("""Méthode permettant d'afficher le niveau en fonction 
		de la liste de structure renvoyée par generer()""")
		#Chargement des images (seule celle d'arrivée contient de la transparence)
		mur = pygame.image.load(image_mur).convert()
		mur0 = pygame.image.load(image_mur0).convert_alpha()
		mur1 = pygame.image.load(image_mur1).convert_alpha()
		mur2 = pygame.image.load(image_mur2).convert_alpha()
		mur3 = pygame.image.load(image_mur3).convert_alpha()
		mur4 = pygame.image.load(image_mur4).convert_alpha()
		mur5 = pygame.image.load(image_mur5).convert_alpha()
		mur6 = pygame.image.load(image_mur6).convert_alpha()
		mur7 = pygame.image.load(image_mur7).convert_alpha()
		mur8 = pygame.image.load(image_mur8).convert_alpha()
		mur9 = pygame.image.load(image_mur9).convert_alpha()
		mur10 = pygame.image.load(image_mur10).convert_alpha()
		mur11 = pygame.image.load(image_mur11).convert_alpha()
		mur12 = pygame.image.load(image_mur12).convert_alpha()
		mur13 = pygame.image.load(image_mur13).convert_alpha()
		mur14 = pygame.image.load(image_mur14).convert_alpha()
		mur15 = pygame.image.load(image_mur15).convert_alpha()
		mur16 = pygame.image.load(image_mur16).convert_alpha()
		mur17 = pygame.image.load(image_mur17).convert_alpha()
		mur18 = pygame.image.load(image_mur18).convert_alpha()
		mur19 = pygame.image.load(image_mur19).convert_alpha()
		mur20 = pygame.image.load(image_mur20).convert_alpha()
		mur21 = pygame.image.load(image_mur21).convert_alpha()
		mur22 = pygame.image.load(image_mur22).convert_alpha()
		mur23 = pygame.image.load(image_mur23).convert_alpha()
		mur24 = pygame.image.load(image_mur24).convert_alpha()
		mur25 = pygame.image.load(image_mur25).convert_alpha()
		mur26 = pygame.image.load(image_mur26).convert_alpha()
		mur27 = pygame.image.load(image_mur27).convert_alpha()
		mur28 = pygame.image.load(image_mur28).convert_alpha()
		mur29 = pygame.image.load(image_mur29).convert_alpha()
		mur30 = pygame.image.load(image_mur30).convert_alpha()
		mur31 = pygame.image.load(image_mur31).convert_alpha()
		mur32 = pygame.image.load(image_mur32).convert_alpha()
		mur33 = pygame.image.load(image_mur33).convert_alpha()
		mur34 = pygame.image.load(image_mur34).convert_alpha()
		mur35 = pygame.image.load(image_mur35).convert_alpha()
		mur36 = pygame.image.load(image_mur36).convert_alpha()
		mur37 = pygame.image.load(image_mur37).convert_alpha()
		mur38 = pygame.image.load(image_mur38).convert_alpha()
		mur39 = pygame.image.load(image_mur39).convert_alpha()
		mur40 = pygame.image.load(image_mur40).convert_alpha()
		mur41 = pygame.image.load(image_mur41).convert_alpha()
		mur42 = pygame.image.load(image_mur42).convert_alpha()
		mur43 = pygame.image.load(image_mur43).convert_alpha()
		mur44 = pygame.image.load(image_mur44).convert_alpha()
		mur45 = pygame.image.load(image_mur45).convert_alpha()
		mur46 = pygame.image.load(image_mur46).convert_alpha()
		mur47 = pygame.image.load(image_mur47).convert_alpha()
		mur48 = pygame.image.load(image_mur48).convert_alpha()
		mur49 = pygame.image.load(image_mur49).convert_alpha()
		mur50 = pygame.image.load(image_mur50).convert_alpha()
		mur51 = pygame.image.load(image_mur51).convert_alpha()
		mur52 = pygame.image.load(image_mur52).convert_alpha()
		mur53 = pygame.image.load(image_mur53).convert_alpha()
		mur54 = pygame.image.load(image_mur54).convert_alpha()
		mur55 = pygame.image.load(image_mur55).convert_alpha()
		mur56 = pygame.image.load(image_mur56).convert_alpha()
		mur57 = pygame.image.load(image_mur57).convert_alpha()
		mur58 = pygame.image.load(image_mur58).convert_alpha()
		mur59 = pygame.image.load(image_mur59).convert_alpha()
		mur60 = pygame.image.load(image_mur60).convert_alpha()
		mur61 = pygame.image.load(image_mur61).convert_alpha()
		mur62 = pygame.image.load(image_mur62).convert_alpha()
		mur63 = pygame.image.load(image_mur63).convert_alpha()
		mur64 = pygame.image.load(image_mur64).convert_alpha()
		mur65 = pygame.image.load(image_mur65).convert_alpha()
		mur66 = pygame.image.load(image_mur66).convert_alpha()
		mur67 = pygame.image.load(image_mur67).convert_alpha()
		mur68 = pygame.image.load(image_mur68).convert_alpha()
		mur69 = pygame.image.load(image_mur69).convert_alpha()
		mur70 = pygame.image.load(image_mur70).convert_alpha()
		mur71 = pygame.image.load(image_mur71).convert_alpha()
		mur72 = pygame.image.load(image_mur72).convert_alpha()
		mur73 = pygame.image.load(image_mur73).convert_alpha()
		mur74 = pygame.image.load(image_mur74).convert_alpha()
		mur75 = pygame.image.load(image_mur75).convert_alpha()
		mur76 = pygame.image.load(image_mur76).convert_alpha()
		mur77 = pygame.image.load(image_mur77).convert_alpha()
		mur78 = pygame.image.load(image_mur78).convert_alpha()
		mur79 = pygame.image.load(image_mur79).convert_alpha()
		mur80 = pygame.image.load(image_mur80).convert_alpha()
		mur81 = pygame.image.load(image_mur81).convert_alpha()
		mur82 = pygame.image.load(image_mur82).convert_alpha()
		mur83 = pygame.image.load(image_mur83).convert_alpha()
		mur84 = pygame.image.load(image_mur84).convert_alpha()
		mur85 = pygame.image.load(image_mur85).convert_alpha()
		mur86 = pygame.image.load(image_mur86).convert_alpha()
		mur87 = pygame.image.load(image_mur87).convert_alpha()
		mur88 = pygame.image.load(image_mur88).convert_alpha()
		mur89 = pygame.image.load(image_mur89).convert_alpha()
		mur90 = pygame.image.load(image_mur90).convert_alpha()
		mur91 = pygame.image.load(image_mur91).convert_alpha()
		mur92 = pygame.image.load(image_mur92).convert_alpha()
		mur93 = pygame.image.load(image_mur93).convert_alpha()
		mur94 = pygame.image.load(image_mur94).convert_alpha()
		mur95 = pygame.image.load(image_mur95).convert_alpha()
		mur96 = pygame.image.load(image_mur96).convert_alpha()
		mur97 = pygame.image.load(image_mur97).convert_alpha()
		mur98 = pygame.image.load(image_mur98).convert_alpha()
		mur99 = pygame.image.load(image_mur99).convert_alpha()
		mur100 = pygame.image.load(image_mur100).convert_alpha()
		mur101 = pygame.image.load(image_mur101).convert_alpha()
		mur102 = pygame.image.load(image_mur102).convert_alpha()
		mur103 = pygame.image.load(image_mur103).convert_alpha()
		mur104 = pygame.image.load(image_mur104).convert_alpha()
		mur105 = pygame.image.load(image_mur105).convert_alpha()
		mur106 = pygame.image.load(image_mur106).convert_alpha()
		mur107 = pygame.image.load(image_mur107).convert_alpha()
		mur108 = pygame.image.load(image_mur108).convert_alpha()
		mur109 = pygame.image.load(image_mur109).convert_alpha()
		mur110 = pygame.image.load(image_mur110).convert_alpha()
		mur111 = pygame.image.load(image_mur111).convert_alpha()
		mur112 = pygame.image.load(image_mur112).convert_alpha()
		mur113 = pygame.image.load(image_mur113).convert_alpha()
		mur114 = pygame.image.load(image_mur114).convert_alpha()
		mur115 = pygame.image.load(image_mur115).convert_alpha()
		mur116 = pygame.image.load(image_mur116).convert_alpha()
		mur117 = pygame.image.load(image_mur117).convert_alpha()
		mur118 = pygame.image.load(image_mur118).convert_alpha()
		mur119 = pygame.image.load(image_mur119).convert_alpha()
		mur120 = pygame.image.load(image_mur120).convert_alpha()
		mur121 = pygame.image.load(image_mur121).convert_alpha()
		mur122 = pygame.image.load(image_mur122).convert_alpha()
		mur123 = pygame.image.load(image_mur123).convert_alpha()
		mur124 = pygame.image.load(image_mur124).convert_alpha()
		mur125 = pygame.image.load(image_mur125).convert_alpha()
		mur126 = pygame.image.load(image_mur126).convert_alpha()
		mur127 = pygame.image.load(image_mur127).convert_alpha()
		mur128 = pygame.image.load(image_mur128).convert_alpha()
		mur129 = pygame.image.load(image_mur129).convert_alpha()
		mur130 = pygame.image.load(image_mur130).convert_alpha()
		mur131 = pygame.image.load(image_mur131).convert_alpha()
		mur132 = pygame.image.load(image_mur132).convert_alpha()
		mur133 = pygame.image.load(image_mur133).convert_alpha()
		mur134 = pygame.image.load(image_mur134).convert_alpha()
		mur135 = pygame.image.load(image_mur135).convert_alpha()
		mur136 = pygame.image.load(image_mur136).convert_alpha()
		mur137 = pygame.image.load(image_mur137).convert_alpha()
		mur138 = pygame.image.load(image_mur138).convert_alpha()
		mur139 = pygame.image.load(image_mur139).convert_alpha()
		mur140 = pygame.image.load(image_mur140).convert_alpha()
		mur141 = pygame.image.load(image_mur141).convert_alpha()
		mur142 = pygame.image.load(image_mur142).convert_alpha()
		mur143 = pygame.image.load(image_mur143).convert_alpha()
		mur144 = pygame.image.load(image_mur144).convert_alpha()
		mur145 = pygame.image.load(image_mur145).convert_alpha()
		mur146 = pygame.image.load(image_mur146).convert_alpha()
		mur147 = pygame.image.load(image_mur147).convert_alpha()
		mur148 = pygame.image.load(image_mur148).convert_alpha()
		mur149 = pygame.image.load(image_mur149).convert_alpha()
		mur150 = pygame.image.load(image_mur150).convert_alpha()
		mur151 = pygame.image.load(image_mur151).convert_alpha()
		mur152 = pygame.image.load(image_mur152).convert_alpha()
		mur153 = pygame.image.load(image_mur153).convert_alpha()
		mur154 = pygame.image.load(image_mur154).convert_alpha()
		depart = pygame.image.load(image_depart).convert_alpha()
		arrivee = pygame.image.load(image_arrivee).convert_alpha()
		
		#On parcourt la liste du niveau
		num_ligne = 0
		for ligne in self.structure:
			#On parcourt les listes de lignes
			num_case = 0
			for sprite in ligne:
				#On calcule la position réelle en pixels
				x = num_case * taille_sprite
				y = num_ligne * taille_sprite
				if sprite == 'm':		   #m = Mur
					fenetre.blit(mur, (x,y))
				elif sprite == '0':		   #m = Mur
					fenetre.blit(mur0, (x,y))
				elif sprite == '1':		   #1
					fenetre.blit(mur1, (x,y))
				elif sprite == '@':		   #@
					fenetre.blit(mur2, (x,y))
				elif sprite == 'M':		   #M
					fenetre.blit(mur3, (x,y))
				elif sprite == '$':		   #$
					fenetre.blit(mur4, (x,y))
				elif sprite == '£':		   #£
					fenetre.blit(mur5, (x,y))
				elif sprite == '2':		   #∆
					fenetre.blit(mur6, (x,y))
				elif sprite == 'N':		   #N
					fenetre.blit(mur7, (x,y))
				elif sprite == '€':		   #€
					fenetre.blit(mur8, (x,y))
				elif sprite == '3':		   #|
					fenetre.blit(mur9, (x,y))
				elif sprite == '4':		   #-
					fenetre.blit(mur10, (x,y))
				elif sprite == 'A':		   #A
					fenetre.blit(mur11, (x,y))
				elif sprite == 'B':		   #B
					fenetre.blit(mur12, (x,y))
				elif sprite == 'C':		   #C
					fenetre.blit(mur13, (x,y))
				elif sprite == 'D':		   #D
					fenetre.blit(mur14, (x,y))
				elif sprite == 'E':		   #E
					fenetre.blit(mur15, (x,y))
				elif sprite == 'F':		   #F
					fenetre.blit(mur16, (x,y))
				elif sprite == 'G':		   #G
					fenetre.blit(mur17, (x,y))
				elif sprite == 'H':		   #H
					fenetre.blit(mur18, (x,y))
				elif sprite == 'I':		   #I
					fenetre.blit(mur19, (x,y))
				elif sprite == 'J':		   #J
					fenetre.blit(mur20, (x,y))
				elif sprite == 'K':		   #K
					fenetre.blit(mur21, (x,y))
				elif sprite == 'L':		   #L
					fenetre.blit(mur22, (x,y))
				elif sprite == 'O':		   #O
					fenetre.blit(mur23, (x,y))
				elif sprite == 'P':		   #P
					fenetre.blit(mur24, (x,y))
				elif sprite == 'Q':		   #Q
					fenetre.blit(mur25, (x,y))
				elif sprite == 'R':		   #R
					fenetre.blit(mur26, (x,y))
				elif sprite == 'S':		   #S
					fenetre.blit(mur27, (x,y))
				elif sprite == 'T':		   #T
					fenetre.blit(mur28, (x,y))
				elif sprite == 'U':		   #U
					fenetre.blit(mur29, (x,y))
				elif sprite == 'V':		   #V
					fenetre.blit(mur30, (x,y))
				elif sprite == 'W':		   #W
					fenetre.blit(mur31, (x,y))
				elif sprite == 'X':		   #X
					fenetre.blit(mur32, (x,y))
				elif sprite == 'Y':		   #Y
					fenetre.blit(mur33, (x,y))
				elif sprite == 'Z':		   #Z
					fenetre.blit(mur34, (x,y))
				elif sprite == 'a':		   #a
					fenetre.blit(mur35, (x,y))
				elif sprite == 'b':		   #b
					fenetre.blit(mur36, (x,y))
				elif sprite == 'c':		   #c
					fenetre.blit(mur37, (x,y))
				elif sprite == 'd':		   #d
					fenetre.blit(mur38, (x,y))
				elif sprite == 'e':		   #e
					fenetre.blit(mur39, (x,y))
				elif sprite == 'f':		   #f
					fenetre.blit(mur40, (x,y))
				elif sprite == 'g':		   #g
					fenetre.blit(mur41, (x,y))
				elif sprite == 'h':		   #h
					fenetre.blit(mur42, (x,y))
				elif sprite == 'i':		   #i
					fenetre.blit(mur43, (x,y))
				elif sprite == 'j':		   #j
					fenetre.blit(mur44, (x,y))
				elif sprite == 'k':		   #k
					fenetre.blit(mur45, (x,y))
				elif sprite == 'l':		   #l
					fenetre.blit(mur46, (x,y))
				elif sprite == 'm':		   #m
					fenetre.blit(mur47, (x,y))
				elif sprite == 'n':		   #n
					fenetre.blit(mur48, (x,y))
				elif sprite == 'o':		   #o
					fenetre.blit(mur49, (x,y))
				elif sprite == 'p':		   #p
					fenetre.blit(mur50, (x,y))
				elif sprite == 'q':		   #q
					fenetre.blit(mur51, (x,y))
				elif sprite == 'r':		   #r
					fenetre.blit(mur52, (x,y))
				elif sprite == 's':		   #s
					fenetre.blit(mur53, (x,y))
				elif sprite == 't':		   #t
					fenetre.blit(mur54, (x,y))
				elif sprite == 'u':		   #u
					fenetre.blit(mur55, (x,y))
				elif sprite == 'v':		   #v
					fenetre.blit(mur56, (x,y))
				elif sprite == 'w':		   #w
					fenetre.blit(mur57, (x,y))
				elif sprite == 'x':		   #x
					fenetre.blit(mur58, (x,y))
				elif sprite == 'y':		   #y
					fenetre.blit(mur59, (x,y))
				elif sprite == 'z':		   #z
					fenetre.blit(mur60, (x,y))
				elif sprite == '~':		   #~
					fenetre.blit(mur61, (x,y))
				elif sprite == '4':		   #(
					fenetre.blit(mur62, (x,y))
				elif sprite == '5':		   #)
					fenetre.blit(mur63, (x,y))
				elif sprite == '-':		   #-
					fenetre.blit(mur64, (x,y))
				elif sprite == '&':		   #&
					fenetre.blit(mur65, (x,y))
				elif sprite == '²':		   #²
					fenetre.blit(mur66, (x,y))
				elif sprite == '*':		   #*
					fenetre.blit(mur67, (x,y))
				elif sprite == 'µ':		   #µ
					fenetre.blit(mur68, (x,y))
				elif sprite == 'ù':		   #ù
					fenetre.blit(mur69, (x,y))
				elif sprite == '%':		   #%
					fenetre.blit(mur70, (x,y))
				elif sprite == '!':		   #!
					fenetre.blit(mur71, (x,y))
				elif sprite == '§':		   #§
					fenetre.blit(mur72, (x,y))
				elif sprite == ':':		   #:
					fenetre.blit(mur73, (x,y))
				elif sprite == '?':		   #?
					fenetre.blit(mur74, (x,y))
				elif sprite == '<':		   #<
					fenetre.blit(mur75, (x,y))
				elif sprite == '>':		   #>
					fenetre.blit(mur76, (x,y))
				elif sprite == '^':		   #^
					fenetre.blit(mur77, (x,y))
				elif sprite == '¨':		   #¨
					fenetre.blit(mur78, (x,y))
				elif sprite == '¤':		   #¤
					fenetre.blit(mur79, (x,y))
				elif sprite == '°':		   #°
					fenetre.blit(mur80, (x,y))
				elif sprite == '+':		   #+
					fenetre.blit(mur81, (x,y))
				elif sprite == '5':		   #≤
					fenetre.blit(mur82, (x,y))
				elif sprite == '6':		   #≥
					fenetre.blit(mur83, (x,y))
				elif sprite == '7':		   #∓
					fenetre.blit(mur84, (x,y))
				elif sprite == '∞':		   #∞
					fenetre.blit(mur85, (x,y))
				elif sprite == '±':		   #±
					fenetre.blit(mur86, (x,y))
				elif sprite == '≠':		   #≠
					fenetre.blit(mur87, (x,y))
				elif sprite == '∝':		   #∝
					fenetre.blit(mur88, (x,y))
				elif sprite == '∀':		   #∀
					fenetre.blit(mur89, (x,y))
				elif sprite == '≡':		   #≡
					fenetre.blit(mur90, (x,y))
				elif sprite == '≪':		   #≪
					fenetre.blit(mur91, (x,y))
				elif sprite == '≫':		   #≫
					fenetre.blit(mur92, (x,y))
				elif sprite == '≅':		   #≅
					fenetre.blit(mur93, (x,y))
				elif sprite == '≈':		   #≈
					fenetre.blit(mur94, (x,y))
				elif sprite == '℉':		   #℉
					fenetre.blit(mur95, (x,y))
				elif sprite == '℃':		   #℃
					fenetre.blit(mur96, (x,y))
				elif sprite == '∇':		   #∇
					fenetre.blit(mur97, (x,y))
				elif sprite == '√':		   #√
					fenetre.blit(mur98, (x,y))
				elif sprite == '←':		   #←
					fenetre.blit(mur99, (x,y))
				elif sprite == '↑':		   #↑
					fenetre.blit(mur100, (x,y))
				elif sprite == '→':		   #→
					fenetre.blit(mur101, (x,y))
				elif sprite == '↓':		   #↓
					fenetre.blit(mur102, (x,y))
				elif sprite == '⋮':		   #⋮
					fenetre.blit(mur103, (x,y))
				elif sprite == '⋯':		   #⋯
					fenetre.blit(mur104, (x,y))
				elif sprite == '⋰':		   #⋰
					fenetre.blit(mur105, (x,y))
				elif sprite == '⋱':		   #⋱
					fenetre.blit(mur106, (x,y))
				elif sprite == '∎':		   #∎
					fenetre.blit(mur107, (x,y))
				elif sprite == '∅':		   #∅
					fenetre.blit(mur108, (x,y))
				elif sprite == '∑':		   #∑
					fenetre.blit(mur109, (x,y))
				elif sprite == '⋈':		   #⋈
					fenetre.blit(mur110, (x,y))
				elif sprite == '⨀':		   #⨀
					fenetre.blit(mur111, (x,y))
				elif sprite == '⨂':		   #⨂
					fenetre.blit(mur112, (x,y))
				elif sprite == '⨁':		   #⨁
					fenetre.blit(mur113, (x,y))
				elif sprite == '⨄':		   #⨄
					fenetre.blit(mur114, (x,y))
				elif sprite == '⨃':		   #⨃
					fenetre.blit(mur115, (x,y))
				elif sprite == '∔':		   #∔
					fenetre.blit(mur116, (x,y))
				elif sprite == '∸':		   #∸
					fenetre.blit(mur117, (x,y))
				elif sprite == '⋒':		   #⋒
					fenetre.blit(mur118, (x,y))
				elif sprite == '⋓':		   #⋓
					fenetre.blit(mur119, (x,y))
				elif sprite == '⊟':		   #⊟
					fenetre.blit(mur120, (x,y))
				elif sprite == '⊠':		   #⊠
					fenetre.blit(mur121, (x,y))
				elif sprite == '⊡':		   #⊡
					fenetre.blit(mur122, (x,y))
				elif sprite == '⊞':		   #⊞
					fenetre.blit(mur123, (x,y))
				elif sprite == '⋉':		   #⋉
					fenetre.blit(mur124, (x,y))
				elif sprite == '⋊':		   #⋊
					fenetre.blit(mur125, (x,y))
				elif sprite == '⋇':		   #⋇
					fenetre.blit(mur126, (x,y))
				elif sprite == '⊝':		   #⊝
					fenetre.blit(mur127, (x,y))
				elif sprite == '⊕':		   #⊕
					fenetre.blit(mur128, (x,y))
				elif sprite == '⊖':		   #⊖
					fenetre.blit(mur129, (x,y))
				elif sprite == '⊗':		   #⊗
					fenetre.blit(mur130, (x,y))
				elif sprite == '⊘':		   #⊘
					fenetre.blit(mur131, (x,y))
				elif sprite == '⊙':		   #⊙
					fenetre.blit(mur132, (x,y))
				elif sprite == '⊛':		   #⊛
					fenetre.blit(mur133, (x,y))
				elif sprite == '⊚':		   #⊚
					fenetre.blit(mur134, (x,y))
				elif sprite == '†':		   #†
					fenetre.blit(mur135, (x,y))
				elif sprite == '‡':		   #‡
					fenetre.blit(mur136, (x,y))
				elif sprite == '⨂':		   #⨂
					fenetre.blit(mur137, (x,y))
				elif sprite == '△':		   #△
					fenetre.blit(mur138, (x,y))
				elif sprite == '⋘':		   #⋘
					fenetre.blit(mur139, (x,y))
				elif sprite == '⋙':		   #⋙
					fenetre.blit(mur140, (x,y))
				elif sprite == '≦':		   #≦
					fenetre.blit(mur141, (x,y))
				elif sprite == '≧':		   #≧
					fenetre.blit(mur142, (x,y))
				elif sprite == '⋖':		   #⋖
					fenetre.blit(mur143, (x,y))
				elif sprite == '⋗':		   #⋗
					fenetre.blit(mur144, (x,y))
				elif sprite == '≑':		   #≑
					fenetre.blit(mur145, (x,y))
				elif sprite == '≒':		   #≒
					fenetre.blit(mur146, (x,y))
				elif sprite == '≓':		   #≓
					fenetre.blit(mur147, (x,y))
				elif sprite == '⊲':		   #⊲
					fenetre.blit(mur148, (x,y))
				elif sprite == '⊳':		   #⊳
					fenetre.blit(mur149, (x,y))
				elif sprite == '⊴':		   #⊴
					fenetre.blit(mur150, (x,y))
				elif sprite == '⊵':		   #⊵
					fenetre.blit(mur151, (x,y))
				elif sprite == '⋐':		   #⋐
					fenetre.blit(mur152, (x,y))
				elif sprite == '⋑':		   #⋑
					fenetre.blit(mur153, (x,y))
				elif sprite == '❤':		   #❤
					fenetre.blit(mur154, (x,y))
				elif sprite == 'd':		   #d = Départ
					fenetre.blit(depart, (x,y))
				elif sprite == 'a':		   #a = Arrivée
					fenetre.blit(arrivee, (x,y))
				num_case += 1
			num_ligne += 1
			
			
			
			
class Perso:
	"""Classe permettant de créer un personnage"""
	def __init__(self, droite, gauche, haut, bas, niveau):
		#Sprites du personnage
		self.droite = pygame.image.load(droite).convert_alpha()
		self.gauche = pygame.image.load(gauche).convert_alpha()
		self.haut = pygame.image.load(haut).convert_alpha()
		self.bas = pygame.image.load(bas).convert_alpha()
		#Position du personnage en cases et en pixels
		self.case_x = 0
		self.case_y = 0
		self.x = 0
		self.y = 0
		#Direction par défaut
		self.direction = self.droite
		#Niveau dans lequel le personnage se trouve 
		self.niveau = niveau
	
	
	def deplacer(self, direction):
		"""Methode permettant de déplacer le personnage"""
		
		#Déplacement vers la droite
		if direction == 'droite':
			#Pour ne pas dépasser l'écran
			if self.case_x < (nombre_sprite_cote - 1):
				#On vérifie que la case de destination n'est pas un mur
				if self.niveau.structure[self.case_y][self.case_x+1] != 'm':
					#Déplacement d'une case
					self.case_x += 1
					#Calcul de la position "réelle" en pixel
					self.x = self.case_x * taille_sprite
			#Image dans la bonne direction
			self.direction = self.droite
		
		#Déplacement vers la gauche
		if direction == 'gauche':
			if self.case_x > 0:
				if self.niveau.structure[self.case_y][self.case_x-1] != 'm':
					self.case_x -= 1
					self.x = self.case_x * taille_sprite
				elif self.niveau.structure[self.case_y][self.case_x-1] != '':
    				self.case_x -= 1
					self.x = self.case_x * taille_sprite
			self.direction = self.gauche
		
		#Déplacement vers le haut
		if direction == 'haut':
			if self.case_y > 0:
				if self.niveau.structure[self.case_y-1][self.case_x] != 'm':
					self.case_y -= 1
					self.y = self.case_y * taille_sprite
			self.direction = self.haut
		
		#Déplacement vers le bas
		if direction == 'bas':
			if self.case_y < (nombre_sprite_cote - 1):
				if self.niveau.structure[self.case_y+1][self.case_x] != 'm':
					self.case_y += 1
					self.y = self.case_y * taille_sprite
			self.direction = self.bas
