# print three times larger of first and last element of an array [11, 5, 9]
nums = [11, 5, 9]
ret = []
val = 0
if nums[0] >= nums[2]:
    val = nums[0]
else:
    val = nums[2]

for i in range(0, 3):
    ret.append(val)

print(ret)