from ..pathfinding import settings as S
from .Tache import Tache

def Calculdistance(coord: list):
    """Fonction qui calcul la distance entre les points d'assemblages d'une taches.

    :param coord : liste[liste] des points d'assemblages.
    :return : ditance : distance total, en nb de cases, entre les points d'assemblages.
    """
    distance : int = 0
    size = len(coord)
    if size < 2:
        distance = 0
    else:
        for tra in range(size//2):
            distance = abs(coord[tra][0]-coord[tra+1][0]) + abs(coord[tra][1] - coord[tra+1][1]) + distance
    return distance


def Extracint(liste_str):
    """Fonction qui permet d'obtenir à partir des données lu par readline() une liste d'entier qui correspond à la ligne.

    :param liste_str : chaine de caractères correspondant à une ligne du fichier.
    :return : liste d'entier correspondant à la ligne du fichier.
    """
    liste_str = liste_str[:-1] + " "
    tempstr = ""
    res = []
    for i in liste_str :
        if i != " ":
            tempstr = tempstr + i
        else :
            res.append(int(tempstr))
            tempstr = ""
    return(res)

#lecture du fichier
def Input_global(nomfichier : str):
    """Fonction qui permet de transformer tout un fichier texte de jeu de données en caractéristiques du problème.

    :param nomdefichier : str, nom du fichier que l'on va traiter.
    :return dict : dictionnaire contenant toutes les variables importantes du fichier.
    """

    with open("./input_files/" + nomfichier + ".txt","r") as fichier:
        caracglob = Extracint(fichier.readline())
        GRILLE = caracglob[:2]
        BRAS = caracglob[2]
        NBPTDEMONT = caracglob[3]
        NBTACHES = caracglob[4]
        NBETAPES = caracglob[5]

        #bout de code Anthime
        S.lines = GRILLE[0]
        S.columns = GRILLE[1]

        #Boucle pour remplir LPOINTDEMONT.
        LPOINTDEMONT = []
        for j in range(NBPTDEMONT):
            LPOINTDEMONT.append(Extracint(fichier.readline()))

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
            LTASK[w] = Tache(nbcase, nbassemb, nbpoint, coordtask)

    return {"Ltsk": LTASK,"Lpointdemont": LPOINTDEMONT, "Grille": GRILLE, "Bras": BRAS, "Nbptdemont": NBPTDEMONT, "Nbtaches": NBTACHES,"Nbetapes": NBETAPES}

#### Example de fonctionnement d'appel de la liste sur le fichier a_ecample.txt:
#### >>> print(LTASK[0].nbcase)
#### 1
#### Ce qui est bien la valeur du nombre de cases séparant les deux points d'assemblages de la tache 0 dans 'a_example.txt
#### Alors, On a donc mit chaque élément de la liste en tant qu'objet de type 'Tache'
#### >>> print(type(LTASK[0]))
#### <class '__main__.Tache'>