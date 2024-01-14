class Tournoi:
    def __init__(self, nom, date):
        self.nom = nom
        self.date = date
        self.joueurs_participants = []  # Liste des identifiants des joueurs participants
        self.matchs = []  # Liste des matchs du tournoi

    def ajouter_joueur(self, identifiant_joueur):
        self.joueurs_participants.append(identifiant_joueur)

    def ajouter_match(self, match):
        self.matchs.append(match)

    def __repr__(self):
        return f"Tournoi {self.nom}, date: {self.date}, joueurs participants: {self.joueurs_participants}"
