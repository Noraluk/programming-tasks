nums = [int(x) for x in input().split()]
chas = str(input())

nums.sort()

result = []
for i in range(3):
    result.append(str(nums[ord(chas[i].upper())-ord('A')]))

print(' '.join(i for i in result))
