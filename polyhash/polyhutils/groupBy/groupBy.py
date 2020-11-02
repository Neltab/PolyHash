import yield_chain
from Arm import Arm
from dataclasses import dataclass

# ! Import la classe Tache plus proprement
@dataclass
class Taches:
    nbcases : int
    nbpointassemblage : int
    #rendement = points/distance (distance en nombre de cases au sein de la tache si nbcase = 1 rendement = nbpoint)
    rendement : int
    coordtask : int

__all__ = ['groupBy']

class groupBy:
    def rendement(taches: list, pointsMontage: list, nbBras: int) -> list:
        return yield_chain.get_arms(taches, pointsMontage, nbBras)

if __name__ == "__main__":
    testa = [Taches(nbcases=1, nbpointassemblage=2, rendement=10.0, coordtask=[[2, 3], [3, 3]]), Taches(nbcases=1, nbpointassemblage=1, rendement=5.0, coordtask=[[4, 0]]), Taches(nbcases=1, nbpointassemblage=1, rendement=1.0, coordtask=[[3,3]])]
    pma = [[1, 1], [1, 3], [3, 2]]
    bras = groupBy.rendement(testa, pma, 2)
    for b in bras:
        print(b)