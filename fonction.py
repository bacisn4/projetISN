import random


def gamertag(): # on defini la fonction gamertag
    pseudo=raw_input("Veuillez tapez votre nom de joueur s'il vous plait") # interaction avec l'utilisateur pour son pseudo
    if len(pseudo)>3 and len(pseudo)<10: # si la longueur de son pseudo est compris entre 3 et 10
        print("ce nom est valide ") # afficher
        return pseudo # retrouner le pseudo
    else:
        print("ce nom n'est pas valide ") #sinon afficher
        return gamertag() # refaire toute la fonction gamertag depuis le debut

def lettre_user():

    lettre = raw_input("Tapez une lettre")
    lettre = lettre.lower() #minuscule
    if len(lettre)>1:
        print("Vous n'avez pas saisi une lettre valide.")
        return recup_lettre()
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

def mot_hasard():

	mots = [line.strip() for line in open('J:\dicofr.txt')]  #on cree une liste contenant tt les lettres du dico
	return mots[random.randint(0,len(mots))] #on pioche une valeur au hasard de la liste crée donc un mot du dico

