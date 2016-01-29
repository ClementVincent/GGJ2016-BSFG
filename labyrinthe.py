from joueurs import *
from matrice import *
from carte import *
from inondation import *
from random import *

class Labyrinthe (object) :
	
	def __init__(self, nbVillageoisTot, nbGuerriersTot, paInit = 2, pmInit= 2, paPas = 1, pmPas = 1) :
		self.joueurs = []
		for i in range(1,2):
			self.joueurs.append(Joueurs(i,nbVillageoisTot // 2, nbGuerrierTot // 2, paInit, pmInit))
		self.plateau = Matrice()
		self.joueurCourant = joueurs[random.randint(0,2)]
		self.dicoCarte = self.creerDicoCarte()
		carteCourant = self.tireCarteAlea()
	
	def creerDicoCarte (self):
		dico = { "croissement" : [], "droit" : [], "coins" :  [] }
		for i in range(200) :
			dicoCArte["ceoissement"].append(Carte(True,True,True,False))
		for i in range(150) :
			dicoCArte["coins"].append(Carte(True,True,False,False))
		for i in range(56) :
			dicoCArte["doit"].append(Carte(True,False,True,False))
		return dicoCarte
	
	def tireCarteAlea (self) :
		lsType = ["croissement", "coins", "droit"]
		for elem in lsType : 
			if self.dicoCarte[elem] == [] :
				lsType.remove(elem)
		for elem in self.dicoCarte :
			if elem not in lsType and dicoCarte[elem] != [] :
				lsType.append(elem)
		typeCarte = random.choice(lsType)
		del self.dicoCarte[typeCarte][0]
		return self.dicoCarte[typeCarte].tournerRandom()
	
	def changerJoueurCourant (self) :
		self.joueurCourant = (self.joueurCourant + 1) % 2 
	
	def piocherCarte (self) :
		nvCarte = self.tireCarteAlea()
		ancienneCarte = self.prendreCarte()
		self.poserCarte(nvCarte)
		self.mettreCarteDico(ancienneCarte)
	
	def testActionPossible (self) :
		return self.getJoueurCourant.getNbPa() != 0
		
plateau = Labyrinthe()
