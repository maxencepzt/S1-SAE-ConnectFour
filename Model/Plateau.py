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