# leetcode 29

def func(nums,val):
    n = len(nums)
    k = 0
    for i in range(0,n):
        if val != nums[i]:
            nums[k] = nums[i]
            k += 1
    return k