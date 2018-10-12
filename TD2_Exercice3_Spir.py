def score(mot):
    Liste_1 = ['a','e','i','l','n','o','r','s','t','u']
    Liste_2 = ['d','g','m']
    Liste_3 = ['b','c','p']
    Liste_4 = ['f','h','v']
    Liste_8 = ['j','q']
    Liste_10 = ['k','w','x','y','z']
    Score = 0
    for Lettre in mot:
        if Lettre in Liste_1 :
            Score += 1
        elif Lettre in Liste_2 :
            Score += 2
        elif Lettre in Liste_3 :
            Score += 3
        elif Lettre in Liste_4 :
            Score += 4
        elif Lettre in Liste_8 :
            Score += 8
        elif Lettre in Liste_10 :
            Score += 10
    return Score


def max_score(l):
    Meilleur = l[0]
    for mot in l:
        if score(mot) > score(Meilleur):
            Meilleur = mot
    return (Meilleur, score(Meilleur))