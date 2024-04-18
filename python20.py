def dictionnaire_croise(dico1, dico2):
    resultat = {}
    
    for cle1, valeur1 in dico1.items():
        if valeur1 in dico2:
            resultat[valeur1] = dico1[cle1]
    
    return resultat

dico1 = {"a": 1, "b": 2, "c": 3}
dico2 = {"x": "a", "y": "b"}
resultat = dictionnaire_croise(dico1, dico2)
print(resultat)
