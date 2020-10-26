from polyhash import Node

class Node:

    gridX: int
    gridY: int
    gCost: int
    hCost: int
    parent: Node
    walkable: bool

    def __init__(self, walkable, gridX, gridY):
        self.gridX = gridX
        self.gridY = gridY
        self.walkable = walkable

    def fCost(self):
        return (self.gCost + self.hCost)