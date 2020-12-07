# put your python code here

numbers_sum = []
numbers_squared = []

while True:
    n = int(input())
    numbers_sum.append(n)
    if sum(numbers_sum) != 0:
        continue
    else:
        numbers_squared = [x ** 2 for x in numbers_sum]
        break

print(sum(numbers_squared))
