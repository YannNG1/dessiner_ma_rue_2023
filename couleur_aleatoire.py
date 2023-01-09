# Dépendances
from ma_rue import rue, affiche 
from random import randint

def couleur_aleatoire():
    '''
    Renvoie une couleur HTML valide
    au format 'rgb(rouge, vert, bleu)'
    où rouge, vert et bleu sont des entiers
    compris entre 0 et 255 choisis aléatoirement.
    
    '''

    i = randint(1, 50)
    if i==1: 

        rouge = 215
        vert = 186
        bleu = 206
    else:
        
        rouge = randint(0, 255)
        vert = randint(0, 255)
        bleu = randint(0, 255)
    
    return f"rgb({rouge},{vert},{bleu})"


if __name__ == '__main__':

    # Tests
    affiche(rue)
    couleur = couleur_aleatoire()
    rue.fill_style = couleur
    rue.fill_rect(0, 0, rue.width, rue.height)
    rue.font = '48px Lucida Console'
    rue.text_align = 'center'
    rue.stroke_text(couleur, rue.width/2, rue.height/2)