# Model/Pion.py

from Model.Constantes import *

#
# Ce fichier implémente les données/fonctions concernant le pion
# dans le jeu du Puissance 4
#
# Un pion est caractérisé par :
# - sa couleur (const.ROUGE ou const.JAUNE)
# - un identifiant de type int (pour l'interface graphique)
#
# L'identifiant sera initialisé par défaut à None
#

def type_pion(pion: dict) -> bool:
    """
    Détermine si le paramètre peut être ou non un Pion

    :param pion: Paramètre dont on veut savoir si c'est un Pion ou non
    :return: True si le paramètre correspond à un Pion, False sinon.
    """
    return type(pion) == dict and len(pion) == 2 and const.COULEUR in pion.keys() \
        and const.ID in pion.keys() \
        and pion[const.COULEUR] in const.COULEURS \
        and (pion[const.ID] is None or type(pion[const.ID]) == int)


def construirePion(couleur: int) -> dict:
    """Fonction permettant de construire un pion

    :param couleur: Couleur du pion à construire
    :param id: Id attribué au pion
    :raises TypeError: Si le paramètre n'est pas un entier
    :raises ValueError: Si l'entier ne représente pas une couleur
    :return: Un dictionnaire représentant le pion
    """
    
    if type(couleur) != int:
        raise TypeError("construirePion : Le paramètre n'est pas de type entier")
    if couleur not in const.COULEURS:
        raise ValueError(f"construirePion : la couleur {couleur} n'est pas correcte")
    return {const.COULEUR: couleur, const.ID: None}

def getCouleurPion(pion: dict) -> int:
    """Fonction permettant d'obtenir la couleur d'un pion

    :param pion: Pion séléctionné
    :raises TypeError: Si le paramètre n'est pas un dictionnaire
    :return: Retourne la couleur du pion passé en paramètre
    """
    
    if type_pion(pion) == False:
        raise TypeError("getCouleurPion : Le paramètre n'est pas un pion")
    return pion[const.COULEUR]

def setCouleurPion(pion: dict, couleur: int) -> None:
    """Fonction qui modifie la couleur du pion

    :param pion: Pion séléctionné
    :param couleur: Couleur voulant être affectée
    :raises TypeError: Si le paramètre pion n'est pas un pion
    :raises TypeError: Si le paramètre couleur n'est pas un entier
    :raises ValueError: Si le paramètre couleur n'est pas une couleur
    :return: Ne retourne rien
    """
    
    if type_pion(pion) == False:
        raise TypeError("setCouleurPion : Le paramètre n'est pas un pion")
    if type(couleur) != int:
        raise TypeError("setCouleurPion : Le second paramètre n'est pas un entier")
    if couleur not in const.COULEURS:
        raise ValueError(f"setCouleurPion : Le second paramètre {couleur} n'est pas une couleur")
    pion[const.COULEUR] = couleur
    return None

def getIdPion(pion: dict) -> int:
    """Fonction permettant d'obtenir l'identifiant d'un pion

    :param pion: Pion séléctionné
    :raises TypeError: Si le paramètre pion n'est pas un pion
    :return: Retourne l'identifiant du pion passé en paramètre
    """
    if type_pion(pion) == False:
        raise TypeError("getIdPion : Le paramètre n'est pas un pion")
    return pion[const.ID]

def setIdPion(pion: dict, id: int) -> None:
    """Fonction qui modifie l'identifiant du pion

    :param pion: Pion séléctionné
    :param id: Identifiant voulant être affectée
    :raises TypeError: Si le paramètre pion n'est pas un pion
    :raises TypeError: Si le paramètre id n'est pas un entier
    :return: Ne retourne rien
    """
    if type_pion(pion) == False:
        raise TypeError("setIdPion : Le paramètre n'est pas un pion")
    if type(id) != int:
        raise TypeError("setIdPion : Le second paramètre n'est pas un entier. ")
    pion[const.ID] = id
    return None