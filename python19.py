dictionnaire1 = {"un": 1, "deux": 2, "trois": 3}
dictionnaire2 = {"quatre": 4, "cinq": 5, "six": 6}

print(dictionnaire1)
print(dictionnaire2)


dictionnaire1.update(dictionnaire2)

print("Dictionnaire fusionné :", dictionnaire1)


dictionnaire1 = {"un": 1, "deux": 2, "trois": 3}
dictionnaire2 = {"quatre": 4, "cinq": 5, "six": 6}

dictionnaire_fusionne = {**dictionnaire1, **dictionnaire2}

print("Dictionnaire fusionné :", dictionnaire_fusionne)

