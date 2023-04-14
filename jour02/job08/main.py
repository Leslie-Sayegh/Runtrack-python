# ramplir plusieur condition
def fruit(type, saison) :

    if type == "fruit" and saison == "hiver" :
        return "orange, mandarine, kiwi"
    elif type == "fruit" and saison == "ete" :
        return "poire, fraise, cassis"
    elif type == "legume" and saison == "ete" :
        return "artichaut, aubergine, navet"
    else :
        return "ne pas manger"
    
print (fruit("fruit", "hiver"))


