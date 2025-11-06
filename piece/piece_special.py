from piece import Piece
from porte import Porte

class EntranceHall(Piece): 

    """Pièce de départ"""

    def __init(self, row = 0): 

        config = {
            "nord": True,
            "sud": False, # Mur
            "est": True,
            "ouest": True
        }

        super().__init__(
            nom="Entrance Hall",
            row=row,
            portes_config=config,
            cost_gemmes=0,
            rarete=0
        )

        for porte in self.portes.values():
            if porte is not None:
                porte.niveau_verouillage = 0