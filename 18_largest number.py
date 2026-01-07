def func(nums):
    n = len(nums)
    largest = nums[0]
    for i in range(0,n):
        largest = max(largest, nums[i])
    return largest


def func2(num):
    m = len(num)
    large = num[0]
    for i in range(0, m):
        if num[i] > large:
            large = num[i]
    return large
         
        