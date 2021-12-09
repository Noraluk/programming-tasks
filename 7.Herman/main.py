import math

r = int(input())

general_area = math.pi * math.pow(r, 2)
taxi_area = 1/2 * math.pow(2*r, 2)

print("{:.6f}".format(general_area))
print("{:.6f}".format(taxi_area))
