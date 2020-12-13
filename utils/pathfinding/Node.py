from __future__ import annotations

class Node:
    """Classe Node, elle contient toutes les informations pour l'exécution de l'algo A*
        Chaque case du tableau géant que l'on traite est une Node.

        Parameters
        ----------
        gridX: int = coordonnée X de la Node dans le tableau
        gridY: int = coordonnée Yde la Node dans le tableau
        gCost: int = distance à la node de départ
        hCost: int = distance à la node de d'arrivée
        parent: Node = Node parent, utilisée dans l'algorithme pour pouvoir retrouver son chemin
        walkable: bool = False si cette Node est un obstacle
    """

    gCost: int = 0
    hCost: int = 0
    parent: Node

    def __init__(self, walkable, gridX, gridY):
        self.gridX = gridX
        self.gridY = gridY
        self.walkable = walkable

    def fCost(self):
        """Cout total de la Node, l'objectif est de trouver le chemin ayant le fcost le plus faible
        """
        return (self.gCost + self.hCost)