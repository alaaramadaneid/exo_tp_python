import re

def detecter_dates(chaine):
    pattern = r'\b\d{2}/\d{2}/\d{4}\b'
    dates = re.findall(pattern, chaine)
    return dates

print(detecter_dates("Les dates importantes sont 12/05/2022 et 23/11/2023."))
