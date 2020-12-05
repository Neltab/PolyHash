from . import yield_chain

__all__ = ['groupBy']

class groupBy:
    @staticmethod
    def rendement(taches: list, pointsMontage: list, nbBras: int) -> list:
        return yield_chain.get_arms(taches, pointsMontage, nbBras)
