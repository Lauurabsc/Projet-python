from porte import Porte

class Piece : 
    
    def __init__(self, nom, row, porte_config, gemmes, rarete, image, objet, effet_special, condition_placement): 
        self.nom = nom
        self.gemmes = gemmes
        self.objets = objet
        self.effet_special = effet_special
        self.rarete = rarete
        self.condition_placement = condition_placement

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

    def on_enter(self, joueur):
        """ Méthode appelée quand le joueur entre dans la pièce."""
        print(f"Le joueur entre dans : {self.nom}")



class EntranceHall(Piece): 

    """Pièce de départ"""

    def __init(self, row = 0): 

        config = {
            "nord": True,
            "sud": False, # Mur
            "est": True,
            "ouest": True
        }

        super().__init__(
            nom="Entrance Hall",
            row=row,
            portes_config=config,
            cost_gemmes=0,
            rarete=0
        )

        for porte in self.portes.values():
            if porte is not None:
                porte.niveau_verouillage = 0