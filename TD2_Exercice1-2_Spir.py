#import os
#os.chdir('C:/Users/Public/Documents/Python_Scripts')

f=open("frenchssaccent.dic","r")
Dico = f.read()
f.close()

Lexique = Dico.split('\n')

def Solutions(l): #l = liste des n lettres (8 ou moins)
    n = len(l)
    #Détermination de la liste des possibilités
    Possibles = []
    for Mot in Lexique :
        Tirage = l[:] #On fait une copie du tirage
        nMot = len(Mot)

        if nMot <= n : #On vérifie que le mot est assez court
            Compte = 0 #Compte des lettres du mot présentes dans le tirage (permet de valider)
            for Lettre in Mot :
                if Lettre in Tirage :
                    Tirage.remove(Lettre)
                    Compte += 1
            if Compte == nMot:
                Possibles.append(Mot)
    return Possibles

def Solutions(Possibles):
    if len(Possibles) == 0:
        return "Aucune solution"
    else :
        Meilleur = Possibles[0]
        for Mot in Possibles :
            if len(Mot) > len(Meilleur) :
                Meilleur = Mot
    return Meilleur



"""
Tests :
l = ['a', 'r', 'b', 'g', 'e', 's', 'c', 'j']
l = ['b', 'p', 'd', 'w', 's', 'y', 'w', 'i']
"""
