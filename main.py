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

def fleche_haut_et_bas(x, y, rotation):
    #### TODO: Figure out comment utiliser les coordonnées de base
    #### pour configurer les autres flèches
    
    fleche = ([[9,2], [9,3]], # barre 1
              [[10, 3], [10, 4]], # barre 2
              [[11, 4], [11, 5]]) # barre 3
    
    if rotation == True:
        fleche_inversee = fleche
        for barre in fleche_inversee:
            for pixel in barre:
                pixel[1] *= -1 
    
    for barre in range(len(fleche)):
        if rotation == False:
            for pixel in fleche[barre]:
                draw_image(pixel[0] + x, pixel[1] + y, jaune)
                if barre == 0:
                    draw_image(pixel[0] + 4 + x, pixel[1] + y , jaune)
                elif barre == 1:
                    draw_image(pixel[0] + 2 + x, pixel[1] + y, jaune)
        else:
            for pixel in fleche_inversee[barre]:
                draw_image(pixel[0] + x, pixel[1] + y, jaune)
                if barre == 0:
                    draw_image(pixel[0] + 4 + x, pixel[1] + y , jaune)
                elif barre == 1:
                    draw_image(pixel[0] + 2 + x, pixel[1] + y, jaune)

def dessiner_fleches(dims):    
    for colonne in range(9, dims.largeur - 9):
        if (colonne - 9) % 8 == 0:
            fleche_haut_et_bas(colonne - 9, 0, False)
            fleche_haut_et_bas(colonne - 9, 0, True) #### marche pas
            
    
    
    
    ### pas ça, trop compliqué
    for colonne in range(9, dims.largeur - 9):
        for rangee in range(2, 6):
            if (rangee == 2) & ((colonne - 9) % 4 == 0):
                draw_image(colonne, rangee, jaune)                
        for rangee in range(dims.hauteur - 6, dims.hauteur - 1):
            if (rangee == dims.hauteur - 2) & ((colonne - 9) % 4 == 0):
                draw_image(colonne, rangee, jaune)
    pass

def dessiner_grille(dims):
    for colonne in range(7, dims.largeur - 7):
        # Dessine les lignes horizontales grises du contour
        draw_image(colonne, 7, gris)
        draw_image(colonne, dims.hauteur - 8, gris)
        
        # Dessine les lignes verticales grises du contour
        for ligne in range(7, dims.hauteur - 7):
            draw_image(7, ligne, gris)
            draw_image(dims.hauteur - 8, ligne, gris)
            
            # Dessine les grilles grises au milieu
            # Chaque carré noir de la grille mesure 7x7
            if (colonne > 7)  & (ligne > 7):
                if ((colonne - 7) % 8 == 0) | ((ligne - 7) % 8 == 0):
                    draw_image(colonne, ligne, gris)
                    draw_image(ligne, colonne, gris)

def dessiner_carre(dims):
    for rangee in range(1,6):
        for col in range(1,6):
            draw_image(rangee, col, rouge)

def remplir_grille_initiale(dims):
    dessiner_grille(dims)
    dessiner_carre(dims)
    dessiner_fleches(dims)
    
    
def glisse(format):
    dims = taille_de_la_grille(format)
    set_screen_mode(dims.largeur, dims.hauteur, 10) ### mettre à 4 quand fini 
    remplir_grille_initiale(dims)
    
    
glisse(4)
    
# coup = struct(ligne = ligne, fin = booléen)
# jouer_coup(grille, coup, joueur)
# joueur1 = rouge, joueur2 = vert
