import math

a, b = [float(x) for x in input().split()]

c = math.pow(a, 2) + math.pow(b, 2)
print("{:.6f}".format(math.sqrt(c)))
