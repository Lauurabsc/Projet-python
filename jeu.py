# Importation des bibliothèques
import pygame
from manoir import Manoir

class Jeu:
    """
    Classe principale du jeu
    
    Elle gère :
    - l'initialisation de Pygame,
    - la création de la fenêtre d'affichage,
    - la boucle principale du jeu (gestion des événements et rafraîchissement de l'écran).
    - l'affichage du manoir
    """

    def __init__(self):
        """
        Constructeur de la classe Jeu.
        Initialise la fenêtre, le titre du jeu et les variables de contrôle
        """
        # Initialisation de pygame (affichage, clavier, etc.)
        pygame.init()

        # Dimensions de la fenêtre exprimées en pixels
        self.LARGEUR = 350
        self.HAUTEUR = 630

        # Création de la fenêtre du jeu
        self.fenetre = pygame.display.set_mode((self.LARGEUR, self.HAUTEUR))
        # Titre de la fenêtre 
        pygame.display.set_caption("Blue Prince - Version IPS")

        # Création du manoir
        self.manoir = Manoir()

        # Contrôle de la boucle de jeu
        self.en_cours = True # La boucle est active

        self.clock = pygame.time.Clock()  # Régule le nombre d'images par seconde

    def boucle_principale(self):
        """
        Boucle principale du jeu
        
        Elle tourne tant que la variable "en_cours" est vraie.
        À chaque itération :
        - les événements (fermeture, clavier, etc.) sont traités
        - la fenêtre est remplie (fond noir)
        - l'affichage est mis à jour
        """
        # Tant que en_cours est vrai, FAIRE : 
        while self.en_cours:
            # Parcours des événements du joueur
            for evenement in pygame.event.get():
                if evenement.type == pygame.QUIT: # Si on clique sur la croix de la fenêtre
                    self.en_cours = False # On sort de la boucle 

            # Couleur de fond = noir - accueille la grille, le joueur, etc.
            self.fenetre.fill((0, 0, 0))

            # Dessin des cases composant la grille
            self.manoir.dessin_case(self.fenetre)

            # A COMPLETER

            # Rafraîchit l'écran
            pygame.display.flip()

            # Vitesse d’actualisation (30 images par seconde)
            self.clock.tick(30)

        # Quitte Pygame à la fin du jeu
        pygame.quit()
