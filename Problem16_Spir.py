k=2**1000

def solve(n):
    l=[int(i) for i in str(n)] #liste des digits de n
    Somme = 0
    for i in l:
        Somme += i
    return Somme

assert solve(2**15) == 26

print(solve(k))