#bubble sort O(n^2) worst case
def bubble_sort(arr):
    for i in range(0, len(arr)):
        for j in range(0, len(arr) - i - 1):
            if arr[j] > arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
    return arr

result = bubble_sort([7,1,5,8,3,2,4,6])
print(result)