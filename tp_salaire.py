def calcule_salaire_mansuel(salaireAnnuel):
    salaireMansuel= salaireAnnuel/12
    return salaireMansuel
def calcule_salaire_Hebdomadire(salaireMansuel):
    salaireHebdomadaire= salaireMansuel/4
    return salaireHebdomadaire
def calcule_salaire_horaire(salaireHebdomadaire,haireTravail):
    salaireHoraire= salaireHebdomadaire/haireTravail
    return salaireHoraire
salaireAnnuel=int(input("entrée votre salaire annuel  : "))
haireTravail=int(input("entrée le nombre des heurs travailée par semaine  : "))

salaireMansuel=calcule_salaire_mansuel(salaireAnnuel)

salaireHebdomadaire=calcule_salaire_Hebdomadire(salaireMansuel)

salaireHoraire=calcule_salaire_horaire(salaireHebdomadaire,haireTravail)
print("votre salaire horaire est de :",salaireHoraire," $")