user_input = float(input())

if user_input < 2:
    print("Analytic")
elif 2 <= user_input <= 3:
    print("Synthetic")
elif user_input > 3:
    print("Polysynthetic")
