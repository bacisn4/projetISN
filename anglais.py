#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      eleve
#
# Created:     15/05/2014
# Copyright:   (c) eleve 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from fonction_ang import *

gamertag_ang()


mot_a_trouver = mot_hasard_ang()
lettres_trouvees = []
mot_trouve = mot_cacher(mot_a_trouver, lettres_trouvees)
nb_essai = 4587

while mot_a_trouver!=mot_trouve and nb_essai>0:
        print("Word to found: " + mot_trouve)
        lettre = lettre_user()
        if lettre in lettres_trouvees: # lettre deja essayer
            print("You have already chosen this letter.")
        elif lettre in mot_a_trouver: # lettre dans le mot a trouver
            lettres_trouvees.append(lettre)
            print("Well done.")
        else:
            nb_essai -= 1
            print("This letter is not in the word.")
        print ("Tried letters: "),
        for lettre in lettres_trouvees:
            print lettre,
        print
        mot_trouve = mot_cacher(mot_a_trouver, lettres_trouvees)


if mot_a_trouver==mot_trouve:
        print("Congratulations ! You found the word !!")
else:
        print("HUNG !!!") + (pseudo ("You lost the word was: " + mot_a_trouver))
