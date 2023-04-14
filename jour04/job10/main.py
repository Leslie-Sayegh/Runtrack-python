#afficher valeur L[1]
def new_func():
    L = [1, 2, 3, 4, 5]
    a=L.index(1)
    print (a)
    b=L.index(2)
   
    c=L.index(3)
   
    d=L.index(4)
  
    e=L.index(5)
   
L = new_func()

#ecrire fonction qui remplace L[3] par la somme L[2]&L[4] 


L = [1, 2, 3, 4, 5]

L[1] = 2
L[2] = L[1] + L[3]
print (L)


#affichr la valeur du dernier therme 
def new_func():
    L = [1, 2, 3, 4, 5]
    print (L[-1])
L = new_func()