import os
#os.chdir('C:/Users/Ariane/Documents/Fichiers_Python') pour changer le chemin

f=open("names.txt","r")
Texte = f.read()
f.close()


ListeTexte = Texte.split(',')
ListeTrie = sorted(ListeTexte)
TexteTrie = ",".join(ListeTrie)

f=open("names.txt","w")
f.write(TexteTrie)
f.close()