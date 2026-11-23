#linear search O(n) time complexity
import time
def linear_search(arr, target):
    start = time.time()
    for num in arr:
        if target == num:
            return True
    end = time.time()
    print(end - start)
    return False

result = linear_search([3, 7, 12, 18, 24, 31, 39, 45, 52, 67, 73, 81, 94], 284)
print(result)