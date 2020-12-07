grade = float(input())
maximum = float(input())
percentage = int((grade / maximum) * 100)

if 90 <= percentage <= 100:
    print("A")
elif 80 <= percentage < 90:
    print("B")
elif 70 <= percentage < 80:
    print("C")
elif 60 <= percentage < 70:
    print("D")
elif percentage < 60:
    print("F")
