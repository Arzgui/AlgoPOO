# Demander à l'utilisateur de saisir une date au format "AAAA/MM/JJ"
date_saisie = input("Veuillez saisir une date au format AAAA/MM/JJ : ")

# Diviser la date saisie en année, mois et jour
annee, mois, jour = map(int, date_saisie.split('/'))

# Si le mois est janvier (1) ou février (2), ajuster l'année et le mois
if mois == 1 or mois == 2:
    annee -= 1
    mois += 12

# Calculer le nombre N en utilisant la formule donnée
N = (jour + ((13 * mois + 3) // 5) + (5 * annee // 4) - (annee // 100) + (annee // 400)) % 7

# Définir une liste de noms de jours de la semaine
jours_semaine = ["lundi", "mardi", "mercredi", "jeudi", "vendredi", "samedi", "dimanche"]

# Afficher le résultat
jour_semaine = jours_semaine[N]
print(f"Le {jour} {mois} {annee} est un {jour_semaine}.")

