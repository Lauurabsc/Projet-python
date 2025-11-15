import random

from piece.pieces_oranges import Corridor, Foyer, Hallway, PassageWay
from piece.pieces_bleues import (Den, Garage, Nook, RampusRoom, TrophyRoom,
                                 Vault)
from piece.pieces_vertes import Cloister, Courtyard
from piece.pieces_violettes import (Bedrooms, GuestBedroom, MasterBedroom,
                                 ServantsQuarters)

class Pioche : 
    """
    Gère la pioche des pièces, la rareté et le tirage.
    """
    class_piece_list = [Bedrooms, GuestBedroom, ServantsQuarters, MasterBedroom, Foyer, Hallway, PassageWay, Corridor, Den, Garage, Nook, Vault,  RampusRoom, TrophyRoom, Courtyard, Cloister]
    
    def __init__(self):
        
        # On stockes les classes de pièces
        self.pieces_disponibles = self.creer_pioche_initiale()

    def creer_pioche_initiale(self): 
        """
        Crée la liste des pièces disponibles en respectant la rareté.
        """
        pioche = []

        for piece in self.class_piece_list:
            pioche.extend([piece]*(6//piece.rarete))
        
        return pioche

    def tirer_trois_pieces(self, contrainte_dict, is_bordure): 
        """
        Tire trois pièces valides de la pioche.
        C'est ici qu'on gère les conditions d'éligibilité
        Retourne aussi l'angle de rotation à appliquer à la pièce
        """

        if len(self.pieces_disponibles) < 3:
            return []
        
        # Exclure les pieces non accessibles
        class_piece_eligible = {}
        for class_piece in self.class_piece_list:
            piece = class_piece()
            is_eligible, angle = piece.est_eligible(contrainte_dict, is_bordure)
            if is_eligible:
                class_piece_eligible[class_piece] = angle        
        pieces_eligibles = [piece for piece in self.pieces_disponibles if piece in class_piece_eligible.keys()]
        
        classes_tirees = random.sample(pieces_eligibles, 3)
        # Verification si une piece coûte 0 gemmes
        for piece_class in classes_tirees:
            if piece_class.gemmes == 0:
                piece_tiree_1 = [classes_tirees[0],class_piece_eligible[classes_tirees[0]]]
                piece_tiree_2 = [classes_tirees[1],class_piece_eligible[classes_tirees[1]]]
                piece_tiree_3 = [classes_tirees[2],class_piece_eligible[classes_tirees[2]]]
                return [piece_tiree_1, piece_tiree_2, piece_tiree_3]
        
        classes_eligibles_gratuites = [piece for piece in pieces_eligibles if piece.gemmes == 0 ]
        classes_tirees[-1] = random.sample(classes_eligibles_gratuites, 1)[0]
        piece_tiree_1 = [classes_tirees[0],class_piece_eligible[classes_tirees[0]]]
        piece_tiree_2 = [classes_tirees[1],class_piece_eligible[classes_tirees[1]]]
        piece_tiree_3 = [classes_tirees[2],class_piece_eligible[classes_tirees[2]]]
        return [piece_tiree_1, piece_tiree_2, piece_tiree_3]
    
    def retirer_piece(self, classe_piece): 
        """
        Retire une pièce de la pioche après qu'elle a été choisie
        """
        self.pieces_disponibles.remove(classe_piece)
