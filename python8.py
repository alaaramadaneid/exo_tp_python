def elements_communs(liste1, liste2):
    return list(set(liste1) & set(liste2))

liste1 = [1, 2, 3, 4, 5]
liste2 = [4, 5, 6, 7, 8]
print(elements_communs(liste1, liste2))
