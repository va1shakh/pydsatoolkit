#count character frequency from a string
def count_frequency(string):
    freq = {}
    for char in string:
        if char not in freq:
            freq[char] = 1
        else:
            freq[char] += 1
    return freq


result = count_frequency("vaishakh")
print(result)