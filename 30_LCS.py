# lcs, leetcode 128

def brute(nums):
    n = len(nums)
    max_count = 0
    for i in range(0,n):
        num = nums[i]
        count = 0
        while num in nums:
            count += 1
            num += 1
        max_count = max(max_count, count)
    return max_count