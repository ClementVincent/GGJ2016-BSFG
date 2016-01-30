from joueurs import *
from matrice import *
from cartes import *
from inondation import *
import random

class Labyrinthe (object) :
	
	def __init__(self, nbVillageois = 10, nbGuerriers = 5, paInit = 2, pmInit= 2, paPas = 1, pmPas = 1) :
		self.joueurs = []
		self.lsType = ["croissement", "coins", "droit"]
		for i in range(1,3):
			self.joueurs.append(Joueur(i,nbVillageois, nbGuerriers, paInit, pmInit))
		self.plateau = Matrice()
		self.joueurCourant = random.randint(0,1)
		self.dicoCarte = self.creerDicoCarte()
		self.placeCarte()
		carteCourant = self.tireCarteAlea()
	
	def placeCarte (self) :
		for i in range(self.plateau.nbLignes) :
			for j in range(self.plateau.nbColonnes) :
				if j != 9 or i != 9 :
					self.plateau.setVal(j,i,self.tireCarteAlea())
		self.plateau.setVal(9,9,Carte(False,False,False,False))
		
	
	def creerDicoCarte (self):
		dicoCarte = { "croissement" : [], "droit" : [], "coins" :  []}
		for i in range(200) :
			dicoCarte["croissement"].append(Carte(True,True,True,False))
		for i in range(150) :
			dicoCarte["coins"].append(Carte(True,True,False,False))
		for i in range(56) :
			dicoCarte["droit"].append(Carte(True,False,True,False))
		return dicoCarte
	
	def tireCarteAlea (self) :
		for elem in self.lsType : 
			if self.dicoCarte[elem] == [] :
				self.lsType.remove(elem)
		for elem in self.dicoCarte :
			if elem not in self.lsType and self.dicoCarte[elem] != [] :
				self.lsType.append(elem)
		typeCarte = random.choice(self.lsType)
		carte = self.dicoCarte[typeCarte][0]
		self.dicoCarte[typeCarte].pop(0)
		carte.tournerRandom()
		return carte
	
	def changerJoueurCourant (self) :
		self.joueurCourant = (self.joueurCourant + 1) % 2 
	
	def piocherCarte (self) :
		nvCarte = self.tireCarteAlea()
		ancienneCarte = self.prendreCarte()
		self.poserCarte(nvCarte)
		self.mettreCarteDico(ancienneCarte)
	
	def testActionPossible (self) :
		return self.getJoueurCourant.getNbPa() != 0
	
	def getCoordG (self,numJoueur,numGuer) :
		plateau=self.plateau
		for ligne in range(plateau.nbLignes) :
			for colonne in range(plateau.nbColonnes) :
				if (numJoueur,numGuer) in plateau.getVal(ligne,colonne).guerriers :
					return (ligne,colonne)
	

	#fonction prennant le guerrier numGuerrier du joueur numJoueur sur le Lab et retournant le guerrier 
	def getGuerrierL(self,numJoueur,numGuerrier):
		coordG=self.getCoordG(numJoueur,numGuerrier)


	# ordre < M + tuple > id guerrier + direction de déplacement
	def jouerTours (self,ordre) :
		pass
		
		#numG2 est le numéro du guerrier attaqué, il va perdre dommages% de point de vie en moins, si jamais il arrive a 0% de hp il meurt et son villageois est libéré
	def fight(self,numG2,dommages=10):
		self.joueurs[self.joueurCourant].guerriers[numG2].vie-=dommages
		if self.joueurs[self.joueurCourant].guerriers[numG2].vie<=0:

			self.joueurs[self.joueurCourant].retirerGuerrier(numG2)




plateau = Labyrinthe()

