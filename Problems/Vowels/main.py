vowels = 'aeiou'
# create your list here

string = input()

string_vowels = [x for x in string if x in vowels]
print(string_vowels)
