numbers = input()
new_list = [int(x) for x in numbers if int(x) % 2 == 1]
print(new_list)
