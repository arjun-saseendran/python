nums = [5, 4, 2, 1, 4]
max = nums[0]
min = nums[0]

for num in nums:
    if(max < num):
        max = num
    elif min > num:
        min = num

print('The big number is:',max)
print('The small number is:',min)
