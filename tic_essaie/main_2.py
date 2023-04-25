#mporter les modules 

import pygame
import random
import math
from math import inf as infinity
import sys
import os
import time

#
pygame.init()
pygame.font.init()

#Taille de la fenettre resolution
Width, Height = 770,770

#importer fichier (cross et cergle) 

Win = pygame.display.set_mode((Width,Height)) # créer la fenetre du jeu
Cross = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Cross.png")), (Width//3, Height//3))

Circle = pygame.transform.scale(pygame.image.load(os.path.join("Assets", "Circle.png")), (Width//3, Height//3))

#créer couleur : rg vert, bleu (o,o,o) = noir 
Bg = (0,0,0)

# dire combien de fois on va passer dans une boucle par second
Clock = pygame.time.Clock()

# fonctions de base qui correspondent aux jouers
AI = +1
Humain = -1

#?? 
FPS = 120 

# fonction principale
def main() :
    #boucle infinie pour que la fenetre s'ouvre à l'infinie 
    
    run = True
#!!! attention penser à mettre condition pour quelle se ferme si non plantage appli voir ordi
    while run : 
# fermer par la croix
        for event in pygame.event.get() :
            if event.type == pygame.QUIT :
                quit()
        

