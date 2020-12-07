vowels = ["a", "e", "i", "o", "u"]
string = input()

for char in string:
    if not char.isalpha():
        break
    elif char in vowels:
        print("vowel")
    else:
        print("consonant")
