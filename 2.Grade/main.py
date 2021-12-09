def cal_grade(a, b, c):
    result = a+b+c
    if 100 >= result >= 80:
        return 'A'
    elif 80 > result >= 75:
        return 'B+'
    elif 75 > result >= 70:
        return 'B'
    elif 70 > result >= 65:
        return 'C+'
    elif 65 > result >= 60:
        return 'C'
    elif 60 > result >= 55:
        return 'D+'
    elif 55 > result >= 50:
        return 'D'
    elif 50 > result >= 0:
        return 'F'


a = int(input())
b = int(input())
c = int(input())

print(cal_grade(a, b, c))
