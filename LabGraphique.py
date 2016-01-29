#class labyrinthe


# M mouvement, P placement de carte, si P retourne les coordonnées du déplacement, si M saisir en plus le numéro du guerrier
def saisirOrdre(self):
	def choixValide(choix,dicoChoix):
		return choix in dicoChoix.keys()
	def affichageChoix(dicoChoix):
		for clee,description in dicoChoix.items():
			print(clee+" - "+description)

	dicoChoix1={"M":"Pour bouger un guerrier","T":"Pour tourner la Carte","D":"Pour déplacer une carte"}

	affichageChoix(dicoChoix1)
	choix=input(">")
	while not choixValide(choix,dicoChoix1):
		print("Votre choix n'est pas valide")
		affichageChoix(dicoChoix1)
		choix=input(">")
	if choix=="M":
		print("Enter le numéro d'un guerrier")
		numG=input(">")
		while numG not in {str(i) for i in self.joueurs[self.joueurCourant-1].guerriers}:
			print("Le guerrier que vous demandez n'est pas disponible")

			print("Enter le numéro d'un guerrier")
			numG=input(">")
		print("Enter des coordonnées de destination pour votre guerrier")
		x=input("Enter le numéro de ligne de destination")
		y=input("Enter le numéro de colonne de la destination")
		coordoGuerrier=self.

		while x not in {str(a) for a in range(self.plateau.nbLignes)} or y not in {str(a) for a in range(self.plateau.nbColonnes)}:
			print("Les coordonnées saisi ne sont pas correctes ou la case n'est pas accessible")



