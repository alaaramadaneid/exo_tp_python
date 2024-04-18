def union_excluding_n(list_of_sets, n):
    union_set = set()
    
    for s in list_of_sets:
        union_set |= s
    
    union_set.discard(n)
    
    return union_set

list_of_sets = [{1, 2, 3}, {3, 4, 5}, {5, 6, 7}]
n = 5
print(union_excluding_n(list_of_sets, n))
