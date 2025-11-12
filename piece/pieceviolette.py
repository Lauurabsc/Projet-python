from piece.piece import Piece
from porte import Porte


# Pièce Bedrooms
class Bedrooms(Piece):

    """Pièce 'Bedrooms'
    Effet : +2 pas en entrant"""
    
    def __init__(self, row,col, porte_entree_direction=None):
        config = {"nord": True, "sud": True, "est": True, "ouest": True}

        super().__init__(
            nom="Bedrooms",
            row=row,
            col=col,
            porte_config=config,
            porte_entree_direction=porte_entree_direction,
            image_path="Images_Blue_Prince/Images/Bedrooms/Bedroom.png",
            rarete=1,
            couleur="violette"
        )

    def on_enter(self, joueur, jeu):
        """ Redéfinition de l'effet : +2 pas. """
        super().on_enter(joueur, jeu)
        joueur.inventaire.ajouter_pas(2)


# Pièce GuestBedroom
class GuestBedroom(Piece):

    """Pièce 'Guest Bedroom'
    Effet : +10 pas si elle est selectionnée
    Sans issue"""

    def __init__(self, row,col, porte_entree_direction):
        config = {"nord": False, "sud": False, "est": False, "ouest": False}
        config[porte_entree_direction] = True
        super().__init__(
            nom="Guest Bedroom",
            row=row,
            col=col,
            porte_config=config,
            image_path="Images_Blue_Prince/Images/Bedrooms/Guest_Bedroom.png",
            rarete=1,
            couleur="violette"
        )


    def on_draft(self, joueur, jeu):
        """ Redéfinition de l'effet : +10 pas au choix. """
        joueur.inventaire.ajouter_pas(10)


# Pièce ServantsQuarters      
class ServantsQuarters(Piece):
    
    """Pièce 'Servants's Quarters'
    Effet : Donne des clés en fonction du nombre de chambres déjà posées"""

    def __init__(self, row: int,col, porte_entree_direction: str):
        config = {"nord": True, "sud": True, "est": True, "ouest": True}
        config[porte_entree_direction] = True

        super().__init__(
            nom="Servant's Quarters",
            row=row,
            col=col,
            porte_config=config,
            image_path="Images_Blue_Prince/Images/Bedrooms/Servants_Quarters.png",
            rarete=2,
            objets=["2_des", "1_gemme", "detecteur_metaux", "pelle"],
            couleur="violette"
        )
   
    def on_discover(self, joueur, jeu, col, row, direction_entree):
        """
        Effet activé à la POSE de la pièce.
        On compte combien de pièces violettes sont déjà sur la grille.
        """
        super().on_discover(joueur, jeu, col, row, direction_entree)
        count_chambres = 0
       
        for r in jeu.manoir.grille:
            for piece in r:
                if piece and piece.couleur == "violette":
                    count_chambres += 1
       
        cles_a_donner = max(0, count_chambres - 1)
        cles_a_donner = min(cles_a_donner, 10)
       
        if cles_a_donner > 0:
            joueur.inventaire.ajouter_cles(cles_a_donner)


# Pièce MasterBedroom
class MasterBedroom(Piece):

    """Pièce 'Master Bedroom
    Rare, se trouve dans les niveaux supérieurs"""

    def __init__(self, row: int,col, porte_entree_direction: str):
        config = {"nord": True, "sud": True, "est": True, "ouest": True}
        config[porte_entree_direction] = True

        super().__init__(
            nom="Master Bedroom",
            row=row,
            col=col,
            porte_config=config,
            rarete=3,
            condition_placement="niveaux_superieurs",
            image_path="Images_Blue_Prince/Images/Bedrooms/Master_Bedroom.png",
            objets=["2_des", "4_or", "1_cle", "3_gemmes", "lockpick"],
            couleur="violette"
        )


# Pièce Boudoir


# Pièce Nursery


# Pièce BunkRoom


# Pièce HerLadyshipsChamber

