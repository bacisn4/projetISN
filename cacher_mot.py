#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      Thomas
#
# Created:     10/04/2014
# Copyright:   (c) Thomas 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------


def mot_cacher(mot_reponse, lettre_user):
    mot_masque = ""
    for lettre in mot_reponse:
        if lettre in lettre_user:
            mot_masque += lettre
        else:
            mot_masque += "_"
    return mot_masque