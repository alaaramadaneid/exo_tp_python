def trier_etudiants(etudiants):
    return sorted(etudiants, key=lambda x: x[1], reverse=True)

etudiants = [("Alice", 88), ("Bob", 95), ("Charlie", 78)]
etudiants_tries = trier_etudiants(etudiants)
print("Etudiants triés:", etudiants_tries)
