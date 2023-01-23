# Dépendances
from ma_rue import rue, affiche 

# Définitions

# Fonction toit1()
def toit1(x, niveau):
    '''
    Dessine un triangle plein de couleur noir de 40 pixels de haut
    et avec une base de 160 pixels 
    Paramètres :
        x : abcisse du centre du toit
        niveau : numero du niveau (0 pour les rdc, ...)
    '''
    y = rue.height - niveau * 60 # ordonnée de la base du toit

    #Dessin du triagnle
    rue.begin_path()
    rue.move_to(x-80,y)  
    rue.line_to(x,y-40)
    rue.line_to(x+80, y)
    rue.close_path()
    rue.stroke()

    #Remplissage du triangle
    
    rue.fill_style = "black"
    rue.fill()
if __name__ == '__main__':
    # Tests
    affiche(rue)
    toit1(rue.width/2, 2)