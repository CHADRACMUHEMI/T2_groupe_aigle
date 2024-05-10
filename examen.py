listes=[]
nombre='oui'
while nombre =="oui":
    nombres= int(input("entrer les nombre separés par la virgule"))
    listes.append(nombres)
    nombre=input("voulez-vous continnuer oui ou non")
print(listes)
for i in listes:
    print(i)
for i in range(0,len(listes)):
    somme=sum(listes)
print("la somme de tous les nombres dans la liste est ",somme)
taille_liste=len(listes)
moyenne=sum(listes)/taille_liste
print("la moyenne de ces nombres est ",moyenne)

for i in listes:
    if(i<moyenne):
        continue
print("le nombres superieur a la moyenne est ",i)
for nombres in range(0,len(listes)):
    modulo=listes[nombres]%2
    if(modulo!=0):
        continue
    print(listes[nombres])

