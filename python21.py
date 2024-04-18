def intersection_without_multiples_of_three(set1, set2):
    intersection_set = set1.intersection(set2)
    
    filtered_set = {x for x in intersection_set if x % 3 != 0}
    
    return filtered_set

set1 = {1, 2, 3, 4, 6, 9}
set2 = {2, 3, 5, 6, 7, 9}
print(intersection_without_multiples_of_three(set1, set2))
