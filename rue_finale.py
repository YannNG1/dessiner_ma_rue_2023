# Dépendances

from sol import sol
from immeuble import *

# Définitions


def rue_finale(canvas):
    
    # Affichage de ma rue
    affiche(canvas)
    
    
    # Dessin des immeubles
    x= 130
    for i in range(4):
        immeuble(x)
        x= x+175
    
    
        
    # Dessin du sol de la rue
    sol()
    
if __name__ == '__main__':
    # Tests
    rue_finale(rue)