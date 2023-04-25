#code césar
#décalé vers la droite de 1 (z-a) 
minuscules = 'abcdefghijklmnopqrstuvwxyz'
MSG=input('message à coder: ')
print(len(MSG))
dcl=int(input('nombre de décalage: '))
n=0
 
toto=str(MSG)
popo=str(minuscules)
nouveauMot = ""
 
while n < len(MSG):
    lettr=toto[n]
    lettre=minuscules.index(lettr)+dcl
    rempl=popo[lettre]
    nouveauMot += rempl
    n=n+1
 
print(MSG) 
print(nouveauMot)