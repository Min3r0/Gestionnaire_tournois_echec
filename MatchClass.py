class Match:
    def __init__(self, joueur1, joueur2, resultat=None):
        self.joueur1 = joueur1
        self.joueur2 = joueur2
        self.resultat = resultat  # Peut être None si le match n'a pas encore été joué

    def enregistrer_resultat(self, resultat):
        self.resultat = resultat

    def __repr__(self):
        return f"Match entre {self.joueur1} et {self.joueur2}, résultat: {self.resultat}"
