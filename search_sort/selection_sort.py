#selection sort O(n^2) worst case
def selection_sort(arr):
    start = 0
    while start < len(arr) - 1:
        smallest = float('inf')
        smallest_index = None
        for i in range(start, len(arr)):
            if arr[i] < smallest:
                smallest = arr[i]
                smallest_index = i
        arr[start],arr[smallest_index] = arr[smallest_index],arr[start]
        start += 1
    return arr
result = selection_sort([8,6,1,5,3,2,4,7])
print(result)