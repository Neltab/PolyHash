class Arm:
    """ Classe représentant le bras lié à un point de montage.
    
    Parameters
    ----------

    """
    def __init__(self):
        self.pm = []
        self.pmIndice = 0
        self.taches = []
        self.tachesIndices = []
        self.points = 0
        self.etapes = 0
        self.movements = []

        self.occupiedCell = [] #Liste des cases occupées par le bras
        self.isDoingTask = False
        self.taskMoves = [] #Tableau contenant tous les nextMoves pour la tache en cours
        self.taskDone = [] #Contient tous les taches terminées
        self.movementsDone = [] #Tous les mouvements effectués réellement
        self.currentMovements = []

    def timeBeforeRetract(self):
        opposite = {"L":"R","R":"L","U":"D","D":"U"}
        counter = 0
        for moves in self.taskMoves:
            for i in range(len(moves) - 1):
                counter += 1
                if moves[i] != "W" and moves[i] == opposite[moves[i + 1]]:
                    return counter


    def set_pm(self, pm, indice):
        if not self.represent_int(indice):
            return
        indice = int(indice)

        if indice < 0:
            return

        self.pmIndice = indice
        self.pm = pm

    def add_task(self, task, indice):
        if not self.represent_int(indice):
            return
        indice = int(indice)

        if indice < 0:
            return

        self.tachesIndices.append(indice)
        self.taches.append(task)

    def add_points(self, points):
        if not self.represent_int(points):
                return
        points = int(points)

        if points < 0:
            return

        self.points += points

    def add_steps(self, steps):
        if not self.represent_int(steps):
                return
        steps = int(steps)

        if steps < 0:
            return

        self.etapes += steps

    def represent_int(self, n):
        try:
            int(n)
            return True
        except ValueError:
            return False

    def __str__(self):
        #TODO: refaire la valeur de sortie
        return f"Point de montage : {self.pm}\nPoints maximum obtenables : {self.points}"
