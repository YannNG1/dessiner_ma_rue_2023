# Dépendances
from ma_rue import rue, affiche
from toit1 import toit1
from toit2 import toit2
from random import randint

# Définitions

# Fonction toits()

def toits(x, niveau):
    '''
    Dessine aléatoirement un toit plat ou un toit en pointe
    à l'ordonnée du niveau passé en paramètre
    Paramètres
        x : abscisse du centre de l'étage
        y_sol: ordonnée du sol
        niveau : numéro de l'étage en partant de 0 pour le rdc
    '''
    toits = randint(1,2)
    if toits == 1:
        toit1(x, niveau)
    else:
        toit2(x, niveau) 

if __name__ == '__main__':
    # Tests
    affiche(rue)
    for i in range(5) :
        for j in range(6) :
            toits(0 + 200 * i, j)