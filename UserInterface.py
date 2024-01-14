import Verification
import export_result
from ChargementFichiersClass import LoadingFiles
from GestionFichiersClass import FileManagement
from JoueurClass import Player
from TournoiClass import Tournament
from Verification import check_format_date, verif_score


class UserInterface:
    @staticmethod
    def display_menu():
        print("Bienvenue dans le gestionnaire de tournois d'échecs")
        print("1. Ajouter un joueur")
        print("2. Créer un tournoi")
        print("3. Enregistrer un résultat de match")
        print("4. Exporter les résultats d'un tournoi au format CSV")
        print("5. Quitter")

    @staticmethod
    def add_player():
        global birth_date, elo_ranking
        name = input("Entrez le nom du joueur: ")
        firstname = input("Entrez le prénom du joueur: ")

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

        player = LoadingFiles.charger_joueurs()
        identifier = len(player) + 1
        new_player = Player(identifier, name, firstname, birth_date, elo_ranking)
        player.append(new_player)
        FileManagement.save_players(player)

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
    def register_match_result():
        global selected_tournament, selected_match, result
        tournament = LoadingFiles.load_tournaments()

        print("Liste des tournament disponibles :")
        for index, tournament in enumerate(tournament, start=1):
            print(f"{index}. {tournament.name}")

        enter_check = False
        while not enter_check:
            tournament_choice = int(input("Sélectionnez un tournoi (entrez le numéro) : ")) - 1
            if 0 <= tournament_choice < len(tournament):
                selected_tournament = tournament[tournament_choice]
                enter_check = True
            print("L'entrer n'est pas bonne")

        print(f"Matchs du tournoi {selected_tournament.name} :")
        for index, match in enumerate(selected_tournament.matchs, start=1):
            print(f"{index}. {match}")

        enter_check = False
        while not enter_check:
            tournament_choice = int(input("Sélectionnez un match à enregistrer (entrez le numéro) : ")) - 1
            if 0 <= tournament_choice < len(selected_tournament.matchs):
                selected_match = selected_tournament.matchs[tournament_choice]
                enter_check = True
            print("L'entrer n'est pas bonne")

        enter_check = False
        while not enter_check:
            result = input("Entrez le résultat du match (1-0, 0.5-0.5, 0-1) : ")
            enter_check = verif_score
            if not enter_check:
                print("L'entrer n'est pas bonne")

        selected_match.register_result(result)
        FileManagement.save_tournaments(tournament)


if __name__ == "__main__":
    while True:
        UserInterface.display_menu()
        choice = input("Entrez le numéro de l'option souhaitée: ")

        if choice == "1":
            UserInterface.add_player()
        elif choice == "2":
            UserInterface.create_tournament()
        elif choice == "3":
            UserInterface.register_match_result()
        elif choice == "4":
            export_result.exporter_resultats_csv()
        elif choice == "5":
            break
        else:
            print("Choix invalide. Veuillez sélectionner une option valide.")
