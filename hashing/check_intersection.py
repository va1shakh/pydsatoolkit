#find common elements in a given two lists
def find_common_elements(arr1, arr2):
    return set(arr1) & set(arr2)

result = find_common_elements([3,6,7,8,9,55], [4,5,10,7,55])
print(result)