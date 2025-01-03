# L’élève placé au fond de la classe, près du radiateur, est le meilleur de la classe. Pour tuer le temps,
# il décide de plier une feuille en deux puis en deux, puis... en deux, puis... Écrivez un algorithme
# qui calcule l’épaisseur du pliage final à partir du nombre de plis et de l’épaisseur initiale de la
# feuille.

epaisseur = float(input("Veuillez entrez l'épaisseur de la feuille en mm: "))
nbplis = int(input("Entre le nombre de plis: "))

for i in range(nbplis):
    epaisseur = epaisseur*nbplis
print(epaisseur)

