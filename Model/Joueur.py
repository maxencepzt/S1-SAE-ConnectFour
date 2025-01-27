from Model.Constantes import *
from Model.Pion import *
from Model.Plateau import *
from random import randint



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

def getPionJoueur(joueur: dict) -> dict:
    """Fonction permettant de créer un pion d'une certaine couleur à partir de la couleur d'un joueur

    :param joueur: Joueur séléctionné
    :raises ValueError: Si le paramètre n'est pas un joueur
    :return: Retourne un pion
    """
    if type_joueur(joueur) == False:
        raise ValueError("getPionJoueur : Le paramètre ne correspond pas à un joueur ")
    return {const.COULEUR: joueur[const.COULEUR], const.ID: None}

def setPlateauJoueur(joueur: dict, plateau: list) -> None:
    """Fonction qui affecte le plateau au joueur

    :param joueur: Joueur séléctionné
    :param plateau: Plateau séléctionné
    :raises TypeError: Si le premier paramètre ne correspond pas à un joueur
    :raises TypeError: Si le deuxième paramètre ne correspond pas à un plateau
    :return: Ne retourne rien
    """
    if type_joueur(joueur) == False:
        raise TypeError("setPlateauJoueur : Le premier paramètre ne correspond pas à un joueur")
    if type_plateau(plateau) == False:
        raise TypeError("setPlateauJoueur : Le deuxième paramètre ne correspond pas à un plateau")
    
    joueur[const.PLATEAU] =  plateau
    return None

def setPlacerPionJoueur(joueur: dict, fonction: callable) -> None:
    """Cette fonction affecte une fonction au joueur

    :param joueur: Joueur séléctionné
    :param fonction: Fonction séléctionnée
    :raises TypeError: Si le premier paramètre ne correspond pas à un joueur
    :raises TypeError: Si le premier paramètre ne correspond pas à une fonction
    :return: Ne retourne rien
    """
    if type_joueur(joueur) == False:
        raise TypeError("setPlacerPionJoueur : Le premier paramètre ne correspond pas à un joueur")
    if callable(fonction) == False:
        raise TypeError("setPlacerPionJoueur : le second paramètre n'est pas une fonction")
    
    joueur[const.PLACER_PION] = fonction
    return None

def _placerPionJoueur(joueur: list) -> int:
    """Fonction qui cherche une place pour pouvoir placer le pion, avec prise en compte du mode etendu

    :param joueur: Joueur séléctionné
    :return: Retourne un entier pour pouvoir placer le pion
    """
    if getModeEtenduJoueur(joueur):
        res = randint(- const.NB_COLUMNS, const.NB_COLUMNS + const.NB_LINES - 1)
        if 0 <= res <=  const.NB_LINES - 1:
            while joueur[const.PLATEAU][0][res] != None:
                res = randint(0, const.NB_COLUMNS-1)
    else:
        res = randint(0, const.NB_COLUMNS-1)
        while joueur[const.PLATEAU][0][res] != None:
            res = randint(0, const.NB_COLUMNS-1)
        
    return res

def initialiserIAJoueur(joueur: list, play: bool) -> None:
    """Fonction qui permet de placer un pion quand c'est l'IA stupide qui joue

    :param joueur: Joueur séléctionné
    :param play: Si le joueur joue en premier (True) ou en second (False)
    :raises TypeError: Si le premier paramètre n'est pas un joueur
    :raises TypeError: Si le second paramètre n'est pas un booléen
    :return: Ne retourne rien
    """
    if type_joueur(joueur) == False:
        raise TypeError("initialiserIAJoueur: Le premier paramètre n'est pas un joueur")
    if type(play) != bool:
        raise TypeError("initialiserIAJoueur: Le second paramètre n'est pas un booléen")
    
    if play == False:
        setPlacerPionJoueur(joueur, _placerPionJoueur)
    return None

def getModeEtenduJoueur(joueur: dict) -> bool:
    """Fonction qui nous informe si le jeu est en mode etendu

    :param joueur: Joueur séléctionné, type dictionnaire
    :raises TypeError: Si le type de paramètre ne correspond pas à un joueur
    :return: Renvoie un booléen True si le jeu est en mode etendu, False sinon
    """
    if type_joueur(joueur) == False:
        raise TypeError("getModeEtenduJoueur : le paramètre ne correspond pas à un joueur")
    return const.MODE_ETENDU in joueur

def setModeEtenduJoueur(joueur: dict, ajoutSuppr: bool) -> None:
    """Fonction qui ajoute une clé const.MODE_ETENDU à joueur si ajoutSuppr vaut True, sinon elle supprime la clé const.MODE_ETENDU de joueur.

    :param joueur: Joueur séléctionné, type dictionnaire
    :param ajoutSuppr: Booléen qui va ajouter ou supprimer const.MODE_ETENDU de joueur
    :raises TypeError: Si le type de paramètre ne correspond pas à un joueur
    :raises TypeError: Si le type de paramètre ne correspond pas à un booléen
    :return: Ne retourne rien
    """
    if type_joueur(joueur) == False:
        raise TypeError("setModeEtenduJoueur : le premier paramètre ne correspond pas à un joueur")
    if type(ajoutSuppr) != bool:
        raise TypeError("setModeEtenduJoueur : le deuxième paramètre ne correspond pas à un booléen")
    if ajoutSuppr:
        joueur[const.MODE_ETENDU] = None
    else:
        del joueur[const.MODE_ETENDU]
    return None