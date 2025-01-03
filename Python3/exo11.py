# Réécrire l’algorithme précédent, mais cette fois-ci on ne connaît pas d’avance combien l’utilisateur
# souhaite saisir de nombres. La saisie des nombres s’arrête lorsque l’utilisateur entre un zéro. 

maxNombre = float(input("Entrez le 1er nombre : "))

while maxNombre != 0:
    nombre = float(input("Entrez un nombre : "))
    if nombre > maxNombre:
        maxNombre = nombre
    elif nombre == 0:
        print("Le plus grand  nombre est :", maxNombre)
        break