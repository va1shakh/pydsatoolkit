def remove_num(numbers, index):
    for i in range(index, len(numbers) - 1):
        numbers[i] = numbers[i + 1]
    numbers.pop()
    return numbers
result = remove_num([10, 20, "cat", 30, 40, 50, 60], 2)
print(result)