#fonction qui, recevant une taille n en paramètre
# tapis de n+1 lignes/n+1 colonnes traversé par une diagonale.

def tapisserie(n): 
	# Le bord 
	bord="+" 
	for i in range(n+1): bord +="-" 
	bord+="+" 
  
	# La boucle d'affichage 
	print(bord) 
	for i in range(n+1): 
		tapis="" 
		for j in range(n-i): tapis+="#" 
		tapis+=" " 
		for j in range(i): tapis+="#" 
		print("|" + tapis + "|") 
	# for 
	print(bord) 
# tapisserie() 
  
tapisserie(10)