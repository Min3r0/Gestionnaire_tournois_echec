class Joueur:
    def __init__(self, identifiant, nom, prenom, date_naissance, classement_elo):
        self.identifiant = identifiant
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.classement_elo = classement_elo

    def modifier_joueur(self, nom, prenom, date_naissance, classement_elo):
        self.nom = nom
        self.prenom = prenom
        self.date_naissance = date_naissance
        self.classement_elo = classement_elo

    def __repr__(self):
        return f"Joueur {self.identifiant}: {self.prenom} {self.nom}, né le {self.date_naissance}, Elo: {self.classement_elo}"
