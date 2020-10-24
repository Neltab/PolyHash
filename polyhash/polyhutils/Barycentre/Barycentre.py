import math
import copy
import random

# Fonction qui relie les taches à un point de montage principal
# Et a un second à utiliser en cas de nécessité (optionnel)
def pm_finder_barycentre(taches: list, pointsMontage: list) -> list:
    sommeX = 0.0
    sommeY = 0.0
    barycentres = []
    #Pour chaque tache, on calcule les coordonnées de son barycentre (moyenne des coordonnées des points)
    for tache in taches:
        # TODO: changer coord et dist par le nom de la variable de la classe
        nbCases = tache.dist
        for coord in tache.coord :
            sommeX += coord[0]
            sommeY += coord[1]
        barycentres.append([sommeX/nbCases, sommeY/nbCases])

    min = float('inf')
    jMin = 0
    pointsMontageLies = [[] for i in range(len(pointsMontage))]

    #Pour chaque Barycentre, on va associer ce dernier au point de montage le plus proche
    #Pour ça on crée un tableau dont l'indice correspond à l'indice du point de montage et
    #Dans chaque lignes, on place tous l'indice des taches associées grâce au barycentre
    for i in range(len(barycentres)):
        for j in range(len(pointsMontage)):
            dist = calc_dist(barycentres[i], pointsMontage[i])
            if dist < min:
                min = dist
                jMin = j
        pointsMontageLies[jMin].append(i)

    return pointsMontageLies

def calc_dist(x: list, y: list) -> int:
    return math.abs(x[0] - y[0]) + math.abs(x[1] - y[1])


#############################
##                         ##
##     Liste de taches     ##
##                         ##
#############################

# * Possibilités d'amélioration :
# *  - Chercher la distance minimale entre 2 taches grâce à l'algo de pathfinding
# *  - Tester si la tache qu'on veut ajouter n'est pas plus proche d'un autre PM
def pm_liste(taches: list, pointsMontage: list) -> list:
    pointsMontageLies = [[] for i in range(len(pointsMontage))]
    tachesCopy = copy.deepcopy(taches)

    # while taches != [] :
    #     for pm in pointsMontage:
    #         for tache in taches:
    #             # TODO: changer coord et dist par le nom de la variable de la classe
    #             dist = calc_dist(tache.coord[0], pm)
    #             if dist < distMin:
    #                 distMin = dist
    #                 tacheMin = tache
    #         pointsMontageLies.append(tacheMin)

    for i in range(len(pointsMontage)):
        distMin = float('inf')

        for tache in tachesCopy:
            dist = calc_dist(tache.coord[0], pointsMontage[i])
            if dist < distMin:
                distMin = dist
                tacheMin = tache

        pointsMontageLies[i].append(tacheMin)
        tachesCopy.remove(tacheMin)

    # On associes toutes les taches à un point de montage
    while tachesCopy != []:

        # Pour chaque point de montage on va chercher la tache la plus proche de sa derniere tache effectuée
        for i in range(len(pointsMontage)):

            # On prend la derniere tache ajoutée comme nouveau point de départ
            # On cherche toujours la tache la plus proche parmi les taches restantes
            tacheMin = next_tache(pointsMontageLies[i][-1], tachesCopy)
            pointsMontageLies[i].append(tacheMin)
            tachesCopy.remove(tacheMin)

#tacheDepart : tache
#taches: liste de tache
def next_tache(tacheDepart, taches: list):
    distMin = float('inf')
    for tache in taches:
        dist = calc_dist(tache.coord[0], tacheDepart.coord[-1])
        if dist < distMin:
            distMin = dist
            tacheMin = tache
    return tacheMin



def get_max_index(tab: list, remaining_edges: list) -> int:
    maxV = -1
    maxIndex = 0
    for i in remaining_edges:
        if tab[i] > maxV:
            maxIndex = i
            maxV = tab[i]
    return maxIndex


if __name__ == "__main__":
    # test = {"1":"non","3":"oui"}
    # try:
    #     print(test[0])
    # except KeyError:
    #     test[0] = "oui"
    #     print(test)

    # test = [0,1,2,3,4,5,6]
    # test2 = [t for t in test]
    # test3 = copy.deepcopy(test)
    # test2[3] = 10
    # print(test)

    nb_edges = 6
    PM = [2,1]
    tab = [[random.randint(1, 100) for i in range(nb_edges)] for j in range(nb_edges)]
    # tab = [[-1, 68, 16, 49, 13, 7, 85, 25, 65, 13, 88, 66, 15, 79, 66],
    #         [25, -1, 90, 85, 95, 74, 18, 84, 43, 88, 31, 88, 14, 7, 80],
    #         [13, 44, -1, 12, 10, 100, 76, 97, 44, 44, 95, 52, 24, 58, 29],
    #         [59, 92, 52, -1, 65, 90, 75, 25, 16, 19, 76, 39, 10, 60, 2],
    #         [97, 60, 11, 9, -1, 64, 36, 21, 3, 31, 77, 10, 27, 62, 74],
    #         [33, 44, 15, 54, 40, -1, 24, 94, 60, 50, 26, 48, 2, 91, 61],
    #         [13, 3, 95, 64, 95, 78, -1, 44, 78, 99, 80, 55, 30, 96, 100],
    #         [65, 82, 61, 52, 40, 5, 22, -1, 100, 31, 62, 62, 32, 23, 72],
    #         [56, 23, 92, 63, 8, 34, 31, 49, -1, 58, 37, 28, 55, 1, 39],
    #         [5, 22, 83, 48, 50, 34, 77, 28, 76, -1, 31, 45, 91, 1, 2],
    #         [4, 55, 79, 95, 11, 64, 82, 94, 30, 68, -1, 54, 51, 20, 46],
    #         [35, 17, 85, 2, 10, 35, 98, 59, 28, 37, 19, -1, 89, 24, 2],
    #         [8, 61, 14, 48, 29, 5, 60, 52, 81, 37, 88, 88, -1, 27, 72],
    #         [46, 48, 31, 98, 92, 13, 83, 34, 64, 15, 49, 96, 36, -1, 27],
    #         [17, 54, 34, 48, 45, 40, 98, 11, 64, 79, 15, 49, 81, 12, -1]]

    edges = [i for i in range(nb_edges)]
    tasks = [[pm] for pm in PM]
    
    for i in range(nb_edges):
        for j in range(nb_edges):
            if i == j:
                tab[i][j] = -1

    for i in PM:
        edges.remove(i)

    for i in tab:
        print(i)
    
    for i in range(nb_edges - len(PM)):
        current = i%len(PM)
        maxIndex = get_max_index(tab[tasks[current][-1]], edges)
        tasks[current].append(maxIndex)
        edges.remove(maxIndex)

    print("\n")
    print(tasks)