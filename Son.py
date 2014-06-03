#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      jonathan
#
# Created:     31/05/2014
# Copyright:   (c) jonathan 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
import pygame #pour afficher l'image, on importe toute la bibliotheque de pygame, c'est ? dire tout les outils n?cessaire pour pygame
from pygame.locals import *

pygame.music.init()# initialise tout les modules

son = pygame.mixer.music.load("musique.wav")# on importe la musique souhait?e
pygame.mixer.son.play(loops=-1, maxtime=0, fade_ms=0)# on dit a pygame de lancer cette music, de plus on met loops=-1 pour boucler la musique

pygame.mixer.son.set_volume(0.2) # on regle le volume  du son ( de 0 ? 1 )
