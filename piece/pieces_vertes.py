from piece.piece import Piece


# Courtyard
class Courtyard(Piece):
    """"pièce Coutyard
    """
    rarete = 1
    gemmes = 1
    image_path = "Images_Blue_Prince/Images/Green Rooms/Courtyard.png"
    nom = "Courtyard"
    couleur ="verte"
    objets = ['Detecteur_Metal', 'Lockpick'] 
    def __init__(self):
        config = {"nord": False, "sud": True, "est": True, "ouest": True}
        super().__init__(
            nom=self.nom,
            porte_config=config,
            image_path=self.image_path,
            rarete=self.rarete,
            gemmes=self.gemmes,
            objets=self.objets,
            couleur=self.couleur
        )

# Cloister
class Cloister(Piece):
    """"pièce Cloister
    """
    rarete = 2
    gemmes = 3
    image_path = "Images_Blue_Prince/Images/Green Rooms/Cloister.png"
    nom = "Cloister"
    couleur ="verte"
    objets = [] # Vide 
    condition_placement = 'center'
    def __init__(self):
        config = {"nord": True, "sud": True, "est": True, "ouest": True}
        super().__init__(
            nom=self.nom,
            porte_config=config,
            image_path=self.image_path,
            rarete=self.rarete,
            gemmes=self.gemmes,
            objets=self.objets,
            couleur=self.couleur,
            condition_placement = self.condition_placement
        )
