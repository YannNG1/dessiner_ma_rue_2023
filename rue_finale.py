# Dépendances

from sol import sol
from immeuble import *

# Définitions


def rue_finale(canvas):
    
    # Affichage de ma rue
    affiche(canvas)
    
    
    # Dessin des immeubles
    immeuble(130)
    immeuble(300)
    immeuble(470)
    immeuble(640)
    
        
    # Dessin du sol de la rue
    sol()
    
if __name__ == '__main__':
    # Tests
    rue_finale(rue)