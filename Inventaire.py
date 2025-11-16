# Importation des bibliothèques
import os

import pygame


class Inventaire:
    """
    Classe Inventaire
    Gère les objets du joueur :
    - Objets consommables : pas, pièces d'or, gemmes, clés, dés
    - Objets permanents : détecteur de métal, kit de crochetage, patte de lapin
    """

    def __init__(self):
        # Objets consommables
            # Initialisation
        self.pas = 70     # nombre de pas disponibles
        self.piece_or = 0 # pièces d'or
        self.gemmes = 2   # gemmes
        self.cles = 0     # clés
        self.des = 0      # dés

        # Objets permanents
        self.objets_permanents = []

        # Dossiers d’images
        dossier_consommable = "Images_inventaire/Objets_consommables"
        dossier_permanent = "Images_inventaire/Objets_permanents"

        # Chargement des images 
        self.images = {
            "Pas": self.charger_image("Steps.png", dossier_consommable),
            "Or": self.charger_image("Gold.png", dossier_consommable),
            "Gemme": self.charger_image("Gem.png", dossier_consommable),
            "Clé": self.charger_image("Key.png", dossier_consommable),
            "Dé": self.charger_image("Dice.png", dossier_consommable),

            "Pomme": self.charger_image("pomme.png", dossier_consommable),
            "Lockpick": self.charger_image("Lockpick.png", dossier_permanent),
            "Detecteur_Metal": self.charger_image("Metal_Detector.png", dossier_permanent),
            "Patte_Lapin": self.charger_image("Rabbit_Foot.png", dossier_permanent)
        }

    # Chargement d’image
    def charger_image(self, nom, dossier):
        """Charge et redimensionne l'image"""
        chemin = os.path.join(dossier, nom)
        if os.path.exists(chemin):
            image = pygame.image.load(chemin)
            return pygame.transform.scale(image, (50, 50))

    # Ajout de ressources
    def ajouter_pas(self, n=1):
        """Ajoute n pas"""
        self.pas += n
        
    def ajouter_piece_or(self, n=1):
        """Ajoute n pièces d'or"""
        self.piece_or += n

    def ajouter_gemmes(self, n=1):
        """Ajoute n gemmes"""
        self.gemmes += n

    def ajouter_cles(self, n=1):
        """Ajoute n clés"""
        self.cles += n

    def ajouter_des(self, n=1):
        """Ajoute n dés"""
        self.des += n

    # Dépense de ressources
    def consommer_pas(self, n=1):
        """Retire 1 (=1) pas à chaque déplacement"""
        self.pas = max(0, self.pas - n)

    def depense_piece_or(self, n=1):
        """Dépense n pièces d'or si c'est possible"""
        if n < 0:
            return False
        if self.piece_or >= n:
            self.piece_or -= n
            return True
        return False

    def depense_gemmes(self, n=1):
        """Dépense n gemmes si c'est possible"""
        if n < 0:
            return False
        if self.gemmes >= n:
            self.gemmes -= n
            return True
        return False

    def depense_cle(self, n=1):
        """Dépense n clé si c'est possible"""
        if n < 0:
            return False
        if self.cles >= n:
            self.cles -= n
            return True
        return False

    def depense_de(self, n=1):
        """Dépense n dés si c'est possible"""
        if n < 0:
            return False
        if self.des >= n:
            self.des -= n
            return True
        return False

    # Gestion des objets permanents
    def ajouter_objet_permanent(self, nom):
        """Ajoute un objet permanent seulement s'il n'est pas déjà présent"""
        if nom not in self.objets_permanents:
            self.objets_permanents.append(nom)

    # Affichage à l'écran
    def afficher(self, fenetre, rect_inventaire):
        """Affiche les objets de l'inventaire dans la zone prévue (en haut à droite)."""
        font = pygame.font.SysFont(None, 24)

        # Intérieur du cadre inventaire
        x = rect_inventaire.x + 20
        y = rect_inventaire.y + 50

        ressources = [
        ("Pas", self.pas),
        ("Or", self.piece_or),
        ("Gemme", self.gemmes),
        ("Clé", self.cles),
        ("Dé", self.des)
        ]

        for nom, valeur in ressources:
            image = self.images.get(nom)
            if image:
                fenetre.blit(image, (x, y))
                texte = font.render(str(valeur), True, (255, 255, 255))
                fenetre.blit(texte, (x + 60, y + 15))
                x += 100  # espace horizontal entre les icônes

        # Ligne des objets permanents 
        y = y + 60  # une ligne plus bas
        x = rect_inventaire.x + 20
        for nom in self.objets_permanents:
            image = self.images.get(nom)
            if image:
                fenetre.blit(image, (x, y))
                x += 70
