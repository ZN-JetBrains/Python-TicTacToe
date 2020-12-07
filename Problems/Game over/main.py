scores = input().split()
# put your python code here
counter = 0
correct_answers = 0

for score in scores:
    if counter >= 3:
        print("Game over")
        print(correct_answers)
        break
    elif score == "C":
        correct_answers += 1
    elif score == "I":
        counter += 1
else:
    print("You won")
    print(correct_answers)
