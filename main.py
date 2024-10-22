# Auteurs: Ann-Sophie Gironne et Oscar Parent
# Date: 20 octobre 2024
# Matricules: 20153433 et ?????
#
# TODO: Écrire la description du programme
# TODO: Changer scale à 4 dans glisse() quand fini



blanc = "#fff"
gris = "#444"
rouge = "#f00"
vert = "#0f0"
jaune = "#770"
noir = "#000"

from tp1 import *

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
    # Les ajustements en x et y permettent de dessiner les autres flèches
    fleche = ([9 + x, 2, 1, 2],     # barre 1
              [10 + x, 3, 1, 2],    # barre 2
              [11 + x, 4, 1, 2],    # barre 3
              [12 + x, 3, 1, 2],    # barre 4
              [13 + x, 2, 1, 2])    # barre 5
    
    # Dessine la flèche barre par barre
    for rect in range(len(fleche)):
        fill_rectangle(fleche[rect][0],
                       fleche[rect][1],
                       fleche[rect][2],
                       fleche[rect][3],
                       couleur)
    return fleche
                    
def fleches_bas(x, dims, couleur):
    y = dims.hauteur
    # Positions de la première flèche en bas à gauche
    # Les ajustements en x et y permettent de dessiner les autres flèches
    fleche = ([9 + x, y - 4, 1, 2],   # barre 1
              [10 + x, y - 5, 1, 2],  # barre 2
              [11 + x, y - 6, 1, 2],  # barre 3
              [12 + x, y - 5, 1, 2],  # barre 4
              [13 + x, y - 4, 1, 2])  # barre 5
    
    # Dessine la flèche barre par barre
    for rect in range(len(fleche)):
        fill_rectangle(fleche[rect][0],
                       fleche[rect][1],
                       fleche[rect][2],
                       fleche[rect][3],
                       couleur)
    return fleche

def fleches_gauche(y, couleur):
    # Positions de la première flèche en haut à gauche
    # Les ajustements en x et y permettent de dessiner les autres flèches
    fleche = ([2, 9 + y, 2, 1],    # barre 1
              [3, 10 + y, 2, 1],   # barre 2
              [4, 11 + y, 2, 1],   # barre 3
              [3, 12 + y, 2, 1],   # barre 4
              [2, 13 + y, 2, 1])   # barre 5
    
    # Dessine la flèche barre par barre
    for rect in range(len(fleche)):
        fill_rectangle(fleche[rect][0],
                       fleche[rect][1],
                       fleche[rect][2],
                       fleche[rect][3],
                       couleur)
                
    return fleche
                    
def fleches_droite(y, dims, couleur):
    x = dims.largeur
    # Positions de la première flèche en haut à droite
    # Les ajustements en x et y permettent de dessiner les autres flèches
    fleche = ([x - 4, 9 + y, 2, 1],     # barre 1
              [x - 5, 10 + y, 2, 1],    # barre 2
              [x - 6, 11 + y, 2, 1],    # barre 3
              [x - 5, 12 + y, 2, 1],    # barre 4
              [x - 4, 13 + y, 2, 1])    # barre 5
    
    # Dessine la flèche barre par barre
    for rect in range(len(fleche)):
        fill_rectangle(fleche[rect][0],
                       fleche[rect][1],
                       fleche[rect][2],
                       fleche[rect][3],
                       couleur)
    
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
    ligne = ([7, 7 + y, x - 15, 1],     # haut
             [7, 15 + y, x - 15, 1],    # bas
             [7, 7 + y, 1, 9],          # gauche
             [x - 8, 7 + y, 1, 9])      # droite
    
    for rect in range(len(ligne)):
        fill_rectangle(ligne[rect][0],
                       ligne[rect][1],
                       ligne[rect][2],
                       ligne[rect][3],
                       couleur)
    return ligne

def lignes_verticales(dims, x, couleur):
    y = dims.hauteur
    ligne = ([7 + x, 7, 9, 1],           # haut
             [7 + x, y - 8, 9, 1],       # bas
             [7 + x, 7, 1, y - 15],      # gauche
             [15 + x, 7, 1, y - 15])     # droite
    
    for rect in range(len(ligne)):
        fill_rectangle(ligne[rect][0],
                       ligne[rect][1],
                       ligne[rect][2],
                       ligne[rect][3],
                       couleur)
    return ligne
    

def initialisation_grille(dims, couleur):
    nb_lignes = (dims.largeur - 14) // 8
    
    horiz = []; verti = []
    
    for decalage in range(nb_lignes):
        horiz.append(lignes_horizontales(dims, decalage * 8, couleur))
        verti.append(lignes_verticales(dims, decalage * 8, couleur))
    
    grille = struct(horiz = horiz, verti = verti)
    
    return grille

def initialisation_jetons(dims):
    taille_matrice = (dims.largeur - 14) // 8
    jetons = creer_matrice(taille_matrice)
    return jetons

def ajouter_jeton(jetons, index, position, joueur):
    # La position tourne en sens horloge (haut = 0, droite = 1, ...)
    if position == 0:
        decalage_bas(jetons, index, joueur)
    elif position == 1:
        decalage_gauche(jetons, index, joueur, True)
    elif position == 2:
        decalage_haut(jetons, index, joueur)
    elif position == 3:
        decalage_droite(jetons, index, joueur, True)
    dessiner_jetons(jetons)
    
def decalage_gauche(jetons, index, joueur, matrice):
    # Ajoute un élément à droite pour décaler la ligne vers la gauche
    if matrice:
        # Décale une ligne dans la matrice complète
        nouvelle_ligne = jetons[index][1:] + [joueur]
        jetons[index] = nouvelle_ligne

    else:
        # Décale une ligne donnée
        ligne_decalee = jetons[1:] + [joueur]
        return ligne_decalee

def decalage_droite(jetons, index, joueur, matrice):
    # Ajoute un élément à gauche pour décaler la ligne vers la droite
    if matrice:
        # Décale une ligne dans la matrice complète
        nouvelle_ligne = [joueur] + jetons[index][:-1]
        jetons[index] = nouvelle_ligne

    else:
        # Décale une ligne donnée
        ligne_decalee = [joueur] + jetons[:-1]
        return ligne_decalee

def decalage_haut(jetons, index, joueur):
    colonne_originale = []
    
    # Extraction des valeurs originales des jetons
    for ligne in jetons:
        colonne_originale.append(ligne[index])
    
    # Décalage des valeurs des jetons
    nouvelle_colonne = decalage_gauche(colonne_originale, 0, joueur, False)
    
    # Remplacement des valeurs des jetons dans la matrice
    for ligne in range(len(jetons)):
        jetons[ligne][index] = nouvelle_colonne[ligne]
        
    
def decalage_bas(jetons, index, joueur):
    colonne_originale = []
    
    # Extraction des valeurs originales des jetons
    for ligne in jetons:
        colonne_originale.append(ligne[index])
    
    # Décalage des valeurs des jetons
    nouvelle_colonne = decalage_droite(colonne_originale, 0, joueur, False)
    
    # Remplacement des valeurs des jetons dans la matrice
    for ligne in range(len(jetons)):
        jetons[ligne][index] = nouvelle_colonne[ligne]

def dessiner_fleche(fleche, couleur):
    for rect in range(len(fleche)):
        fill_rectangle(fleche[rect][0],
                       fleche[rect][1],
                       fleche[rect][2],
                       fleche[rect][3],
                       couleur)

def dessiner_jetons(jetons):
    for ligne in range(len(jetons)):
        for jeton in range(len(jetons[ligne])):
            if jetons[ligne][jeton] == 1:
                fill_rectangle(jeton * 8 + 8,
                               ligne * 8 + 8,
                               7, 7, rouge)
            elif jetons[ligne][jeton] == 2:
                fill_rectangle(jeton * 8 + 8,
                               ligne * 8 + 8,
                               7, 7, vert)
            else:
                fill_rectangle(jeton * 8 + 8,
                               ligne * 8 + 8,
                               7, 7, noir)
                                
def dessiner_ligne(ligne, couleur):
    for rect in range(len(ligne)):
        fill_rectangle(ligne[rect][0],
                       ligne[rect][1],
                       ligne[rect][2],
                       ligne[rect][3],
                       couleur)

def chercher_ligne(grille, index, horizontal):
    if horizontal:
        return grille.horiz[index]
    else:
        return grille.verti[index]
       
def chercher_fleche(fleches, index, position):
    # L'index de position tourne en sens horloge (haut = 0, droite = 1,...)
    if position == 0:
        return fleches.haut[index]
    elif position == 2:
        return fleches.bas[index]
    elif position == 1:
        return fleches.droite[index]
    elif position == 3:
        return fleches.gauche[index]

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