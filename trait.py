# Dépendances
from ma_rue import rue, affiche

# Définitions

# Fonction trait()
def trait(x1,y1,x2,y2):
    '''
    dessine un trait entre les 2 points transmis en paramètres
    Paramètres
        x1, y1 : coordonnées du début du trait
        x2, y2 : coordonnées de la fin du trait
    
    '''
    rue.stroke_style = 'black'
    rue.stroke_line(x1, y1, x2, y2)

if __name__ == '__main__':
    # Tests
    affiche(rue)
    trait(50, 25, rue.width/2, rue.height/2)