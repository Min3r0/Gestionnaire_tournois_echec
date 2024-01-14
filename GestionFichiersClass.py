import json


class FileManagement:
    @staticmethod
    def save_players(joueurs):
        with open('joueurs.json', 'w') as fichier:
            json.dump(joueurs, fichier, default=lambda obj: obj.__dict__)

    @staticmethod
    def save_tournaments(tournois):
        with open('tournois.json', 'w') as fichier:
            json.dump(tournois, fichier, default=lambda obj: obj.__dict__)
