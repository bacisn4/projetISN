#-------------------------------------------------------------------------------
# Name:        module3
# Purpose:
#
# Author:      eleve
#
# Created:     10/04/2014
# Copyright:   (c) eleve 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
def gamertag(): # on defini la fonction gamertag
    pseudo=raw_input("Veuillez tapez votre nom de joueur s'il vous plait") # interaction avec l'utilisateur pour son pseudo
    if len(pseudo)>3 and len(pseudo)<10: # si la longueur de son pseudo est compris entre 3 et 10
        print("ce nom est valide ") # afficher
        return pseudo # retrouner le pseudo
    else:
        print("ce nom n'/est pas valide ") #sinon afficher
        return gamertag() # refaire toute la fonction gamertag depuis le debut

gamer=gamertag() # enregistre le choix du pseudo dans la variable gamer
print gamer # afficher ce pseudo