class Guerrier (object) :
	
	def __init__ (self,vie = 100, numJoueur, numGuerrier) :
		self.vie = vie
		self.numJoueur = numJoueur
		self.numGuerrier = numGuerrier
	
	def perdVie (self,pointDgt) :
		self.vie -= pointDgt
