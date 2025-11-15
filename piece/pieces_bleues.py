from piece.piece import Piece


# Pièce Vault
class Vault(Piece):
    """Pièce Vault
    +40 pièces d'or à la découverte
    Pas de porte"""
    nom="Vault"
    image_path="Images_Blue_Prince/Images/Rooms/Vault.png"
    rarete=3
    gemmes=3
    couleur="bleue"
    def __init__(self):
        config = {"nord": False, "sud": True, "est": False, "ouest": False}

        super().__init__(
            nom=self.nom,
            porte_config=config,
            image_path=self.image_path,
            rarete=self.rarete,
            gemmes=self.gemmes,
            couleur=self.couleur,
            effet_special = "Donne 40 pièces d'or à la découverte"
        )
    
    def on_discover(self, joueur, manoir, col, row):
        super().on_discover(joueur, manoir, col, row)
        joueur.inventaire.ajouter_piece_or(40)


# Pièce Nook
class Nook(Piece):
    """Pièce Nook
    +1 clé
    Deux portes en L"""
    nom="Nook"
    image_path="Images_Blue_Prince/Images/Rooms/Nook.png"
    rarete=1
    gemmes=0
    couleur="bleue"
    objets = ['des']
    def __init__(self):
        config = {"nord": False, "sud": True, "est": False, "ouest": True}

        super().__init__(
            nom=self.nom,
            porte_config=config,
            image_path=self.image_path,
            rarete=self.rarete,
            gemmes=self.gemmes,
            couleur=self.couleur,
            objets=self.objets,
            effet_special = "Contient 1 clé à la découverte"
        )
    
    def on_discover(self, joueur, manoir, col, row):
        super().on_discover(joueur, manoir, col, row)
        joueur.inventaire.ajouter_cles(1)


# Pièce Garage
class Garage(Piece):
    """Pièce Garage
    +3 clés
    Une seule porte (cul-de-sac)"""
    nom="Garage"
    image_path="Images_Blue_Prince/Images/Rooms/Garage.png"
    rarete=2
    gemmes=1
    couleur="bleue"
    objets = ['crochetage_kit','detecteur_metal']
    def __init__(self):
        # Une seule porte : celle par laquelle on entre
        config = {"nord": False, "sud": True, "est": False, "ouest": False}

        super().__init__(
            nom=self.nom,
            porte_config=config,
            image_path=self.image_path,
            rarete=self.rarete,
            gemmes=self.gemmes,
            couleur=self.couleur,
            objets=self.objets,
            effet_special="Contient 3 clés à la découverte"
        )

    def on_discover(self, joueur, manoir, col, row):
        super().on_discover(joueur, manoir, col, row)
        joueur.inventaire.ajouter_cles(3)


# Pièce Den
class Den(Piece):
    """Pièce Den
    +1 gemme
    Trois portes en T"""
    nom="Den"
    image_path="Images_Blue_Prince/Images/Rooms/Den.png"
    rarete=1   
    gemmes=0   
    couleur="bleue"
    objets=['des','patte_lapin']
    def __init__(self):
        # Trois portes : disposition en T (entrée + deux latérales)
        config = {"nord": False, "sud": True, "est": True, "ouest": True}

        super().__init__(
            nom=self.nom,
            porte_config=config,
            image_path=self.image_path,
            rarete=self.rarete,
            gemmes=self.gemmes,
            couleur=self.couleur,
            effet_special="Contient 1 gemme à la découverte"
        )

    def on_discover(self, joueur, manoir, col, row):
        super().on_discover(joueur, manoir, col, row)
        joueur.inventaire.ajouter_gemmes(1)


# Rumpus Room
class RampusRoom(Piece):
    """"pièce Rumpus Room
    """
    rarete = 1
    gemmes = 1
    image_path = "Images_Blue_Prince/Images/Rooms/Rumpus_Room.png"
    nom = "RumpusRoom"
    couleur ="bleue"
    objets = ['des', 'kit_crochetage', 'patte_lapin']  
    def __init__(self):
        config = {"nord": True, "sud": True, "est": False, "ouest": False}
        super().__init__(
            nom=self.nom,
            porte_config=config,
            image_path=self.image_path,
            rarete=self.rarete,
            gemmes=self.gemmes,
            objets=self.objets,
            couleur=self.couleur
        )


# Trophy Room
class TrophyRoom(Piece):
    """"pièce Trophy Room
    """
    rarete = 3
    gemmes = 5
    image_path = "Images_Blue_Prince/Images/Rooms/Trophy_Room.png"
    nom = "TrophyRoom"
    couleur ="bleue"
    objets = ['des', 'kit_crochetage']  
    def __init__(self):
        config = {"nord": False, "sud": True, "est": False, "ouest": True}
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
        super().on_discover(joueur, manoir, col, row)
        joueur.inventaire.ajouter_gemmes(8)

