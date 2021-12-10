def swap(first, second):
    tmp = first
    first = second
    second = tmp
    return first, second


ball = '*'
box = [ball, '', '']
methods = str(input())

for method in methods:
    if method == 'A':
        box[0], box[1] = swap(box[0], box[1])
    elif method == 'B':
        box[1], box[2] = swap(box[1], box[2])
    elif method == 'C':
        box[2], box[0] = swap(box[2], box[0])

print(box.index(ball)+1)
