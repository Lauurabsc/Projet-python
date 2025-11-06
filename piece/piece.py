import pygame
from ..porte import Porte

TAILLE_CASE = 70

class Piece : 
    """
        Classe de base pour toute les pièces du manoir pour ses caractéristiques et son affichage.
    """
    def __init__(self, nom, row, porte_config, gemmes, rarete, image_path, objet, effet_special, condition_placement, couleur): 

        self.nom = nom
        self.gemmes = gemmes
        self.objets = objet
        self.effet_special = effet_special
        self.rarete = rarete
        self.condition_placement = condition_placement
        self.couleur = couleur 
        self.image_path= image_path


        self.position =(None, row)
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

    def draw(self, fenetre): 
        """
        Méthode pour dessiner la pièce sur la fenêtre principale. 
        """
        if self.est_decouverte : 
            fenetre.blit(self.image_surface, self.rect)

    def on_enter(self, joueur):
        """ Méthode appelée quand le joueur entre dans la pièce."""
        print(f"Le joueur entre dans : {self.nom}")
        pass 

    def on_draft(self, joueur,jeu): 
        """Méthode appelée quand le joueur choisit cette pièce"""
        pass

    def on_discover(self, joueur, jeu): 
        """Méthode appelée quand la pièce est placée sur la grille"""
        pass


