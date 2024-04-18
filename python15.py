def traiter_data(data):
    tuples_actifs = filter(lambda x: x[2] == "actif", data)
    
    #  tuple filtré
    tuples_tries = sorted(tuples_actifs, key=lambda x: x[1], reverse=True)
    

    resultat = [(t[0], t[1]) for t in tuples_tries]
    
    return resultat


data = [("id1", 10, "actif"), ("id2", 15, "inactif"), ("id3", 20, "actif")]
resultat = traiter_data(data)
print(resultat)
