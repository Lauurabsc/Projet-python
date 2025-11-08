from .piece import Piece
from ..porte import Porte


class Hallway(Piece): 
    """Pièce Hallway 
    La pièce la plus simple, avec 4 portes
    """
    def __init__(self,row): 
        config = {"nord": True, "sud": True, "est": True, "ouest": True}
    
        super().__init__(
            nom="Hallway",
            row=row,
            porte_config=config,
            image_path="Images_Blue_Prince/Images/Hallways/Hallway.png", 
            gemmes=0,
            rarete=1, 
            objets=None,
            effet_special=None,
            condition_placement=None,
            couleur="orange"
        )

class SecretPassage(Piece): 
    """Pièce 'Secret passage'
    Pièce sans issue qui déclenche un choix de 3 pièce après selection d'une couleur
    """
    
    def __init__(self, row, porte_entree): 

        config = {"nord": False, "sud": False, "est": False, "ouest": False}
        config[porte_entree] = True

        super().__init__(
            nom="Secret Passage",
            row=row,
            porte_config=config,
            image_path="Images_Blue_Prince/Images/Hallways/Secret_Passage.png", # Supposition
            gemmes=0,
            rarete=2, 
            objets=None,
            effet_special="Déclenche un draft de couleur spécial",
            condition_placement=None,
            couleur="orange"
        )

    def on_enter(self, joueur, jeu): 
        """Effet activé à l'entrée du joueur"""
        super().on_enter(joueur, jeu)

        # A ajouter dans jeu.py : La logique du jeu (choix du livre, génération des 3 salles et des 2 sécurité doit etre dans la fonction de l'objet 'jeu')

        pass


class Foyer(Piece): 
    """Pièce 'Foyer'
    Effet : Déverouille toutes les portes des couloirs (pièces oranges) actuels et futurs.
    """

    def __init__(self, row): 
        config = {"nord": True, "sud": True, "est":False, "ouest": False}
        super().__init__(
            nom="Foyer",
            row=row,
            porte_config=config,
            image_path="Images_Blue_Prince/Images/Hallways/Foyer.png", 
            gemmes=1, 
            rarete=3,
            objets=None,
            effet_special="Déverrouille toutes les portes des couloirs",
            condition_placement=None,
            couleur="orange"
        )

    def on_draft(self, joueur, jeu): 

        """Effect activé au moment du choix
        1. Ajoute un drpaeua permanent au joueur
        2. Déverouille tous les couloirs déjà posés
        """

        if not hasattr(joueur, "effet_actifs"): 
            joueur.effet_actifs = {}
        joueur.effet_actifs["deverouillage_foyer"] = True

        # Parcourt la grille pour dévérouiller les pièces oranges 
        for r in jeu.manoir.grille : 
            for piece in r : 
                if piece and piece.couleur == "orange": 
                    print(f"Déverrouillage des portes de {piece.nom}")
                    for porte in piece.portes.values(): 
                        if porte is not None : 
                            porte.niveau_verouillage = 0 


class GreatHall(Piece): 
    """Pièce 'Great Hall'
    Un grand couloir dont les portes sont verouillées sauf si le joueur possède un Foyer. 
    """

    def __init__(self, row, porte_entree):
        config = {"nord": True, "sud": True, "est": True, "ouest": True}

        # Porte où le joueur est entrée pour ne pas la verouiller
        self.porte_entree_direction = porte_entree

        super().__init__(
            nom="Great Hall",
            row=row,
            porte_config=config,
            image_path="Images_Blue_Prince/Images/Hallways/Great_Hall.png",
            gemmes=1, 
            rarete=3, 
            objets=None,
            effet_special="Portes verrouillées sans Foyer",
            condition_placement=None,
            couleur="orange"
        )

    def on_discover(self, joueur, jeu, col, row) : 
        """
        Effet activé à la pose d
        Vérifie si le joueur à l'effet "Foyer". 
        """

        super().on_discover(joueur, jeu, col, row)

        # Verification si le joueur a l'effet du Foyer

        if hasattr(joueur, "effet_actifs"):
            a_le_foyer = joueur.effet_actifs.get("deverouillage_foyer", False)
        else:
            a_le_foyer = False

        if a_le_foyer :

            for porte in self.portes.values(): 
                if porte is not None: 
                    porte.niveau_verouillage = 0
        else : 
            for direction, porte in self.portes.items(): 
                if porte is not None : 
                    if direction == self.porte_entree_direction: 
                        porte.niveau_verouillage = 0 
                    else : 
                        porte.niveau_verouillage = 1


