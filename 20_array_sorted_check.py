def func(nums):
    n =len(nums)
    for i in range(nums):
        if nums[i] > nums[i+1]:
            return False
    return True