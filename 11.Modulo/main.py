nums = []
for i in range(10):
    nums.append(int(input()))

without_dup_nums = []
[without_dup_nums.append(x % 42) for x in nums if x %
 42 not in without_dup_nums]

print(len(without_dup_nums))
