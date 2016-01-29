class Guerrier (object) :
	
	def __init__ (self,vie = 100, numJoueur, numGuerrier) :
		self.vie = vie
		self.numJoueur = numJoueur
		self.numGuerrier = numGuerrier
		self.villageois = None
	
	def perdVie (self,pointDgt) :
		self.vie -= pointDgt
	
	def prendVillageois (self, numVillageois) :
		self.villageois = numVillageois
	
	def testPasVillageois (self) :
		return self.villageois == None

