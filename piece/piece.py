import pygame
from porte import Porte


TAILLE_CASE = 70


class Piece :
    """
        Classe de base pour toute les pièces du manoir pour ses caractéristiques et son affichage.
    """


    def __init__(self, nom, row,col, porte_config, gemmes=0, rarete=0, image_path=None,
             objets=None, effet_special=None, condition_placement=None, couleur=None, porte_entree_direction=None,default_orientation=None):


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

                # Vérifie si la porte en cours de création est la porte d'entrée
                est_la_porte_entree = (direction == porte_entree_direction)

                # On force le déverouillage si c'est le cas
                self.portes[direction] = Porte(row=row, force_unlocked=est_la_porte_entree)


        # Charge l'image de la pièce
        original_surface = pygame.image.load(image_path)

        # Appliquer la rotation si nécessaire
        rotated_surface = self.rotate_image_if_needed(
            original_surface, 
            default_orientation, 
            porte_entree_direction
        )
        self.image_surface = pygame.transform.scale(rotated_surface, (TAILLE_CASE, TAILLE_CASE))

        # Gère la position en PIXELS de la pièce sur l'écran
        self.rect = self.image_surface.get_rect()
        
    def rotate_image_if_needed(self, surface, default_orientation, new_direction):
        """
        Fait pivoter la surface de l'image si la direction d'entrée 
        ne correspond pas à l'orientation par défaut de l'image.
        
        Suppose que l'orientation par défaut est "sud" (le bas de l'image).
        """
        # Si l'image n'a pas d'orientation (symétrique) ou si on est dans la bonne direction
        if not default_orientation or not new_direction or default_orientation == new_direction:
            return surface # Pas de rotation

        # On définit que l'orientation par défaut de nos images est "sud" (le bas)
        orientation_map = {
            "sud": 0,    # L'image de base pointe vers le sud
            "est": 90,   # Pour entrer par l'ouest, tourner de 90° anti-horaire
            "nord": 180,   # Pour entrer par le nord, tourner de 180°
            "ouest": 270     # Pour entrer par l'est, tourner de 270° (ou -90°)
        }


        # Angle de l'image de base
        default_angle = orientation_map[default_orientation]
        # Angle de la nouvelle porte d'entrée
        new_angle = orientation_map[new_direction]
            
        # L'angle de rotation est la différence
        rotation_angle = new_angle - default_angle
            
        if rotation_angle != 0:
            return pygame.transform.rotate(surface, rotation_angle)
        else:
            return surface

   
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


    def on_discover(self, joueur, jeu, col, row, direction_entree):
        """Méthode appelée quand la pièce est placée sur la grille"""
        self.set_position_pixels(col,row)
        self.est_decouverte = True
        print(f"La pièce {self.nom} est découverte et placée en ({col}, {row})")


