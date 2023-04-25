#fonction paramètres: le nombre de marches (penser aller et retour)
                    # la hauteur de chaque marche (en cm)
#calculer combien de mètre effectué par semaine.
#code doit être :
#Pour x marches de y cm, le gardien parcours z.zz m par semaine.
#semaine == 7 jours ;
#descend et remonte 
#calcul en cm #résultat est à exprimer en m.

# fonction 
#def hauteurParcourue (nb, h) :
   #print("Pour { :d} marches de { :d} cm, il parcourt { :.2f} m par semaine !"
        #.format(nb, h, nb*h*2*5*7/100.0))
         

def Toilette ( M,H) :
    HM = H / 100
    DJ = 5 * 2 * HM 
    DS = DJ * 7
    DT = DS * M
    return f"Pour {M} marches de {H} cm, le gardien parcours {DT:.2f} m par semaine."

print (Toilette(100, 20))

