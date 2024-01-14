import json


class GestionFichiers:
    @staticmethod
    def sauvegarder_joueurs(joueurs):
        with open('joueurs.json', 'w') as fichier:
            json.dump(joueurs, fichier, default=lambda obj: obj.__dict__)

    @staticmethod
    def sauvegarder_tournois(tournois):
        with open('tournois.json', 'w') as fichier:
            json.dump(tournois, fichier, default=lambda obj: obj.__dict__)
