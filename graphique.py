import pygame
from labyrinthe import *

from pygame.locals import *

pygame.init()

liste[

def afficheLaby (fenetre, labyrinthe, message = "") :
	myfont = pygame.font.SysFont("monospace",20)
	FDT = myfont.render("Fin du tour", 1, (255,255,0))
	fenetre.blit(FDT, (1650, 975))
	for x in range(labyrinthe.plateau.nbLignes) :
		for y in range(labyrinthe.plateau.nbColonnes):
			carte = labyrinthe.plateau.getVal(y,x)
			i = carte.codeCarte()
			carte = pygame.image.load("images/Carte"+str(i)+".jpeg").convert()
			fenetre.blit(carte,(x*100,y*100))
	pygame.display.flip()


def lancerJeu(labyrinthe) :
	fenetre = pygame.display.set_mode((1800,1024))
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
			coordJC = labyrinthe.getCoordG(labyrinthe.joueurCourant,1)
			if event.type == KEYDOWN and event.key == K_UP :
				if labyrinthe.plateau.getVal(coordJC[1],coordJC[0]).passageNord(labyrinthe.plateau.getVal(coordJC[1]+1,coordJC[0])) :
					labyrinthe.jouerTour("M",coordJC[0] + 1, coordJC[1])
				else : 
					message = "La position n'est pas acessible"
			elif event.type == KEYDOWN and event.key == K_DOWN :
				if labyrinthe.plateau.getVal(coordJC[1],coordJC[0]).passageSud(labyrinthe.plateau.getVal(coordJC[1]-1,coordJC[0])) :
					labyrinthe.jouerTour("M",coordJC[0]-1, coordJC[1])
				else : 
					message = "La position n'est pas acessible"
			elif event.type == KEYDOWN and event.key == K_LEFT :
				if labyrinthe.plateau.getVal(coordJC[1],coordJC[0]).passageOuest(labyrinthe.plateau.getVal(coordJC[1],coordJC[0]+1)) :
					labyrinthe.jouerTour("M",coordJC[0], coordJC[1]-1)
				else : 
					message = "La position n'est pas acessible"
			elif event.type == KEYDOWN and event.key == K_RIGHT :
				if labyrinthe.plateau.getVal(coordJC[1],coordJC[0]).passageEst(labyrinthe.plateau.getVal(coordJC[1]+1,coordJC[0]-1)) :
					labyrinthe.jouerTour("M",coordJC[0], coordJC[1]+1)
				else : 
					message = "La position n'est pas acessible"
			elif event.type == MOUSEBUTTONDOWN and event.button == 1 and event.pos[1] > 975: #clique sur le bouton fin du tour
				changement = 0
		res = finTour(labyrinthe)
		if res == 0 : # le joueur courant à gagné
			continuer = 0
			changement = 0
		elif res == 1 : # le joueur courant à apporter un villageois au temple
			message = "Le joueur %d viens de sacrifier un villageois" % (labyrinthe)
		labyrinthe.changerJoueurCourant()
		afficheLaby(fenetre, labyrinthe)
		labyrinthe.changerJoueurCourant()


# Création du labyrinthe

#~ nbVillageois = int(input("Entrez un nombre de villageois par joueur (5-10) : "))
#~ nbGuerrier = int(input("Entrez un nombre de guerrier par joueur (2-5) : "))
#~ labyrinthe(nbVillageois = nbVillageois, nbGuerriers = nbGuerrier)
labyrinthe = Labyrinthe()
lancerJeu(labyrinthe)
