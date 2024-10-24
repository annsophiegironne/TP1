# Auteurs: Ann-Sophie Gironne et Oscar Parent
# Date: 20 octobre 2024
# Matricules: 20153433 et 20273034
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



# Retourne une struct avec membres largeur et hauteur à partir du format donné

def taille_de_la_grille(format):
    if format == 4:
        dims = struct(largeur = 47, hauteur = 47)
    elif format > 4:
        nouveaux_pixels = (format - 4) * 8
        dims = struct(largeur = 47 + nouveaux_pixels,
                      hauteur = 47 + nouveaux_pixels)
    return dims


# Retourne une matrice de rectangles affichables à l'écran pour les 
# flèches du haut

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


# Retourne une matrice de rectangles affichables à l'écran pour les 
# flèches du bas

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


# Retourne une matrice de rectangles affichables à l'écran pour les 
# flèches du côté gauche

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


# Retourne une matrice de rectangles affichables à l'écran pour les 
# flèches du côté droit

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


# Retourne une matrice "fleches" composée des positions des flèches
# des quatres côtés à afficher 

def initialisation_fleches(dims, couleur):
    nb_fleches = (dims.largeur - 14) // 8
    
    haut = []; bas = []; gauche = []; droite = []
    
    for decalage in range(nb_fleches):
        # Appel aux fonctions respectives pour chaque flèche
        haut.append(fleches_haut(decalage * 8, couleur))
        bas.append(fleches_bas(decalage * 8, dims, couleur))
        gauche.append(fleches_gauche(decalage * 8, couleur))
        droite.append(fleches_droite(decalage * 8, dims, couleur))
        
    fleches = struct(haut = haut,
                     bas = bas,
                     droite = droite,
                     gauche = gauche)
    return fleches
 
    
# Retourne une matrice de format NxN initialisée avec chaque élement
# égal à zéro    

def creer_matrice(format):
    matrice = [None] * format
    
    for i in range(format):
        matrice[i] = [0] * format
    
    return matrice
  
    
# Retourne une matrice des lignes horizontales
    
def lignes_horizontales(dims, y, couleur):
    x = dims.largeur
    ligne = ([7, 7 + y, x - 15, 1],     # haut
             [7, 15 + y, x - 15, 1],    # bas
             [7, 7 + y, 1, 9],          # gauche
             [x - 8, 7 + y, 1, 9])      # droite

    return ligne


# Retourne une matrice des lignes verticales

def lignes_verticales(dims, x, couleur):
    y = dims.hauteur
    ligne = ([7 + x, 7, 9, 1],           # haut
             [7 + x, y - 8, 9, 1],       # bas
             [7 + x, 7, 1, y - 15],      # gauche
             [15 + x, 7, 1, y - 15])     # droite
    
    return ligne
  
    
# Retourne une grille initialisée avec les positions des lignes verticales
# et horizontales

def initialisation_grille(dims, couleur):
    nb_lignes = (dims.largeur - 14) // 8
    
    horiz = []; verti = []
    
    for decalage in range(nb_lignes):
        horiz.append(lignes_horizontales(dims, decalage * 8, couleur))
        verti.append(lignes_verticales(dims, decalage * 8, couleur))

    grille = struct(horiz = horiz, verti = verti)
    
    return grille


# Initialisation de la matrice permettant de garder en mémoire la position
# des jetons

def initialisation_jetons(dims):
    taille_matrice = (dims.largeur - 14) // 8
    jetons = creer_matrice(taille_matrice)
    return jetons


# Permet d'ajouter un jeton à différentes positions en fonction du joueur
# et décale la matrice des positions des jetons en conséquence

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
    
    
# Décale une rangée de la matrice des jetons vers la gauche
    
def decalage_gauche(jetons, index, joueur, matrice):
    if matrice:
        # Décale une ligne dans la matrice complète
        nouvelle_ligne = jetons[index][1:] + [joueur]
        jetons[index] = nouvelle_ligne

    else:
        # Décale une ligne donnée
        ligne_decalee = jetons[1:] + [joueur]
        return ligne_decalee

    
# Décale une rangée de la matrice des jetons vers la droite
    
def decalage_droite(jetons, index, joueur, matrice):
    if matrice:
        # Décale une ligne dans la matrice complète
        nouvelle_ligne = [joueur] + jetons[index][:-1]
        jetons[index] = nouvelle_ligne

    else:
        # Décale une ligne donnée
        ligne_decalee = [joueur] + jetons[:-1]
        return ligne_decalee

    
# Décale une colonne de la matrice des jetons vers le haut
    
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
        
        
# Décale une colonne de la matrice des jetons vers le bas

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

        
# Dessine une flèche donnée sur la grille
        
def dessiner_fleche(fleche, couleur):
    for rect in range(len(fleche)):
        fill_rectangle(fleche[rect][0],
                       fleche[rect][1],
                       fleche[rect][2],
                       fleche[rect][3],
                       couleur)

        
# Prend la matrice des jetons et affiche les couleurs des jetons à l'écran
        
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
    
    
# Prend les dimensions et une grille en entrée, puis affiche la grille 
# à l'écran

def dessiner_grille(dims, grille):
    nb_lignes = (dims.largeur - 14) // 8
    
    for i in range(nb_lignes):
        dessiner_ligne(grille.horiz[i], gris)
        dessiner_ligne(grille.verti[i], gris)
        
        
# Prend les positions d'une ligne (rangée/colonne) donnée et affiche à l'écran

def dessiner_ligne(ligne, couleur):
    for rect in range(len(ligne)):
        fill_rectangle(ligne[rect][0],
                       ligne[rect][1],
                       ligne[rect][2],
                       ligne[rect][3],
                       couleur)

        
# Retourne la ligne horizontale de la grille située à un index donné
        
def hori_chercher_ligne(grille, index): return grille.horiz[index]


# Retourne la ligne verticale de la grille située à un index donné

def vert_chercher_ligne(grille, index): return grille.verti[index]

## Retourne la position d'une flèche à un index donné

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

## Permet de dessiner le carré du joueur dans le coin gauche
    
def dessiner_joueur(couleur):
    fill_rectangle(1, 1, 5, 5, couleur)

## Initialise la grille avec tous les aspects visuels

def remplir_grille_initiale(dims):
    grille =  initialisation_grille(dims, gris)
    dessiner_grille(dims, grille)  
    dessiner_joueur(rouge)
    fleches = initialisation_fleches(dims, jaune)
    
# Fonction principale
    
def glisse(format):
    dims = taille_de_la_grille(format)
    set_screen_mode(dims.largeur, dims.hauteur, 6) ### mettre à 4 quand fini 
    remplir_grille_initiale(dims)

# Fonction générale permettant de faire jouer un son
    
def son(duree, frequence):
    beep(duree, frequence)
    
# Encode le son pour quand on survole la flèche    
    
def survol_fleche():
    son(0.025, 1500)

# Encode le son pour quand un coup est joué    
    
def son_coup():
    son(0.15, 2000)

    
## Encode les sons pour la musique triste    
    
def musique_triste():
    son(0.1, 1000)
    son(0.1, 900)
    son(0.1, 800)
    son(0.1, 700)
    son(0.1, 600)
    son(0.1, 500)
    son(0.75, 100)
    
    
## Encode les sons pour la musique joyeuse
    
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