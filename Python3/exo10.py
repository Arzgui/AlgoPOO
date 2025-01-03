# Écrire un algorithme qui demande successivement 20 nombres à l’utilisateur, et qui lui dise ensuite 
# quel était le plus grand parmi ces 20 nombres. 
# SANS TABLEAUX !!! 


maxNombre = float(input("Entrez le 1er nombre : "))

for i in range(2, 21):
    nombre = float(input(f"Entrez le {i}ème nombre : "))
    if nombre > maxNombre:
        maxNombre = nombre

print("Le plus grand nombre parmi les 20 nombres est :", maxNombre)

    
    