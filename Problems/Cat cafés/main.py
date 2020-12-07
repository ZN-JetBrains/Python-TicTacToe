cafe = 0
name = ""

while True:
    input_ = input().split()
    if len(input_) <= 1:
        break
    else:
        if int(input_[1]) > cafe:
            cafe = int(input_[1])
            name = input_[0]

print(name)
