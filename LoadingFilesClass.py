import json

from JoueurClass import Player
from TournoiClass import Tournament


class LoadingFiles:
    @staticmethod
    def load_players():
        try:
            with open('joueurs.json', 'r') as fichier:
                joueurs_data = json.load(fichier)
                joueurs = [Player(**joueur) for joueur in joueurs_data]
                return joueurs
        except FileNotFoundError:
            return []

    @staticmethod
    def load_tournaments():
        try:
            with open('tournois.json', 'r') as fichier:
                tournois_data = json.load(fichier)
                tournois = [Tournament(**tournoi) for tournoi in tournois_data]
                return tournois
        except FileNotFoundError:
            return []


