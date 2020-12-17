class Tache:
    """ Classe représentant une tache à effectuer.
    
    Parameters
    ----------
    nbcase: int = nombre de case à parcourir
    nbassemb: int = nombre de points à parcourir
    nbpoint: int = Nombre de points rapporté par la tache
    coordtask: List[int] = coordonnées des points a parcourir

    Methods
    -------
    """
    def __init__(self, nbcase : int, nbassemb : int, nbpoint : int, coordtask : list):
        self.nbcase = nbcase
        self.nbassemb = nbassemb
        self.nbpoint = nbpoint
        self.coordtask = coordtask