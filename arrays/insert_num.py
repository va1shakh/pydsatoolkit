def insert_num(numbers, index, element):
    numbers.append(None)
    for i in range(len(numbers) - 1, index, -1):
        numbers[i] = numbers[i - 1]
    numbers[index] = element
    return numbers

result = insert_num([1,2,3,5,6,7,8,9,10], 3, 4)
print(result)