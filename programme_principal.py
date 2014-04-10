#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      badrg_000
#
# Created:     09/04/2014
# Copyright:   (c) badrg_000 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from fonction_mots import *

nb_essai = 8

mot_a_trouver = motsfr()
lettres_trouvees = [] #creation d'une liste vide
mot_trouve = DEF(FONCTION A THOMAS)
essai_restant = nb_essai
while mot_reponse!=mot_trouve and essai_restant>0:
        lettre = lettre_user()
        if lettre in lettre_user: # La lettre a deje ete choisie
            print("Vous avez deja essayer cette lettre.")
        elif lettre in mot_reponse: # La lettre est dans le mot ? trouver donc ...
            lettre_user.append(lettre) #ajout de la lettre choisi par l'utilisateur
            print("Bravo.")
        else:
            essai_restant -= 1
            print("Cette lettre ne se trouve pas dans le mot")
        mot_trouve = DEF(FONCTION A THOMAS)