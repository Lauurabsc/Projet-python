import pygame
from ..porte import Porte

TAILLE_CASE = 70

class Piece : 
    """
        Classe de base pour toute les pièces du manoir pour ses caractéristiques et son affichage.
    """
    def __init__(self, nom, row, porte_config, image_path, gemmes=0, rarete=1, objets=None, effet_special=None, condition_placement=None, couleur=None): 

        self.nom = nom
        self.gemmes = gemmes
        self.objets = objets if objets is not None else []
        self.effet_special = effet_special
        self.rarete = rarete
        self.condition_placement = condition_placement
        self.couleur = couleur 
        self.image_path = image_path


        self.position =(None, None)
        self.est_decouverte = False

        # Creation des portes
        self.portes = {
            "nord": None,
            "sud": None,
            "est": None,
            "ouest": None
        }

        for direction, est_presente in porte_config.items():
            if est_presente:
                self.portes[direction] = Porte(row=row)

        # Charge l'image de la pièce
        self.image_surface = pygame.image.load(image_path)
        self.image_surface = pygame.transform.scale(self.image_surface, (TAILLE_CASE, TAILLE_CASE))

        # Gère la position en PIXELS de la pièce sur l'écran

        self.rect = self.image_surface.get_rect()
    
    def set_position_pixels(self, col,row): 
        """Met à jour la position logique (grille) et
        la position d'affichage (pixels) de la pièce.
        """
        self.position = (col,row)
        self.rect.x = col * TAILLE_CASE
        self.rect.y = row * TAILLE_CASE


    def draw(self, fenetre): 
        """
        Méthode pour dessiner la pièce sur la fenêtre principale. 
        """
        if self.est_decouverte : 
            fenetre.blit(self.image_surface, self.rect)

    def on_enter(self, joueur,jeu):
        """ Méthode appelée quand le joueur entre dans la pièce."""
        print(f"Le joueur entre dans : {self.nom}")
        pass 

    def on_draft(self, joueur,jeu): 
        """Méthode appelée quand le joueur choisit cette pièce"""
        pass

    def on_discover(self, joueur, jeu, col, row): 
        """Méthode appelée quand la pièce est placée sur la grille"""
        self.set_position_pixels(col,row)
        self.est_decouverte = True
        print(f"La pièce {self.nom} est découverte et placée en ({col}, {row})")


