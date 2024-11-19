
"""
Aray Intersection mencari array yang sama

"""

def array_intersection(arr1, arr2):
    return list(set(arr1) & set(arr2))

arr1 = [1, 2, 3, 4, 5]
arr2 = [3, 4, 5, 6, 7]
result = array_intersection(arr1, arr2)
print(result) 

