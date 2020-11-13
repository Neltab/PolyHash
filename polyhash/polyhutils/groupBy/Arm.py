class Arm:
    def __init__(self):
        self.pm = 0
        self.taches = []
        self.points = 0
        self.etapes = 0
        self.movements: list

    def set_pm(self, pm):
        if not self.represent_int(pm):
            return
        pm = int(pm)

        if pm < 0:
            return

        self.pm = pm

    def add_task(self, task):
        if not self.represent_int(task):
            return
        task = int(task)

        if task < 0:
            return

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
        return "[Point de montage: {0}, Taches: {1}, Points: {2}, Etapes: {3}]".format(self.pm, self.taches, self.points, self.etapes)

