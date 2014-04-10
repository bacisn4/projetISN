#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      eleve
#
# Created:     10/04/2014
# Copyright:   (c) eleve 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------

ans = True
while ans:
    print("""
    1. Francais
    2. Anglais

    Appuyer sur entrer pour quitter
    """)
    ans=input("Choisissez une langue")
    if ans =="1":
        print("le jeux sera en version francaise")
    elif ans=="2":
        print("le jeux sera en version anglaise")
