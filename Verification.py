import re

from ChargementFichiersClass import LoadingFiles


def check_format_date(chaine):
    pattern = r'^\d{4}-\d{2}-\d{2}$'  # Modèle AAAA-MM-JJ
    if re.match(pattern, chaine):
        return True
    else:
        return False


def verif_score(chaine):
    chaines_acceptees = ["1-0", "0.5-0.5", "0-1"]
    if chaine in chaines_acceptees:
        return True
    else:
        return False


def player_already_exists(nom, prenom, date_naissance):
    joueurs = LoadingFiles.charger_joueurs()

    for joueur in joueurs:
        if joueur.name == nom and joueur.prenom == prenom and joueur.date_naissance == date_naissance:
            return True

    return False
