import random

magicnumber = random.randint(1, 10)

nombreSaisie = int(input("Veuillez saisir un nombre entre 1 et 10: "))


for i in range(nombreSaisie):
    if nombreSaisie == magicnumber:
        print("Gagné!")
        print(magicnumber)
    elif nombreSaisie < magicnumber:
        print("Trop petit")
        print(magicnumber)
    elif nombreSaisie > magicnumber:
        print("Trop grand")
        print(magicnumber)
    elif nombreSaisie<1 or nombreSaisie>10:
        print("Saisie incorrecte")