#count character frequency from a string
def count_frequency(string):
    seen = set()
    freq = {}
    for char in string:
        if char not in seen:
            seen.add(char)
            freq[char] = 1
        else:
            freq[char] += 1
    return freq


result = count_frequency("vaishakh")
print(result)