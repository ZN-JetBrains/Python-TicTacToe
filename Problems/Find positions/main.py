# put your python code here
sequence = input().split(" ")
number = input()
index = 0
positions = []

for digit in sequence:
    if digit == number:
        positions.append(str(index))
    index += 1

if len(positions) == 0:
    print("not found")
else:
    output = " ".join(positions)
    print(output)
