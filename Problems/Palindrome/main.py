word = input()

index = 0
r_index = len(word) - 1

for _ in range(len(word)):
    if word[index] != word[r_index]:
        print("Not palindrome")
        break
    index += 1
    r_index -= 1
else:
    print("Palindrome")
