from piece.piece import Piece
from porte import Porte

class EntranceHall(Piece): 

    """Pièce de départ"""

    def __init__(self, row = 0): 

        config = {
            "nord": True,
            "sud": False, # Mur
            "est": True,
            "ouest": True
        }

        super().__init__(
            nom="Entrance Hall",
            row=row,
            porte_config=config,

            image_path="Images_Blue_Prince/Images/Rooms/Entrance_Hall.png",
            gemmes=0,
            rarete=0, 
            objets = None, 
            effet_special = None, 
            couleur = None
        )

        for porte in self.portes.values():
            if porte is not None:
                porte.niveau_verouillage = 0

class Antechamber(Piece): 
    """Pièce 'Anterchamber"

    Pièce fixe au Rang 9. Toutes les portes sont scellées.
    """

    def __init__(self, row = 8): 

        config = {
            "nord": True,
            "sud": True,
            "est": True,
            "ouest": True
        }

        super().__init__(
            nom="Antechamber",
            row=row, 
            porte_config=config,
            gemmes=0,       
            rarete=0,      
            image_path="images/Antechamber.png",
            objets=None,
            effet_special="Portes scellées. Doit être déverrouillée.",
            condition_placement="Fixe au rang 9", 
            couleur=None
        )

        for porte in self.portes.values():
            if porte is not None:
                porte.niveau_verouillage = "scellee"

    def on_enter(self, joueur, jeu): 
        """Méthode si le joueur réussit à entrer"""

        super().on_enter(joueur, jeu)
        print(f"Le joueur est entré dans l'{self.nom} ! Objectif atteint.")

        