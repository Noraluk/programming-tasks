a, b = [int(x) for x in input().split()]


i = 1
result = i
while a >= i and b >= i:
    if a % i == 0 and b % i == 0:
        result = i
    i = i+1

print(result)
