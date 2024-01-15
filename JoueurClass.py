class Player:
    def __init__(self, ID, name, firstname, birthdate, elo_ranking):
        self.ID = ID
        self.name = name
        self.firstname = firstname
        self.birthdate = birthdate
        self.elo_ranking = elo_ranking

    def modifier_joueur(self, name, firstname, birthdate, elo_ranking):
        self.name = name
        self.firstname = firstname
        self.birthdate = birthdate
        self.elo_ranking = elo_ranking

    def __repr__(self):
        return f"Joueur {self.ID}: {self.firstname} {self.name}, né le {self.birthdate}, Elo: {self.elo_ranking}"
