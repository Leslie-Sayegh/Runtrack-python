# afficher nombre premier jusqu'a 100
for i in range (3, 101) :
    trouve=0
    for j in range (2, i) :
        if i%j == 0 :
         trouve = 1
    if trouve == 0 :
        print (i)     


            