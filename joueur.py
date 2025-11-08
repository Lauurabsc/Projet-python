import pygame
from Inventaire import Inventaire


class Joueur : 
    """
    Classe représentant le joueur :

    Elle gère : 
        - La position du joueur dans le manoir
        - Les méthodes de déplacement 
        - Elle possède un objet inventaire
    """

    def __init__(self, ligne_depart, colonne_depart):

        """
        Initialise le joueur.
        """

        # Position de départ
        self.ligne = ligne_depart
        self.colonne = colonne_depart

        # Inventaire
        self.inventaire = Inventaire()
        
        #Effet
        self.effets_actifs = {}

    def deplacer(self, direction, manoir):
        """
        Tente de déplacer le joueur dans une direction.
        Retire 1 pas à chaque déplacement réussi (possible).
        """
        deplacement_reussi = False

        if direction == "haut":
            if self.ligne > 0:
                self.ligne -= 1
                deplacement_reussi = True
                
        elif direction == "bas":
            if self.ligne < manoir.lignes - 1:
                self.ligne += 1
                deplacement_reussi = True
                
        elif direction == "gauche":
            if self.colonne > 0:
                self.colonne -= 1
                deplacement_reussi = True
                
        elif direction == "droite":
            if self.colonne < manoir.colonnes - 1:
                self.colonne += 1
                deplacement_reussi = True
        
        # Si le déplacement a réussi, nous retirons 1 pas
        if deplacement_reussi:
            self.inventaire.consommer_pas()

            
        return deplacement_reussi
    

    def dessiner_curseur(self, surface_manoir, taille_case, couleur):
        """
        Dessine le cadre blanc (curseur) à la position actuelle du joueur.
        """
        rect_joueur_x = self.colonne * taille_case
        rect_joueur_y = self.ligne * taille_case
        
        pygame.draw.rect(surface_manoir,couleur,(rect_joueur_x, rect_joueur_y, taille_case, taille_case),3)