# put your python code here
grades = input().split(" ")
only_a = [grade for grade in grades if grade == "A"]
proportion = len(only_a) / len(grades)
print(round(proportion, 2))
