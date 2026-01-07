def func(nums):
    max = nums[0]
    n = len(nums)
    for i in range(0,n):
        if nums[i] > max:
            max = nums[i]
    return max