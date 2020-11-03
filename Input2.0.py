############
#Fonction qui calcul la distance entre les points d'assemblages.
def Calculdistance(coord: list):
    distance : int = 0
    size = len(coord)
    if size < 2:
        distance = 0
    else:
        for tra in range(size//2):
            distance = abs(coord[tra][0]-coord[tra+1][0]) + abs(coord[tra][1] - coord[tra+1][1]) + distance
    return distance

#Fonction qui permet d'obtenir à partir des données lu par readline() une liste d'entier qui correspond à la ligne.
#Les listes que cette fonction traite sont des listes de str, où des entiers(encore en str) sont séparés par des espaces
#et ou il y a le caractère "retour à la ligne" = "/n" a la fin de la séquence. (il faudra le remplacer par un caractère espace)
def Extracint(liste):
    liste = liste[:-1] + " "
    tempstr = ""
    res = []
    for i in liste :
        if i != " ":
            tempstr = tempstr + i
        else :
            res.append(int(tempstr))
            tempstr = ""
    return(res)
############

with open("a_example.txt","r") as fichier:
    caracglob = Extracint(fichier.readline())
    GRILLE = caracglob[:2]
    BRAS = caracglob[2]
    NBPTDEMONT = caracglob[3]
    NBTACHES = caracglob[4]
    NBETAPES = caracglob[5]

    #Boucle pour remplir LPOINTDEMONT.
    LPOINTDEMONT = []
    for j in range(NBPTDEMONT):
        LPOINTDEMONT.append(Extracint(fichier.readline()))

    #Création de la classe "Tache" pour lister les taches et leur caractéristique.
    class Tache:
        def __init__(self, nbcase : int, nbassemb : int, nbpoint : int, coordtask : list):
            self.nbcase = nbcase
            self.nbassemb = nbassemb
            self.nbpoint = nbpoint
            self.coordtask = coordtask

    #On stock chaqu'une des taches dans une liste dont l'indice de la liste = indice tache.
    LTASK = [0 for nt in range(NBTACHES)]

    #Boucle pour lire toute les taches et remplir LTASK.
    for w in range(NBTACHES):
        infotask = Extracint(fichier.readline())
        nbpoint = infotask[0]
        nbassemb = infotask[1]
        #Execption de la dernière ligne qui n'a pas de "/n" donc on rajoute un derniere élément pour qu'elle ai la bonne taille
        if w == NBTACHES -1 :
            temp = Extracint(fichier.readline() + " ")
        else :
            temp = Extracint(fichier.readline())
        #mise en forme des coord: [x1, y1 ,x2, y2 ...] -> [[x1, y1],[x2,y2]...]
        coordtask = []
        if len(temp) > 2:
            for long in range(0, len(temp),2):
                coordtask.append(temp[long:long+2])
        else :
            coordtask = [temp]
        nbcase = Calculdistance(coordtask)
        exec("Tache" + str(w) + " = " + "Tache(nbcase, nbassemb, nbpoint, coordtask)")
        LTASK[w] = Tache(nbcase, nbassemb, nbpoint, coordtask)


#### Example de fonctionnement d'appel de la liste sur le fichier a_ecample.txt:
#### >>> print(LTASK[0].nbcase)
#### 1
#### Ce qui est bien la valeur du nombre de cases séparant les deux points d'assemblages de la tache 0 dans 'a_example.txt
#### Alors, On a donc mit chaque élément de la liste en tant qu'objet de type 'Tache'
#### >>> print(type(LTASK[0]))
#### <class '__main__.Tache'>