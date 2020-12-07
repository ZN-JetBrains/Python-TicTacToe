digits = [int(x) for x in input()]
new_list = [sum(digits[0:x:1]) for x in range(1, len(digits) + 1)]

print(new_list)
