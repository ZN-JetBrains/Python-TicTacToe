prime_numbers = [num for num in range(1, 1000 + 1) if num > 1 and all(num % i != 0 for i in range(2, num - 1))]
