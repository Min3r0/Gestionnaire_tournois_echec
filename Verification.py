import re

from LoadingFilesClass import LoadingFiles


def check_format_date(chain):
    pattern = r'^\d{4}-(0[1-9]|1[0-2])-(0[1-9]|[12][0-9]|3[01])$'  # Modèle AAAA-MM-JJ
    if re.match(pattern, chain):
        return True
    else:
        return False


def verif_score(chain):
    accepted_strings = ["1-0", "0.5-0.5", "0-1"]
    if chain in accepted_strings:
        return True
    else:
        return False


def player_already_exists(name, firstname, birthdate):
    players = LoadingFiles.load_players()
    if not players:
        return False
    else:
        for player in players:
            if (player.name == name and player.firstname == firstname and player.birthdate == birthdate):
                return True

    return False
