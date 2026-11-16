def find_max_min(numbers):
    largest = float('-inf')
    smallest = float('inf')

    for num in numbers:
        if num > largest:
            largest = num
        if num < smallest:
            smallest = num
    return (smallest, largest)
result = find_max_min([3,6,7,8,10,9,22,86,32,82])
print(result)