#   1480. Running Sum of 1D Array

def runningSum (nums):
    resurt = nums[0]
    length = len(nums)
    for i in range(1, length):
        nums[i] += nums[i -1]
    return nums

print(runningSum([3,1,2,10,1]))