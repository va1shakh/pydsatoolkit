#binary search O(log n) time complexity
def binary_search(arr, target):
    start = 0
    end = len(arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if target == arr[mid]:
            return True
        elif target > arr[mid]:
            start = mid + 1
        elif target < arr[mid]:
            end = mid - 1
    return False

result = binary_search([3, 7, 12, 18, 24, 31, 39, 45, 52, 67, 73, 81, 94], 284)
print(result)