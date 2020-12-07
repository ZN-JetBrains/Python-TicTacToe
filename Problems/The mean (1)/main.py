mean = 0.0
counter = 0

while True:
    string = input()
    if string == ".":
        break
    else:
        mean += float(string)
        counter += 1

print(mean / counter)
