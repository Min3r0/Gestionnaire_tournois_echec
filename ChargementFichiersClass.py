import json

from JoueurClass import Joueur
from TournoiClass import Tournoi


class ChargementFichiers:
    @staticmethod
    def charger_joueurs():
        try:
            with open('joueurs.json', 'r') as fichier:
                joueurs_data = json.load(fichier)
                joueurs = [Joueur(**joueur) for joueur in joueurs_data]
                return joueurs
        except FileNotFoundError:
            return []

    @staticmethod
    def charger_tournois():
        try:
            with open('tournois.json', 'r') as fichier:
                tournois_data = json.load(fichier)
                tournois = [Tournoi(**tournoi) for tournoi in tournois_data]
                return tournois
        except FileNotFoundError:
            return []
