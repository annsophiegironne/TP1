# Auteurs: Ann-Sophie Gironne et Oscar Parent
# Date: 20 octobre 2024
# Matricules: 20153433 et 20273034
#
# Ce programme encode un jeu sur ordinateur pour 2 personnes, 
# le jeu de "glisse". Le principe est similaire au tic tac toe, le joueur
# qui remplit le plus de lignes gagne la partie. Le joueur peut ajouter son
# jeton sur la grille en cliquant sur les flèches des quatre côtés. Attention
# à ne pas répéter des configurations précédentes! Le jeu de glisse fonctionne
# pour des grilles de 4x4, 5x5 et 6x6.

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


# Fait une copie d'une matrice qui est par la suite modifiée
def copie_matrice(matrice):
    copie = []
    for ligne in matrice:
        nouvelle_ligne = []
        for valeur in ligne:
            nouvelle_ligne.append(valeur)
        copie.append(nouvelle_ligne)
    return copie


# Cette fonction parcourt les configurations précédentes pour s'assurer que
# le joueur ne répète pas les mêmes mouvements. Elle vérifie que le coup
# joué par le joueur ne reproduit ni une ligne ni une colonne déjà
# présentes dans les configurations précédentes au même index.
def verifier_memoire(memoire, jetons, cote, index):
    cols = inverser_matrice(jetons)
    format = len(jetons)
   
    for config in memoire:
        cols_config = inverser_matrice(config)
        if cote in [1,3]:
            if config[index] == jetons[index] and 0 not in jetons[index]:
                return True
            elif cols_config[-(2 - cote)] == cols[-(2 - cote)]:
                if 0 not in cols[-(2 - cote)]:
                    return True
        else:
            if cols_config[index] == cols[index] and 0 not in cols[index]:
                return True
            elif cote == 2:
                if config[3] == jetons[3] and 0 not in config[3]:
                    return True
            elif cote == 0:
                if config[0] == jetons[0] and 0 not in config[0]:
                    return True
    return False
     

# Cette fonction est responsable de vérifier si le coup joué entraîne la
# victoire du joueur. Le nombre de lignes/colonnes pleines sont comptabilisées
# pour chaque joueur. La fonction retourne l'index de la ligne gagnante (ou
# les index lorsque plus d'une ligne est remplie), de même que le joueur
# gagnant
def verifier_victoire(jetons):
    # Inversion de la matrice pour la vérification des colonnes
    cols = inverser_matrice(jetons)
   
    # Extraction du format de la matrice pour simuler une ligne gagnante
    format = len(jetons)
  
    # Stocke les index des lignes pleines
    lignes_horiz1 = []
    lignes_horiz2 = []
    lignes_verti1 = []
    lignes_verti2 = []
  
    # Comptabilise les lignes remplies par chaque joueur
    compteur1 = 0
    compteur2 = 0
  
    # Identification des rangées/colonnes pleines un index à la fois
    for index in range(format):
        if jetons[index] == [1] * format:
            lignes_horiz1.append(index)
            compteur1 += 1
        elif jetons[index] == [2] * format:
            lignes_horiz2.append(index)
            compteur2 += 1
        elif cols[index] == [1] * format:
            lignes_verti1.append(index)
            compteur1 += 1
        elif cols[index] == [2] * format:
            lignes_verti2.append(index)
            compteur2 += 1

    # Retourne le joueur gagnant et les index des lignes gagnantes
    if compteur1 > compteur2:
        return 1, lignes_verti1, lignes_horiz1
    elif compteur2 > compteur1:
        return 2, lignes_verti2, lignes_horiz2
    else:
        return -1, [], []
      

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
# flèches du haut et du bas
def fleches_haut_bas(x, dims, orientation):
    ajust = dims.hauteur
   
    # Définit l'ajustement en y en fonction de l'orientation de la flèche
    if orientation == "h":
        y = [2, 3, 4, 3, 2]
    elif orientation == "b":
        y = [ajust - 4, ajust - 5, ajust - 6, ajust - 5, ajust - 4]
   
    # Les ajustements en x et y permettent de dessiner les autres flèches
    fleche = ([9 + x, y[0], 1, 2],       # barre 1
              [10 + x, y[1], 1, 2],      # barre 2
              [11 + x, y[2], 1, 2],      # barre 3
              [12 + x, y[3], 1, 2],      # barre 4
              [13 + x, y[4], 1, 2])      # barre 5
   
    return fleche

# Retourne une matrice de rectangles affichables à l'écran pour les
# flèches du côté gauche et droite
def fleches_gauche_droite(y, dims, orientation):
    ajust = dims.largeur
   
    if orientation == "g":
        x = [2, 3, 4, 3, 2]
    elif orientation == "d":
        x = [ajust - 4, ajust - 5, ajust - 6, ajust - 5, ajust - 4]
   
   
    # Positions de la première flèche en haut à gauche
    # Les ajustements en x et y permettent de dessiner les autres flèches
    fleche = ([x[0], 9 + y, 2, 1],    # barre 1
              [x[1], 10 + y, 2, 1],   # barre 2
              [x[2], 11 + y, 2, 1],   # barre 3
              [x[3], 12 + y, 2, 1],   # barre 4
              [x[4], 13 + y, 2, 1])   # barre 5
   
    return fleche


# Retourne une struct "fleches" composée des positions des flèches
# des quatres côtés à afficher
def initialisation_fleches(dims, couleur):
    nb_fleches = (dims.largeur - 14) // 8
  
    haut = []; bas = []; gauche = []; droite = []
  
    for decalage in range(nb_fleches):
        # Appel aux fonctions respectives pour chaque flèche
        haut.append(fleches_haut_bas(decalage * 8, dims, "h"))
        bas.append(fleches_haut_bas(decalage * 8, dims, "b"))
        gauche.append(fleches_gauche_droite(decalage * 8, dims, "g"))
        droite.append(fleches_gauche_droite(decalage * 8, dims, "d"))
   
    # Objet avec les coordonnées de toutes les flèches
    fleches = struct(haut = haut,
                     bas = bas,
                     droite = droite,
                     gauche = gauche)
   
    # Dessiner toutes les flèches dans une couleur donnée
    dessiner_toutes_fleches(dims, fleches, jaune)

    return fleches
 
    
# Permet de dessiner toutes les flèches d'un coup pour une couleur donnée    
def dessiner_toutes_fleches(dims, fleches, couleur):
    nb_fleches = (dims.largeur - 14) // 8

    for index in range(nb_fleches):
        dessiner_fleche(fleches.haut[index], couleur)
        dessiner_fleche(fleches.bas[index], couleur)
        dessiner_fleche(fleches.gauche[index], couleur)
        dessiner_fleche(fleches.droite[index], couleur)

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
    remplie = [remplie_verti, remplie_horiz] * 2
    decalage = [decalage_bas, decalage_gauche, decalage_haut, decalage_droite]
    ajout = [ajout_verti, ajout_horiz] * 2
   
    matrice = (position in [1,3])
    # La position tourne en sens horloge (haut = 0, droite = 1, ...)
    # Vérifie si la ligne est remplie et si oui, décaler les valeurs
    if remplie[position](jetons, index):
        decalage[position](jetons, index, joueur, matrice)
    else:
        ajout[position](jetons, index, joueur, position)
           
    dessiner_jetons(jetons)


# Vérifie si la ligne horizontale à l'index donné est pleine
def remplie_horiz(jetons, index):
    return False if 0 in jetons[index] else True

# Vérifie si la ligne verticale à l'index donné est pleine          
def remplie_verti(jetons, index):
    jetons_inverse = inverser_matrice(jetons)
    return remplie_horiz(jetons_inverse, index)

 
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
# Le paramètre matrice n'est pas utilisé, il sert à uniformiser l'utilisation
# des fonctions de décalage
def decalage_haut(jetons, index, joueur, matrice):
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
# Le paramètre matrice n'est pas utilisé, il sert à uniformiser l'utilisation
# des fonctions de décalage
def decalage_bas(jetons, index, joueur, matrice):
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



# Ajoute un jeton dans une case quand une des flèches horizontales est activée
def ajout_horiz(jetons, index, joueur, cote):
    ligne = jetons[index]
  
    if cote == 1: logique_droite(ligne, joueur)
     
    if cote == 3: logique_gauche(ligne, joueur)


# Ajoute un jeton dans une case quand une des flèches verticales est activée
def ajout_verti(jetons, index, joueur, cote):
    ligne = []

    for jet in jetons:
        ligne.append(jet[index])

    if cote == 2: logique_bas(ligne, joueur, jetons, index)

    if cote == 0: logique_haut(ligne, joueur, jetons, index)


# Les fonctions logique_droite et logique_gauche fonctionnent
# de la même manière, la seule différence est le sens de l'opération.
# (gauche à droite ou droite à gauche)
# Elles sont responsables d'appliquer les changements sur la grille pour 
# chaque jeton placé. 
def logique_droite(ligne, joueur):
    
    length = len(ligne)-1
    
    if ligne[length] == 0:
        ligne[length] = joueur
        return
    
    
    temp = 1 
    
    # Cet algorithme ignore la première case puis 
    # vérifie que s'il y a un jeton sur une case 
    # qui n'est pas entourée de cases vides, alors, 
    # déplace le jeton à la prochaine case.
    # Ce processus est répété pour l'entièreté de la ligne.
    while temp <= length:
        if ligne[temp] == 0:
            temp += 1
            continue
        if ligne[temp] == 1 or ligne[temp] == 2:
            if (temp < length and
               (ligne[temp - 1] != 0 or
                ligne[temp + 1] == 0)):
                temp += 1
                continue
            
            # Déplace le jeton 
            ligne[temp - 1] = ligne[temp]
            ligne[temp]     = 0
          
            temp += 1

    # Assigne le jeton de la couleur du joueur 
    # à la dernière case de la ligne. 
    ligne[length] = joueur


# Les fonctions logique_droite et logique_gauche fonctionnent
# de la même manière, la seule différence est le sens de l'opération.
# (gauche à droite ou droite à gauche)
# Elles sont responsables d'appliquer les changements sur la grille pour 
# chaque jeton placé. 
def logique_gauche(ligne, joueur):
    
    if ligne[0] == 0:
        ligne[0] = joueur
        return
    
    temp = len(ligne) - 2
      

    # Cet algorithme ignore la première case puis 
    # vérifie que s'il y a un jeton sur une case 
    # qui n'est pas entourée de cases vides, alors, 
    # déplace le jeton à la prochaine case.
    # Ce processus est répété pour l'entièreté de la ligne.
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
        
        
        
            # Déplace le jeton
            ligne[temp + 1] = ligne[temp]
            ligne[temp]     = 0
            
            temp -= 1
    # Assigne le jetons de la couleur du joueur 
    # à la première case de la ligne. 
    ligne[0] = joueur



# Les fonctions logique_haut et logique_bas fonctionnent
# de la même manière, la seule différence est le sens de l'opération.
# (gauche à droite ou droite à gauche)
# Les fonctions haut et bas convertissent chaque instance 
# de case de rangée à index i en une ligne puis retourne cette ligne 
# à la fin de la fonction.
# Elles sont responsables d'appliquer les changements sur la grille pour 
# chaque jeton placé. 
def logique_haut(ligne, joueur, jetons, index):
    temp = len(ligne) - 2


    # Cet algorithme ignore la première case puis 
    # vérifie que s'il y a un jeton sur une case 
    # qui n'est pas entourée de cases vides, alors, 
    # déplace le jeton à la prochaine case.
    # Ce processus est répété pour l'entièreté de la ligne.
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
            
            #if temp = 0 

            # Déplace jeton
            ligne[temp + 1] = ligne[temp]
            ligne[temp] = 0

            temp -= 1

    # Place jeton dans la première case
    ligne[0] = joueur

    # Mise à jour des jetons de la matrice
    for i in range(len(jetons)):
        jetons[i][index] = ligne[i]



# Les fonctions logique_haut et logique_bas fonctionnent
# de la même manière, la seule différence est le sens de l'opération.
# (gauche à droite ou droite à gauche)
# Les fonctions haut et bas convertissent chaque instance 
# de case de rangée à index i en une ligne puis retournent cette ligne 
# à la fin de la fonction.
# Elles sont responsables d'appliquer les changements sur la grille pour 
# chaque jeton placé. 
def logique_bas(ligne, joueur, jetons, index):
   

    length = len(ligne)-1
     
    if ligne[length] == 0:
        ligne[length] = joueur
        
        for i in range(len(jetons)):
            jetons[i][index] = ligne[i]
        return
              
    temp = 1

    while temp <= length:
        if ligne[temp] == 0:
            temp += 1
            continue
        if ligne[temp] == 1 or ligne[temp] == 2:
            if (temp < length and
                (ligne[temp - 1] != 0 or
                ligne[temp + 1] == 0)):
                temp += 1
                continue
            
            # Déplace jeton
            ligne[temp - 1] = ligne[temp]
            ligne[temp] = 0

            temp += 1

    # Place jeton dans la dernière case
    ligne[length] = joueur

    # Mise à jour des jetons de la matrice
    for i in range(len(jetons)):
        jetons[i][index] = ligne[i]

          
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
          

        # Dessiner nouvelle fleche et nouvelle ligne
        if fleche_surv != -1 and ligne_surv != -1:
            dessiner_fleche(fleche_surv, blanc)
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
    if joueur == 1:
        couleur = rouge
    elif joueur == 2:
        couleur = vert
    else:
        couleur = noir
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


# Initialisation de laconfiguration de l'écran du jeu en fonction d'un format
# de grille spécifié
def initialisation_ecran_de_jeu(format):
    dims = taille_de_la_grille(format)
    set_screen_mode(dims.largeur, dims.hauteur, 4)
  
    return dims
  

# En cas de défaite d'un joueur, joue la musique triste et dessine la grille
# de la couleur appropriée
def defaite(dims, fleches, grille, joueur):
    dessiner_toutes_fleches(dims, fleches, jaune)
    musique_triste()
    dessiner_grille(dims, grille, rouge if joueur == 1 else vert)
    sleep(3)


# Dessine les lignes de victoire en fonction du joueur et de l'orientation
def victoire_lignes(grille, lignes, joueur, orientation):
    couleur = rouge if joueur == 1 else vert
   
    for index in lignes:
        if orientation == "v":
            ligne = verti_chercher_ligne(grille, index)
        if orientation == "h":
            ligne = horiz_chercher_ligne(grille, index)
        dessiner_ligne(ligne, couleur)


# En cas de victoire d'un joueur, fait jouer la musique joyeuse et dessine
# les lignes horizontales et/ou verticales de la couleur appropriée
def victoire(dims, grille, verti, horiz, fleches, joueur):
    dessiner_toutes_fleches(dims, fleches, jaune)
    dessiner_grille(dims, grille, gris)
    musique_joyeuse()
    victoire_lignes(grille, verti, joueur, "v")
    victoire_lignes(grille, horiz, joueur, "h")
    sleep(3)

    
    
# Fonction principale du jeu, regroupe tous les éléments nécessaires au
# bon fonctionnement de la partie
def glisse(format):

    # Initialisation de tous les paramètres nécessaires associés à la grille
    dims = initialisation_ecran_de_jeu(format)
    jetons, fleches, grille = initialisation_objets(dims)
    remplir_grille_initiale(dims)

    # Initialisation des variables de gestion des états du jeu
    partie_en_cours = True
    joueur = 1 # Tour du joueur (1 ou 2)
    etat_prec = (-1, -1)
    beep = False
    memoire_configs = []
    gagnant = -1
  
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
       
        # Gestion des actions lorsqu'un coup est joué
        if souris.button:
            cote, index = jouer_tour(selection, 
                                     jetons, 
                                     dims, 
                                     joueur, souris)

            if cote != -1 and index != -1:    
                # Vérifie si le coup joué recrée une configuration précédente
                config_existe = verifier_memoire(memoire_configs, jetons, cote,
                                                 index)

                # Vérifie si le coup joué entraîne la victoire d'un joueur
                gagnant, index_v, index_h = verifier_victoire(jetons)

                # Gestion des différents scénarios après que le coup soit joué
                if config_existe:
                    defaite(dims, fleches, grille, joueur)
                    break

                elif gagnant != -1:
                    victoire(dims, grille, index_v, index_h, 
                                 fleches, joueur)
                    break

                else:
                    copie = copie_matrice(jetons)
                    memoire_configs.append(copie)

                     # Tour du joueur suivant
                    joueur = 1 if joueur == 2 else 2

                    dessiner_joueur(3)   # Change le carré en noir

                    sleep(0.2)           # Court temps de pause
                    dessiner_joueur(joueur)

# Fonction permettant l'ajout d'un jeton dans la grille en fonction du joueur
# et de la position de la souris
def jouer_tour(ligne, jetons, dims, joueur, souris):
  
    position = obtenir_cote(dims, souris)
    
    # Si le bouton est enclenché
    if souris.button:
        if position is not None and ligne is not None and ligne[0] is not None:
            horiz = (position == 1 or position == 3)
            index = (ligne[0][horiz] // 8) - 1
            ajouter_jeton(jetons, index, position, joueur)
            son_coup()
            
            # Empêche de cliquer 2 fois accidentellement
            sleep(0.1)
            
            return position, index
        else:
            return -1, -1


# Retourne le côté survolé par la souris
def obtenir_cote(dims, souris):
    x = souris.x
    y = souris.y
  
    # Détermine le côté en fonction des extrémités survolées
    if x + 1 <= 8 and 8 <= y + 1 <= dims.hauteur - 8:
        return 3
    elif 8 <= x - 1 <= dims.largeur and y - 1 >= dims.hauteur - 8:
        return 2
    elif x - 1 >= dims.largeur - 8 and 8 <= y - 1 <= dims.hauteur - 8:
        return 1
    elif 8 <= x + 1 <= dims.largeur and y + 1 <= 8:
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


# Appel à la fonction principale      
glisse(5)