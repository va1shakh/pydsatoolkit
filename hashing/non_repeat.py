#find first non repeating number from a list by using dict
def find_non_repeat(arr):
    freq = {}
    for num in arr:
        if num not in freq:
            freq[num] = 1
        else:
            freq[num] += 1
    for key,value in freq.items():
        if value == 1:
            return key

result = find_non_repeat([4, 5, 1, 2, 1, 4, 5, 3])
print(result)