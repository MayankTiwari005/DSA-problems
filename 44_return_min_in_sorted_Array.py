# minimum from array

def brute(nums, target):
    n = len(nums)
    mini = float("inf")
    for i in range(0,n):
        mini = min(mini, nums[i])
    return mini

def optimal(nums):
    n = len(nums)
    mini = float("inf")
    low = 0
    high = n - 1
    while low <= high:
        mid = (low + high) // 2
        if nums[mid] <= nums[high]:
            mini = min(mini, nums[mid])
            high = mid - 1
        else:
            mini = min(mini, nums[low])
            low = mid + 1
    return mini

