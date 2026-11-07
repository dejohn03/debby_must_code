def move_zeros(nums):
    i = 0
    j = 0 
    for i in range(len(nums)):
        for j in range(len(nums)):
                if nums[j] == 0:
                    nums[i], nums[j] = nums[j], nums[i]
    return nums

print(move_zeros([0,1,0,3,12]))
print(move_zeros([0,0,1]))
print(move_zeros([1,2,3]))


