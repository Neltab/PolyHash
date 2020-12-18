from typing import List, NewType
from ..input.Tache import Tache
Coordinates = List[int]

class Arm:
    """ Classe représentant le bras lié à un point de montage.
    
    Parameters
    ----------
        Initialisation
    pm: List[int] = Coordonnées du point de montage du bras\n
    taches: List[Tache] = Liste des taches que le bras devras potentiellement effectuer\n
    tachesIndices: List[int] = Liste des indices des tâches stockées dans la variable tâches\n
    points: int = Nombre de points maximum que le bras peut produire s'il remplit toutes ses taches\n
    etapes: int = Nombre d'étapes minimum que le bras devra effectuer (sans conflits ni retractation)\n
    movements: List[List[str]] = Mouvements que le bras devras effectuer pour faire toutes ses taches\n
    ----------
        Déplacements
    occupiedCell: List[List[int]] = Cases occupées par le bras lors de la résolution\n
    isDoingTask: bool = Indique si le bras est entrain d'effectuer une tache\n
    currentMovements: List[str] = Liste des mouvements que le bras s'apprete à faire\n
    taskDone: List[Tache] = Liste des taches que le bras a terminées\n
    movementsDone: List[str] = Liste des mouvements validés qui pourront être fournir en sortie du programme\n
    taskMoves: List[str] = Liste des mouvements pour la tache en cours (non implémenté, pour la gestion des conflits)\n

    Methods
    -------
    set_pm: Defini le point de montage du bras\n
    add_tack: Ajoute une tache au bras\n
    add_points: Ajoute un certain nombre de points passé en entré au bras\n
    add_steps: Ajoute un nombre d'étapes au bras\n
    represent_int: Renvoie un booléen indiquant si le nombre en entrée peut etre converti en entier\n
    """


    def __init__(self):
        self.pm = []
        self.taches = []
        self.tachesIndices = []
        self.points = 0
        self.etapes = 0
        self.movements = []

        self.occupiedCell = [] #Liste des cases occupées par le bras
        self.isDoingTask = False
        self.currentMovements = []
        self.taskDone = [] #Contient tous les taches terminées
        self.movementsDone = [] #Tous les mouvements effectués réellement
        self.taskMoves = [] #Tableau contenant tous les nextMoves pour la tache en cours


    def timeBeforeRetract(self):
        """Donne le nombre d'étapes avant rétractation du bras

        Cette methode n'est jamais utilisé car aucune gestion
        des collisions n'a été implémenté

        :return int: Nombre d'étapes avant rétractation du bras
        """
        opposite = {"L":"R","R":"L","U":"D","D":"U"}
        counter = 0
        for moves in self.taskMoves:
            for i in range(len(moves) - 1):
                counter += 1
                if moves[i] != "W" and moves[i] == opposite[moves[i + 1]]:
                    return counter


    def set_pm(self, pm: Coordinates):
        """Defini le point de montage du bras

        :param pm : Coordonnées du point de montage
        """
        self.pm = pm


    def add_task(self, task: Tache, indice: int):
        """Ajoute une tache au bras

        :param task : Tache a ajouter à la liste des taches
        :param indice : Indice de la tâche
        """
        self.taches.append(task)
        self.tachesIndices.append(indice)


    def add_points(self, points: int):
        """Ajoute un certain nombre de points passé en entré au bras

        :param points : Nombre de points à ajouter
        """

        if not self.represent_int(points):
                return
        points = int(points)

        if points < 0:
            self.add_points(-points)

        self.points += points


    def add_steps(self, steps: int):
        """Ajoute un nombre d'étapes au bras

        :param task : Nombre d'étapes à ajouter
        """

        if not self.represent_int(steps):
                return
        steps = int(steps)

        if steps < 0:
            self.add_steps(-steps)

        self.etapes += steps


    def represent_int(self, n: int):
        """Renvoie un booléen indiquant si le nombre en entrée peut etre converti en entier

        :param n : Nombre à tester
        """
        try:
            int(n)
            return True
        except ValueError:
            return False


    def __str__(self):
        #TODO: refaire la valeur de sortie
        return f"Point de montage : {self.pm}\nPoints maximum obtenables : {self.points}"
