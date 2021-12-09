def get_inputs(a):
    values = []
    for i in range(a):
        values.append(int(input()))
    return values


a = int(input())
inputs = get_inputs(a)

print(min(inputs))
print(max(inputs))
