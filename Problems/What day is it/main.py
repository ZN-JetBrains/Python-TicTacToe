reference_time = 10.5

user_input = int(input())
time = reference_time + user_input

if 0 < time < 24:
    print("Tuesday")
elif time < 0:
    print("Monday")
elif time > 24:
    print("Wednesday")
elif time == 0:
    print("Tuesday")
