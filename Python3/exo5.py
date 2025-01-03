sommeNotes = 0
sommeCoeff = 0
nbMatieres = int(input("Veuillez saisir le nombre de matières: "))

for i in range(nbMatieres):
    notes = float(input("Entrez une note: "))
    coeff = int(input("Entrez le coefficient de cette note: "))

    if 0 <= notes <= 20 and 1 <= coeff <= 10:
        sommeNotes += notes * coeff
        sommeCoeff += coeff

    if sommeCoeff > 0:
        total = sommeNotes / sommeCoeff
        appreciation = ""

    # Pour utiliser f-strings il suffit de mettre un f devant la chaine de caractères et pour insérer
    # la valeur d’une variable dans la chaine il suffit de mettre la variable entre accolade.
    # Si il n’y a pas de variable a substituer il n’est pas nécessaire de mettre le f devant.

    if 16 <= total <= 20:
        appreciation = "Très bien"
    elif 12 <= total < 16:
        appreciation = "Bien"
    elif 8 <= total < 12:
        appreciation = "Assez bien"
    elif 4 <= total < 8:
        appreciation = "Insuffisant"
    else:
        appreciation = "Nul"

    print(f"La moyenne est de {total}, la mention est \"{appreciation}\".")
else:
    print("Aucun calcul de moyenne n'a été effectué car les notes ou coefficients étaient invalides.")
