from piece.piece import Piece
import random

# Pièce Vault
# +40 or, rarete 3, cost 3gemmes, 
class Vault(Piece):
    """Pièce Vault
    +40 pièces d'or à la découverte
    Pas de porte"""

    def __init__(self, row: int, porte_entree: str):
        config = {"nord": False, "sud": False, "est": False, "ouest": False}
        config[porte_entree] = True

        super().__init__(
            nom="Vault",
            row=row,
            porte_config=config,
            image_path="Images_Blue_Prince/Images/Rooms/Vault.png",
            rarete=3,
            gemmes=3,
            couleur="bleue",
            effet_special = "Donne 40 pièces d'or à la découverte"
        )
    
    def on_discover(self, joueur, jeu, col, row):
        super().on_discover(joueur, jeu, col, row)
        joueur.inventaire.ajouter_piece_or(40)


# Pièce Nook
class Nook(Piece):
    """Pièce Nook
    +1 clé
    Deux portes en L"""

    def __init__(self, row: int, porte_entree: str):
        config = {"nord": False, "sud": False, "est": False, "ouest": False}
        config[porte_entree] = True

        # Deuxième porte choisie aléatoirement (à l'opposé de l'entrée)
        if porte_entree == "nord":
            config["est"] = True
        elif porte_entree == "sud":
            config["ouest"] = True
        elif porte_entree == "est":
            config["sud"] = True
        elif porte_entree == "ouest":
            config["nord"] = True

        super().__init__(
            nom="Nook",
            row=row,
            porte_config=config,
            image_path="Images_Blue_Prince/Images/Rooms/Nook.png",
            rarete=1,
            gemmes=0,
            couleur="bleue",
            effet_special = "Contient 1 clé à la découverte"
        )
    
    def on_discover(self, joueur, jeu, col, row):
        super().on_discover(joueur, jeu, col, row)
        joueur.inventaire.ajouter_cles(1)


# Pièce Garage
class Garage(Piece):
    """Pièce Garage
    +3 clés
    Une seule porte (cul-de-sac)"""

    def __init__(self, row: int, porte_entree: str):
        # Une seule porte : celle par laquelle on entre
        config = {"nord": False, "sud": False, "est": False, "ouest": False}
        config[porte_entree] = True

        super().__init__(
            nom="Garage",
            row=row,
            porte_config=config,
            image_path="Images_Blue_Prince/Images/Rooms/Garage.png",
            rarete=2,  
            gemmes=1,  
            couleur="bleue",
            effet_special="Contient 3 clés à la découverte"
        )

    def on_discover(self, joueur, jeu, col, row):
        super().on_discover(joueur, jeu, col, row)
        joueur.inventaire.ajouter_cles(3)

# Pièce Music Room

# Pièce Locker Room
class LockerRoom(Piece):
    """Pièce Locker Room
    Plusieurs clés à la découverte répandues dans le manoir"""

    def __init__(self, row: int, porte_entree: str):
        # Deux portes opposées
        config = {"nord": False, "sud": False, "est": False, "ouest": False}
        config[porte_entree] = True

        # La porte opposée 
        if porte_entree == "nord":
            config["sud"] = True
        elif porte_entree == "sud":
            config["nord"] = True
        elif porte_entree == "est":
            config["ouest"] = True
        elif porte_entree == "ouest":
            config["est"] = True

        super().__init__(
            nom="Locker Room",
            row=row,
            porte_config=config,
            image_path="Images_Blue_Prince/Images/Rooms/Locker_Room.png",
            rarete=3,     
            gemmes=1,     
            couleur="bleue",
            effet_special="Ajoute plusieurs clés réparties dans le manoir"
        )

    def on_discover(self, joueur, jeu, col, row):
        super().on_discover(joueur, jeu, col, row)

        # Nombre de clés aléatoire entre 3 et 6 
        nbre_cles = random.randint(3, 6)
        joueur.inventaire.ajouter_cles(nbre_cles)


# Pièce Den
class Den(Piece):
    """Pièce Den
    +1 gemme
    Trois portes en T"""

    def __init__(self, row: int, porte_entree: str):
        # Trois portes : disposition en T (entrée + deux latérales)
        config = {"nord": False, "sud": False, "est": False, "ouest": False}
        config[porte_entree] = True

        # Ajoute deux autres portes perpendiculaires à l’entrée
        if porte_entree in ["nord", "sud"]:
            config["est"] = True
            config["ouest"] = True
        else:  # entrée par est ou ouest
            config["nord"] = True
            config["sud"] = True

        super().__init__(
            nom="Den",
            row=row,
            porte_config=config,
            image_path="Images_Blue_Prince/Images/Rooms/Den.png",
            rarete=1,        
            gemmes=0,         
            couleur="bleue",
            effet_special="Contient 1 gemme à la découverte"
        )

    def on_discover(self, joueur, jeu, col, row):
        super().on_discover(joueur, jeu, col, row)
        joueur.inventaire.ajouter_gemmes(1)


# Pièce Wine Cellar
# Pièce Trophy Room
# Pièce Ballroom
# Pièce Pantry
# Pièce Rumpus Room
# Pièce Office

