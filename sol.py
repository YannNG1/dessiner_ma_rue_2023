# Dépendances
from ma_rue import rue, affiche 
from trait import trait 
# Définitions

# Fonction sol()
def sol():
    '''
    Trace une ligne horizontale au niveau du sol de la rue
    d'épaisseur 3 pixels et de longueur 760 pixels
    centrée dans le canvas
            
    '''

    y_sol = rue.height-1 # ordonnée du sol de la rue
    rue.lineWidth=3
    trait(20,y_sol,780,y_sol)


if __name__ == '__main__':
    # Tests
    affiche(rue)
    sol()