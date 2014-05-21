#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      eleve
#
# Created:     17/04/2014
# Copyright:   (c) eleve 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import pygame #pour afficher l'image, on importe toute la biblioth?que de pygame
from pygame.locals import *

pygame.init()# initialise tout les modules

pygame.display.set_caption('LeJeuD_P_endu')

fenetre = pygame.display.set_mode((640, 480))# on dit a pygame la taille de la fenetre que l'on veut


#BOUCLE PRINCIPALE
continuer = 1
while continuer:
    for event in pygame.event.get():
        if event.type == QUIT:
            continuer = 0
	#Chargement et affichage de l'?cran d'accueil
	accueil = pygame.image.load("image_python.jpg").convert()
	fenetre.blit(accueil, (0,0))

	#Rafraichissement
	pygame.display.flip()


