class Tournament:
    def __init__(self, name, date):
        self.name = name
        self.date = date
        self.participants_players = []  # Liste des identifiants des joueurs participants
        self.matchs = []  # Liste des matchs du tournoi

    def add_players(self, identifiant_joueur):
        self.participants_players.append(identifiant_joueur)

    def add_match(self, match):
        self.matchs.append(match)

    def __repr__(self):
        return f"Tournoi {self.name}, date: {self.date}, joueurs participants: {self.participants_players}"
