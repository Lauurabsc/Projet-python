import pygame
import random
from porte import Porte

TAILLE_CASE = 70

class Piece :
    """
        Classe de base pour toute les pièces du manoir pour ses caractéristiques et son affichage.
    """
    def __init__(self, nom, porte_config, image_path, gemmes=0, rarete=0,
             objets=None, effet_special=None, condition_placement=None, 
             couleur=None):
        
        self.nom = nom
        self.gemmes = gemmes
        self.porte_config = porte_config
        self.objets = objets if objets is not None else []
        self.effet_special = effet_special
        self.rarete = rarete
        self.condition_placement = condition_placement
        self.couleur = couleur
        self.image_path = image_path
        self.position = (None, None)
        self.est_decouverte = False
        self.portes = {}
        
        # Charge l'image de la pièce
        self.original_surface = pygame.image.load(self.image_path)
        self.image_surface = pygame.transform.scale(self.original_surface, (TAILLE_CASE, TAILLE_CASE))

        # Gère la position en PIXELS de la pièce sur l'écran
        self.rect = self.image_surface.get_rect()
    
    def generate_portes(self, joueur, ligne, direction_entree):
        """Genere les portes de la piece
        """ 
        force_unlocked = False
        if self.couleur == 'orange' and 'deverouillage_foyer' in joueur.effets_actifs:
            force_unlocked = True
        for direction, est_presente in self.porte_config.items():
            if force_unlocked:  
                self.portes[direction] = Porte(ligne=ligne, force_unlocked=force_unlocked)
            elif est_presente:
                # Vérifie si la porte en cours de création est la porte d'entrée
                est_la_porte_entree = (direction == direction_entree)
                # On force le déverouillage si c'est le cas
                self.portes[direction] = Porte(ligne=ligne, force_unlocked=est_la_porte_entree)
    
    def est_eligible(self, contrainte_dict, is_bordure):
        """vérifie si la piece est eligible au tirage 
            par rapport à des contraintes sur les portes disponibles
            par rapport condition_placement et à la position dans le manoir
            
            contrainte_dict (dict): {nord/sud/ouest/est : True/False}
                True : une porte dans la direction doit exister
                False : une porte dans la direction ne doit pas exister
            is_bordure (bool): 
                True si la position de la future position du joueur est en bordure du manoir
                False sinon
                
            Retourne True, angle si la pièce est éligible.
            angle représente l'angle de rotation à appliquer à la configuration par défaut de la pièce 
            pour la rendre éligible à contrainte_dict. S'il y a plusieurs angles possibles, retourne la première obtenue
            Retroune False, None sinon           
        """
        if not is_bordure and self.condition_placement == 'bordure':
            return False, None
            
        if is_bordure and self.condition_placement == 'centre':
            return False, None
        
        eligible = False
        for angle in (0, 90, 180, 270):
            self.rotate_piece(angle)
            result = []
            for direction in contrainte_dict.keys():
                result.append(contrainte_dict[direction] == self.porte_config[direction])
            try:
                result.remove(False)
            except ValueError:
                eligible = True
                print(f"Piece {self.nom} éligible : {self.porte_config}")
            if eligible:
                return True, angle
            self.rotate_piece(360-angle)
        return False, None
                
    def rotate_piece(self, angle=90):
        """Tourne une piece selon l'angle souhaité.
        L'angle souhaité doit être un multiple de 90 compris entre 90 et 270
        """
        if angle in [90, 180, 270]:
            if angle == 90:
                self.porte_config = {'nord':self.porte_config['ouest'],
                                    'sud':self.porte_config['est'],
                                    'est':self.porte_config['nord'],
                                    'ouest':self.porte_config['sud']}

            elif angle == 180:
                self.porte_config = {'nord':self.porte_config['sud'],
                                    'sud':self.porte_config['nord'],
                                    'est':self.porte_config['ouest'],
                                    'ouest':self.porte_config['est']}
        
            elif angle == 270:
                self.porte_config = {'nord':self.porte_config['est'],
                                    'sud':self.porte_config['ouest'],
                                    'est':self.porte_config['sud'],
                                    'ouest':self.porte_config['nord']}

            rotated_surface = pygame.transform.rotate(self.original_surface, -angle)
            self.image_surface = pygame.transform.scale(rotated_surface, (TAILLE_CASE, TAILLE_CASE))
        
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

    def on_enter(self, joueur):
        """ Méthode appelée quand le joueur entre dans la pièce.
        Gère l'apparition ALÉATOIRE des objets listés dans self.objets.
        """
        print(f"Le joueur entre dans : {self.nom}")

        a_la_patte = "Patte_Lapin" in joueur.inventaire.objets_permanents
        a_le_detecteur = "Detecteur_Metal" in joueur.inventaire.objets_permanents

        map_objet_action = {
            "Pomme": lambda: joueur.inventaire.ajouter_pas(2), 
            "Gemme": lambda: joueur.inventaire.ajouter_gemmes(1),
            "Clé": lambda: joueur.inventaire.ajouter_cles(1),
            "Dé": lambda: joueur.inventaire.ajouter_des(1),
            "Or": lambda: joueur.inventaire.ajouter_piece_or(1), 
            
            # Objets permanents 
            "Kit_crochetage": lambda: joueur.inventaire.ajouter_objet_permanent("Kit_crochetage"),
            "Detecteur_Metal": lambda: joueur.inventaire.ajouter_objet_permanent("Detecteur_Metal"),
            "Patte_Lapin": lambda: joueur.inventaire.ajouter_objet_permanent("Patte_Lapin"),
        }

        for nom_objet in self.objets:
    
            if nom_objet in map_objet_action:
                
                chance_de_base = 0.5 # 30% de base
                

                if a_la_patte:
                    chance_de_base += 0.40 # Bonus de 20% 
                    

                if a_le_detecteur and nom_objet in ["cles", "piece_or"]:
                    chance_de_base += 0.40 # Bonus de 25% 

                if random.random() < chance_de_base:
                    if nom_objet in ["kit_crochetage", "detecteur_metal", "patte_lapin"]:
                        if nom_objet not in joueur.inventaire.objets_permanents:
                            action = map_objet_action[nom_objet]
                            action()
                    
                    else:
                        action = map_objet_action[nom_objet]
                        action()

        pass

    def on_draft(self, joueur, jeu):
        """Méthode appelée quand le joueur choisit cette pièce"""
        pass


    def on_discover(self, joueur, manoir, col, row):
        """Méthode appelée quand la pièce est placée sur la grille"""
        self.set_position_pixels(col,row)
        self.est_decouverte = True
        print(f"La pièce {self.nom} est découverte et placée en ({row}, {col})")


