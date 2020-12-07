numbers = []

while True:
    string = input()
    if string == ".":
        break
    else:
        num = float(string)
        numbers.append(num)

print(min(numbers))
