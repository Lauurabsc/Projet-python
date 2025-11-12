import random 
from piece.pieceorange import Hallway, SecretPassage, Foyer, GreatHall
from piece.pieceviolette import Bedrooms, GuestBedroom, ServantsQuarters, MasterBedroom
from piece.pieces_bleues import Vault, Nook, Garage, LockerRoom, Den

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
        pioche.extend([Hallway] * 10)         # Orange
        pioche.extend([Bedrooms] * 5)         # Violette
        pioche.extend([GuestBedroom] * 5)     # Violette
        pioche.extend([Nook] * 5)             # Bleue
        pioche.extend([Den] * 5)              # Bleue

        # Rareté 2
        pioche.extend([SecretPassage] * 5)    # Orange
        pioche.extend([ServantsQuarters] * 3) # Violette
        pioche.extend([Garage] * 3)           # Bleue

        # Rareté 3
        pioche.extend([Foyer] * 2)            # Orange
        pioche.extend([GreatHall] * 2)        # Orange
        pioche.extend([MasterBedroom] * 2)    # Violette
        pioche.extend([Vault] * 2)            # Bleue
        pioche.extend([LockerRoom] * 2)       # Bleue

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
