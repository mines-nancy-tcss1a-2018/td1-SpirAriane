def score(mot):
    points = {'a':1,'b':3,'c':3,'d':2,'e':1,'f':4,'g':2,'h':4,'i':1,'j':8,'k':10,'l':1,'m',2,'n':1,'o':1,'p':3,'q':8,'r':1,'s':1,'t':1,'u':1,'v':4,'w':10,'x':10,'y':10,'z':10}
    Score = 0
    for Lettre in mot:
        Score += points[Lettre]
    return Score


def max_score(l):
    Meilleur = l[0]
    for mot in l:
        if score(mot) > score(Meilleur):
            Meilleur = mot
    return (Meilleur, score(Meilleur))
