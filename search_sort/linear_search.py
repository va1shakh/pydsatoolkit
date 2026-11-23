#linear search O(n) time complexity
def linear_search(arr, target):
    for num in arr:
        if target == num:
            return True
    return False

result = linear_search([3,6,67,9,10,23,1,5,7], 100)
print(result)