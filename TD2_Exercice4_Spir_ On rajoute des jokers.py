"""
Pour autoriser l'utilisation d'un seul joker, il suffit de rajouter deux lignes (cf lignes)
En effet, le '?' ne sera pas présent dans le Mot du Lexique, 
 on saura donc qu'il est toujours libre à la fin du compte des caractères utilisés pour le mot.
Avant, on constatait que si toutes les lettres du mot était dans le tirage, c'était bon.
Maintenant, il suffit d'avoir toutes les lettres du mot sauf une (qui sera remplacé par ?),
 pour rajouter le mot aux possibilités.

Concernant le calcul du score, il faut simplement éviter de compter la lettre que remplace ?
"""

#import os
#os.chdir('C:/Users/Public/Documents/Python_Scripts')

f=open("frenchssaccent.dic","r")
Dico = f.read()
f.close()

Lexique = Dico.split('\n')

def Liste_possibles2(l): #l = liste des n lettres (8 ou moins)
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
            if Compte == nMot: #Toutes les lettres du mot sont dans le tirage
                Possibles.append(Mot)
            elif Compte == nMot-1 and '?' in Tirage: # Il manque une lettre du mot, mais il y a le ? pour la remplacer 
                Possibles.append(Mot)
    return Possibles


def score2(mot,tirage):
    points = {'a':1,'b':3,'c':3,'d':2,'e':1,'f':4,'g':2,'h':4,'i':1,'j':8,'k':10,'l':1,'m':2,'n':1,'o':1,'p':3,'q':8,'r':1,'s':1,'t':1,'u':1,'v':4,'w':10,'x':10,'y':10,'z':10}
    Score = 0
    for Lettre in mot:
        if Lettre in tirage:
            Score += points[Lettre]
    return Score

def max_score2(l,tirage):
    Meilleur = l[0]
    for mot in l:
        if score2(mot,tirage) > score2(Meilleur,tirage):
            Meilleur = mot
    return (Meilleur, score2(Meilleur))
    


"""
test = ['z','x','c','v','r','r','t','?']
"""

