nums = []
sum = 0
for i in range(9):
    nums.append(int(input()))
    sum += nums[i]

for i in range(9):
    for j in range(i+1, 9):
        if (sum - 100) == (nums[i] + nums[j]):
            for k in range(9):
                if k != i and k != j:
                    print(nums[k])
            exit(0)
