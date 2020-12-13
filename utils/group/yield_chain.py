from typing import List, NewType
from .Arm import Arm
from ..input.Tache import Tache

__all__ = ['get_arms']

Coordinates = List[int]

def get_arms(taches: List[Tache], pointsMontage: List[Coordinates], nbBras: int) -> List[Arm]:
    """Recherche la configuration de bras optimale pour la grille fournie

    :param tache: Liste des taches de la grille
    :param pointsMontage: Liste des points de montage de la grille
    :param nbBras : Nombre maximal de bras pouvant être installé sur la grille
    :return : Liste de bras
    """
    bras = [Arm() for _ in range(nbBras)]

    nbEdges = len(taches)
    nbPM = len(pointsMontage)

    remainingEdges = [i for i in range(nbEdges)]

    # On génère deux matrices représentative du rendement entre un point de montage et la tache j
    # Ou entre la tache i et la tache j
    # Cas extrême : i = j, on ne peut pas donner de rendement, on met donc une valeur négative pour que l'algorithme ignore ce cas

    pmYieldMatrix = [[get_pm_yield(taches[j], pointsMontage[i]) for j in range(nbEdges)] for i in range(nbPM)]
    yieldMatrix = [[(get_yield(taches[i], taches[j]) if j != i else -1) for j in range(nbEdges)] for i in range(nbEdges)]

    for i in range(nbBras):
        indicePM, indiceTache = get_max_index_pm(pmYieldMatrix) # On récupère l'indice du point de montage et de la tache qui offrent le meilleur rendement
        remainingEdges.remove(indiceTache)
        currentTask = taches[indiceTache]

        # Ajout des différentes valeurs définissant le bras
        bras[i].set_pm(pointsMontage[indicePM])
        bras[i].add_task(currentTask)
        bras[i].add_points(currentTask.nbpoint)
        bras[i].add_steps(currentTask.nbcase if currentTask.nbassemb > 1 else 0)

        # bras[i].add_steps(calc_dist(pointsMontage[indicePM], taches[bras[i].tachesIndices[0]].coordtask[0]))
        bras[i].add_steps(calc_dist(pointsMontage[indicePM], bras[i].taches[0].coordtask[0]))

    for i in range(nbEdges - nbBras): # Equivalent à while remaining edges != []
        current = i % nbBras #On récupère l'indice du bras que l'on est entrain de traiter
        # On cherche le meilleur rendement à partir de la dernière tache
        maxIndex = get_max_index(yieldMatrix[bras[current].tachesIndices[-1]], remainingEdges)
        currentTask = taches[maxIndex]

        # On ajoute les différentes valeurs liées à la tache trouvée à notre bras
        bras[current].add_task(currentTask)
        bras[current].add_points(currentTask.nbcase if currentTaskcurrentTaskmoi.nbassemb > 1 else 0)
        bras[current].add_points(currentTask.nbpoint)
        bras[current].add_steps(calc_dist(bras[current].taches[-2].coordtask[-1], bras[current].taches[-1].coordtask[0]))

        remainingEdges.remove(maxIndex)

    return bras


def calc_dist(x: Coordinates, y: Coordinates) -> int:
    """Calcule la distance de Manhattan entre 2 points

    :param x : Le premier point
    :param y : Le second point
    :return : Distance entre les deux points
    """
    dx = abs(int(x[0]) - int(y[0]))
    dy = abs(int(x[1]) - int(y[1]))
    return dx + dy


def get_yield(t1: Tache, t2: Tache) -> float:
    """ Calcule le rendement entre deux taches (en fonction de la distance)\n
    On calcule la distance entre la premiere case de chaque tache car notre
    algorithme de déplacement à tendance à revenir à la premiere case de sa
    tache pour limiter le nombre de cases occupées 

    :param t1 : Premiere tache
    :param t2 : Seconde tache
    :return : Rendement calculé
    """
    dist = calc_dist(t1.coordtask[0], t2.coordtask[0]) + (t2.nbcase if t2.nbassemb > 1 else 0)
    if dist == 0:
        return float('inf')
    return t2.nbpoint / (dist)


def get_pm_yield(tache: Tache, point_montage: List[Coordinates]) -> float:
    """ Calcule le rendement entre une tache et un point de montage (en fonction de la distance)

    :param tache : Premiere tache
    :param point_montage : Seconde tache
    :return : Rendement calculé
    """
    return tache.nbpoint / (calc_dist(point_montage, tache.coordtask[0]) + (tache.nbcase if tache.nbassemb==1 else 0))


def get_max_index(yield_row: List[float], remaining_edges: List[int]) -> int:
    """Recherche le rendement maximum pour un bras donné

    On prend seulement une ligne de la matrice car on s'intéresse a un bras
    en particulier.

    :param yield_row: ligne d'une matrice de rendement
	:param remaining_edges: Liste des indices des taches disponibles
	:returns: indice correspondant à la tache ayant le meilleur rendement
    """
    maxValue = -1
    maxIndex = 0
    for i in remaining_edges:
        if yield_row[i] > maxValue:
            maxIndex = i
            maxValue = yield_row[i]
    return maxIndex

def get_max_index_pm(matrix: List[List[float]]) -> int:
    """Recherche le rendement maximum pour n'importe quel bras\n

    On prend toute la matrice car on recherche le maximum global
    afin de déterminer le couple (point de montage, tache) offrant
    le meilleur rendement indépendemment de l'ordre des points de montage

    :param matrix: Matrice représentative du rendement des points de montage
                   par rapport aux taches
	:returns: indice correspondant à la tache ayant le meilleur rendement
    """
    maxValue = -1
    maxI = 0
    maxJ = 0
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if maxValue < matrix[i][j]:
                maxI = i
                maxJ = j
                maxValue = matrix[i][j]

    # Une fois le point de montage maximisant le rendement trouvé
    # on retire virtuellement le point de montage et sa tache associée
    # pour ne pas associer l'un ou l'autre deux fois
    for i in range(len(matrix[maxI])):
        matrix[maxI][i] = -1
    for i in range(len(matrix)):
        matrix[i][maxJ] = -1

    return maxI, maxJ

def twoOpt(bras: Arm):
    """Fonction optimisant le chemin parcouru pour effectuer les taches

    La fonction est implementée mais n'est pas utilisée car sa complexité
    est trop grande et que d'autres solutions ont été développées
    
    """
    for b in bras:
        size = len(b.taches)
        improved = True

        while improved:
            improved = False
            for i in range(size-3):
                for j in range(i+2,size-1):
                    gain = calc_dist(b.taches[i].coordtask[0], b.taches[j].coordtask[0]) + calc_dist(b.taches[i+1].coordtask[0], b.taches[j+1].coordtask[0]) - calc_dist(b.taches[i].coordtask[0], b.taches[i+1].coordtask[0]) - calc_dist(b.taches[j].coordtask[0], b.taches[j+1].coordtask[0])
                    if gain < 0:
                        b.taches[i+1], b.taches[j] = b.taches[j], b.taches[i+1]
                        improved = True
                        break
