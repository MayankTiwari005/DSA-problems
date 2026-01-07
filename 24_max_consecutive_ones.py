# 485 leetcode
# nums = [1,1,0,1,0,1,1,1,1,0,1,1]

def fun(nums):
    n = len(nums) 
    count = 0
    max_count = 0
    for i in range(0,n):
        if nums[i] == 1:
            count += 1
        else:
            max_count = max(count, max_count)
            count = 0
    return max(max_count, count)

