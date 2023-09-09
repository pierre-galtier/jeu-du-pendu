mot = "pierre"
coup = 10
motaffiche = ["_"] * len(mot)

def mot_affiche(lettre):
    trouve = False
    for i in range(0, len(mot)):
        if mot[i] == lettre:
            motaffiche[i] = lettre
            trouve = True

    for i in motaffiche:
        print(i, end=" ")

    print("")

    if trouve is False:
        return False

while coup > 0:
    lettre_proposee = input("Lettre : ")
    t = mot_affiche(lettre_proposee)
    if t is False: coup -= 1
    print("Coups restants : " + str(coup))
    if not "_" in motaffiche:
        print("Gagné")
        break

print("Fini")
if "_" in motaffiche:
    print("Perdu")