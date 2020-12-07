# Approach one without list comprehension
# n = int(input())

# winners = []
#
# for _ in range(0, n):
#     name = input()
#     if name.endswith("win"):
#         name = name.split(" win", 1)[0]
#         winners.append(name)

# Approach two with list comprehension
lines = [input() for _ in range(int(input()))]
winners = [name.split(" ", 1)[0] for name in lines if name.endswith("win")]

print(winners, len(winners), sep="\n")
