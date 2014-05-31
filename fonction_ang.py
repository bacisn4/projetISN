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

import random

def mot_hasard_ang():
     word = [line.strip() for line in open('G:\dicoang.txt')]
     return word[random.randint(0,len(word))]

def gamertag_ang():
    pseudo=raw_input("Enter your nickname please")
    if len(pseudo)>3 and len(pseudo)<10:
        print("This nickname is valid")
        return pseudo
    else:
        print("This nickname is not valid")
        return gamertag_ang()

def lettre_user():

    lettre = input("Enter a letter")
    lettre = lettre.lower()
    if len(lettre)>1:
        print("The chosen letter is not valid.")
        return lettre_user()
    else:
        return lettre


def mot_cacher(mot_complet, lettres_trouvees):

    mot_masque = ""
    for lettre in mot_complet:
        if lettre in lettres_trouvees:
            mot_masque += lettre
        else:
            mot_masque += "_"
    return mot_masque
