from piece.piece import Piece
from porte import Porte


class Hallway(Piece): 
    """Pièce Hallway
    """
    rarete = 1
    gemmes = 0
    image_path="Images_Blue_Prince/Images/Hallways/Hallway.png"
    nom="Hallway"
    couleur="orange"
    objets=['pommes','gemmes']
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
    def on_discover(self, joueur, manoir, col, row):
        super().on_discover(joueur, manoir, col, row)
        # Faire aléatoire présence de pomme ou gemmes dans la pièce 
        
# Foyer
class Foyer(Piece):
    """"pièce Foyer
    """
    rarete = 2
    gemmes = 2
    image_path = "Images_Blue_Prince/Images/Hallways/Foyer.png"
    nom = "Foyer"
    couleur ="orange"
    objets = ['gemmes', 'kit_crochetage', 'patte_lapin']
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
    
    def on_discover(self, joueur, manoir, row, col): 
        """
        Le joueur obtient l'effet 'deverrouillage foyer' qui déverrouille toutes les portes des pièces oranges existantes
        et toutes les futures.
        """
        
        joueur.ajouter_effets('deverouillage_foyer')

        # Parcourt la grille pour dévérouiller les pièces oranges 
        for r in manoir.grille : 
            for piece in r : 
                if piece and piece.couleur == "orange": 
                    print(f"Déverrouillage des portes de {piece.nom}")
                    for porte in piece.portes.values(): 
                        if porte is not None : 
                            porte.niveau_verouillage = 0 

# PassageWay
class PassageWay(Piece):
    """"pièce Passage way
    """
    rarete = 1
    gemmes = 2
    image_path = "Images_Blue_Prince/Images/Hallways/Passageway.png"
    nom = "Passageway"
    couleur ="orange"
    objets = [] # reste vide 
    def __init__(self):
        config = {"nord": True, "sud": True, "est": True, "ouest": True}
        super().__init__(
            nom=self.nom,
            porte_config=config,
            image_path=self.image_path,
            rarete=self.rarete,
            gemmes=self.gemmes,
            objets=self.objets,
            couleur=self.couleur
        )

# Corridor
class Corridor(Piece):
    """"pièce Corridor
    """
    rarete = 1
    gemmes = 0
    image_path = "Images_Blue_Prince/Images/Hallways/Corridor.png"
    nom = "Corridor"
    couleur ="orange"
    objets = [] # reste vide 
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

    def generate_portes(self, joueur, ligne, direction_entree):
        # porte forcément déverrouillée pour cette piece
        for direction, est_presente in self.porte_config.items():
            if est_presente:
                self.portes[direction] = Porte(ligne=ligne, force_unlocked=True)




