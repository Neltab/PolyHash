from __future__ import annotations

class Node:
    #Coordonnées de la Node
    gridX: int
    gridY: int

    gCost: int = 0 #distance à la node de départ
    hCost: int = 0 #distance à la node d'arrivée
    parent: Node
    walkable: bool #si la Node est un obstacle ou pas

    def __init__(self, walkable, gridX, gridY):
        self.gridX = gridX
        self.gridY = gridY
        self.walkable = walkable

    def fCost(self): #cout total de la Node, l'objectif est de trouver le chemin ayant le fcost le plus faible
        return (self.gCost + self.hCost)