nums = [1,1,1,2,3,4,4,5,6,7,7,8,9,9,9,10]

def func(nums):
    n = len(nums)
    if n == 1:
        return 1
    i = 0
    j = i+1
    while j<n:
        if nums[i] != nums[j]:
            i += 1
            nums[i], nums[j] = nums[j], nums[i]
        j += 1
    return i+1

