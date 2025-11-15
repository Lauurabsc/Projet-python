# Importation des bibliothèques
import pygame

from Inventaire import Inventaire
from joueur import Joueur
from manoir import Manoir
from piece.piece_special import Antechamber, EntranceHall
from tirage import Pioche


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
    
        # Le rectangle qui définit où dessiner cette surface sur la fenêtre principale
        self.rect_manoir = self.manoir.surface.get_rect(topleft=(50, 50))

        # Pièce d'entrée
        self.entree = EntranceHall(row=8, col=2)
            # Placement de la pièce d'entrée sur la grille
        self.manoir.ajouter_piece(self.entree, ligne=8, colonne=2)

        # Pièce de sortie
        self.sortie = Antechamber(row=0, col=2)
            # Placement de la pièce de sortie sur la grille
        self.manoir.ajouter_piece(self.sortie, ligne=0, colonne=2)

        # Zones inventaire (en huat à droite)
        self.rect_inventaire = pygame.Rect(
            self.rect_manoir.right + 50,  
            self.rect_manoir.top,        
            800,                          
            250                          
        )

        # Zones des pièces

        self.rect_choix_piece = pygame.Rect(
            self.rect_inventaire.left,    
            self.rect_inventaire.bottom + 50, 
            self.rect_inventaire.width,  
            400                          
        )

        # Création du joueur à la position de départ (EntranceHall)
        self.joueur = Joueur(ligne_depart=8, colonne_depart=2)

        # Jeu a 2 états : "EXPLORATION" ou "TIRAGE_PIECE"
        self.etat_jeu = "EXPLORATION"

        # Création de la pioche
        self.pioche = Pioche()

        # Les 3 pièces qui sont proposées
        self.pieces_proposees = []

        # Où la nouvelle pièce sera placée
        self.coordonnees_tirage = None
        
        # Par quelle porte le joueur va entrer
        self.direction_entree = None

        # Map pour traduire la direction de l'action en direction d'entrée 
        self.map_direction_opposee = {"nord": "sud", "sud": "nord", "ouest": "est", "est": "ouest"}
        
        # Curseur d'action par le déplacement
        self.porte_selectionnee = None

        # Map pour traduire ZQSD en direction
        self.map_mouvement_direction = {
            pygame.K_z: "nord",
            pygame.K_s: "sud",
            pygame.K_q: "ouest",
            pygame.K_d: "est"
        }

        # Contrôle de la boucle de jeu
        self.en_cours = True # La boucle est active
        self.clock = pygame.time.Clock()  # Régule le nombre d'images par seconde

    def lancer_tirage_piece(self, coords_cible, direction_action):
        """
        Passe le jeu en mode "TIRAGE_PIECE".
        Demande 3 pièces à la Pioche et les instancie.
        """
        ligne_cible, col_cible = coords_cible
        self.direction_entree = self.map_direction_opposee[direction_action]
        # contrainte sur les pieces eligibles
        contrainte_dict ={}
        if ligne_cible == self.manoir.lignes:
            contrainte_dict['nord'] = False
        if ligne_cible == 0:
            contrainte_dict['sud'] = False
        if col_cible == self.manoir.largeur:
            contrainte_dict['est'] = False
        if col_cible == 0:
            contrainte_dict['ouest'] = False
        contrainte_dict[self.direction_entree] = False
        # Demande 3 classes de pièce à la Pioche
        classes_tirees = self.pioche.tirer_trois_pieces(contrainte_dict)
        
        if not classes_tirees:
            print("Tirage annulé (pioche vide ?)")
            return 

        #Stocker les infos
        self.coordonnees_tirage = coords_cible
        self.pieces_proposees = []
        
        #  Instancier les 3 pièces
        for classe_piece in classes_tirees:
            piece = classe_piece(row=ligne_cible, col=col_cible, porte_entree_direction=self.direction_entree)
            self.pieces_proposees.append(piece)

            
        # Changer l'état du jeu
        self.etat_jeu = "TIRAGE_PIECE"

    def confirmer_choix_piece(self, index_choix): 
        """
        Finalise le choix du joueur, place la pièce, déplace le joueur
        et remet le jeu en mode EXPLORATION.
        """
        # Vérifie si l'index est valide
        if not (0 <= index_choix < len(self.pieces_proposees)):
            print(f"Erreur : Choix d'index invalide ({index_choix})")
            return

        # Récupère la pièce choisie
        piece_choisie = self.pieces_proposees[index_choix]
        
        # Payer le coût en gemmes
        self.joueur.inventaire.depense_gemmes(piece_choisie.gemmes)
        # Retirer la classe de la pièce de la pioche
        self.pioche.retirer_piece(type(piece_choisie))
        
        # Générer les portes de la pièce 
        ligne, col = self.coordonnees_tirage
        piece_choisie.generate_portes(ligne, self.direction_entree)
        
        # Ajouter la pièce au manoir
        self.manoir.ajouter_piece(piece_choisie, ligne, col)
        
        # Appeler 'on_discover' pour les effets de pose 
        piece_choisie.on_discover(self.joueur, self, col, ligne, self.direction_entree)
        
        # Appeler 'on_draft' pour les effets de choix 
        piece_choisie.on_draft(self.joueur, self)
        
        # Déplacer le joueur dans la nouvelle pièce
        self.joueur.deplacer_vers(ligne, col)
        
        # Appeler 'on_enter'
        piece_choisie.on_enter(self.joueur, self)
        
        #Revenir à l'exploration
        self.etat_jeu = "EXPLORATION"
        self.pieces_proposees = []
        self.coordonnees_tirage = None
        self.direction_entree = None

    def dessiner_interface_droite(self): 
        """
        Dessine l'interface de droite (inventaire + zone d'action)
        en fonction de l'état du jeu.
        """
        # Dessin de l'inventaire (toujours affiché)
        pygame.draw.rect(self.fenetre, self.COULEUR_CADRE, self.rect_inventaire, 2)
        texte_inv = self.font_titre.render("Inventaire", True, self.COULEUR_CADRE)
        self.fenetre.blit(texte_inv, (self.rect_inventaire.x + 10, self.rect_inventaire.y + 10))
        
        # Affichage de l'inventaire
        self.joueur.inventaire.afficher(self.fenetre, self.rect_inventaire)

        
        # Dessin de la zone d'action (change en fonction de l'état)
        pygame.draw.rect(self.fenetre, self.COULEUR_CADRE, self.rect_choix_piece, 2)

        if self.etat_jeu == "EXPLORATION":
            # Afficher les instructions de déplacement
            titre = self.font_titre.render("Exploration", True, self.COULEUR_CADRE)
            self.fenetre.blit(titre, (self.rect_choix_piece.x + 10, self.rect_choix_piece.y + 10))

            txt_zqsd = self.font_normal.render("ZQSD : Se déplacer ", True, self.COULEUR_CADRE)
            self.fenetre.blit(txt_zqsd, (self.rect_choix_piece.x + 10, self.rect_choix_piece.y + 50))
            
            txt_arrow = self.font_normal.render("Flèches : Viser une porte", True, self.COULEUR_CADRE)
            self.fenetre.blit(txt_arrow, (self.rect_choix_piece.x + 10, self.rect_choix_piece.y + 75))

            txt_space = self.font_normal.render("ESPACE : Ouvrir / Traverser", True, self.COULEUR_CADRE)
            self.fenetre.blit(txt_space, (self.rect_choix_piece.x + 10, self.rect_choix_piece.y + 100))

            # Afficher la porte visée
            txt_visee = self.font_normal.render(f"Porte visée : {self.porte_selectionnee.upper()}", True, (255, 255, 0))
            self.fenetre.blit(txt_visee, (self.rect_choix_piece.x + 10, self.rect_choix_piece.y + 140))


        elif self.etat_jeu == "TIRAGE_PIECE":
            # Afficher les 3 pièces proposées
            texte_choix = self.font_titre.render("Choisissez une pièce (1, 2, 3) :", True, (255, 255, 0))
            self.fenetre.blit(texte_choix, (self.rect_choix_piece.x + 10, self.rect_choix_piece.y + 10))
   
            # Affichage des 3 pièces
            card_width = 180
            card_height = 250
            card_y = self.rect_choix_piece.y + 60
            x_start = self.rect_choix_piece.x + 100

            for i, piece in enumerate(self.pieces_proposees):
                # Calcule la position de la carte
                card_x = x_start + i * (card_width + 50)
                rect_card = pygame.Rect(card_x, card_y, card_width, card_height)
                
                # Dessine le cadre
                pygame.draw.rect(self.fenetre, self.COULEUR_CADRE, rect_card, 1)

                # Afficher l'image
                img_scaled = pygame.transform.scale(piece.image_surface, (card_width - 20, card_width - 20))
                self.fenetre.blit(img_scaled, (card_x + 10, card_y + 10))

                
                # Afficher le nom
                nom_texte = self.font_normal.render(piece.nom, True, self.COULEUR_CADRE)
                self.fenetre.blit(nom_texte, (card_x + 10, card_y + card_width))
                
                # Afficher le numéro de choix
                num_texte = self.font_titre.render(str(i+1), True, (255, 255, 0))
                self.fenetre.blit(num_texte, (card_x + (card_width // 2) - 5, card_y + card_height - 35))
    
    def dessiner_curseur_action(self, surface): 
        """
        Dessine le "trait épais" sur la porte sélectionnée (curseur d'action).
        """

        # Position en pixels du coin de la case du joueur
        taille = self.manoir.taille_case
        x = self.joueur.colonne * taille
        y = self.joueur.ligne * taille
        epaisseur = 5 # "Trait épais"
        couleur = (255, 255, 255) # Blanc

        # Marge pour que le trait soit "sur" le bord
        marge = epaisseur // 2

        if self.porte_selectionnee == "nord":
            pygame.draw.line(surface, couleur, (x + marge, y + marge), (x + taille - marge, y + marge), epaisseur)
        elif self.porte_selectionnee == "sud":
            pygame.draw.line(surface, couleur, (x + marge, y + taille - marge), (x + taille - marge, y + taille - marge), epaisseur)
        elif self.porte_selectionnee == "ouest":
            pygame.draw.line(surface, couleur, (x + marge, y + marge), (x + marge, y + taille - marge), epaisseur)
        elif self.porte_selectionnee == "est":
            pygame.draw.line(surface, couleur, (x + taille - marge, y + marge), (x + taille - marge, y + taille - marge), epaisseur)

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
                
                    if self.etat_jeu == "EXPLORATION":

                        # Selection d'une direction par le joueur (ZQSD)
                        if evenement.key in self.map_mouvement_direction:
                            self.porte_selectionnee = self.map_mouvement_direction[evenement.key]
                        
                        # Valider de la direction avec la touche "espace"
                        elif evenement.key == pygame.K_SPACE:
                            statut, coords = self.joueur.tenter_action(self.porte_selectionnee, self.manoir)
                        
                            if statut == "MOUVEMENT_REUSSI":
                                # La porte est ouverte et mène à une pièce connue
                                self.joueur.deplacer_vers(coords[0], coords[1])
                                piece = self.manoir.grille[coords[0]][coords[1]]
                                if piece:
                                    piece.on_enter(self.joueur, self)
                                
                            elif statut == "DECOUVERTE":
                                # Appelle au tirage
                                self.lancer_tirage_piece(coords, self.porte_selectionnee)
                            
                            elif statut == "MOUVEMENT_ECHOUE":
                                print(f"Impossible d'ouvrir la porte {self.porte_selectionnee}.")
                                # (Mur, porte verrouillée, etc.)
                    
                    # Le joueur choisit une pièce
                    elif self.etat_jeu == "TIRAGE_PIECE":
                        if evenement.key == pygame.K_1:
                            self.confirmer_choix_piece(0)
                        elif evenement.key == pygame.K_2:
                            self.confirmer_choix_piece(1)
                        elif evenement.key == pygame.K_3:
                            self.confirmer_choix_piece(2)

                            # A complter le Re-roll avec les dés


            # Couleur de fond = noir - accueille la grille, le joueur, etc.
            self.fenetre.fill(self.COULEUR_FOND)
            
            # Dessin du manoir
            self.manoir.surface.fill(self.COULEUR_FOND)

            # Dessin de la grille sur la surface du manoir
            self.manoir.dessiner()

            # Dessin des pièces
            for ligne in self.manoir.grille:
                for piece in ligne:
                    if piece:
                        piece.draw(self.manoir.surface)

            # Dessin du curseur du joueur sur le manoir
            self.joueur.dessiner_curseur(self.manoir.surface, self.manoir.taille_case, (255, 255, 255))
            
            # On ne dessine le curseur d'action que si on explore
            if self.etat_jeu == "EXPLORATION":
                self.dessiner_curseur_action(self.manoir.surface)

            # Surface du Manoir sur la fenêtre principale
            self.fenetre.blit(self.manoir.surface, self.rect_manoir)

            self.dessiner_interface_droite()

            self.joueur.inventaire.afficher(self.fenetre, self.rect_inventaire)

            # Défaite
                # Si le joueur n'a plus de pas
            if self.joueur.inventaire.pas <= 0:
                texte_defaite = self.font_titre.render ("Plus de pas, la partie est PERDUE !", True, (255, 0, 0))
                self.fenetre.blit(texte_defaite, (self.LARGEUR//2, self.HAUTEUR//2 - 45))        
                pygame.display.flip()
                pygame.time.wait(4000) # Temps pour lire le message de défaite
                self.en_cours = False

            # Victoire
                # Si le joueur atteint la pièce finale
            piece_actuelle = self.manoir.grille[self.joueur.ligne][self.joueur.colonne]
            if isinstance(piece_actuelle, Antechamber):
                ecriture_victoire = pygame.font.Font(None, 55)

                texte_victoire = ecriture_victoire.render("Victoire ! Vous avez atteint l'Antechamber !", True, (255, 215, 0))
                self.fenetre.blit(texte_victoire, (self.LARGEUR//2 - 400, self.HAUTEUR//2 - 45)) 
                pygame.display.flip()
                pygame.time.wait(4000) # Temps pour lire le message de défaite
                self.en_cours = False

            # A COMPLETER

            # Rafraîchit l'écran
            pygame.display.flip()

            # Vitesse d’actualisation (30 images par seconde)
            self.clock.tick(30)

        # Quitte Pygame à la fin du jeu
        pygame.quit()
