# Dépendances
from ma_rue import rue, affiche
from facade import facade
from portes import portes
from fenetre import fenetre
from random import randint

# Définitions

# Fonction rdc()
def rdc(x, couleur):
    '''
    Dessine le rdc sur une facade au niveau do sol de la rue
    avec une seule porte et 2 fenêtres placées aléatoirement.
    Paramètres
        x : abscisse du milieu de la base du RDC
        couleur : couleur fixée par l'immeuble        
    '''
    # Dessine la facade
    facade(x, couleur, 0)
    a= 0
    # Choix d'une distribution
    distribution = randint(1,3)
    if  distribution == 1:
        a = x + 140/3
        portes(a,399)
        b= x - 140/3
        fenetre(b, 390)
        fenetre(x, 390)
        
    
    elif distribution == 2:
        portes(x,399)
        b= x - 140/3
        fenetre(b, 390)
        a = x + 140/3
        fenetre(a, 390)

    else:
        a = x - 140/3
        portes(a,399)
        b= x + 140/3
        fenetre(b, 390)
        fenetre(x, 390)
        
    
if __name__ == '__main__':
    # Tests
    from couleur_aleatoire import couleur_aleatoire
    affiche(rue)
    for i in range(7) :
        rdc(i*160, couleur_aleatoire())