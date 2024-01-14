class Match:
    def __init__(self, player1, player2, result=None):
        self.player1 = player1
        self.player2 = player2
        self.result = result  # Peut être None si le match n'a pas encore été joué

    def register_result(self, result):
        self.result = result

    def __repr__(self):
        return f"Match entre {self.player1} et {self.player2}, résultat: {self.result}"
