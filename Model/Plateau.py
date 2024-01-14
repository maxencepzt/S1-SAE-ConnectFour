from Model.Constantes import *
from Model.Pion import *


#
# Le plateau représente la grille où sont placés les pions.
# Il constitue le coeur du jeu car c'est dans ce fichier
# où vont être programmées toutes les règles du jeu.
#
# Un plateau sera simplement une liste de liste.
# Ce sera en fait une liste de lignes.
# Les cases du plateau ne pourront contenir que None ou un pion
#
# Pour améliorer la "rapidité" du programme, il n'y aura aucun test sur les paramètres.
# (mais c'est peut-être déjà trop tard car les tests sont fait en amont, ce qui ralentit le programme...)
#

def type_plateau(plateau: list) -> bool:
    """
    Permet de vérifier que le paramètre correspond à un plateau.
    Renvoie True si c'est le cas, False sinon.

    :param plateau: Objet qu'on veut tester
    :return: True s'il correspond à un plateau, False sinon
    """
    if type(plateau) != list:
        return False
    if len(plateau) != const.NB_LINES:
        return False
    wrong = "Erreur !"
    if next((wrong for line in plateau if type(line) != list or len(line) != const.NB_COLUMNS), True) == wrong:
        return False
    if next((wrong for line in plateau for c in line if not(c is None) and not type_pion(c)), True) == wrong:
        return False
    return True


def construirePlateau() -> list:
    """Fonction permettant de construire un pion

    :return: Retourne une liste de liste sur NB_LINES x NB_COLUMNS contenant des None
    """
    lst = []
    for i in range(const.NB_LINES):
        lstTemp = []
        for j in range(const.NB_COLUMNS):
            lstTemp.append(None)
        lst.append(lstTemp)
    return lst


def placerPionPlateau(plateau: list, pion: dict, numCol: int) -> int:
    """Fonction permettant de placer un pion sur le plateau

    :param plateau: Le plateau du jeu
    :param pion: Le pion séléctionné
    :param numCol: La colonne sur le plateau séléctionnée
    :raises TypeError: Si le premier paramètre n'est pas un plateau
    :raises TypeError: Si le deuxième paramètre n'est pas un pion
    :raises TypeError: Si le troisième paramètre n'est pas un entier
    :raises ValueError: Si l'entier saisie est compris dans la taille de la colonne 
    :return: Retourne la position du pion placé, -1 si impossible 
    """
    if type_plateau(plateau) == False:
        raise TypeError("placerPionPlateau : Le premier paramètre ne correspond pas à un plateau")
    if type_pion(pion) == False:
        raise TypeError("placerPionPlateau : Le second paramètre n'est pas un pion")
    if type(numCol) != int:
        raise TypeError("placerPionPlateau : Le troisième paramètre n'est pas un entier")
    if not (0 <= numCol and numCol <= const.NB_COLUMNS - 1):
        raise ValueError(f"placerPionPlateau : La valeur de la colonne {numCol} n'est pas correcte")

    pos = -1
    i = 0
    if plateau[i][numCol] == None:
        while i < const.NB_LINES and plateau[i][numCol] == None:
            pos = i
            i += 1
        plateau[pos][numCol] = pion
    

    return pos


def toStringPlateau(plateau: list) -> str:
    """Donne le tableau sous forme texte.
    Peut être utile dans la console pour débugger.

    :param plateau: Plateau séléctionné
    :return: Retourne le plateau sous forme texte.
    """
    tab = ""
    for i in range(const.NB_LINES):
        for j in range(const.NB_COLUMNS):
            case = plateau[i][j]
            if case != None:
                if case[const.COULEUR] == 1:
                    tab += "\x1B[43m \x1B[0m"
                elif case[const.COULEUR] == 0:
                    tab += "\x1B[41m \x1B[0m"
            else:
                tab += " "
        tab += "\n"
    tab += "-" * const.NB_COLUMNS + "\n" + "".join(str(i) for i in range(const.NB_COLUMNS))
    return tab


def detecter4horizontalPlateau(plateau: list, couleur: int) -> list:
    f"""Détecte si 4 pions de la même couleur sont alignés horizontalement

    :param plateau: Plateau séléctionné
    :param couleur: Couleur séléctionnée
    :raises TypeError: Si le premier paramètre ne correspond pas à un plateau
    :raises TypeError: Si le second paramètre n'est pas un entier
    :raises ValueError: La valeur de la couleur {couleur} n'est pas correcte
    :return: Retourne une liste des pions alignés verticalement, il peut y avoir plusieurs lignes.
    """
    if type_plateau(plateau) == False:
        raise TypeError("detecter4horizontalPlateau : Le premier paramètre ne correspond pas à un plateau")
    if type(couleur) != int:
        raise TypeError("detecter4horizontalPlateau : le second paramètre n'est pas un entier ")
    if couleur not in const.COULEURS:
        raise ValueError(f"détecter4horizontalPlateau : La valeur de la couleur {couleur} n'est pas correcte")
    
    lst = []
    for i in range(const.NB_LINES):
        lstTemp = []
        j = 0
        continuer = True
        while continuer and j < const.NB_COLUMNS -3 and len(lstTemp) <= 4:
            pion1, pion2, pion3, pion4 = plateau[i][j], plateau[i][j+1], plateau[i][j+2], plateau[i][j+3]
            if pion1 != None and pion2 != None and pion3 != None and pion4 != None:
                if getCouleurPion(pion1) == getCouleurPion(pion2) == getCouleurPion(pion3) == getCouleurPion(pion4) == couleur:
                    lstTemp.extend([pion1, pion2, pion3, pion4])
                    continuer = False
            j += 1
        if len(lstTemp) == 4:
            lst.extend(lstTemp)
            lstTemp = []
            
    return lst

def detecter4verticalPlateau(plateau: list, couleur: int) -> list:
    f"""Détecte si 4 pions de la même couleur sont alignés verticalement

    :param plateau: Plateau séléctionné
    :param couleur: Couleur séléctionnée
    :raises TypeError: Si le premier paramètre ne correspond pas à un plateau
    :raises TypeError: Si le second paramètre n'est pas un entier
    :raises ValueError: La valeur de la couleur {couleur} n'est pas correcte
    :return: Retourne une liste des pions alignés verticalement, il peut y avoir plusieurs lignes.
    """
    if type_plateau(plateau) == False:
        raise TypeError("detecter4verticalPlateau : Le premier paramètre ne correspond pas à un plateau")
    if type(couleur) != int:
        raise TypeError("detecter4verticalPlateau : le second paramètre n'est pas un entier ")
    if couleur not in const.COULEURS:
        raise ValueError(f"detecter4verticalPlateau : La valeur de la couleur {couleur} n'est pas correcte")
    
    lst = []
    for i in range(const.NB_COLUMNS):
        lstTemp = []
        j = 0
        continuer = True
        while continuer and j < const.NB_LINES -3 and len(lstTemp) <= 4:
            pion1, pion2, pion3, pion4 = plateau[j][i], plateau[j+1][i], plateau[j+2][i], plateau[j+3][i]
            if pion1 != None and pion2 != None and pion3 != None and pion4 != None:
                if getCouleurPion(pion1) == getCouleurPion(pion2) == getCouleurPion(pion3) == getCouleurPion(pion4) == couleur:
                    lstTemp.extend([pion1, pion2, pion3, pion4])
                    continuer = False
            j += 1
        if len(lstTemp) == 4:
            lst.extend(lstTemp)
            lstTemp = []
            
    return lst

def detecter4diagonaleDirectePlateau(plateau: list, couleur: int) -> list:
    f"""Détecte si 4 pions de la même couleur sont alignés sur la diagonale directe.

    :param plateau: Plateau séléctionné
    :param couleur: Couleur séléctionnée
    :raises TypeError: Si le premier paramètre ne correspond pas à un plateau
    :raises TypeError: Si le second paramètre n'est pas un entier
    :raises ValueError: La valeur de la couleur {couleur} n'est pas correcte
    :return: Retourne une liste des pions alignés sur la diagonale directe, il peut y avoir plusieurs lignes.
    """
    if type_plateau(plateau) == False:
        raise TypeError("detecter4diagonaleDirectePlateau : Le premier paramètre ne correspond pas à un plateau")
    if type(couleur) != int:
        raise TypeError("detecter4diagonaleDirectePlateau : le second paramètre n'est pas un entier ")
    if couleur not in const.COULEURS:
        raise ValueError(f"detecter4diagonaleDirectePlateau : La valeur de la couleur {couleur} n'est pas correcte")
    
    lst = []
    for i in range(const.NB_LINES - 3):
        for j in range(const.NB_COLUMNS - 3):
            lstTemp = []
            for k in range(4):
                ligne = i + k
                colonne = j + k
                lstTemp.append(plateau[ligne][colonne])

            fonctionne = True
            for case in lstTemp:
                if case == None:
                    fonctionne = False
                elif case[const.COULEUR] == couleur:
                    fonctionne = False
            if fonctionne:
                lst.extend(lstTemp)

    return lst

def detecter4diagonaleIndirectePlateau(plateau: list, couleur: int) -> list:
    f"""Détecte si 4 pions de la même couleur sont alignés sur la diagonale indirecte.

    :param plateau: Plateau séléctionné
    :param couleur: Couleur séléctionnée
    :raises TypeError: Si le premier paramètre ne correspond pas à un plateau
    :raises TypeError: Si le second paramètre n'est pas un entier
    :raises ValueError: La valeur de la couleur {couleur} n'est pas correcte
    :return: Retourne une liste des pions alignés sur la diagonale indirecte, il peut y avoir plusieurs lignes.
    """
    if type_plateau(plateau) == False:
        raise TypeError("detecter4diagonaleIndirectePlateau : Le premier paramètre ne correspond pas à un plateau")
    if type(couleur) != int:
        raise TypeError("detecter4diagonaleIndirectePlateau : le second paramètre n'est pas un entier ")
    if couleur not in const.COULEURS:
        raise ValueError(f"detecter4diagonaleIndirectePlateau : La valeur de la couleur {couleur} n'est pas correcte")
    
    lst = []
    for i in range(const.NB_LINES - 3):
        for j in range(3, const.NB_COLUMNS):
            lstTemp = []
            for k in range(4):
                ligneK = i + k
                colonneK = j - k
                lstTemp.append(plateau[ligneK][colonneK])

            fonctionne = True
            for case in lstTemp:
                if case == None:
                    fonctionne = False
                elif case[const.COULEUR] == couleur:
                    fonctionne = False
            if fonctionne:
                lst.extend(lstTemp)

    return lst

def getPionsGagnantsPlateau(plateau: list) -> list:
    """Donne toutes les séries pions pouvant être gagants

    :param plateau: Plateau séléctionné
    :raises TypeError: Si le paramètre ne correspond pas à un plateau
    :return: Retourne une liste des pions alignés sur la verticale, diagonale, diagonale directe et indirecte
    """
    if type_plateau(plateau) == False:
        raise TypeError("getPionsGagnantsPlateau : Le paramètre n'est pas un plateau")
    
    lst = []
    for couleur in const.COULEURS:
        lst += detecter4horizontalPlateau(plateau, couleur)
        lst += detecter4verticalPlateau(plateau, couleur)
        lst += detecter4diagonaleDirectePlateau(plateau, couleur)
        lst += detecter4diagonaleIndirectePlateau(plateau, couleur)
    
    return lst

def isRempliPlateau(plateau: list) -> bool:
    """Informe si le tableau est rempli ou non.

    :param plateau: Plateau séléctionné
    :raises TypeError: Si le paramètre ne correspond pas à un plateau
    :return: Retourne un booléen si le tableau est rempli ou non
    """
    if type_plateau(plateau) == False:
        raise TypeError("isRempliPlateau : Le paramètre n'est pas un plateau")
    
    i = 0
    rempli = True
    while rempli and i < const.NB_COLUMNS:
        if plateau[0][i] == None:
            rempli = False
        i += 1
    return rempli

def placerPionLignePlateau(plateau: list, pion: dict, numLigne: int, left: bool) -> tuple:
    """
    if type_plateau(plateau) != False:
        raise TypeError("placerPionLignePlateau : Le premier paramètre n'est pas un plateau")
    if type_pion(pion) != False:
        raise TypeError("placerPionLignePlateau : Le second paramètre n'est pas un pion")
    if type(numLigne) != int:
        raise TypeError(" placerPionLignePlateau : le troisième paramètre n'est pas un entier")
    if not(0 <= numLigne and numLigne <= const.NB_LINES - 1):
        raise ValueError(f"Le troisième paramètre {numLigne} ne désigne pas une ligne")
    if type(left) != bool:
        raise TypeError("placerPionLignePlateau : le quatrième paramètre n'est pas un booléen")
    """
    lstPion = [pion]
    descente = None
    if left: # Dans le cas où on place le pion à gauche
        i = 0
        while i <= const.NB_COLUMNS -1 and plateau[numLigne][i] != None: # On parcourt toute la liste à partir de la gauche, jusqua tomber sur un None ou bien arriver au bout de la ligne
            lstPion.append(plateau[numLigne][i]) # On ajoute a chaque fois le pion à la liste
            i += 1
            
        for k in range(min(len(lstPion), const.NB_COLUMNS)): # Boucle qui va tout décaller d'un coup en fonction de la taille de la liste
                plateau[numLigne][k] = lstPion[k]
        descente = numLigne
        while descente+1  < const.NB_LINES -1 and plateau[descente+1][len(lstPion)-1] == None :
            plateau[descente+1][len(lstPion)-1] = plateau[descente][len(lstPion)-1]
            plateau[descente][len(lstPion)-1] = None
            descente += 1
    
    else: # Dans le cas où on place le pion à droite
        i = const.NB_COLUMNS -1
        while 0 <= i and plateau[numLigne][i] != None: # On parcourt toute la liste à partir de la droite, jusqua tomber sur un None ou bien arriver au bout de la ligne
            lstPion.append(plateau[numLigne][i]) # On ajoute a chaque fois le pion à la liste
            i -= 1
            
        for k in range(min(len(lstPion), const.NB_COLUMNS)): # Boucle qui va tout décaller d'un coup en fonction de la taille de la liste
            plateau[numLigne][const.NB_COLUMNS-1-k] = lstPion[k]
        descente = numLigne
        while descente + 1 < const.NB_LINES - 1 and plateau[descente + 1][const.NB_COLUMNS-1-len(lstPion)+1] == None:
            plateau[descente + 1][const.NB_COLUMNS-1-len(lstPion)+1] = plateau[descente][const.NB_COLUMNS-1-len(lstPion)+1]
            plateau[descente][const.NB_COLUMNS-1-len(lstPion)+1] = None
            descente += 1
    
    return (lstPion, descente)

def encoderPlateau(plateau: list) -> int:
    """Fonction permettant d'encoder le plateau en une chaine de caractère

    :param plateau: Plateau séléctionné
    :raises TypeError: Si le paramètre ne correspond pas à un plateau.
    :return: Une chaîne de caractères représentant l'encodage du plateau.
    """
    if type_plateau(plateau) == False:
        raise TypeError("encoderPlateau : le paramètre ne correspond pas à un plateau")
    tab = ""
    for i in range(const.NB_LINES):
        for j in range(const.NB_COLUMNS):
            if plateau[i][j] == None:
                tab += "_"
            elif plateau[i][j][const.COULEUR] == 0:
                tab += "J"
            else:
                tab += "R"
    return tab