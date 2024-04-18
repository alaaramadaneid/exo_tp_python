def mot_max(chaine):
    mots = chaine.split() 
    mot_plus_long = ''

    for mot in mots:
        if len(mot) > len(mot_plus_long):
            mot_plus_long = mot

    return mot_plus_long

chaine = input("Entre your word : ")
mot = mot_max(chaine)
print(mot)
