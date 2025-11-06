from ..porte import Porte

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



