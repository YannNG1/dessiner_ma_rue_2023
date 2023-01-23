# Dépendances
from ma_rue import rue, affiche
from rectangle import rectangle

# Définitions
'''
    Dessine un rectangle de 60 pixels de haut et 140 pixels de large
    Paramètres :
        x : abcisse du centre de la façade
        couleur : couleur de la façade fixée par l'immeuble
        niveau : numéro du niveau (0 pour les rdc, ...)
'''
# Fonction
def facade(x, couleur, niveau):
    
    y = rue.height - niveau * 60 # ordonnée de la base de la facade
    rectangle(x, y-1, 140, 60, couleur)



if __name__ == '__main__':
    # Tests
    from couleur_aleatoire import couleur_aleatoire
    affiche(rue)
    couleur = couleur_aleatoire()
    for n in range(6) :
        facade(rue.width/2, couleur, n)