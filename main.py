# Auteurs: Ann-Sophie Gironne et Oscar Parent
# Date: 20 octobre 2024
# Matricules: 20153433 et ?????
#
# TODO: Écrire la description du programme
#### en 5x5 on ajoute 8 pixels à droite et en bas pour ajouter un carré
#### 4x4 c'est 47 x 47 pixels
### TODO: Changer scale à 4 dans glisse() quand fini



blanc = "#fff"
gris = "#444"
rouge = "#f00"
vert = "#0f0"
jaune = "#770"


def taille_de_la_grille(format):
    if format == 4:
        dims = struct(largeur = 47, hauteur = 47)
    elif format > 4:
        nouveaux_pixels = (format - 4) * 8
        dims = struct(largeur = 47 + nouveaux_pixels,
                      hauteur = 47 + nouveaux_pixels)
    return dims

def fleches_haut(x, couleur):    
    # Positions de la première flèche en haut à gauche
    fleche = ([[9 + x, 2], [9 + x, 3]],     # barre 1
              [[10 + x, 3], [10 + x, 4]],   # barre 2
              [[11 + x, 4], [11 + x, 5]],   # barre 3
              [[12 + x, 3], [12 + x, 4]],   # barre 4
              [[13 + x, 2], [13 + x, 3]])   # barre 5
    
    # Dessine la flèche barre par barre
    for barre in range(len(fleche)):
            for pixel in fleche[barre]:
                draw_image(pixel[0], pixel[1], couleur)
    return fleche
                    
def fleches_bas(x, dims, couleur):
    y = dims.hauteur
    # Positions de la première flèche en bas à gauche
    fleche = ([[9 + x, y - 3], [9 + x, y - 4]],    # barre 1
              [[10 + x, y - 4], [10 + x, y - 5]],  # barre 2
              [[11 + x, y - 5], [11 + x, y - 6]],  # barre 3
              [[12 + x, y - 4], [12 + x, y - 5]],  # barre 4
              [[13 + x, y - 3], [13 + x, y - 4]])  # barre 5
    
    # Dessine la flèche barre par barre
    for barre in range(len(fleche)):
            for pixel in fleche[barre]:
                draw_image(pixel[0], pixel[1], couleur)
    return fleche

def fleches_gauche(y, couleur):
    # Positions de la première flèche en haut à gauche
    fleche = ([[2, 9 + y], [3, 9 + y]],     # barre 1
              [[3, 10 + y], [4, 10 + y]],   # barre 2
              [[4, 11 + y], [5, 11 + y]],   # barre 3
              [[3, 12 + y], [4, 12 + y]],   # barre 4
              [[2, 13 + y], [3, 13 + y]])   # barre 5
    
    # Dessine la flèche barre par barre
    for barre in range(len(fleche)):
            for pixel in fleche[barre]:
                draw_image(pixel[0], pixel[1], couleur)
                
    return fleche
                    
def fleches_droite(y, dims, couleur):
    x = dims.largeur
    # Positions de la première flèche en haut à droite
    fleche = ([[x - 3, 9 + y], [x - 4, 9 + y]],     # barre 1
              [[x - 4, 10 + y], [x - 5, 10 + y]],   # barre 2
              [[x - 5, 11 + y], [x - 6, 11 + y]],   # barre 3
              [[x - 4, 12 + y], [x - 5, 12 + y]],   # barre 4
              [[x - 3, 13 + y], [x - 4, 13 + y]])   # barre 5
    
    # Dessine la flèche barre par barre
    for barre in range(len(fleche)):
            for pixel in fleche[barre]:
                draw_image(pixel[0], pixel[1], couleur)
    
    return fleche
                    
def initialisation_fleches(dims, couleur):
    nb_fleches = (dims.largeur - 14) // 8
    
    haut = []; bas = []; gauche = []; droite = []
    
    for decalage in range(nb_fleches):
        haut.append(fleches_haut(decalage * 8, couleur))
        bas.append(fleches_bas(decalage * 8, dims, couleur))
        gauche.append(fleches_gauche(decalage * 8, couleur))
        droite.append(fleches_droite(decalage * 8, dims, couleur))
        
    fleches = struct(haut = haut,
                     bas = bas,
                     droite = droite,
                     gauche = gauche)
    return fleches
 
def creer_matrice(format):
    matrice = [None] * format
    
    for i in range(format):
        matrice[i] = [0] * format
    
    return matrice
    
def lignes_horizontales(dims, y, couleur):
    x = dims.largeur
    ligne = ([range(7, x - 7), range(7 + y, 8 + y)],         # haut
             [range(7, x - 7), range(15 + y, 16 + y)],       # bas
             [range(x - 8, x - 7), range(7 + y, 16 + y)],    # droite
             [range(7, 8), range(7 + y, 16 + y)])            # gauche
    
    for barre in range(len(ligne)):
        for x in ligne[barre][0]:
            for y in ligne[barre][1]:
                draw_image(x, y, couleur)
    
    return ligne

def lignes_verticales(dims, x, couleur):
    y = dims.hauteur
    ligne = ([range(7 + x, 16 + x), range(7, 8)],           # haut
             [range(7 + x, 16 + x), range(y - 8, y - 7)],   # bas
             [range(7 + x, 8 + x), range(7, y - 8)],        # droite
             [range(15 + x, 16 +x ), range(7, y - 8)])      # gauche
    
    for barre in range(len(ligne)):
        for x in ligne[barre][0]:
            for y in ligne[barre][1]:
                draw_image(x, y, couleur)
    
    return ligne
    

def initialisation_grille(dims, couleur):
    nb_lignes = (dims.largeur - 14) // 8
    
    horiz = []; verti = []
    
    for decalage in range(nb_lignes):
        horiz.append(lignes_horizontales(dims, decalage * 8, couleur))
        verti.append(lignes_verticales(dims, decalage * 8, couleur))
    
    grille = struct(horiz = horiz, verti = verti)
    
    return grille

def ajouter_jeton(grille, index, horizontal, joueur):
    pass

def dessiner_fleche(fleche, couleur):
    for barre in range(len(fleche)):
        for pixel in fleche[barre]:
            draw_image(pixel[0], pixel[1], couleur)
            
def dessiner_ligne(ligne, couleur):
    for trait in range(len(ligne)):
        for x in ligne[trait][0]:
            for y in ligne[trait][1]:
                draw_image(x, y, couleur)

def chercher_ligne(grille, index, horizontal):
    if horizontal:
        return grille.horiz[index]
    else:
        return grille.verti[index]
    
def chercher_fleche(fleches, index, haut, droite):
    if haut:
        return fleches.haut[index]
    else:
        return fleches.bas[index]
    if droite:
        return fleches.droite[index]
    else:
        return fleches.gauche[index]

def positions_jetons(format):
    pass

def dessiner_joueur(couleur):
    fill_rectangle(1, 1, 5, 5, couleur)

def remplir_grille_initiale(dims):
    initialisation_grille(dims, gris)
    dessiner_joueur(rouge)
    fleches = initialisation_fleches(dims, jaune)
    
    
def glisse(format):
    dims = taille_de_la_grille(format)
    set_screen_mode(dims.largeur, dims.hauteur, 6) ### mettre à 4 quand fini 
    remplir_grille_initiale(dims)
    
def son(duree, frequence):
    beep(duree, frequence)
    
def survol_fleche():
    son(0.025, 1500)

def son_coup():
    son(0.15, 2000)

def musique_triste():
    son(0.1, 1000)
    son(0.1, 900)
    son(0.1, 800)
    son(0.1, 700)
    son(0.1, 600)
    son(0.1, 500)
    son(0.75, 100)
    
def musique_joyeuse():
    son(0.1, 500)
    son(0.1, 600)
    son(0.1, 700)
    son(0.1, 800)
    son(0.1, 900)
    son(0.1, 1000)
    son(0.1, 0)
    son(0.1, 1000)
    son(0.1, 0)
    son(0.1, 1000)
    son(0.1, 0)
    son(0.4, 1000)
        
        
glisse(4)
    
# coup = struct(ligne = ligne, fin = booléen)
# jouer_coup(grille, coup, joueur)
# joueur1 = rouge, joueur2 = vert
