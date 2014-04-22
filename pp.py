#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      badrg_000
#
# Created:     20/04/2014
# Copyright:   (c) badrg_000 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from fonction import *

utilisateur = gamertag()


mot_a_trouver = mot_hasard()
lettres_trouvees = []
mot_trouve = mot_cacher(mot_a_trouver, lettres_trouvees)
nb_essai = 6

while mot_a_trouver!=mot_trouve and nb_essai>0:
        print("Mot a trouver: " + mot_trouve)
        lettre = lettre_user()
        if lettre in lettres_trouvees: # lettre deja essayer
            print("Vous avez deje choisi cette lettre.")
        elif lettre in mot_a_trouver: # lettre dans le mot a trouver
            lettres_trouvees.append(lettre)
            print("Bien joue.")
        else:
            nb_essai -= 1
            print("cette lettre n'est pas dans le mot")
        mot_trouve = mot_cacher(mot_a_trouver, lettres_trouvees)


if mot_a_trouver==mot_trouve:
        print("Bravo ! ") + (utilisateur ("Vous avez trouve le mot"))
else:
        print("PENDU !!! Vous avez perdu" + utilisateur ("Le mot etait: " + mot_a_trouver))


