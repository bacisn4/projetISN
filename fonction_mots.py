#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      badrg_000
#
# Created:     08/04/2014
# Copyright:   (c) badrg_000 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

from mots_hasard import *

def motsfr():
    return choice(mots)

#Cette fonction renvoit le mot choisi dans le dictionnaire


def lettre_user():
    lettre = input("Choisissez une lettre: ")
    lettre = lettre.lower()   #minuscule
    if len(lettre)>1:
        print("Votre saisie n'est pas valide.")
        return lettre_user()
    else:
        return lettre

#Cette fonction recoit les lettres choisis par l'utilisateur et invalide la saisie s'il y a plus d'1 lettre dans celle-ci


