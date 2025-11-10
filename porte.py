import random


class Porte :
    """
    Représente une porte connectant deux pièces dans le manoir.


    Chaque porte possède un niveau de verrouillage qui détermine
    si le joueur peut la franchir et si cela nécessite une clé.
    """


    def __init__(self, row, force_unlocked=False):
        """
        Initialise une nouvelle instance de Porte.


        :param verouillage: (int, optionnel) Le niveau de verrouillage initial.
                            0 = déverrouillée (défaut).
        """
        if force_unlocked:
            self.niveau_verouillage = 0
        else:
            self.verouillage_aleatoire(row)


    def est_verouillee(self):
        """
        Vérifie si la porte est actuellement verrouillée (niveau 1 ou 2).


        :return: (bool) True si la porte est verrouillée, False sinon.
        """
        # On vérifie si c'est un entier > 0
        if isinstance(self.niveau_verouillage, int):
            return self.niveau_verouillage > 0
        
        # On vérifie si c'est "scellee"
        if isinstance(self.niveau_verouillage, str):
            return self.niveau_verouillage == "scellee"
        
        return False
   
    def verouillage_aleatoire(self, row):
        """
        Définit aléatoirement le niveau de verrouillage en fonction de la rangée.


        La difficulté (probabilité de verrous) augmente avec le numéro de
        la rangée, en suivant les règles du projet :
        - Rangée 0 : Toujours niveau 0.
        - Rangée 8 : Toujours niveau 2.
        - Rangées 1-7 : Probabilité progressive basée sur un tirage.


        :param row: (int) Le numéro de la rangée (0-8) où la porte se situe.
        """
        # Première rangée --> que des portes dévérouillées
        if row == 0 :
            self.niveau_verouillage = 0


        #Dernière rangée --> que des portes verouillées à double tour
        elif row == 8 :
            self.niveau_verouillage = 2


        #Rangée intermédiaire : Plus la rangée augmente, plus la proba d'avoir des niveaux élevées augmente
        elif 1<= row <= 7 :
            niveaux_possibles = [0,1,2]
            poids_total = 12


            tirage = random.randint(1,poids_total) #Lance un dé de 1 à 12


            # Division des 12 résultats en 3 tranches


            # Tranche 2 : Difficile
            seuil_lvl_2 = row


            # Tranche 1 : Moyen
            seuil_lvl_1 = seuil_lvl_2 + 4


            # Tranche 0 : le reste


            # Si le dé tombe sur la première tranche --> vérouillé à double tour
            if tirage <= seuil_lvl_2 :
                self.niveau_verouillage = 2


            # Si le dé tombe sur la tranche 2 : porte vérouillée
            elif tirage <= seuil_lvl_1 :
                self.niveau_verouillage = 1


            #Si le dé n'est tombé sur aucune des deux tranches : porte dévérouillé
            else :
                self.niveau_verouillage = 0


   
