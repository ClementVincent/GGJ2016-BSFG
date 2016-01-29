class Matrice(object) :
	
	def __init__(self, nbColonnes = 20, nbLignes = 20, valInit = 0) :
		self.nbColonnes = nbColonnes
		self.nbLignes = nbLignes
		self.matrice = []
		for i in range(self.nbColonnes) :
			self.matrice.append([])
			for j in range(self.nbLignes) :
				self.matrice[i].append(0)
	
	def getVal(self, posX, posY) :
		'''Cette methode prend en argument une position et retourne la carte a cette position'''
		return self.matrice[posY][posX]
	
	def setVal (self, posX, posY, nvVal) :
		'''Cette methode prend en argument une carte et une position. Elle remplace la carte et
		retourne la carte expulsée'''
		carteRetire = self.getVal(posX,posY)
		self.matrice[posY][posX] = nvVal
		return carteRetire
