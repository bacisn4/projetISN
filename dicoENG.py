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

def mot_hasard_ang():
     word = [line.strip() for line in open('E:\dicoang.txt')]
     return word[random.randint(0,len(word))]

