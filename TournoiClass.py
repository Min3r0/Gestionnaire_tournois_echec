import JoueurClass


class Tournament:
    def __init__(self, name, date, participants_players=None, matchs=None):
        self.name = name
        self.date = date
        self.participants_players = participants_players or []
        self.matchs = matchs or []

    def add_player(self, Player):
        self.participants_players.append(Player)

    def add_match(self, match):
        self.matchs.append(match)

    def __repr__(self):
        tournament_info = f"Tournoi {self.name}, date: {self.date}\n"

        return tournament_info
