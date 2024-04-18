def plus_longue_croissante(liste):
    temp_sublist = [liste[0]]
    
    longest_sublist = [liste[0]]
    
    for i in range(1, len(liste)):
        if liste[i] > temp_sublist[-1]:
            temp_sublist.append(liste[i])
        else:
            if len(temp_sublist) > len(longest_sublist):
                longest_sublist = temp_sublist
            temp_sublist = [liste[i]]
    
    if len(temp_sublist) > len(longest_sublist):
        longest_sublist = temp_sublist
    
    return longest_sublist

print(plus_longue_croissante([1, 2, 2, 3, 2, 3, 4, 1]))
