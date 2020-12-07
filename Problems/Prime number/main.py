number = int(input())
divisor_count = 0


for i in range(1, number + 1):
    if number % i == 0:
        divisor_count += 1

    if number == 1 or divisor_count > 2:
        print("This number is not prime")
        break
else:
    print("This number is prime")
