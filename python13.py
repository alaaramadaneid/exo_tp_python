def max_min_moyenne(numbers):
    maxNumber = max(numbers)
    minNumber = min(numbers)
    moyenne =  sum(numbers) / len(numbers)
    return maxNumber , minNumber , moyenne

test_taple = (10,20,20,40, 50)
resultat = max_min_moyenne(test_taple)
print("Max, Min , Moyenne :", resultat) 