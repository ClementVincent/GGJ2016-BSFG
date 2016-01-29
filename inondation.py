from matrice import *

def marquageDirect(calque,mat,val=1,marque=1):
	marquage_effec=False
	i=0
	while i<calque.getNbLignes():
		j=0
		while j<calque.getNbColonnes():
			if calque.getVal(i,j)==0 and val in {calque.getVal(x,y) for (x,y) in  [(i-1,j),(i,j-1),(i+1,j),(i,j+1)] if x in range(calque.getNbLignes()) and y in range(calque.getNbColonnes())} and mat.getVal(i,j)!=1:
				calque.setVal(i,j,marque)
				marquage_effec=True
			j+=1
		i+=1
	return marquage_effec

def estAccessible(mat,pos1,pos2):
	return estAccessible2(mat,pos1,pos2)!=None

def labyrintheValide(mat):	
	return estAccessible2(mat,(0,0),(mat.getNbLignes()-1,mat.getNbColonnes()-1))!=None

def estAccessible2(mat,pos1,pos2):
	calque=Matrice(mat.getNbLignes(),mat.getNbColonnes())
	calque.setVal(pos1[0],pos1[1],1)
	val=1
	reussit=True
	while reussit and calque.getVal(pos2[0],pos2[1])==0:
		reussit=marquageDirect(calque,mat,val,val+1)
		val+=1

	res=None
	if calque.getVal(pos2[0],pos2[1])==val:
		res=calque

	return res

def cheminDecroissant_3(calque,pos1,pos2):
	chemin=[pos1]
	def case_adj(case):
		def valide(cordo):
			return cordo[0] in range(calque.getNbLignes()) and cordo[1] in range(calque.getNbColonnes())
		d=[(1,0),(0,1),(-1,0),(0,-1)]
		return [(x+case[0],y+case[1]) for (x,y) in d if valide((x+case[0],y+case[1]))]

	while chemin[-1]!=pos2:
		valeur_retenu=[x for x in case_adj(chemin[-1]) if calque.getVal(x[0],x[1])==calque.getVal(chemin[-1][0],chemin[-1][1])-1][0]
		chemin.append(valeur_retenu)
	return chemin

def plusCourtChemin(matrice,pos1,pos2):
	#on fait attention a bien definir estAccessible2 avec pos2 PUIS pos1, ainsi pos1 a bien la valeur le plus grande et on peut remonter dans l'ordre decroissant
	cheminValide=estAccessible2(matrice,pos2,pos1)

	if cheminValide!=None:

		calque=estAccessible2(matrice,pos2,pos1)
		chemin=cheminDecroissant_3(calque,pos1,pos2)#on parcourt donc de pos1 qui contient la plus grande valeur vers pos2
	else:
		chemin=None
	return chemin