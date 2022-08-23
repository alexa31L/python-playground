from collections import Counter


def count_vowel(string):
    vowels = {'a', 'e', 'i', 'o', 'u'}

    counter = Counter(string)
    sum = 0
    for key, item in counter.items():
        if key in vowels:
            sum += item 

    return sum

print(count_vowel('abcdef'))



a_string = "Abcde"
lowercase = a_string.lower()
vowel_counts = {}

for vowel in "aeiou":
    count = lowercase.count(vowel)
    vowel_counts[vowel] = count
    
print(vowel_counts)