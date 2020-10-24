import math

def yield_chain(taches: list, pointsMontage: list):
    nb_edges = len(taches)
    pmYieldMatrix = [[get_pm_yield(taches, pointsMontage, i, j) for j in range(nb_edges)] for i in range(len(pointsMontage))]
    yieldMatrix = [[get_yield(taches, i, j) for j in range(nb_edges)] for i in range(nb_edges)] #Matrice donnant le rendement d'un point i vers un point j
    remainingEdges = [i for i in range(nb_edges)] #Tous les sommets n'appartenant pas une des chaines
    yieldChain = [] #Chaines de tache

    for pm in pointsMontage:
        firstTaskIndex = get_max_index(pm, remainingEdges)
        yieldChain.append(firstTaskIndex)
        remainingEdges.remove(firstTaskIndex)

    for i in range(nb_edges):
        yieldMatrix[i][i] = -1

    for i in range(nb_edges - len(pointsMontage)): # Equivalent à while remaining edges != []
        current = i%len(pointsMontage)
        maxIndex = get_max_index(yieldMatrix[yieldChain[current][-1]], remainingEdges)
        yieldChain[current].append(maxIndex)
        remainingEdges.remove(maxIndex)

def calc_dist(x: list, y: list) -> int:
    return math.abs(x[0] - y[0]) + math.abs(x[1] - y[1])

def get_yield(taches, i, j):
    # TODO: remplacer tache.coord par le vrai nom de la variable
    # TODO: remplacer tache.points par le vrai nom de la variables
    return taches[j].points / calc_dist(taches[i].coord[-1], taches[j].coord[0])

def get_pm_yield(pointsMontage, taches, i, j):
    # TODO: remplacer tache.coord par le vrai nom de la variable
    # TODO: remplacer tache.points par le vrai nom de la variables
    return taches[j].points / calc_dist(pointsMontage[i], taches[j].coord[0])

def get_max_index(yieldRow: list, remaining_edges: list) -> int:
    maxV = -1
    maxIndex = 0
    for i in remaining_edges:
        if yieldRow[i] > maxV:
            maxIndex = i
            maxV = yieldRow[i]
    return maxIndex