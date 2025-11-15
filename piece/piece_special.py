from piece.piece import Piece
from porte import Porte

class EntranceHall(Piece): 

    """Pièce de départ"""

    def __init__(self):

        config = {
            "nord": True,
            "sud": False, # Mur
            "est": True,
            "ouest": True
        }

        super().__init__(
            nom="Entrance Hall",
            porte_config=config,
            image_path="Images_Blue_Prince/Images/Rooms/Entrance_Hall.png",
            gemmes=0,
            rarete=0, 
            objets = None, 
            effet_special = None, 
            couleur = None
        )

class Antechamber(Piece): 
    """Pièce 'Anterchamber"

    Pièce fixe au Rang 9. Toutes les portes sont scellées.
    """

    def __init__(self): 

        config = {
            "nord": True,
            "sud": True,
            "est": True,
            "ouest": True
        }

        super().__init__(
            nom="Antechamber",
            porte_config=config,
            gemmes=0,       
            rarete=0,      
            image_path="Images_Blue_Prince/Images/Rooms/Antechamber.png",
            objets=None,
            effet_special=None,
            condition_placement="Fixe au rang 9", 
            couleur=None
        )

    def on_enter(self, joueur): 
        """Méthode si le joueur réussit à entrer"""

        super().on_enter(joueur)
        print(f"Le joueur est entré dans l'{self.nom} ! Objectif atteint.")

        