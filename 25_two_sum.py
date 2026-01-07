# 1 leetcode
# [5,9,1,2,4,15,6,3]
#

def brute(nums, target):
    n = len(nums)
    for i in range(0,n-1):
        for j in range(i+1, n):
            if nums[i] + nums[j] == target:
                return [i,j]

def func(nums, target):
    n = len(nums)
    hash_maps = {}
    for i in range(0,n):
        rem = target - nums[i]
        if rem in hash_maps:
            return [hash_maps[rem], i]
        hash_maps[nums[i]] = i
    