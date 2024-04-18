def compter_lettres(chaine):
    Acont = {}
    for lettre in chaine:
        if lettre in  Acont:
             Acont[lettre] += 1
        else:
             Acont[lettre] = 1
    return  Acont

print(compter_lettres("Hello")) 
