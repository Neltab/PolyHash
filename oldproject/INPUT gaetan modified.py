from dataclasses import dataclass

##############
def Calculdistance(coord: list):
    distance : int = 0
    size = len(coord)
    if size < 2:
        distance = 1
    else:
        for tra in range(size//2):
            distance = abs(int(coord[tra])-int(coord[tra+1])) + abs(int(coord[tra]) - int(coord[tra+1])) + distance
    return distance

##############


fichier = open("a_example.txt","r")
caracglob = fichier.readline()

L=[]                                                            #tableau de traitement de la premiere ligne
LPTDEMONT= []                                                    #tableau des coordonnées des points de montages



caracglob = caracglob[:-1]
caracglob = caracglob + " "

#Extarction des valeurs de la premiere ligne
tempcaracstr = ""

for i in caracglob:
    if i != " ":
        tempcaracstr = tempcaracstr + i
    if i == " ":
        if tempcaracstr != "":
            L.append(int(tempcaracstr))
        tempcaracstr = ""

###Variable de caractéristique de la grille
GRILLE = L[:2]
BRAS = L[2]
NBPTDEMONT = L[3]
NBTACHES = L[4]
NBETAPES = L[5]


###boucle pour remplir LPTDEMONT qui est la liste des coordonnées des pt de montage
for w in range(NBPTDEMONT):
    tempcoordptmont = []
    tempptmont = ""
    coordptmont = fichier.readline()
    coordptmont = coordptmont[:-1]
    coordptmont = coordptmont + " "
    for j in coordptmont:
        if j != " ":
            tempptmont = tempptmont + j
        if j == " ":
            if tempptmont != "":
                tempcoordptmont.append(int(tempptmont))
            tempptmont = ""
    LPTDEMONT.append(tempcoordptmont)
print(LPTDEMONT)


###création de la classe pour les taches

@dataclass
class Taches:
    nbcases : int
    nbpointassemblage : int
    #rendement = points/distance (distance en nombre de cases au sein de la tache si nbcase = 1 rendement = nbpoint)
    rendement : int
    coordtask : int

#Création de la boucle pour prendre les coordonnées des points d'assemblages des tables
lcoordtask=[]
result = []

for p in range(NBTACHES - 1):
    lcoordtask = []
    ltempstr = []
    tempstr = ""
    caractask = fichier.readline()
    caractask = caractask[:-1]
    caractask= caractask + " "
    for k in caractask:
        if k != " ":
            tempstr = tempstr + k
        if k == " ":
            if tempstr != "":
                ltempstr.append(int(tempstr))
            tempstr = ""
    pointstask = ltempstr[0]
    nbptassemblagetask = ltempstr[1]

    ltempstr = []
    tempstr = ""
    coordtask = fichier.readline()
    coordtask = coordtask[:-1]
    coordtask = coordtask + " "

    for fr in coordtask:
        if fr != " ":
            tempstr = tempstr + fr
        if fr == " ":
            if tempstr != "":
                ltempstr.append(int(tempstr))
            tempstr = ""
    moment = []
    if len(ltempstr)>2:
        for fed in range(0, len(ltempstr), 2):
            tempo = ltempstr[fed:fed+2]
            moment.append(tempo)
    else:
        moment = [ltempstr]
    nbcase = Calculdistance(moment)
    rendement = pointstask#/nbcase
    exec('Tache' + str(p) + '=' + 'Taches(nbcase, nbptassemblagetask, rendement, moment)')
    lcoordtask.append(moment)
    result.append(Taches(nbcase, nbptassemblagetask, rendement, moment))

#dernière ligne du fichier texte n'a pas de '/n' on la traite donc apart
lcoordtask = []
ltempo = []

lec = fichier.readline()
lec = lec[:-1]
lec.split()
[lcoordtask.append(int(i)) for i in lec if i != " " and i != "\n"]
pointstask = lcoordtask[0]
nbptassemblagetask = lcoordtask[1]

lec = fichier.readline()
lec.split()
[lcoordtask.append(int(i)) for i in lec if i != " " and i != "\n"]
if nbptassemblagetask >2:
    for saz in range(0, nbptassemblagetask, 2):
        tempo = lec[saz:saz+2]
        ltempo.append(int(tempo))
else:
    ltempo = [lec]

nbcase = Calculdistance(ltempo)
rendement = pointstask#/nbcase
exec('Tache'+str(NBTACHES-1) + '=' + 'Taches(nbcase, nbptassemblagetask, rendement, ltempo)')
result.append(Taches(nbcase, nbptassemblagetask, rendement, ltempo))
print(result)
print(LPTDEMONT)
fichier.close()


###EN RECAP:
###VARIABLES IMPORTANTES: GRILLE, BRAS, NBPTDEMONT, NBTACHES, NBETAPES
###LES TACHES SONT NOTEES COMME CECI : TACHE1 -> "Tache1" et sont composées des variables énoncé dans la création de la classe
###LA LISTE "LPTDEMONT" est la liste des coordonnées des pt de montage

if __name__ == "__main__":
    ""