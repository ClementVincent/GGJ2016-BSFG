class Joueur(object):
	
	#permet de créer un joueur
	def __init__(self,numJoueur,nbVillagois=10,nbGuerrier=5,pa=10,pm=5):
		self.numJoueur=numJoueur
		self.nbVillagois=nbVillagois
		self.nbGuerriers=nbGuerrier
		self.pa=pa
		self.pm=pm
		self.main=[]
		self.guerriers=[]

	#retourne le nombre de villageois du
	def getNbVillageois(self):
		return self.nbVillagois

	#retourne le nombre de guerrier du joueur
	def getNbGuerrier(self):
		return self.nbGuerriers

	#retourne le nombre de pa du joueur
	def getNbPa(self):
		return self.pa

	#retourne le nombre de pm du joueur
	def getNbPm(self):
		return self.pm

	#set le nombre de pa du joueur à n
	def setPa(self,n):
		self.pa=n

	#set le nombre de pm du joueur à n
	def setPm(self,n):
		self.pm=n

	#attribue le nombre n de villageois au joueur
	def setVillageois(self,n):
		self.nbVillagois=n

	#attribue le nombre n de guerrier au joueur
	def setGuerriers(self,n):
		self.nbGuerriers=n


	#prend la carte de la main et la supprime et la retourne
	def prendreCarte(self):
		indice=random.randint(2)
		buff=self.main[buff]
		self.main.remove(indice)
		return buff



	def initGuerrier(self):
		self.guerriers=[Guerrier(numJoueur=self.numJoueur,numGuerrier=i) for i in range(self.getNbGuerrier)]
	#
	def retirerGuerrier(self,numGuerrier):
		self.guerriers=[guerriers for guerriers in self.guerriers if guerriers.numGuerrier!=numGuerrier]
