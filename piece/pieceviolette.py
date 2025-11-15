from piece.piece import Piece


# Pièce Bedrooms
class Bedrooms(Piece):

    """Pièce 'Bedrooms'
    Effet : +2 pas en entrant"""
    rarete = 1
    gemmes = 0
    image_path="Images_Blue_Prince/Images/Bedrooms/Bedroom.png"
    couleur="violette"
    nom="Bedrooms"
    objets=['gemmes','pommes','cles','des']
    def __init__(self):
        config = {"nord": False, "sud": True, "est": False, "ouest": True}

        super().__init__(
            nom=self.nom,
            porte_config=config,
            image_path=self.image_path,
            rarete=self.rarete,
            gemmes=self.gemmes,
            couleur=self.couleur,
            objets=self.objets
        )

    def on_enter(self, joueur):
        """ Redéfinition de l'effet : +2 pas. """
        super().on_enter(joueur)
        joueur.inventaire.ajouter_pas(2)

# Guest Bedroom
class GuestBedroom(Piece):
    """"pièce Guest Bedroom
    """
    rarete = 1
    gemmes = 0
    image_path = "Images_Blue_Prince/Images/Bedrooms/Guest_Bedroom.png"
    nom = "GestBedroom"
    couleur ="violette"
    objets = ['cles', 'gemmes']
    def __init__(self):
        config = {"nord": False, "sud": True, "est": False, "ouest": False}
        super().__init__(
            nom=self.nom,
            porte_config=config,
            image_path=self.image_path,
            rarete=self.rarete,
            gemmes=self.gemmes,
            objets=self.objets,
            couleur=self.couleur
        )

    def on_discover(self, joueur, manoir, col, row):
        """ Redéfinition de l'effet : +10 pas au choix. """
        super().on_discover(joueur, manoir, col, row)
        joueur.inventaire.ajouter_pas(10)


# Servant's Quarters
class ServantsQuarters(Piece):
    """"pièce Servant's Quarters
    """
    rarete = 2
    gemmes = 1
    image_path = "Images_Blue_Prince/Images/Bedrooms/Servants_Quarters.png"
    nom = "ServantsQuarters"
    couleur ="violette"
    objets = ['des', 'gemmes', 'detecteur_metal']
    def __init__(self):
        config = {"nord": False, "sud": True, "est": False, "ouest": False}
        super().__init__(
            nom=self.nom,
            porte_config=config,
            image_path=self.image_path,
            rarete=self.rarete,
            gemmes=self.gemmes,
            objets=self.objets,
            couleur=self.couleur
        )
    def on_discover(self, joueur, manoir, col, row):
        """
        Effet activé à la POSE de la pièce.
        On compte combien de pièces violettes sont déjà sur la grille.
        """
        super().on_discover(joueur, manoir, col, row)
        count_chambres = 0
       
        for r in manoir.grille:
            for piece in r:
                if piece and piece.couleur == "violette":
                    count_chambres += 1
       
        cles_a_donner = max(0, count_chambres - 1)
        cles_a_donner = min(cles_a_donner, 10)
       
        joueur.inventaire.ajouter_cles(cles_a_donner)


# Master Bedroom
class MasterBedroom(Piece):
    """"pièce Master Bedroom
    """
    rarete = 3
    gemmes = 2
    image_path = "Images_Blue_Prince/Images/Bedrooms/Master_Bedroom.png"
    nom = "MasterBedroom"
    couleur ="violette"
    objets = ['des', 'cles', 'gemmes', 'kit_crochetage']
    def __init__(self):
        config = {"nord": False, "sud": True, "est": False, "ouest": False}
        super().__init__(
            nom=self.nom,
            porte_config=config,
            image_path=self.image_path,
            rarete=self.rarete,
            gemmes=self.gemmes,
            objets=self.objets,
            couleur=self.couleur
        )
    def on_discover(self, joueur, manoir, col, row):
        """
        Effet activé à la POSE de la pièce.
        On compte combien de pièces sont déjà sur la grille.
        """
        super().on_discover(joueur, manoir, col, row)
        count_room = 0
       
        for r in manoir.grille:
            for piece in r:
                if piece:
                    count_room += 1
       
        pas_a_donner = max(0, count_room - 1)
       
        joueur.inventaire.ajouter_pas(pas_a_donner)