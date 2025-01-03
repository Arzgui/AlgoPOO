depart = int(input("Veuillez saisir la valeur de départ: "))
arrivee = int(input("Veuillez saisir la valeur d'arrivée: "))
pas = int(input("Veuillez saisir le pas souhaité: "))

for i in range(depart,arrivee,pas):
    print(i)