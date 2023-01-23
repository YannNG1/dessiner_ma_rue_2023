# Dépendances
from ma_rue import rue, affiche
from couleur_aleatoire import couleur_aleatoire
from rdc import rdc
from etage import etage
from toits import toits

from random import randint

# Définitions

def immeuble(x):
    '''
    Dessine un immeuble selon les règles urbanistiques imposées
    
    Paramètres
        x : abscisse du milieu de la base de l'immeuble
        
    '''
    # Nombre d'étage (aléatoire)
    niveau = randint(0, 4)
    

    #Couleur facade (aléatoire)
    couleur = couleur_aleatoire()
    
    # Dessin du RDC
    rdc(x,couleur)

    # Dessin des étages
    for i in range(niveau):
        etage(x, couleur, i+1)
    

    # Dessin du toit
    toits(x, niveau+1)

if __name__ == '__main__':
    # Tests
    affiche(rue)
    immeuble(rue.width/3)
    immeuble(2*rue.width/3)