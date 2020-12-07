height = int(input())
empty_to_print = height
start = 1
string = "#"
for _ in range(height):
    start += 2
    empty_to_print -= 1
    print(empty_to_print * " ", end="")
    print(string)
    string += "##"
