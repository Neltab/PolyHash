class Node:

    gridX: int
    gridY: int
    gCost: int
    hCost: int
    parent = "defaultValue" #supposed to be a Node type also

    def __init__(self, walkable, position, gridX, gridY):
        self.walkable = walkable
        self.position = position
        self.gridX = gridX
        self.gridY = gridY

    def fCost(self):
        return (self.gCost + self.hCost)