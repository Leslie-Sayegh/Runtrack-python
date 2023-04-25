L = [8, 24, 27, 48, 2, 16, 9, 102, 7, 84, 91]
long = len(L)

#produit des valeurs de [50, 70]
p = 1
for i in range (0, long) :
     if 50 <= L[i] <= 70 :
          p = p*L[i]
print ("produit des valeurs comprises entre 50 et 70 : ", p)