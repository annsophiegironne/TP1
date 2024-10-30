# Auteurs: Ann-Sophie Gironne et Oscar Parent
# Date: 20 octobre 2024
# Matricules: 20153433 et 20273034
#
# TODO: Écrire la description du programme
# TODO: Changer scale à 4 dans glisse() quand fini


# Couleurs et codes RGB associés
blanc = "#fff"
gris = "#444"
rouge = "#f00"
vert = "#0f0"
jaune = "#770"
noir = "#000"

from tp1 import *

# Inverse la matrice en mettant la colonne 1 à la position de la rangée 1
# et ainsi de suite. Permet de vérifier les colonnes comme des rangées

def inverser_matrice(matrice):
    format = len(matrice)
    colonne = []
    matrice_inverse = []
   
    for x in range(format):
        for y in range(format):
            colonne.append(matrice[y][x])
        matrice_inverse.append(colonne)
        colonne = []
   
    return matrice_inverse

def copie_matrice(matrice):
    copie = []
    for ligne in matrice:
        nouvelle_ligne = []
        for valeur in ligne:
            nouvelle_ligne.append(valeur)
        copie.append(nouvelle_ligne)
    return copie

def verifier_configuration(memoire_jetons, jetons):
    cols = inverser_matrice(jetons)
   
    format = len(jetons)
   
    config_existante = False
 
    for config in memoire_jetons:
        cols_config = inverser_matrice(config)
        for index in range(format):
            if cols[index] == cols_config[index] and 0 not in cols[index]:
                return True
            elif jetons[index] == config[index] and 0 not in jetons[index]:
                return True
            else:
                continue
    return False

       

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

def ajouter_jeton(jetons, index, position, joueur, format):
    # La position tourne en sens horloge (haut = 0, droite = 1, ...)
    if position == 0:
       
        if remplie_verti(jetons, index, format):
            decalage_bas(jetons, index, joueur)
        else:
            ajout_verti(jetons, index, joueur, 0)
       
       
    elif position == 1:
       
        if remplie_horiz(jetons, index, format):   
            decalage_gauche(jetons, index, joueur, True)
        else:
            ajout_horiz(jetons, index, joueur, 1)
       
    elif position == 2:
       
        if remplie_verti(jetons, index, format):
            decalage_haut(jetons, index, joueur)
        else:
            ajout_verti(jetons, index, joueur, 2)
       
    elif position == 3:
       
        if remplie_horiz(jetons, index, format):
            decalage_droite(jetons, index, joueur, True)
        else:
            ajout_horiz(jetons, index, joueur, 3)
       
    dessiner_jetons(jetons)
    return jetons


def remplie_horiz(jetons, index, format):
    compteur = 0
   
    for jeton in jetons[index]:
        if jeton == 1 or jeton == 2:
            compteur += 1
           
    if compteur == format:
        return True
    else:
        return False
       
   
def remplie_verti(jetons, index, format):
    colonne_originale = []
    compteur = 0
   
    # Extraction des valeurs originales des jetons
    for ligne in jetons:
        colonne_originale.append(ligne[index])
   
    for jeton in colonne_originale:
        if jeton == 1 or jeton == 2:
            compteur += 1
   
    return True if compteur == format else False

   
"""
TODO delete this comment after refactoring into
multiple functions


ok first of all sry for this mess of a function
but ajout_horiz et ajout_verti work the same heres how:


this just consists of moving the whole row by 1 (left or right)
based on a few conditions

    1. it won't overwrite a jeton/its being shifted to an empty
        space
    2. if a jeton is is surrounded by empty spaces it caused this
        undefined behavior:

        [1, 0, 0, 2, 0, 0, 1]
        + 1 on the left should give us:

        [1, 1, 0, 2, 0, 0, 1]

        but it gave:

        [1, 1, 0, 0, 2, 0, 1]

        so thats what the big if statement
        is checking.

    3. if a jeton is on an edge, don't move it

    that's basically it its just cloned 4x with slightly
    diff values to account for different sides

   
"""
   
def ajout_horiz(jetons, index, joueur, cote):
    ligne = jetons[index]
   
    if cote == 1:
        temp = 1
       
        while temp <= len(ligne) - 1:
            if ligne[temp] == 0:
                temp += 1
                continue
            if ligne[temp] == 1 or ligne[temp] == 2:
                print(temp)
               
                if (temp < len(ligne) -1 and
                   (ligne[temp - 1] != 0 or
                    ligne[temp + 1] == 0)):
                    temp += 1
                    continue
               
                ligne[temp - 1] = ligne[temp]
                ligne[temp]     = 0
               
                temp += 1
               
        ligne[len(ligne)-1] = joueur
      
    if cote == 3:
       
        temp = len(ligne) - 2
       
        while temp >= 0:
           
            if ligne[temp] == 0:
                temp -= 1
                continue
            if ligne[temp] == 1 or ligne[temp] == 2:
                if (temp > 0             and
                   (ligne[temp + 1] != 0 or
                    ligne[temp - 1] == 0)):
                    temp -= 1
                    continue
               
                ligne[temp + 1] = ligne[temp]
                ligne[temp]     = 0
               
                temp -= 1
       
        ligne[0] = joueur
               
       
#TODO split en plusieurs fonctions
       
def ajout_verti(jetons, index, joueur, cote):
    ligne = []

    for jet in jetons:
        ligne.append(jet[index])

    if cote == 2:
        temp = 1

        while temp <= len(ligne) - 1:
            if ligne[temp] == 0:
                temp += 1
                continue
            if ligne[temp] == 1 or ligne[temp] == 2:
                if (temp < len(ligne) - 1 and
                   (ligne[temp - 1] != 0 or
                    ligne[temp + 1] == 0)):
                    temp += 1
                    continue

                ligne[temp - 1] = ligne[temp]
                ligne[temp] = 0

                temp += 1

        ligne[len(ligne) - 1] = joueur

        for i in range(len(jetons)):
            jetons[i][index] = ligne[i]

    if cote == 0:

        temp = len(ligne) - 2

        while temp >= 0:

            if ligne[temp] == 0:
                temp -= 1
                continue
            if ligne[temp] == 1 or ligne[temp] == 2:
                if (temp > 0 and
                   (ligne[temp + 1] != 0 or
                    ligne[temp - 1] == 0)):
                   
                    temp -= 1
                    continue

                ligne[temp + 1] = ligne[temp]
                ligne[temp] = 0

                temp -= 1

        ligne[0] = joueur
        for i in range(len(jetons)):
            jetons[i][index] = ligne[i]

   
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
   
# Identifie la flèche survolée par la souris en fonction de la position
# sur la grille

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
   
   
   
# Fonction responsable de changer la couleur des lignes/flèches survolées
# et de jouer un son lorsque survolées par la souris. La fonction
# utilise ses états précédents pour se "rappeler" des ancients états       

def surveiller_survol(dims, fleches, grille, souris, beep, etat_precedent):  
    # Surveille le survol et met à jour si nécessaire
    derniere_fleche, derniere_ligne = etat_precedent

    # Identifie la flèche/ligne survolée
    fleche_surv, ligne_surv = identifier_fleche(dims, fleches, grille, souris)

    # Si flèche/ligne survolée change
    if fleche_surv != derniere_fleche or ligne_surv != derniere_ligne:
       
        # Permettre au son de jouer
        beep = True
       
        # Réinitialiser la dernière flèche/ligne survolée
        if derniere_fleche != -1:
            dessiner_fleche(derniere_fleche, jaune)
          
        if derniere_ligne != -1:
            dessiner_ligne(derniere_ligne, gris)
           

        # Dessiner nouvelle fleche
        if fleche_surv != -1:
            dessiner_fleche(fleche_surv, blanc)
           
        if ligne_surv != -1:
            dessiner_ligne(ligne_surv, blanc)
    
    # Vérifie que le son a le droit de jouer et ensuite l'interdit de jouer
    # jusqu'à temps qu'une nouvelle flèche se fasse survoler
    if beep is True and fleche_surv != -1 and ligne_surv != -1:
        son_survol_fleche()
        sleep(0.1)
        beep = False
   
    # Retourne l'état pour prochaine itération
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


## Permet de dessiner le carré du joueur dans le coin gauche
   
def dessiner_joueur(joueur):
    couleur = rouge if joueur == 1 else vert
    fill_rectangle(1, 1, 5, 5, couleur)

# Initialise la grille avec tous les aspects visuels

def remplir_grille_initiale(dims):
    grille =  initialisation_grille(dims)
    dessiner_grille(dims, grille, gris) 
    dessiner_joueur(1)
    fleches = initialisation_fleches(dims, jaune)
   
# Initialise les positions des jetons, des flèches et de la grille
# et les stocke dans des objets pour y accéder

def initialisation_objets(dims):
    jetons = initialisation_jetons(dims)
    fleches = initialisation_fleches(dims, jaune)
    grille = initialisation_grille(dims)
    return jetons, fleches, grille

def initialisation_ecran_de_jeu(format):
    dims = taille_de_la_grille(format)
    set_screen_mode(dims.largeur, dims.hauteur, 5)
   
    return dims
   

def defaite(dims, grille, joueur):
    musique_triste()
    dessiner_grille(dims, grille, rouge if joueur == 1 else vert)
    sleep(3)
   
    # unfinished
def glisse(format):   #TODO abstract away the inits to an init function

    #       INIT
    print("init")
    dims = initialisation_ecran_de_jeu(format)
    jetons, fleches, grille = initialisation_objets(dims)
    remplir_grille_initiale(dims)

    partie_en_cours = True
    joueur = 1 # Tour du joueur (1 ou 2)
    etat_prec = (-1, -1)
    beep = False
    memoire_jetons = []
   
    # Boucle de jeu principale
    while partie_en_cours:  
        sleep(0.1)
        # Gère les entrées (déplacement de la souris)
        souris = get_mouse()
   
        # Gère les mises à jour des états
        etat_prec, beep  = surveiller_survol(dims,
                                      fleches,
                                      grille,
                                      souris,
                                      beep,
                                      etat_prec)
        selection = etat_prec[0]
          
        if souris.button:
            jouer_tour(selection, jetons, dims, joueur, souris, format)
            config_existante = verifier_configuration(memoire_jetons, jetons)
            for config in memoire_jetons:
                print(config)

            if config_existante:
                defaite(dims, grille, joueur)
                break
            else:
                copie = copie_matrice(jetons)
                memoire_jetons.append(copie)
            joueur = 1 if joueur == 2 else 2
            dessiner_joueur(joueur)
           
           # print(jetons)
            #print(remplie_verti(jetons, 4 ,format))

        #TODO add check victory function


def jouer_tour(ligne, jetons, dims, joueur, souris, format):
   
    position = obtenir_cote(dims, souris)
   
    if souris.button:
        if ligne is not None and ligne[0] is not None:
            horiz = (position == 1 or position == 3)
            index = (ligne[0][horiz] // 8) - 1
            ajouter_jeton(jetons, index, position, joueur, format)
            son_coup()

   
# Retourne le côté survolé par la souris
def obtenir_cote(dims, souris):
    x = souris.x
    y = souris.y
   
   
    if x + 1 <= 8 and 8 <= y + 1 <= dims.hauteur - 8:
        return 3
    if 8 <= x - 1 <= dims.largeur and y - 1 >= dims.hauteur - 8:
        return 2
    if x - 1 >= dims.largeur - 8 and 8 <= y - 1 <= dims.hauteur - 8:
        return 1
    if 8 <= x + 1 <= dims.largeur and y + 1 <= 8:
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


       
glisse(4)


# TODO: Supprimer quand on aura fini
dims = taille_de_la_grille(4)
jetons = initialisation_jetons(dims)
fleches = initialisation_fleches(dims, jaune)
grille = initialisation_grille(dims)