money = int(input())

sheep = 6769
cow = 3848
pig = 1296
goat = 678
chicken = 23

if money >= sheep:
    count = money // sheep
    money -= count * sheep
    print(str(count) + " sheep")
elif money >= cow:
    count = money // cow
    money -= count * cow
    print(str(count) + " cow" if count == 1 else str(count) + " cows")
elif money >= pig:
    count = money // pig
    money -= count * pig
    print(str(count) + " pig" if count == 1 else str(count) + " pigs")
elif money >= goat:
    count = money // goat
    money -= count * goat
    print(str(count) + " goat" if count == 1 else str(count) + " goats")
elif money >= chicken:
    count = money // chicken
    money -= count * chicken
    print(str(count) + " chicken" if count == 1 else str(count) + " chickens")
else:
    print("None")
