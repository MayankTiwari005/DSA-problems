# nums = [7,2,1,5,6,4,8]

def func(nums):
    max_profit = 0
    n = len(nums)
    for i in range(0,n):
        for j in range(i+1,n):
            if nums[j] > nums[i]:
                profit = nums[j] - nums[i]
                max_profit = max(max_profit, profit)
    return max_profit

def optimal(nums):
    n = len(nums)
    max_profit = 0
    min_price = float("inf")
    for i in range(0,n):
        min_price = min(min_price, nums[i])
        max_profit = max(max_profit, nums[i] - min_price)
    return max_profit