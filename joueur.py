import pygame
from Inventaire import Inventaire
from piece.piece import Piece 
from porte import Porte

class Joueur : 
    """
    Classe représentant le joueur :

    Elle gère : 
        - La position du joueur dans le manoir
        - Les méthodes de déplacement 
        - Elle possède un objet inventaire
    """

    def __init__(self, ligne_depart, colonne_depart):

        """
        Initialise le joueur.
        """

        # Position de départ
        self.ligne = ligne_depart
        self.colonne = colonne_depart

        # Inventaire
        self.inventaire = Inventaire()
        
        #Effet
        self.effets_actifs = {}

    def tenter_action(self, direction, manoir): 
        """
        Tente de se déplacer OU d'ouvrir une porte dans une direction.
        Ne modifie pas la position du joueur, mais renvoie un statut.
        
        :param direction: "nord", "sud", "ouest", "est"
        :param manoir: l'objet Manoir pour vérifier la grille
        :return: (str, tuple) ou (str, None)
                 - ("MOUVEMENT_ECHOUE", None) : Mur, hors grille, porte verrouillée
                 - ("MOUVEMENT_REUSSI", (new_ligne, new_col)) : Déplacement vers une pièce connue
                 - ("DECOUVERTE", (new_ligne, new_col)) : Ouvre une porte vers une case vide
        """

        piece_actuelle = manoir.grille[self.ligne][self.colonne]

        # Traduction de la direction en coordonées cibles
        target_ligne, target_colonne = self.ligne, self.colonne

        if direction == "nord":
            target_ligne -= 1
        elif direction == "sud":
            target_ligne += 1
        elif direction == "ouest":
            target_colonne -= 1
        elif direction == "est":
            target_colonne += 1

        # Vérifier les limites de la grille

        if not (0 <= target_ligne < manoir.lignes and 0 <= target_colonne < manoir.colonnes):
            return "MOUVEMENT_ECHOUE", None
        
        # Vérifier si la pièce actuelle a une porte dans cette direction
        porte = piece_actuelle.portes.get(direction)
        if porte is None:
            return "MOUVEMENT_ECHOUE", None
        
        # Vérifier si la porte est vérrouillé
        # A faire : Gérer l'utilisation des clés et kit de corchetage
        if porte.est_verouillee():

            niveau_porte = porte.niveau_verouillage
            a_le_kit = "Lockpick" in self.inventaire.objets_permanents

            # Logique pour le niveau 1
            if niveau_porte == 1:

                if a_le_kit:
                    porte.niveau_verouillage = 0 # On déverrouille la porte
                # Sinon, on vérifie si le joueur a une clé
                elif self.inventaire.depense_cle(1): 
                    print("Porte (Niv 1) ouverte avec 1 Clé.")
                    porte.niveau_verouillage = 0
                else:
                    print("Porte (Niv 1) verrouillée. Clé ou Kit requis.")
                    return "MOUVEMENT_ECHOUE", None

            # Logique pour le niveau 2
            elif niveau_porte == 2:
                # Le kit ne fonctionne pas ici 
                if self.inventaire.depense_cle(1):
                    print("Porte (Niv 2) ouverte avec 1 Clé.") 
                    porte.niveau_verouillage = 0
                else:
                    print("Porte (Niv 2) verrouillée. Clé requise.")
                    return "MOUVEMENT_ECHOUE", None
            
            # Logique pour les portes scellées (Antechamber)
            elif niveau_porte == "scellee":
                print("Cette porte est scellée.") 
                return "MOUVEMENT_ECHOUE", None

        # La porte est accessible
        piece_cible = manoir.grille[target_ligne][target_colonne]
        coordonnees_cible = (target_ligne, target_colonne)

        if piece_cible is not None:
            #La pièce existe déjà, c'est un simple déplacement
            return "MOUVEMENT_REUSSI", coordonnees_cible
        else:
            #La pièce n'existe pas
            return "DECOUVERTE", coordonnees_cible


    def deplacer_vers(self, ligne, colonne):
        """
        Met à jour la position du joueur et consomme un pas.
        """
        self.ligne = ligne
        self.colonne = colonne
        self.inventaire.consommer_pas()
        print(f"Joueur déplacé en ({ligne}, {colonne}). Pas restants : {self.inventaire.pas}")
    

    def dessiner_curseur(self, surface_manoir, taille_case, couleur):
        """
        Dessine le cadre blanc (curseur) à la position actuelle du joueur.
        """
        rect_joueur_x = self.colonne * taille_case
        rect_joueur_y = self.ligne * taille_case
        
        pygame.draw.rect(surface_manoir,couleur,(rect_joueur_x, rect_joueur_y, taille_case, taille_case),3)