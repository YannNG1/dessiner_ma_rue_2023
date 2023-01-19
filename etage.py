# Dépendances
from ma_rue import rue, affiche
from facade import facade
from fenetre import fenetre
from balcon import balcon 

from random import randint

# Définitions

# Fonction etage()
def etage(x, couleur, niveau):
    '''
    Dessine sur une facade un étage avec 3 éléments choisis aléatoirement
    parmi une fenêtre ou une porte fenêtre avec balcon.  
    
    Paramètres
        x : abscisse du milieu de la base de l'étage
        couleur : couleur fixée par l'immeuble
        niveau : numéro de l'étage en partant de 0 pour le rdc
    '''
    y = rue.height - niveau * 60 # ordonnée de la base de l'etage
    
    # Murs
    facade(x, couleur, niveau)
    # Eléments
    x = x - 140/3
    for u in range(3):
        if randint(1,2) == 1:
            fenetre(x+15, y+10)
            x = x + 140/3
        else: 
            balcon(x,y)
            x = x + 140/3

    # Tests
from couleur_aleatoire import couleur_aleatoire
affiche(rue)
couleur = couleur_aleatoire()
for n in range(6) :
    etage(rue.width/2,couleur,n)