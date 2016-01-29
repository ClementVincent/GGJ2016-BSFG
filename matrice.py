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

	def setBloc(self,bloc,x,y):
		for i in range(bloc.nbLignes):
			for j in range(bloc.nbColonnes):
				self.setVal(x+i,y+j,bloc.getVal(i,j))


	def matrice2preCalque(self):
		preCalque=Matrice(self.nbLignes*3,self.nbColonnes*3)

		for i in range(matrice.nbLignes):
			for y in range(matrice.nbColonnes):
				bloc=self.getVal().carte2mat()
				preCalque.setBloc(bloc,i*3,j*3)

		return preCalque








