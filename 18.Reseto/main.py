n, k = [int(x) for x in input().split()]

result = []
nums = []
for i in range(2, n+1):
    nums.append(i)

num_length = len(nums)

i = 0
j = 0
while (len(nums) != 1):
    p = nums[i]
    nums.pop(0)
    result.append(p)

    new_nums = []
    for num in nums:
        if (num % p != 0):
            new_nums.append(num)
        else:
            result.append(num)

    nums = new_nums

result.append(nums[0])
print(result[k-1])
