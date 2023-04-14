#Écrire un programme qui échange les valeurs de la première et de la dernière case

L = [1, 2, 3, 4, 5]
l = len(L)
aux = L[0]
L[0] = L[l-1]
L[l-1] = aux
print (L)

