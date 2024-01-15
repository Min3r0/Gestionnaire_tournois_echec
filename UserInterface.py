import MatchClass
import Verification
import display
import export_result
from LoadingFilesClass import LoadingFiles
from GestionFichiersClass import FileManagement
from JoueurClass import Player
from TournoiClass import Tournament
from Verification import check_format_date, verif_score


class UserInterface:
    @staticmethod
    def display_menu():
        print("""
        Bienvenue dans le gestionnaire de tournois d'échecs
        1. Créer un joueur
        2. Créer un tournoi
        3. Enregistrer un joueur dans un tournois
        4. Créer un match
        5. Enregistrer un résultat de match
        6. Exporter les résultats d'un tournoi au format CSV
        7. Voir la liste des joueurs
        8. Quitter
        """)

    @staticmethod
    def add_player():
        global birth_date, elo_ranking
        name = input("Entrez le nom du joueur: ")
        name = name.upper()
        firstname = input("Entrez le prénom du joueur: ")
        firstname = firstname.capitalize()

        date_verification = False
        while not date_verification:
            birth_date = input("Entrez la date de naissance du joueur (AAAA-MM-JJ): ")
            date_verification = check_format_date(birth_date)
            if not birth_date:
                print("La date de naissance n'est pas dans le bon format (AAAA-MM-JJ)")

        if Verification.player_already_exists(name, firstname, birth_date):
            print("Ce joueur existe déjà.")
            return

        valid_elo_ranking = False
        while not valid_elo_ranking:
            elo_ranking = input("Entrez le classement Elo du joueur: ")
            try:
                elo_ranking = int(elo_ranking)
                if elo_ranking >= 0:
                    valid_elo_ranking = True
                else:
                    print("Le classement Elo doit être un nombre positif.")
            except ValueError:
                print("Veuillez entrer un nombre entier pour le classement Elo.")

        player = LoadingFiles.load_players()
        identifier = len(player) + 1
        new_player = Player(identifier, name, firstname, birth_date, elo_ranking)
        player.append(new_player)
        FileManagement.save_players(player)


    @staticmethod
    def find_player_by_id(player_id):
        players = LoadingFiles.load_players()
        player_id = int(player_id)
        for player in players:
            if player.ID == player_id:
                return player
        return None

    @staticmethod
    def create_tournament():
        global date_tournament
        tournament_name = input("Entrez le nom du tournoi: ")

        date_verification = False
        while not date_verification:
            date_tournament = input("Entrez la date du tournoi (AAAA-MM-JJ): ")
            date_verification = check_format_date(date_tournament)
            if not date_verification:
                print("La date du tournoi n'est pas dans le bon format (AAAA-MM-JJ)")

        tournament = LoadingFiles.load_tournaments()
        new_tournament = Tournament(tournament_name, date_tournament)
        tournament.append(new_tournament)
        FileManagement.save_tournaments(tournament)

    @staticmethod
    def add_player_to_tournament():
        display.display_tournament()
        tournament_name = input("Dans quel tournoi voulez-vous ajouter un joueur : ")
        tournaments = LoadingFiles.load_tournaments()

        selected_tournament = None
        for tournament in tournaments:
            if tournament.name == tournament_name:
                selected_tournament = tournament
                break
        if selected_tournament is None:
            print(f"Aucun tournoi trouvé avec le nom {tournament_name}.")
            return

        display.display_player()
        player_id = input("Entrez l'ID du joueur à ajouter : ")
        player = UserInterface.find_player_by_id(player_id)
        if player is None:
            print(f"Aucun joueur trouvé avec le nom {player_id}.")
            return

        selected_tournament.add_player(player)
        FileManagement.save_tournaments(tournaments)
        print(f"Le joueur {player.name} {player.firstname} a été ajouté au tournoi {selected_tournament.name}.")

    @staticmethod
    def create_match():
        display.display_tournament()
        tournament_name = input("Dans quel tournoi voulez-vous créer le match : ")
        tournaments = LoadingFiles.load_tournaments()

        selected_tournament = None
        for tournament in tournaments:
            if tournament.name == tournament_name:
                selected_tournament = tournament
                break

        if selected_tournament is None:
            print(f"Aucun tournoi trouvé avec le nom {tournament_name}.")
            return

        display.display_players_of_tournament(selected_tournament)

        player1_name = input("Entrez l'ID du joueur 1 : ")
        player2_name = input("Entrez l'ID du joueur 2 : ")
        player1 = UserInterface.find_player_by_id(player1_name)
        player2 = UserInterface.find_player_by_id(player2_name)

        if player1 is None or player2 is None:
            print("Un ou plusieurs joueurs ne sont pas trouvés.")
            return

        # Créer un nouveau match
        new_match = MatchClass.Match(player1, player2)

        # Ajouter le match à la liste des matchs du tournoi
        selected_tournament.add_match(new_match)

        # Sauvegarder les tournois mis à jour dans le fichier tournois.json
        FileManagement.save_tournaments(tournaments)

    @staticmethod
    def register_match_result():
        global selected_tournament, selected_match, result
        tournaments = LoadingFiles.load_tournaments()

        print("Liste des tournois disponibles :")
        for index, tournament in enumerate(tournaments, start=1):
            print(f"{index}. {tournament.name}")

        enter_check = False
        while not enter_check:
            tournament_choice = int(input("Sélectionnez un tournoi (entrez le numéro) : ")) - 1
            if 0 <= tournament_choice < len(tournaments):
                selected_tournament = tournaments[tournament_choice]
                enter_check = True
            else:
                print("L'entrée n'est pas bonne")

        print(f"Matchs du tournoi {selected_tournament.name} :")
        for index, match in enumerate(selected_tournament.matchs, start=1):
            print(f"{index}. {match}")

        enter_check = False
        while not enter_check:
            match_choice = int(input("Sélectionnez un match à enregistrer (entrez le numéro) : ")) - 1
            if 0 <= match_choice < len(selected_tournament.matchs):
                selected_match = selected_tournament.matchs[match_choice]
                enter_check = True
            else:
                print("L'entrée n'est pas bonne")

        enter_check = False
        while not enter_check:
            result = input("Entrez le résultat du match (1-0, 0.5-0.5, 0-1) : ")
            enter_check = verif_score(result)
            if not enter_check:
                print("L'entrée n'est pas bonne")

        # Assurez-vous que selected_match est une instance de la classe Match
        if isinstance(selected_match, MatchClass.Match):
            selected_match.register_result(result)
            FileManagement.save_tournaments(tournaments)
        else:
            print("Erreur : le match sélectionné n'est pas valide.")


if __name__ == "__main__":
    while True:
        UserInterface.display_menu()
        choice = input("Entrez le numéro de l'option souhaitée: ")

        if choice == "1":
            UserInterface.add_player()
        elif choice == "2":
            UserInterface.create_tournament()
        elif choice == "3":
            UserInterface.add_player_to_tournament()
        elif choice == "4":
            UserInterface.create_match()
        elif choice == "5":
            UserInterface.register_match_result()
        elif choice == "6":
            export_result.exporter_resultats_csv()
        elif choice == "7":
            display.display_player()
        elif choice == "8":
            print("Fin du programme merci et à bientôt")
            break
        else:
            print("Choix invalide. Veuillez sélectionner une option valide.")
