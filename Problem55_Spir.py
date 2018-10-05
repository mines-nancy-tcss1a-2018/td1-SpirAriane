def solve(n):
     l=[int(i) for i in str(n)]
     l.reverse()
     Inverse = 0
     taille = len(l)
     for i in range(taille):
         Inverse += l[i] * 10**(taille-(i+1))
     S = n + Inverse
     return S

assert solve(47) == 121


def palindrome(n):
    l=[int(i) for i in str(n)] #On va couper la liste en deux et comparer les deux moitiés
    Moitie = len(l)//2
    Parite = len(l)%2 #Si la liste est impaire, on ne doit pas prendre le digit central
    l1=l[:Moitie] #Première demi-liste
    l2=l[Moitie+Parite:] #Seconde demi-liste
    l2.reverse()
    return l1 == l2

CompteLychrel = 0

for n in range(10000):
    Compteur = 0
    k = solve(n)
    
    while Compteur <= 50 and palindrome(k) == False :
        k = solve(k)
        Compteur += 1
    
    if Compteur <= 50 : #Si la boucle s'est arrêté car a trouvé un palindrome
        CompteLychrel += 1

print(CompteLychrel)
