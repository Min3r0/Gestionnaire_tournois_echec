import LoadingFilesClass


def display_player():
    players = LoadingFilesClass.LoadingFiles.load_players()

    if not players:
        print("Aucun joueur trouvé.")
    else:
        print("Liste des joueurs :")
        for joueur in players:
            print(joueur)


def display_tournament():
    tournaments = LoadingFilesClass.LoadingFiles.load_tournaments()

    if not tournaments:
        print("Aucun tournoi trouvé.")
    else:
        print("Liste des tournois :")
        for tournament in tournaments:
            print(tournament)


def display_players_of_tournament(selected_tournament):
    if not selected_tournament.participants_players:
        print(f"Aucun joueur n'est inscrit au tournoi {selected_tournament.name}.")
    else:
        print(f"Joueurs inscrits au tournoi {selected_tournament.name} :")
        for joueur in selected_tournament.participants_players:
            print(joueur)
