# Importation des bibliothèques
import pygame
import sys

# Initialisation de pygame (affichage, clavier, etc.)
pygame.init()

# Création de la fenêtre
    # Taille de la fenêtre exprimée en pixels
LARGEUR, HAUTEUR = 900, 500
fenetre = pygame.display.set_mode((LARGEUR, HAUTEUR))
    # Titre de la fenêtre
pygame.display.set_caption("Blue Prince - Version IPS")

# Boucle principale du jeu
clock = pygame.time.Clock() # Régule le nombre d'images par seconde
en_cours = True # la boucle est active

# Tant que en_cours est vrai, FAIRE : 
while en_cours:
    # On récupère les évènements du joueur
    for evenement in pygame.event.get():
        if evenement.type == pygame.QUIT: # Si on clique sur la croix de la fenêtre
            en_cours = False # On sort de la boucle 

    # Couleur de fond = noir - accueille la grille, le joueur, etc.
    fenetre.fill((0, 0, 0))

    # Affiche à l'écran
    pygame.display.flip()

    # Vitesse d’actualisation (30 images par seconde)
    clock.tick(30)

# Ferme pygame
pygame.quit()
# Termine le programme python
sys.exit()