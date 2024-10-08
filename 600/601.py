# 601

nums = []
sum = 0

for i in range(12):
  nums.append(int(input()))

for j in range(12):
  if j%2==0:
    sum += nums[j]
  print("{:3d}".format(nums[j]),end='')
  if j%3 == 2:
    print()

print(sum)
