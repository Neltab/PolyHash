# Fonction qui relie les taches à un point de montage principal
# Et a un second à utiliser en cas de nécessité (optionnel)
def pm_finder(taches: list, pointsMontage: list) -> list:
    sommeX = 0.0
    sommeY = 0.0
    barycentres = []
    for tache in taches:
        # TODO: changer coord et dist par le nom de la variable de la classe
        nbCases = tache.dist
        for coord in tache.coord :
            sommeX += coord[0]
            sommeY += coord[1]
        barycentres.append([sommeX/nbCases, sommeY/nbCases])

    min = float('inf')
    iMin = 0
    tachesLiees = []
    for bc in barycentres:
        for i in range(len(pointsMontage)):
            dist = calc_dist(bc, pointsMontage[i])

def calc_dist(barycentre: list, pointsMontage: list) -> int:
    return math.abs(barycentre[0] - pointsMontage[0]) + math.abs(barycentre[1] - pointsMontage[1])

