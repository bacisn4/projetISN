#-------------------------------------------------------------------------------
# Name:        module2
# Purpose:
#
# Author:      badrg_000
#
# Created:     08/04/2014
# Copyright:   (c) badrg_000 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import random

def mot_hasard():

	mots = [line.strip() for line in open('J:\dicofr.txt')]
	return mots[random.randint(0,len(mots))]
