col = int(input())
row = int(input())

if (col == 1 and row == 8) or (col == 8 and row == 1):
    print("3")
elif (col == 8 and row == 8) or (col == 1 and row == 1):
    print("3")
elif 1 < col < 8 and 1 < row < 8:
    print("8")
else:
    print("5")
