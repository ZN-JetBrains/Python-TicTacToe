# put your python code here
def addition(a, b):
    print(a + b)


def subtraction(a, b):
    print(a - b)


def multiplication(a, b):
    print(a * b)


def division(a, b):
    if b == 0:
        print("Division by 0!")
    else:
        print(a / b)


def integer_division(a, b):
    if b == 0:
        print("Division by 0!")
    else:
        print(a // b)


def modulus(a, b):
    if b == 0:
        print("Division by 0!")
    else:
        print(a % b)


def power(a, b):
    print(a ** b)


first_number = float(input())
second_number = float(input())
operation = input()

if operation == "+":
    addition(first_number, second_number)
elif operation == "-":
    subtraction(first_number, second_number)
elif operation == "/":
    division(first_number, second_number)
elif operation == "*":
    multiplication(first_number, second_number)
elif operation == "mod":
    modulus(first_number, second_number)
elif operation == "pow":
    power(first_number, second_number)
elif operation == "div":
    integer_division(first_number, second_number)
