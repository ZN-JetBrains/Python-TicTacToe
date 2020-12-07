income = int(input())
percentage = 0

if 0 <= income <= 15_527:
    percentage = 0
elif 15_528 <= income <= 42_707:
    percentage = 15
elif 42_708 <= income <= 132_406:
    percentage = 25
elif income >= 132_407:
    percentage = 28

tax = income * float(percentage / 100.0)

print(f"The tax for {income} is {percentage}%. That is {round(tax)} dollars!")
