from ChargementFichiersClass import ChargementFichiers
from GestionFichiersClass import GestionFichiers
from JoueurClass import Joueur
from TournoiClass import Tournoi
from Verification import verifier_format_date, verif_score


class InterfaceUtilisateur:
    @staticmethod
    def afficher_menu():
        print("Bienvenue dans le gestionnaire de tournois d'échecs")
        print("1. Ajouter un joueur")
        print("2. Créer un tournoi")
        print("3. Enregistrer un résultat de match")
        print("4. Exporter les résultats d'un tournoi au format CSV")
        print("5. Quitter")

    @staticmethod
    def ajouter_joueur():
        global date_naissance, classement_elo
        nom = input("Entrez le nom du joueur: ")
        prenom = input("Entrez le prénom du joueur: ")

        date_verification = False
        while not date_verification:
            date_naissance = input("Entrez la date de naissance du joueur (AAAA-MM-JJ): ")
            date_verification = verifier_format_date(date_naissance)
            if not date_naissance:
                print ("La date de naissance n'est pas dans le bon format (AAAA-MM-JJ)")

        classement_elo_valide = False
        while not classement_elo_valide:
            classement_elo = input("Entrez le classement Elo du joueur: ")
            try:
                classement_elo = int(classement_elo)
                if classement_elo >= 0:
                    classement_elo_valide = True
                else:
                    print("Le classement Elo doit être un nombre positif.")
            except ValueError:
                print("Veuillez entrer un nombre entier pour le classement Elo.")

        joueurs = ChargementFichiers.charger_joueurs()
        identifiant = len(joueurs) + 1
        nouveau_joueur = Joueur(identifiant, nom, prenom, date_naissance, classement_elo)
        joueurs.append(nouveau_joueur)
        GestionFichiers.sauvegarder_joueurs(joueurs)

    @staticmethod
    def creer_tournoi():
        global date_tournoi
        nom_tournoi = input("Entrez le nom du tournoi: ")

        date_verification = False
        while not date_verification:
            date_tournoi = input("Entrez la date du tournoi (AAAA-MM-JJ): ")
            date_verification = verifier_format_date(date_tournoi)
            if not date_verification:
                print("La date du tournoi n'est pas dans le bon format (AAAA-MM-JJ)")

        tournois = ChargementFichiers.charger_tournois()
        nouveau_tournoi = Tournoi(nom_tournoi, date_tournoi)
        tournois.append(nouveau_tournoi)
        GestionFichiers.sauvegarder_tournois(tournois)

    @staticmethod
    def enregistrer_resultat_match():
        global tournoi_selectionne, match_selectionne, resultat
        tournois = ChargementFichiers.charger_tournois()

        print("Liste des tournois disponibles :")
        for index, tournoi in enumerate(tournois, start=1):
            print(f"{index}. {tournoi.nom}")

        verif_entrer = False
        while not verif_entrer:
            choix_tournoi = int(input("Sélectionnez un tournoi (entrez le numéro) : ")) - 1
            if 0 <= choix_tournoi < len(tournois):
                tournoi_selectionne = tournois[choix_tournoi]
                verif_entrer = True
            print ("L'entrer n'est pas bonne")


        print(f"Matchs du tournoi {tournoi_selectionne.nom} :")
        for index, match in enumerate(tournoi_selectionne.matchs, start=1):
            print(f"{index}. {match}")

        verif_entrer = False
        while not verif_entrer:
            choix_match = int(input("Sélectionnez un match à enregistrer (entrez le numéro) : ")) - 1
            if 0 <= choix_match < len(tournoi_selectionne.matchs):
                match_selectionne = tournoi_selectionne.matchs[choix_match]
                verif_entrer = True
            print ("L'entrer n'est pas bonne")

        verif_entrer = False
        while not verif_entrer:
            resultat = input("Entrez le résultat du match (1-0, 0.5-0.5, 0-1) : ")
            verif_entrer = verif_score
            if not verif_entrer:
                print ("L'entrer n'est pas bonne")

        match_selectionne.enregistrer_resultat(resultat)
        GestionFichiers.sauvegarder_tournois(tournois)

    @staticmethod
    def exporter_resultats_csv():
        # Afficher la liste des tournois disponibles
        # Sélectionner un tournoi
        # Exporter les résultats du tournoi sélectionné au format CSV

# Exemple d'utilisation de l'interface utilisateur
if __name__ == "__main__":
    while True:
        InterfaceUtilisateur.afficher_menu()
        choix = input("Entrez le numéro de l'option souhaitée: ")

        if choix == "1":
            InterfaceUtilisateur.ajouter_joueur()
        elif choix == "2":
            InterfaceUtilisateur.creer_tournoi()
        elif choix == "3":
            InterfaceUtilisateur.enregistrer_resultat_match()
        elif choix == "4":
            InterfaceUtilisateur.exporter_resultats_csv()
        elif choix == "5":
            break
        else:
            print("Choix invalide. Veuillez sélectionner une option valide.")
