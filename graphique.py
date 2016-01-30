import pygame
from labyrinthe import *

from pygame.locals import *

pygame.init()


def afficheLaby (fenetre, labyrinthe) :
	myfont = pygame.font.SysFont("monospace", 15)
	label = myfont.render("BLAAAAAAAAAAAAAA", 1, (255,255,0))
	fenetre.blit(label, (100, 100))
	pygame.display.flip()


def lancerJeu(labyrinthe) :
	fenetre = pygame.display.set_mode((640,480))
	afficheLaby(fenetre,labyrinthe)
	continuer = 1
	changement = 1
	while continuer:
		while changement == 1 :
			changement = 1
			event = pygame.event.wait()
			if event.type == QUIT:
				continuer = 0
				changement = 0
				print("ok")
			if event.type == KEYDOWN and event.key == K_UP :
				labyrinthe.jouerTour("M",labyrinthe.getCoordG()[0] + 1, labyrinthe.getCoordG()[1])
			elif event.type == KEYDOWN and event.key == K_DOWN :
				labyrinthe.jouerTour("M",labyrinthe.getCoordG()[0]-1, labyrinthe.getCoordG()[1])
			elif event.type == KEYDOWN and event.key == K_LEFT :
				labyrinthe.jouerTour("M",labyrinthe.getCoordG()[0], labyrinthe.getCoordG()[1]-1)
			elif event.type == KEYDOWN and event.key == K_RIGHT :
				labyrinthe.jouerTour("M",labyrinthe.getCoordG()[0], labyrinthe.getCoordG()[1]+1)
			#~ elif : #click sur le bouton fin du tour
				#~ changement = 0
			afficheLaby(fenetre, labyrinthe)
		labyrinthe.changerJoueurCourant()

#~ #Ouverture de la fenêtre Pygame
#~ 
#~ fenetre = pygame.display.set_mode((640, 480))
#~ 
#~ 
#~ #Chargement et collage du fond
#~ 
#~ fond = pygame.image.load("background.jpg").convert()
#~ 
#~ fenetre.blit(fond, (0,0))
#~ 
#~ perso = pygame.image.load("perso.png").convert_alpha()
#~ fenetre.blit(perso,(200,300))
#~ 
#~ #Rafraîchissement de l'écran
#~ 
#~ pygame.display.flip()
#~ 
#~ #BOUCLE INFINIE
#~ 
#~ continuer = 1
#~ 
#~ while continuer:
	#~ for event in pygame.event.get():
		#~ if event.type == QUIT:
			#~ continuer = 0
		#~ if event.type == KEYDOWN and event.key == K_UP :
			#~ joueTour()


# Création du labyrinthe

#~ nbVillageois = int(input("Entrez un nombre de villageois par joueur (5-10) : "))
#~ nbGuerrier = int(input("Entrez un nombre de guerrier par joueur (2-5) : "))
#~ labyrinthe(nbVillageois = nbVillageois, nbGuerriers = nbGuerrier)
labyrinthe = Labyrinthe()
lancerJeu(labyrinthe)
