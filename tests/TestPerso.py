from Model.Constantes import *
from Model.Plateau import *
from Model.Pion import *
from random import randint, choice

def plateauRandom() -> None:
    p = construirePlateau()
    for _ in range(20):
        placerPionPlateau(p, construirePion(choice(const.COULEURS)),
        randint(0, const.NB_COLUMNS - 1))
    print(toStringPlateau(p))
    return None

def testDetecter4horizontalPlateau() -> None:
    p = construirePlateau()
    for _ in range(20):
        placerPionPlateau(p, construirePion(choice(const.COULEURS)),
        randint(0, const.NB_COLUMNS - 1))
    print(toStringPlateau(p))
    print(detecter4horizontalPlateau(p,0))
    return None

def testDetecter4verticalPlateau() -> None:
    p = construirePlateau()
    for _ in range(20):
        placerPionPlateau(p, construirePion(choice(const.COULEURS)),
        randint(0, const.NB_COLUMNS - 1))
    print(toStringPlateau(p))
    print(detecter4verticalPlateau(p,0))
    return None

def testDetecter4diagonaleDirectePlateau() -> None:
    p = construirePlateau()
    for _ in range(20):
        placerPionPlateau(p, construirePion(choice(const.COULEURS)),
        randint(0, const.NB_COLUMNS - 1))
    print(toStringPlateau(p))
    print(detecter4diagonaleDirectePlateau(p,1))
    return None

def testDetecter4diagonaleIndirectePlateau() -> None:
    p = construirePlateau()
    for _ in range(20):
        placerPionPlateau(p, construirePion(choice(const.COULEURS)),
        randint(0, const.NB_COLUMNS - 1))
    print(toStringPlateau(p))
    print(detecter4diagonaleIndirectePlateau(p,1))
    return None

def testGetPionsGagnantsPlateau() -> None:
    p = construirePlateau()
    for _ in range(20):
        placerPionPlateau(p, construirePion(choice(const.COULEURS)),
        randint(0, const.NB_COLUMNS - 1))
    print(toStringPlateau(p))
    print(getPionsGagnantsPlateau(p))
    return None

def testIsRempliPlateau() -> None:
    p = construirePlateau()
    for _ in range(60):
        placerPionPlateau(p, construirePion(choice(const.COULEURS)),
        randint(0, const.NB_COLUMNS - 1))
    print(toStringPlateau(p))
    print(isRempliPlateau(p))
    return None
"""
for i in range(200):
    testIsRempliPlateau()
"""