# Importation des bibliothèques
import pygame
from manoir import Manoir
from piece.piece_special import EntranceHall, Antechamber
from Inventaire import Inventaire
from joueur import Joueur


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
        #Initialise le module de police
        pygame.font.init()

        # Constantes de le Fenêtre 
        self.LARGEUR = 1280
        self.HAUTEUR = 720

        #Couleur 
        self.COULEUR_FOND = (2, 33, 79)
        self.COULEUR_CADRE = (200, 200, 200)

        # Création de la fenêtre du jeu
        self.fenetre = pygame.display.set_mode((self.LARGEUR, self.HAUTEUR))
        pygame.display.set_caption("Blue Prince - Projet POO")

        self.font_titre = pygame.font.Font(None, 32) 
        self.font_normal = pygame.font.Font(None, 24)


        # Création du manoir
        self.manoir = Manoir()

        #Création de la Surface du Manoir 
        #Création d'une surface dédiée au manoir
        self.taille_case_manoir = self.manoir.taille_case
        self.largeur_manoir_px = self.manoir.colonnes * self.taille_case_manoir
        self.hauteur_manoir_px = self.manoir.lignes * self.taille_case_manoir
        
        #surface de la grille et les pièces
        self.surface_manoir = pygame.Surface((self.largeur_manoir_px, self.hauteur_manoir_px))
        
        # Le rectangle qui définit où dessiner cette surface sur la fenêtre principale
        self.rect_manoir = self.surface_manoir.get_rect(topleft=(50, 50))

        # Pièce d'entrée
        self.entree = EntranceHall()
            # Placement de la pièce d'entrée sur la grille
        self.manoir.ajouter_piece(self.entree, ligne=8, colonne=2)

        # Pièce de sortie
        self.sortie = Antechamber()
            # Placement de la pièce de sortie sur la grille
        self.manoir.ajouter_piece(self.sortie, ligne=0, colonne=2)

        # Zones inventaire (en huat à droite)
        self.rect_inventaire = pygame.Rect(
            self.rect_manoir.right + 50,  
            self.rect_manoir.top,        
            800,                          
            250                          
        )

        self.inventaire = Inventaire()

        # Zones des pièces

        self.rect_choix_piece = pygame.Rect(
            self.rect_inventaire.left,    
            self.rect_inventaire.bottom + 50, 
            self.rect_inventaire.width,  
            400                          
        )

        # Création du joueur à la position de départ (EntranceHall)
        self.joueur = Joueur(ligne_depart=8, colonne_depart=2)

        # Contrôle de la boucle de jeu
        self.en_cours = True # La boucle est active
        self.clock = pygame.time.Clock()  # Régule le nombre d'images par seconde

    def dessiner_titres(self): 
        # Cadres et Titre Inventaire 

        pygame.draw.rect(self.fenetre, self.COULEUR_CADRE, self.rect_inventaire, 2)
        texte_inv = self.font_titre.render("Inventaire", True, self.COULEUR_CADRE)
        self.fenetre.blit(texte_inv, (self.rect_inventaire.x + 10, self.rect_inventaire.y + 10))
        
        # Cadre et Titre Choix des pièces
        pygame.draw.rect(self.fenetre, self.COULEUR_CADRE, self.rect_choix_piece, 2)
        texte_choix = self.font_titre.render("Please choose a room :", True, self.COULEUR_CADRE)
        self.fenetre.blit(texte_choix, (self.rect_choix_piece.x + 10, self.rect_choix_piece.y + 10))
   
        # 3 pièces
        card_width = 180
        card_height = 250
        card_y = self.rect_choix_piece.y + 60

        #Pièce 1 
        rect_card_1 = pygame.Rect(self.rect_choix_piece.x + 100, card_y, card_width, card_height)
        pygame.draw.rect(self.fenetre, self.COULEUR_CADRE, rect_card_1, 1)

        # Pièce 2
        rect_card_2 = pygame.Rect(rect_card_1.right + 50, card_y, card_width, card_height)
        pygame.draw.rect(self.fenetre, (255, 0, 0), rect_card_2, 2) # Bord rouge

        # Pièce 3
        rect_card_3 = pygame.Rect(rect_card_2.right + 50, card_y, card_width, card_height)
        pygame.draw.rect(self.fenetre, self.COULEUR_CADRE, rect_card_3, 1)

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

                # Quitter en appuyant sur ECHAP
                if evenement.type == pygame.KEYDOWN:
                    if evenement.key == pygame.K_ESCAPE:
                        self.en_cours = False
                    
                    # Déplacement du joueur avec le clavier
                    elif evenement.key in [pygame.K_z, pygame.K_UP]:
                        self.joueur.deplacer("haut", self.manoir)
                    elif evenement.key in [pygame.K_s, pygame.K_DOWN]:
                        self.joueur.deplacer("bas", self.manoir)
                    elif evenement.key in [pygame.K_q, pygame.K_LEFT]:
                        self.joueur.deplacer("gauche", self.manoir)
                    elif evenement.key in [pygame.K_d, pygame.K_RIGHT]:
                        self.joueur.deplacer("droite", self.manoir)


            # Couleur de fond = noir - accueille la grille, le joueur, etc.
            self.fenetre.fill(self.COULEUR_FOND)
            
            # Dessin du manoir
            self.surface_manoir.fill(self.COULEUR_FOND)

            # Dessin de la grille sur la surface du manoir
            self.manoir.dessiner(self.surface_manoir)

            # Dessin des cases composant la grille
            self.manoir.dessiner(self.surface_manoir)

            # Dessin des pièces
            for ligne in self.manoir.grille:
                for piece in ligne:
                    if piece:
                        piece.draw(self.surface_manoir)

            # Dessin du curseur du joueur sur le manoir
            self.joueur.dessiner_curseur(self.surface_manoir, self.manoir.taille_case, (255, 255, 255))

            # Surface du Manoir sur la fenêtre principale
            self.fenetre.blit(self.surface_manoir, self.rect_manoir)

            self.dessiner_titres()

            self.joueur.inventaire.afficher(self.fenetre, self.rect_inventaire)

            # A COMPLETER


            # Rafraîchit l'écran
            pygame.display.flip()


            # Vitesse d’actualisation (30 images par seconde)
            self.clock.tick(30)


        # Quitte Pygame à la fin du jeu
        pygame.quit()
