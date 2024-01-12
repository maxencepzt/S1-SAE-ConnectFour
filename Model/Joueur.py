from Model.Constantes import *
from Model.Pion import *
from Model.Plateau import *



#
# Ce fichier contient les fonctions gérant le joueur
#
# Un joueur sera un dictionnaire avec comme clé :
# - const.COULEUR : la couleur du joueur entre const.ROUGE et const.JAUNE
# - const.PLACER_PION : la fonction lui permettant de placer un pion, None par défaut,
#                       signifiant que le placement passe par l'interface graphique.
# - const.PLATEAU : référence sur le plateau de jeu, nécessaire pour l'IA, None par défaut
# - d'autres constantes nécessaires pour lui permettre de jouer à ajouter par la suite...
#

def type_joueur(joueur: dict) -> bool:
    """
    Détermine si le paramètre peut correspondre à un joueur.

    :param joueur: Paramètre à tester
    :return: True s'il peut correspondre à un joueur, False sinon.
    """
    if type(joueur) != dict:
        return False
    if const.COULEUR not in joueur or joueur[const.COULEUR] not in const.COULEURS:
        return False
    if const.PLACER_PION not in joueur or (joueur[const.PLACER_PION] is not None
            and not callable(joueur[const.PLACER_PION])):
        return False
    if const.PLATEAU not in joueur or (joueur[const.PLATEAU] is not None and
        not type_plateau(joueur[const.PLATEAU])):
        return False
    return True


def construireJoueur(couleur: int) -> dict:
    """Fonction permettant de construire un joueur

    :param couleur: Couleur du joueur à construire
    :raises TypeError: Si le paramètre n'est pas un entier
    :raises ValueError: Si l'entier ne représente pas une couleur
    :return: Un dictionnaire représentant le joueur
    """
    if type(couleur) != int:
        raise TypeError("construireJoueur : Le paramètre n'est pas un entier")
    if couleur not in const.COULEURS:
        raise ValueError(f"construireJoueur : L'entier donné {couleur} n'est pas une couleur.")
    
    return {const.COULEUR: couleur, const.PLATEAU: None, const.PLACER_PION: None}

def getCouleurJoueur(joueur: dict) -> int:
    """Fonction permettant d'obtenir la couleur du joueur

    :param joueur: Joueur séléctionné
    :raises TypeError: Si le paramètre n'est pas un joueur
    :return: Retourne la couleur du joueur passé en paramètre
    """
    if type_joueur(joueur) == False:
        raise TypeError("getCouleurJoueur : Le paramètre ne correspond pas à un joueur")
    
    return joueur[const.COULEUR]

def getPlateauJoueur(joueur: dict) -> list:
    """Fonction permettant d'obtenir le plateau du joueur

    :param joueur: Joueur séléctionné
    :raises TypeError: Si le paramètre n'est pas un joueur
    :return: Retourne le plateau du joueur passé en paramètre
    """
    if type_joueur(joueur) == False:
        raise TypeError("getPlateauJoueur : Le paramètre ne correspond pas à un joueur")
    return joueur[const.PLATEAU]

def getPlacerPionJoueur(joueur: dict) -> callable:
    """Fonction permettant d'obtenir la fonction placerPion du joueur

    :param joueur: Joueur séléctionné
    :raises TypeError: Si le paramètre n'est pas un joueur
    :return: Retourne la fonction placerPion du joueur passé en paramètre
    """
    if type_joueur(joueur) == False:
        raise TypeError("getPlacerPionJoueur : Le paramètre ne correspond pas à un joueur")
    return joueur[const.PLACER_PION]