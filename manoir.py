import pygame

OPOSITE_DIRECTION_DICT = {'nord':'sud',
                          'sud':'nord',
                          'est':'ouest',
                          'ouest':'est'}

class Manoir:
    """
    Classe représentant le manoir du jeu.

    Le manoir est une grille de 9 lignes sur 5 colonnes.
    Chaque case pourra contenir un objet 'Piece' (pièce du manoir).
    """

    def __init__(self):
        """
        Constructeur du manoir
        Initialisation des valeurs par défaut
        """
        self.lignes = 9
        self.colonnes = 5
        self.taille_case = 70
        self.largeur = self.colonnes * self.taille_case
        self.hauteur = self.lignes * self.taille_case
        self.surface = pygame.Surface((self.largeur, self.hauteur))

        # Grille logique : tableau 2D contenant des None
        # Chaque none représente une case vide du manoir
        self.grille = [[None for _ in range(self.colonnes)] for _ in range(self.lignes)]

        # Couleur de la grille : bleu
        self.couleur_grille = (22, 70, 158)

    def dessiner(self):
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
                pygame.draw.rect(self.surface, self.couleur_grille, (x, y, self.taille_case, self.taille_case), 1)

    def ajouter_piece(self, piece, ligne, colonne):
        """
        Ajoute une pièce dans la grille du manoir à la position donnée.
        Les pièces de départ et d'arrivées sont fixes.

        Paramètres :
        - piece : objet de classe Piece
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
    
    def is_bordure(self, coordonnees):
        """ Renvoie True si les coordonnes en entrées sont sur une bordure du manoir
            coordonnes = (ligne, colonne)        
        """
        if coordonnees[0] in [0, self.lignes-1]:
            return True
        elif coordonnees[1] in [0, self.colonnes-1]:
            return True
        else :
            return False
        
    def is_in_grille(self, coordonnees):
        """Renvoie True si les coordonnees existent dans la grille du manoir
            False sinon
        """
        x = coordonnees[0]
        y = coordonnees[1]
        return x >=0 and x < self.lignes and y >= 0 and y < self.colonnes
        
    def recuperer_pieces_adjacentes(self, coordonnees):
        """Renvoie direction:piece si la piece existe dans le manoir
        La direction a pour référence la pièce adjacente.
        {nord: piece1, est:piece2}
        """
        pieces_adjacentes = {}
        for x, direction in ((-1,'nord'),(1,'sud')):
            if self.is_in_grille([coordonnees[0]+x,coordonnees[1]]):
                piece = self.grille[coordonnees[0]+x][coordonnees[1]]
                if piece:
                    pieces_adjacentes[direction] = piece
        
        for y, direction in ((-1,'ouest'),(1,'est')):
            if self.is_in_grille([coordonnees[0],coordonnees[1]+y]):
                piece = self.grille[coordonnees[0]][coordonnees[1]+y]
                if piece:
                    pieces_adjacentes[direction] = piece
        return pieces_adjacentes
    
    def recuperer_contraintes(self, coordonnees, direction_entree):
        """
        Récupèrer l'ensembles des contraintes sur les portes de la piecesà drafter
        """
        # par rapport aux dimensions du manoir
        contrainte_dict = self.recuperer_contraintes_bordure(coordonnees)
        # par rapport à la direction d'entrée du joueur
        contrainte_dict[direction_entree] = True
        
        # par rapport aux autres pieces déjà découvertes
        pieces_list = self.recuperer_pieces_adjacentes(coordonnees)
        pieces_list.pop(direction_entree)
        for direction, piece in pieces_list.items():
            oposite_direction = OPOSITE_DIRECTION_DICT[direction]
            contrainte_dict[direction] = piece.porte_config[oposite_direction]
        
        return contrainte_dict
            

        
    def recuperer_contraintes_bordure(self, coordonnees):
        """
        Récupère les contraintes sur les portes de la piece à drafeter en lien avec les dimensions du manoir
        """
        contrainte_dict = {}
        if coordonnees[0] == self.lignes -1:
            contrainte_dict['sud'] = False
        if coordonnees[0] == 0:
            contrainte_dict['nord'] = False
        if coordonnees[1] == self.colonnes -1:
            contrainte_dict['est'] = False
        if coordonnees[1] == 0:
            contrainte_dict['ouest'] = False
        return contrainte_dict
        
        
