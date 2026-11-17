def reverse_list(numbers):
    start = 0
    end = len(numbers) - 1

    while start < end:
        numbers[start], numbers[end] = numbers[end], numbers[start]
        start += 1
        end -= 1
    return numbers
result = reverse_list([1,2,3,4,5,6,7])
print(result)