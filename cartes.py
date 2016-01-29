from random import *

class Carte(object):
	def __init__(self,murNord,murEst,murSud,murOuest,guerriers={}):
		self.murNord=murNord
		self.murEst=murEst
		self.murOuest=murOuest
		self.murSud=murSud
		self.guerriers=guerriers


	#retire le guerrier numGuerrier du joueur numJoueur de la carte, ne fait rien si il n'y est pas
	def getGuerrier(self,numGuerrier,numJoueur):
		self.guerriers-={(numJoueur,numGuerrier)}

	def addGuerrier(self,numGuerrier,numJoueur):
		self.guerriers|={(numJoueur,numGuerrier)}
	def carte2mat(self):
		mat=Matrice(3,3,1)
		mat.setVal(1,1,0)

		if not self.murNord:
			mat.setVal(0,1,0)
		if not self.murSud:
			mat.setVal(2,1,0)
		if not self.murOuest:
			mat.setVal(0,1,0)
		if not self.murEst:
			mat.setVal(2,1,0)
		return mat



	def tournerHorraire(self):
		stack=self.murNord
		self.murNord=self.murOuest
		self.murOuest=self.murSud
		self.murSud=self.murEst
		self.murEst=stack



	def tournerRandom(self):
		for i in range(randint(0,3)):
			self.tournerHorraire()



