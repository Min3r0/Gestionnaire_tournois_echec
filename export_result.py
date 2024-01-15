import csv

from LoadingFilesClass import LoadingFiles
from MatchClass import Match


def exporter_resultats_csv():
    tournois = LoadingFiles.load_tournaments()

    # Afficher la liste des tournois disponibles
    print("Liste des tournois disponibles :")
    for index, tournoi in enumerate(tournois, start=1):
        print(f"{index}. {tournoi.name}")

    # Sélectionner un tournoi
    choix_tournoi = int(input("Sélectionnez un tournoi (entrez le numéro) : ")) - 1
    tournoi_selectionne = tournois[choix_tournoi]

    # Demander le nom du fichier CSV pour l'exportation
    nom_fichier_csv = input("Entrez le nom du fichier CSV pour l'exportation : ")

    # Exporter les résultats du tournoi sélectionné au format CSV
    with open(nom_fichier_csv, 'w', newline='') as csvfile:
        writer = csv.writer(csvfile)

        # Écrire l'en-tête du fichier CSV
        writer.writerow(["Joueur 1", "Joueur 2", "Résultat"])

        # Écrire les résultats de chaque match dans le fichier CSV
        for match in tournoi_selectionne.matchs:
            # Assurez-vous que match est une instance de la classe Match
            if isinstance(match, Match):
                writer.writerow([match.player1.name, match.player2.name, match.result])
            else:
                print("Erreur : le match sélectionné n'est pas valide.")

    print(f"Les résultats du tournoi {tournoi_selectionne.name} ont été exportés dans {nom_fichier_csv}")
