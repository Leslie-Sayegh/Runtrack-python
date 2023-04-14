#fonction width,height ou Largeur, hauter
#fonction input()
#créer l un rectangle avec des ‘-’ et des ‘|’ 
#|--------|
#|        |
#|--------|

#L = 3
#C = 8
#i == 1
#i == L
#j == 1
#j == C 

L = int(input("Veuillez saisir le nombre de lignes : "))
C = int(input("Veuillez saisir le nombre de colonnes : "))
for i in range (1,L+1) :
    for j in range (1,C+1) :
        if i == 1 or i == L :
            print ("-", end="")
        elif j == 1 or j == C :
            print ("|", end="")
        else : 
            print (" ", end="")
    print ()


#presque pas bon nb "|" dans les lingnes