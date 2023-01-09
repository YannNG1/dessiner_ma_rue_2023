# Dépendance
from ipycanvas import Canvas

# Définition 

# Création d'un canvas nommé rue de 800 pixels de large par 400 pixels de haut
rue = Canvas(width=800, height=400)

# Définition d'une fonction d'affichage
def affiche(canvas) :
    '''
    Efface et affiche le canvas dans le notebook
    '''
    
    canvas.clear()
    display(canvas)
    
# Test

# Affichage du canvas rue pour un test
affiche(rue)
