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
        Il vérifie l'existence d'une porte

        :param direction: (str) "haut", "bas", "gauche", "droite"
        :param manoir: (Manoir) L'objet manoir pour la grille et les limites
        :return: (str) L'action résultante: "MUR", "DEPLACEMENT", ou "TIRAGE"
        """

        piece_actuelle = manoir.grille[self.ligne][self.colonne]
        

        if direction == "haut":
            dir_porte = "nord"
            ligne_cible, col_cible = self.ligne - 1, self.colonne
        elif direction == "bas":
            dir_porte = "sud"
            ligne_cible, col_cible = self.ligne + 1, self.colonne
        elif direction == "gauche":
            dir_porte = "ouest"
            ligne_cible, col_cible = self.ligne, self.colonne - 1
        elif direction == "droite":
            dir_porte = "est"
            ligne_cible, col_cible = self.ligne, self.colonne + 1
        else:
            return "MUR", None
        
        # Vérification si il y a une porte dans la pièce actuelle 

        if piece_actuelle.portes[dir_porte] is None:
            print(f"Déplacement {direction} impossible : C'est un mur.")
            return "MUR", None
        
        # Si la porte existe, verifier la porte est verouillées (à ajouter plus tard)

        # Vérifier si la case cible est dans la grille
        if not (0 <= ligne_cible < manoir.lignes and 0 <= col_cible < manoir.colonnes):
            return "MUR", None # Hors de la grille
    
        # Analyse de la cible
        piece_cible = manoir.grille[ligne_cible][col_cible]

        if piece_cible is not None:
            #La pièce existe déjà
            self.ligne = ligne_cible
            self.colonne = col_cible
            print(f"Déplacement vers pièce existante: {piece_cible.nom}")
            return "DEPLACEMENT", piece_cible
        else:
            # La case est vide
            print("Déplacement vers une case vide, Déclenchement du tirage !")
            # On ne bouge pas encore, on signale au jeu de lancer le tirage
            return "TIRAGE", (ligne_cible, col_cible)

    def dessiner_curseur(self, surface_manoir, taille_case, couleur):
        """
        Dessine le cadre blanc (curseur) à la position actuelle du joueur.
        """
        rect_joueur_x = self.colonne * taille_case
        rect_joueur_y = self.ligne * taille_case
        
        pygame.draw.rect(surface_manoir,couleur,(rect_joueur_x, rect_joueur_y, taille_case, taille_case),3)