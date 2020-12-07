string = "red yellow fox bite orange goose beeeeeeeeeeep"
vowels = 'aeiou'

counter = 0

for char in string:
    for vowel in vowels:
        if char == vowel:
            counter += 1

print(counter)
