digits = [int(x) for x in input()]

average = [(x + (x + 1)) / 2 for x in range(1, len(digits))]
print(average)
