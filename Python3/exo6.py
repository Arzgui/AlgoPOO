nombreDecimal = int(input("Entrez un nombre décimal : "))
binaire = ""

while nombreDecimal > 0:
    reste = nombreDecimal % 2
    binaire = str(reste) + binaire
    nombreDecimal = nombreDecimal // 2

print("Le nombre binaire est :", binaire)
