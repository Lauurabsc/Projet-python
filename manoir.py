import pygame


class Manoir:
    """
    Classe représentant le manoir du jeu.


    Le manoir est une grille de 9 lignes sur 5 colonnes.
    Chaque case pourra contenir un objet 'Piece' (pièce du manoir).
    """


    def __init__(self, lignes=9, colonnes=5, taille_case=70):
        """
        Constructeur du manoir
        Paramètres :
        - lignes : nombre de lignes (hauteur)
        - colonnes : nombre de colonnes (largeur)
        - taille_case : dimension de chaque case (en pixels)
        """
        self.lignes = lignes
        self.colonnes = colonnes
        self.taille_case = taille_case


        # Grille logique : tableau 2D contenant des None
        # Chaque none représente une case vide du manoir
        self.grille = [[None for _ in range(colonnes)] for _ in range(lignes)]


        # Couleur de la grille : bleu
        self.couleur_grille = (22, 70, 158)


    def dessiner(self, surface):
        """
        Cette fonction dessine la grille du manoir sur la fenêtre.
        Chaque case est un rectangle vide délimitant les différentes pièces du manoir.
        """
        for i in range(self.lignes):
            for j in range(self.colonnes):
                # Coordonnées (x, y) du coin supérieur gauche
                x = j * self.taille_case
                y = i * self.taille_case


                # Tracé des bordures des rectangles
                pygame.draw.rect(surface, self.couleur_grille, (x, y, self.taille_case, self.taille_case), 1)


    def ajouter_piece(self, piece, ligne, colonne):
        """
        Ajoute une pièce dans la grille du manoir à la position donnée.
        Les pièces de départ et d'arrivées sont fixes.


        Paramètres :
        - piece : objet de type Piece
        - ligne : position verticale dans la grille
        - colonne : position horizontale dans la grille
        """
        if 0 <= ligne < self.lignes and 0 <= colonne < self.colonnes:
            # Ajoute la pièce dans la grille logique
            self.grille[ligne][colonne] = piece


            # Calcule la position où afficher la pièce à l’écran
            piece.rect.topleft = (colonne * self.taille_case, ligne * self.taille_case)


            # Rend la pièce visible dès qu’elle est placée
            piece.est_decouverte = True  
