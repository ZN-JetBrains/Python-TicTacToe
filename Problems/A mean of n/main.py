n = int(input())

mean = 0.0

for _ in range(0, n):
    temp = int(input())
    mean += float(temp)

print(mean / n)
