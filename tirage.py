import random 
from piece.pieceorange import Hallway, SecretPassage, Foyer, GreatHall

class Pioche : 
    """
    Gère la pioche des pièces, la rareté et le tirage.
    """
    def __init__(self):
        # On stockes les classes de pièces
        self.pieces_disponibles = self.creer_pioche_initiale()

    def creer_pioche_initiale(self): 
        """
        Crée la liste des pièces disponibles en respectant la rareté.
        """
        pioche = []

        # Rareté 1 
        pioche.extend([Hallway] * 10)

        # Rareté 2
        pioche.extend([SecretPassage] * 5)

        # Rareté 3
        pioche.extend([Foyer] * 2)
        pioche.extend([GreatHall] * 2)

        # TO DO : Ajouter les autres pièces

        return pioche

    def tirer_trois_pieces(self, ligne_cible): 
        """
        Tire trois pièces valides de la pioche.
        C'est ici qu'on gère la rareté et les conditions.
        """

        # A Ajouter : logique de rareté, une piece coute 0 gemmes, Verifier conditions de placement

        if len(self.pieces_disponibles) < 3:
            return []
            
        classes_tirees = random.sample(self.pieces_disponibles, 3)
        return classes_tirees
        
    def retirer_piece(self, classe_piece): 
        """
        Retire une pièce de la pioche après qu'elle a été choisie
        """
        self.pieces_disponibles.remove(classe_piece)
