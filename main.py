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
    
def lignes_horizontales(dims, y):
    x = dims.largeur
    ligne = ([7, 7 + y, x - 15, 1],     # haut
             [7, 15 + y, x - 15, 1],    # bas
             [7, 7 + y, 1, 9],          # gauche
             [x - 8, 7 + y, 1, 9])      # droite

    return ligne


# Retourne une matrice des lignes verticales

def lignes_verticales(dims, x):
    y = dims.hauteur
    ligne = ([7 + x, 7, 9, 1],           # haut
             [7 + x, y - 8, 9, 1],       # bas
             [7 + x, 7, 1, y - 15],      # gauche
             [15 + x, 7, 1, y - 15])     # droite
    
    return ligne
  
    
# Retourne une grille initialisée avec les positions des lignes verticales
# et horizontales

def initialisation_grille(dims):
    nb_lignes = (dims.largeur - 14) // 8
    
    horiz = []; verti = []
    
    for decalage in range(nb_lignes):
        horiz.append(lignes_horizontales(dims, decalage * 8))
        verti.append(lignes_verticales(dims, decalage * 8))

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
    if fleche is not None:
        for rect in range(len(fleche)):
            fill_rectangle(fleche[rect][0],
                           fleche[rect][1],
                           fleche[rect][2],
                           fleche[rect][3],
                           couleur)
    
#TODO
def identifier_fleche(dims, fleches, grille, souris):
    x = (souris.x + 1) // 8
    y = (souris.y + 1) // 8
    
    format = (dims.largeur // 8) - 1
    
    fleche = None
    ligne = None
    
    if x == 0 and 0 < y <= format:          # Flèche à gauche
        fleche = fleches.gauche[y - 1]
        ligne = grille.horiz[y - 1]
    if x == format + 1 and 0 < y <= format: # Flèche à droite
        fleche = fleches.droite[y - 1]
        ligne = grille.horiz[y - 1]
    if y == 0 and 0 < x <= format:          # Flèche en haut
        fleche = fleches.haut[x - 1]
        ligne = grille.verti[x - 1]
    if y == format + 1 and 0 < x <= format: # Flèche en bas
        fleche = fleches.bas[x - 1]
        ligne = grille.verti[x - 1]
        
    return fleche, ligne if fleche is not None else -1

# Vérifie la position de la souris sur la grille en temps réel et
# colore les flèches/lignes survolées en blanc


            
# Prend la matrice des jetons et affiche les couleurs des jetons à l'écran
        
def dessiner_jetons(jetons):
    for ligne in range(len(jetons)):
        for jeton in range(len(jetons[ligne])):
            if jetons[ligne][jeton] == 1:
                fill_rectangle((jeton + 1) * 8 + 1,
                               (ligne + 1) * 8 + 1,
                               5, 5, rouge)
            elif jetons[ligne][jeton] == 2:
                fill_rectangle((jeton + 1) * 8 + 1,
                               (ligne + 1) * 8 + 1,
                               5, 5, vert)
            else:
                fill_rectangle((jeton + 1) * 8 + 1,
                               (ligne + 1) * 8 + 1,
                               5, 5, noir)
    
    
    
# Fonction résponsable de changer la couleur des lignes/fleches survolées
# et de jouer un son quand survolées par la souris
# utilise ses états précédants pour se "rapeller" des ancients états        
def surveiller_survol(dims, fleches, grille, souris, beep, etat_precedent):
    # Surveille le survol, met à jour si nécessaire
    derniere_fleche, derniere_ligne = etat_precedent

    # Identifie fleche/ligne survolée
    fleche_surv, ligne_surv = identifier_fleche(dims, fleches, grille, souris)

    # Si flèche/ligne survolée change
    if fleche_surv != derniere_fleche or ligne_surv != derniere_ligne:
        
        # Permettre son de jouer
        beep = True
        
        # Re-init la derniere fleche/ligne survolée
        if derniere_fleche != -1:
            dessiner_fleche(derniere_fleche, jaune)
           
        if derniere_ligne != -1:
            dessiner_ligne(derniere_ligne, gris)
            

        # Dessiner nouvelle fleche 
        if fleche_surv != -1:
            dessiner_fleche(fleche_surv, blanc)
            
        if ligne_surv != -1:
            dessiner_ligne(ligne_surv, blanc)
     
    # Verifie que le son a le droit de jouer et ensuite l'interdit de jouer
    # jusqu'à temps qu'une nouvelle fleche se fasse survolée
    if beep is True:
        son_survol_fleche()
        sleep(0.1)
        beep = False
    
    

    # Return l'état pour prochaine itération
    return (fleche_surv, ligne_surv), beep
    
# Prend les dimensions et une grille en entrée, puis affiche la grille 
# à l'écran

def dessiner_grille(dims, grille, couleur):
    nb_lignes = (dims.largeur - 14) // 8
    
    for i in range(nb_lignes):
        dessiner_ligne(grille.horiz[i], couleur)
        dessiner_ligne(grille.verti[i], couleur)
        
        
# Prend les positions d'une ligne (rangée/colonne) donnée et affiche à l'écran

def dessiner_ligne(ligne, couleur):
    for rect in range(len(ligne)):
        fill_rectangle(ligne[rect][0],
                       ligne[rect][1],
                       ligne[rect][2],
                       ligne[rect][3],
                       couleur)

        
# Retourne la ligne horizontale de la grille située à un index donné
        
def horiz_chercher_ligne(grille, index): return grille.horiz[index]


# Retourne la ligne verticale de la grille située à un index donné

def verti_chercher_ligne(grille, index): return grille.verti[index]

## Retourne la position d'une flèche à un index donné
## POTENTIELLEMENT INUTILE !!!
def retourner_fleche(fleches, index, position):
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
    grille =  initialisation_grille(dims)
    dessiner_grille(dims, grille, gris)  
    dessiner_joueur(rouge)
    fleches = initialisation_fleches(dims, jaune)

# Attend le prochain clic et retourne la position de la souris 
# au moment du clic

def attendre_clic():
    # Quand le bouton est pressé, attendre qu'il ne le soit plus
    while True:
        souris = get_mouse()
        if souris.button == 0: break
        sleep(0.01) # Fluidité de l'interface
     
    # Quand le bouton n'est pas pressé, attendre qu'il le soit
    while True:
        souris = get_mouse()
        if souris.button != 0: break
        sleep(0.01) # Fluidité de l'interface
        
    return souris
   
# Fonction principale du jeu de glisse
    
def glisse(format):
    dims = taille_de_la_grille(format)
    set_screen_mode(dims.largeur, dims.hauteur, 6) ### mettre à 4 quand fini 
    remplir_grille_initiale(dims)
    fleches = initialisation_fleches(dims, noir)
    grille = initialisation_grille(dims)
    

    # unfinished
def mainGameLoop(format):   #TODO abstract away the inits to an init function

    #       INIT
    print("init")
    dims = taille_de_la_grille(format)
    set_screen_mode(dims.largeur, dims.hauteur, 5)
    jetons = initialisation_jetons(dims)
    fleches = initialisation_fleches(dims, jaune)
    grille = initialisation_grille(dims)


    remplir_grille_initiale(dims)

    partie_en_cours = True
    joueur = 1 # Tour du joueur (1 ou 2)
    etat_prec = (-1, -1)
    beep = False
    
    
    #       BOUCLE DE JEU PRINCIPAlE
    while partie_en_cours:   
        sleep(0.2)
    #       INPUTS
        souris = get_mouse()
    
    #       UPDATES
        etat_prec, beep  = surveiller_survol(dims, 
                                      fleches, 
                                      grille, 
                                      souris,
                                      beep,
                                      etat_prec)
        selection = etat_prec[0]
       
        jouer_tour(selection, jetons, dims, joueur, souris)
    
        if souris.button:
            print(jetons)
       # dessiner_jetons(jetons)                            

        #TODO add player turn function
        #TODO add check victory function


def jouer_tour(ligne, jetons, dims, joueur, souris):
    
    position = obtenir_cote(dims, souris)
    
    if souris.button:
        if ligne is not None and ligne[0] is not None:
            
            if position == 1 or position == 3:
                index = (ligne[0][1] // 8) - 1
                ajouter_jeton(jetons, index, position, joueur )
                son_coup()
            if position == 0 or position == 2:
                index = (ligne[0][0] // 8) - 1
                ajouter_jeton(jetons, index, position, joueur)
                son_coup()
    
def obtenir_cote(dims, souris):
    x = souris.x
    y = souris.y
    
    
    if x <= 8 and 8 <= y <= dims.hauteur - 8:
        return 3
    if 8 <= x <= dims.largeur and y >= dims.hauteur - 8:
        return 2
    if x >= dims.largeur - 8 and 8 <= y <= dims.hauteur - 8:
        return 1
    if 8 <= x <= dims.largeur and y <= 8:
        return 0

    
    

# Fonction générale permettant de faire jouer un son
    
def son(duree, frequence):
    beep(duree, frequence)
    
# Encode le son pour quand on survole la flèche    
    
def son_survol_fleche():
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


        
#glisse(4)

mainGameLoop(6)

# TODO: Supprimer quand on aura fini
dims = taille_de_la_grille(4)
jetons = initialisation_jetons(dims)
fleches = initialisation_fleches(dims, jaune)
grille = initialisation_grille(dims)


##### Permet juste de tester le clic pour l'instant
#while True:
#    surveiller_survol(dims, fleches, grille)
    #souris = attendre_clic()
    #fleche = identifier_fleche(dims, fleches, souris)
    #if fleche != -1:
    #    son_coup() # Génère un son quand un coup est joué
    #    dessiner_fleche(fleche, blanc)
        
        



# coup = struct(ligne = ligne, fin = booléen)
# jouer_coup(grille, coup, joueur)
# joueur1 = rouge, joueur2 = vert