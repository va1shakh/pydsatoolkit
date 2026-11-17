def find_two_sum(numbers, target):
    for i in range(0, len(numbers) - 1):
        for j in range(i+1, len(numbers)):
            if numbers[i] + numbers[j] == target:
                return [i,j]
result = find_two_sum([12, 5, 8, 21, 3, 14, 7, 19, 6, 11, 25, 4], 18)
print(result)

#time complexity worse case quadratic
#space complexity constant :)